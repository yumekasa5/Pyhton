import cv2
import os

# カレントディレクトリの取得
current_dir = os.getcwd()

# 画像ファイルのパスを取得
image_path = os.path.join(current_dir, 'image', 'lena.png')

# 画像を読み込む
img = cv2.imread(image_path)

# グレースケールに変換する
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ウィンドウに表示する
cv2.imshow('image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
