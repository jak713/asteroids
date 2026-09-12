

import os

print("ROOT:", os.listdir("/"))
print("ASSETS:", os.listdir("/assets") if os.path.exists("/assets") else "MISSING")
print(
    "FONTS:",
    os.listdir("/assets/fonts")
    if os.path.exists("/assets/fonts")
    else "MISSING"
)

font_path = "/assets/fonts/DepartureMono-Regular.otf"
print("FONT EXISTS:", os.path.exists(font_path))
print("FONT PATH:", font_path)

from main import main

await main()
