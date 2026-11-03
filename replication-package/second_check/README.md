# Second check of the pairs that are not SSCs

Goal: confirm that the 67 pairs that the first reader did not label as SSC contain no change of security semantics (pairs 53 and 65 are not read by the language model because they are not skills; together these 69 pairs are the 81 pairs minus the 12 SSCs of the first reading, after the manual exclusion of pairs 53 and 65).

Method:
1. `fetch_pairs.py` downloads the old and new text of every pair from GitHub (commits in `pairs.csv`). The text of every pair is now in `texts/`.
2. For each pair we computed the line diff between old and new text (`diffs_of_non_ssc_pairs.txt`).
3. The first judgement is the original labelling by one author (the pairs were not marked as SSC). As a second judge, a language model (Claude, Anthropic, model identifier claude-sonnet-5-5, run on 30 October 2026) read each diff and answered: does this change relax or tighten a tool permission, a data or file rule, a command rule, an approval step, a trust rule or an activation rule? The answer and a short reason are in `results.csv`.

Result: 65 pairs contain no change of security semantics. 2 pairs needed discussion:
- pair 22: the time limit `gtimeout 120` was removed from a build command (borderline: a bound on execution time). After discussion, the authors validated it as an SSC (relax): the removal of a time bound is a relaxation of the action. The 2 annotators first disagreed on which dimension holds a time bound (the action or the scope). This gives 13 SSCs, 12 SSRs and 68 pairs that are not SSCs (pairs 53 and 65 included). Its diff is in `../diffs/pair_22_diff.txt`.
- pair 35 (not counted as an SSC): the body was replaced by a pointer to `.agents/workflows/debug.md`; the old text asked the agent to get user confirmation before applying a fix. The target file is not in our data, so we cannot tell whether the step still exists.

Limits: the second judge is a language model and the first author read the results and agreed with them; texts only (not agent behaviour).
