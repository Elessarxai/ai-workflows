# Job 4: Read the audit report you never open

**When:** Before you enter  
**You need:** The audit report, or just the protocol name.

## Prompt

```text
Read this audit for me. I'll attach the audit report, or just name the protocol. If I only named it, find its most recent public audit yourself and tell me which one you're using.

1. Who audited it, when, and which version or commit it covers. Flag it if the audit is old or covers an earlier version.
2. A table of every finding: title | severity | status (fixed, acknowledged, partially fixed, open) | one-line plain meaning.
3. The findings that are NOT fixed, most severe first.
4. For each one, whether it could hurt someone who just holds the token or deposits funds, and how.
5. Any admin powers the report mentions: upgrades, pause, fee control, owner withdrawals.

Quote the report for every status. "Acknowledged" means not fixed. Finish with one line: would you deposit after reading this, and why.
```

## Notes

Look for "acknowledged". It usually means the team decided not to fix it.

---
[← all jobs](../README.md) · from the article [I Want Claude to Do All the Dirty Work of Trading](https://x.com/elessarqq/status/2110353431927869607)
