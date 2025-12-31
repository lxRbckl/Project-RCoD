# Project RCoD 2
> *Return Calls on Discord.* Reconnect to dropped Discord calls on Retina displays. V2. Fall 2023.

---
```bash
#!/bin/bash


# variables <
tokenOpenai=""
tokenDiscord=""

role="call"
skipQuery=false
muteAfterCall=true
contact="jordyn.png"
guildId="974210528958369863"
query="give me an inspiring quote to start my day"

# >


git clone https://github.com/lxRbckl/Project-RCoD.git
cd Project-RCoD

poetry=$(which poetry)
poetry install
poetry run python3 main.py \
  "$role" \
  "$query" \
  "$contact" \
  "$guildId" \
  "$skipQuery" \
  "$tokenOpenai" \
  "$tokenDiscord" \
  "$muteAfterCall" \

cd ..
rm -rf Project-RCoD
```

---
