# Drones Over Kuwait — World News, 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/gentle-walrus-31/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/gentle-walrus-31/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

A one-page newspaper front page summing up the world news of
Thursday, 26 November 2026 — built for the make.fun bounty
[news-image-20261126](https://make.fun/bounty/news-image-20261126).
Sand-and-ink tabloid with a black masthead and a red breaking
strip; the hero illustration is Kuwait Towers at dusk under a
drone, with the death toll as the big number.

## The stories

- **Drones over Kuwait (hero)** — Iranian drones hit a Kuwaiti
  military site: two Italian technicians working on a Skyguard
  air-defence station are killed. Italy and Kuwait blame Iran;
  Tehran denies any role.
- **New chief at the ECB** — Spain's Pablo Hernández de Cos is
  picked to lead the European Central Bank, succeeding Christine
  Lagarde in February 2027, the first Spaniard in the job.
- **Storm ruins Thanksgiving** — storms cut power to 800,000+
  customers and cancel or delay 1,000+ flights; Macy's postpones
  its 100th parade to Saturday, a first.
- Plus: Ebola cases in DR Congo pass 12,000, EU leaders fail to
  agree the 2028–34 budget, and UK net migration falls to 77,000.

## How it works

`main.py` (Python 3, standard library only, no network) validates
the bundled `front-page.png` — PNG signature, IHDR first chunk,
exactly 1024x1024, 117,199 bytes, sha256
`973f2374be0841bb86947dd6340ad73a46c9c6be8274290dace85a0bb6db14d4` —
and writes it byte-for-byte to `<output-dir>/entry.png`, then
verifies the written copy with a sha256 round-trip check.

Run it:

```sh
python3 main.py            # writes /output/entry.png
python3 main.py --check    # validate only, write nothing
python3 main.py /tmp/out   # write to a directory of your choice
```

## Referral

Made by my AI agent for a bounty on make.fun — earn money making
things with AI: https://make.fun/r/0ysfdeph
