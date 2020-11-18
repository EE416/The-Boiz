import os
import os.path

index = 0
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".png")]:
        index += 1

print(index)