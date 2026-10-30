# Downloads old/new SKILL.md text for every pair in pairs.csv that is missing locally.
# Usage: python fetch_pairs.py pairs.csv out_folder
# Needs: Python 3 and internet. Uses raw.githubusercontent.com (public repos only).
import csv, os, sys, time, urllib.request, urllib.parse
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
def get(repo, sha, path):
    url = f"https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(path)}"
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read().decode("utf-8", "replace")
ok = fail = 0
for row in csv.DictReader(open(src, encoding="utf-8")):
    pid = row["pair_id"]
    for kind, sha in (("old", row["old_sha"]), ("new", row["new_sha"])):
        f = os.path.join(out, f"pair_{pid}_{kind}.md")
        if os.path.exists(f):
            continue
        try:
            open(f, "w", encoding="utf-8").write(get(row["repo"], sha, row["path"]))
            ok += 1
        except Exception as e:
            fail += 1
            print("FAILED", pid, kind, row["repo"], sha, e)
        time.sleep(0.3)
print("downloaded", ok, "failed", fail)
