# Replication package

Anonymous replication package for "Towards a Multi-dimension Model for Representing Security Semantics in Evolving AI Agent Skills".

- `pairs.csv`: the 81 consecutive content-changing revision pairs of the 35 sampled skills (the sample of the paper; 13 of them are SSCs, 11 of those are SSRs) (repository, file path, old and new commit SHA, dates, line counts and the automatic triage signals; pair ids start at 0).
- `texts/pair_<n>_old.md`, `texts/pair_<n>_new.md`: the full text of both versions of the skill file, as retrieved through the GitHub REST API. Included: the 13 SSC pairs (1, 9, 13, 23, 24, 26, 31, 56, 57, 60, 62, 63, 65); the pairs 25, 27 and 29, which are not SSCs (pair 25 lies between pairs 24 and 26, and pair 27 between pairs 26 and 28, of the same skill); and the pairs 28, 35, 53 and 67, which we read and excluded or did not count as SSCs. Pair 53 is excluded because the new version of its file is not a skill (a translation tool overwrote it by accident).
- `diffs/pair_<n>_diff.txt`: the diff between the two versions.
- `commit_metadata_deleted_repo_and_selected_pairs.csv`: commit messages, dates and full SHAs for pairs 24, 26, 57 and others.

Pairs 23 to 28 come from the repository enesj/single-tenant-template, which returned HTTP 404 when we checked on 27 October 2026. The files in `texts/` are the only copy of those versions that we have. Pair 25 is the pair (new text of pair 24, old text of pair 26) and pair 27 is (new text of pair 26, old text of pair 28), since consecutive pairs share a commit.
