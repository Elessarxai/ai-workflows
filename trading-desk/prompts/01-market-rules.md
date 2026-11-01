# Job 1: Read the rules before you bet

**When:** Before you enter  
**You need:** The prediction market link or its rules.

## Prompt

```text
Check this prediction market for me before I bet. I'll paste the market link or its rules with this message. If I only sent a link, open it and read the full rules and resolution details yourself.

Do this in order:
1. In one sentence, exactly what has to happen for YES to win.
2. The resolution source and how it decides (one source, a consensus of reporting, an oracle vote).
3. The exact deadline with timezone, and whether "before" or "by" changes which day counts.
4. Every edge case where the obvious answer could resolve the other way: wording, partial events, timing, the source going quiet, disputes.
5. A short checklist of what I should verify right now before buying.

Quote the exact line from the rules for every claim. If the rules are vague, say "unclear" instead of guessing. Finish with one line: the biggest way I could be right and still lose.
```

## Notes

The question in a market's title and the rule that settles it are often two different things. One minute here saves you from the bet where you were right and still lost.

---
[← all jobs](../README.md) · from the article [I Want Claude to Do All the Dirty Work of Trading](https://x.com/elessarqq/status/2110353431927869607)
