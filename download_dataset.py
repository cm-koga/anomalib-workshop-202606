from pathlib import Path
import requests
import zipfile
from tqdm import tqdm


def download_extract_zip(
    url: str,
    zip_path: str,
    extract_dir: str,
):
    zip_path = Path(zip_path)
    extract_dir = Path(extract_dir)

    zip_path.parent.mkdir(parents=True, exist_ok=True)
    extract_dir.mkdir(parents=True, exist_ok=True)

    # ダウンロード
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))

    with (
        open(zip_path, "wb") as f,
        tqdm(
            total=total_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            desc="Downloading",
        ) as pbar,
    ):
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
                pbar.update(len(chunk))

    # 解凍
    with zipfile.ZipFile(zip_path, "r") as zf:
        members = zf.infolist()

        total_uncompressed = sum(m.file_size for m in members)

        with tqdm(
            total=total_uncompressed,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            desc="Extracting",
        ) as pbar:
            for member in members:
                zf.extract(member, extract_dir)
                pbar.update(member.file_size)

    # ZIP削除
    zip_path.unlink()

    print(f"ダウンロード・解凍が完了しました。 {extract_dir}")

if __name__ == "__main__":
    download_extract_zip(
        "https://github.com/cm-koga/assets/releases/download/workshop/wood.zip",
        r"./data/wood.zip",
        r"./data"
    )