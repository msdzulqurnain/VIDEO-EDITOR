import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import MSDZULQURNAIN

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
        
print("Bot telah aktif🔥🔥🔥")
print("@MSPR0JECT | @MsSUPP0RT")

if __name__ == "__main__":
    MSDZULQURNAIN.run_until_disconnected()
