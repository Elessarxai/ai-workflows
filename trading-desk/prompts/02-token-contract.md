# Job 2: Check the token contract before you ape

**When:** Before you enter  
**You need:** Contract address and chain. Runs in **Claude Code** with [REA (Reverse Engineer Anything)](https://github.com/morluto/rea) installed.

## Prompt

```text
Check this token's contract before I buy. I'll give you the contract address and chain with this message. If I didn't, ask me for them in one short question.

1. Fetch the runtime bytecode yourself (eth_getCode through a public RPC for that chain) and save it as runtime.hex.
2. Run REA on it: rea inspect-evm-interface ./runtime.hex hex --json
3. List every function that can change state, with its selector and recovered name, and mark which ones only the owner or an admin role can call.
4. Flag anything that can mint new supply, blacklist or freeze wallets, change buy or sell fees, pause trading, or upgrade the contract (proxy patterns included).
5. Tell me which wallet or role controls each flagged function, and whether ownership looks renounced or sits with a multisig.
6. Verdict: SKIP, CAUTION or NO OWNER TRAPS FOUND, with the reason in one line.

Mark every finding as confirmed or inferred. Recovered names can be wrong, so describe what an unnamed or renamed function does instead. Never call a token safe.
```

## Notes

Two honest limits. Function names come from known signatures, so a renamed function needs a closer look at what it actually does. And the contract part of REA runs on Linux x64, so on Windows you need WSL.

A red flag means "dig deeper". On its own it's never proof.

---
[← all jobs](../README.md) · from the article [I Want Claude to Do All the Dirty Work of Trading](https://x.com/elessarqq/status/2110353431927869607)
