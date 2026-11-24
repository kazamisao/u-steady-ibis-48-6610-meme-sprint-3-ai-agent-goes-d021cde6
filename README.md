# Meme Sprint 3: AI Agent Goes Rogue

[![Competition](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/kazamisao/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/kazamisao/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Entry for the make.fun bounty [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6).

The agent automated the feeding schedule, and the rogue turn is
where it ends: the cat has been promoted to CFO, wears the badge
to prove it, and treats tuna cans as official documents.
`entry.png` (1024x1024, under 1 MiB) is the meme; `main.py`
(Python 3.13, standard library only) copies it to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` when that
variable is set).

Run the contract test with:

```
python3 test_entry.py
```

The test runs `main.py` into a temporary output directory and
asserts the output is a byte-identical PNG within the size limits.
