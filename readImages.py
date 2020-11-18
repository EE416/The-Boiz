import os
import os.path

index = 90
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".png")]:
        try:
            os.rename(os.path.join(dirpath, filename), os.path.join(dirpath + '\..\..',filename))
        except:
            os.rename(os.path.join(dirpath, filename), os.path.join(dirpath + '\..\..',str(index)+".png"))
            index += 1

  