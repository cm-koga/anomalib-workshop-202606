import cv2
import numpy as np
from pathlib import Path

# ===== 設定 =====
image_dir = Path("../data/wood/test_min")
mask_dir = Path("../data/wood/test_min_gt")

brush_size = 12
mask_dir.mkdir(parents=True, exist_ok=True)

image_exts = [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]
image_paths = sorted([
    p for p in image_dir.iterdir()
    if p.suffix.lower() in image_exts
])

drawing = False


def mouse_callback(event, x, y, flags, param):
    global drawing

    image, mask, display = param

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(mask, (x, y), brush_size, 255, -1)

            # 表示用：マスク部分を赤く重ねる
            overlay = image.copy()
            overlay[mask > 0] = (0, 0, 255)
            blended = cv2.addWeighted(image, 0.7, overlay, 0.3, 0)
            display[:] = blended


for image_path in image_paths:
    image = cv2.imread(str(image_path))

    if image is None:
        print(f"読み込み失敗: {image_path}")
        continue

    h, w = image.shape[:2]

    # 1chのマスク画像
    mask = np.zeros((h, w), dtype=np.uint8)

    display = image.copy()

    window_name = "Mask Tool - Enter: save next / ESC: exit"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback, [image, mask, display])

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
            raise SystemExit

cv2.destroyAllWindows()
print("完了しました")
