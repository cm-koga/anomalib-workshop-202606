import cv2
import numpy as np
from pathlib import Path

# ===== 設定 =====
image_dir = Path("../data/wood/test_min")
mask_dir = Path("../data/wood/test_min_gt")

brush_size = 12
image_exts = [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]

mask_dir.mkdir(parents=True, exist_ok=True)

image_paths = sorted([
    p for p in image_dir.iterdir()
    if p.suffix.lower() in image_exts
])

drawing = False
erase_mode = False


def update_display(image, mask, display):
    overlay = image.copy()

    # マスク部分を赤く表示
    overlay[mask > 0] = (0, 0, 255)

    blended = cv2.addWeighted(image, 0.7, overlay, 0.3, 0)
    display[:] = blended


def mouse_callback(event, x, y, flags, param):
    global drawing, erase_mode

    image, mask, display = param

    # 左クリック：描画開始
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        erase_mode = False
        cv2.circle(mask, (x, y), brush_size, 255, -1)
        update_display(image, mask, display)

    # 右クリック：消去開始
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        erase_mode = True
        cv2.circle(mask, (x, y), brush_size, 0, -1)
        update_display(image, mask, display)

    # ボタンを離したら描画終了
    elif event in [cv2.EVENT_LBUTTONUP, cv2.EVENT_RBUTTONUP]:
        drawing = False

    # ドラッグ中
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        if erase_mode:
            cv2.circle(mask, (x, y), brush_size, 0, -1)
        else:
            cv2.circle(mask, (x, y), brush_size, 255, -1)

        update_display(image, mask, display)


def main():
    if not image_dir.exists():
        print(f"画像フォルダが存在しません: {image_dir}")
        return

    if len(image_paths) == 0:
        print("画像が見つかりませんでした")
        return

    window_name = "Mask Tool  Left: draw / Right: erase / Enter: save / ESC: exit"

    for image_path in image_paths:
        image = cv2.imread(str(image_path))

        if image is None:
            print(f"読み込み失敗: {image_path}")
            continue

        h, w = image.shape[:2]

        mask = np.zeros((h, w), dtype=np.uint8)
        display = image.copy()

        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        cv2.setMouseCallback(window_name, mouse_callback, [image, mask, display])

        print(f"編集中: {image_path.name}")

        while True:
            cv2.imshow(window_name, display)
            key = cv2.waitKey(20) & 0xFF

            # Enter
            if key == 13:
                save_path = mask_dir / image_path.name
                cv2.imwrite(str(save_path), mask)
                print(f"保存: {save_path}")
                break

            # ESC
            elif key == 27:
                print("中断しました")
                cv2.destroyAllWindows()
                return

    cv2.destroyAllWindows()
    print("完了しました")


if __name__ == "__main__":
    main()
