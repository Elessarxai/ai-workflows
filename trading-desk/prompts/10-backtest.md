# Job 10: Backtest an idea before you trust it

**When:** Tools you build once  
**You need:** Works best in **Claude Code**, or any setup where Claude can run Python on your data.

## Prompt

```text
Backtest an idea for me. I'll describe the rule in plain words and name the asset. If I don't attach price data, download daily candles yourself from a public source and tell me which one.

Defaults unless I say otherwise: 0.1% fees per trade, 0.05% slippage, 1000 starting balance.

1. Restate my rule as exact entry and exit conditions and check them with me before running.
2. Run it: number of trades, win rate, total return, max drawdown, average win and loss.
3. Plot the equity curve against just holding.
4. Split the data in half and run each half separately.

Then judge it honestly: is the edge real or likely overfitting, and what would break it? Never use future information in a signal. If the result looks too good, assume a bug first and look for it.
```

## Notes

Be careful with this one. A backtest that looks amazing on one coin over one period usually means you found noise, which is why the prompt splits the data in half and makes Claude judge the result before you trust it.

---
[← all jobs](../README.md) · from the article [I Want Claude to Do All the Dirty Work of Trading](https://x.com/elessarqq/status/2110353431927869607)
