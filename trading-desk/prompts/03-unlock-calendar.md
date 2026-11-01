# Job 3: Turn the whitepaper into an unlock calendar

**When:** Before you enter  
**You need:** Token name. Attach the whitepaper if you have it; if not, Claude finds it (web search on).

## Prompt

```text
Build me the unlock calendar for this token. I'll give you the token name, and I may attach the whitepaper. If nothing is attached, find the official tokenomics or vesting docs yourself with web search, and get the current circulating supply from a public source.

Make a table, one row per unlock:
date | amount | % of current circulating supply | who receives it (team, investors, ecosystem, treasury) | cliff or linear | source

Then:
1. Flag every month where unlocks add more than 5% to circulating supply.
2. Say which unlocks go to insiders most likely to sell.
3. List anything the docs leave vague.

Cite the page or link for every number. Never fill a gap with an estimate; write "not stated". If sources disagree, show both.
```

## Notes

"Quote the page" is the important bit. You can check every number in seconds instead of trusting a summary.

---
[← all jobs](../README.md) · from the article [I Want Claude to Do All the Dirty Work of Trading](https://x.com/elessarqq/status/2110353431927869607)
