# Project RCoD 3
> *Return Calls on Discord.* Reconnect to dropped Discord calls on Retina displays. V3. Spring 2024.

---

```bash
#!/bin/bash


# variables <
role="call"

# >


git clone https://github.com/lxRbckl/Project-RCoD.git
cd Project-RCoD

poetry=$(which poetry)
poetry install
poetry run python3 main.py \
  "$role" \

cd ..
rm -rf Project-RCoD
```

---
