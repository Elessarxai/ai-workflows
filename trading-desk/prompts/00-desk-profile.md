# Set up your desk (once)

**When:** Setup  
**You need:** Nothing. Run it inside a Claude Project called **Trading Desk**.

## Prompt

```text
You're setting up my trading desk. Interview me, one question at a time, and keep it fast:

1. What do I trade (spot, perps, memecoins, prediction markets)?
2. What do I hold or watch right now? (tickers, markets, rough size: small, medium, large)
3. My account size, or just the % I risk per trade if I'd rather not say.
4. My trading rules, in my own words. If I don't have any, suggest 5 sensible ones and let me edit them.
5. Which exchange or wallet I export my history from.

Then write one block called DESK PROFILE with everything I told you, short and clean, so I can paste it into this project's instructions. Never ask for passwords, keys or seed phrases.
```

## Notes

Answer its questions, copy the DESK PROFILE it writes into the project's instructions, and you're done. From then on every chat in that project already knows what you hold and what your rules are.

One rule above all: never paste a seed phrase, a private key or an exchange API key into any AI chat. Nothing here needs them.

---
[← all jobs](../README.md) · from the article [I Want Claude to Do All the Dirty Work of Trading](https://x.com/elessarqq/status/2110353431927869607)
