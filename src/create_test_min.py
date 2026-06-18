from pathlib import Path
import shutil

paths = [
    "../data/wood/test/NG/IMG_3792_0201.png",
    "../data/wood/test/NG/IMG_3795_0001.png",
    "../data/wood/test/NG/IMG_3871_0300.png",
    "../data/wood/test/NG/IMG_3790_0100.png",
    "../data/wood/test/NG/IMG_3805_0000.png",
    "../data/wood/test/NG/IMG_3860_0202.png",
    "../data/wood/test/NG/IMG_3860_0301.png",
    "../data/wood/test/NG/IMG_3858_0103.png",
    "../data/wood/test/NG/IMG_3792_0200.png",
    "../data/wood/test/NG/IMG_3809_0102.png",
]

dir_path = Path("../data/wood/test_min")
dir_path.mkdir(parents=True, exist_ok=True)


for path in paths:
    shutil.copy(path, dir_path / Path(path).name)
    