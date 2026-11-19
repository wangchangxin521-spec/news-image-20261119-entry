# 19 November 2026 — The World in One Day

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/wangchangxin521-spec/news-image-20261119-entry/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/wangchangxin521-spec/news-image-20261119-entry/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world news of **Thursday 19 November 2026** —
a newspaper front page built from five AI-generated, text-free panels
with headlines drawn on top.

## The day in five stories

- **GTA VI LAUNCHES WORLDWIDE** — Gamers enter Vice City as Grand Theft
  Auto VI begins its global rollout, to near-perfect reviews.
- **SHENZHEN SUMMIT** — Trump, Xi and Putin meet in a trilateral summit
  in Shenzhen.
- **STRAIT OF HORMUZ** — The US strikes Qeshm Island; three tankers hit
  mines east of the strait and catch fire.
- **FIRST BLACK SPEAKER** — Democrats nominate Hakeem Jeffries for
  Speaker of the House; he would be the first Black Speaker.
- **THE HAGUE** — The World Court rules on the Myanmar case over the
  alleged genocide of the Rohingya.

Ticker: Cyclone Akvan nears India's east coast · Voyager 1 passes one
light-day · EU unveils a €45bn Ukraine loan.

## How it runs

`main.py` (Python 3 standard library only) copies the finished image
to the output directory:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024×1024, under 1 MiB)
```

`build_image.py` is the script that composed `entry.png` from the five
panels (Pillow): masthead, headlines, and ticker are all drawn with
system fonts, so the image stays sharp at any size.

Entered on [make.fun](https://make.fun/?ref=1dr3sg6a&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards
