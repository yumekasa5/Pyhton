import cv2
import os
import numpy as np

#Kernel
kernel = np.zeros((3,3))

#中心差分フィルタ
kernel = 0.5 * np.array(
    [[0, 0, 0],
    [-1, 0, 1],
    [0, 0, 0]]
)

# カレントディレクトリの取得
current_dir = os.getcwd()

# 画像ファイルのパスを取得
image_path = os.path.join(current_dir, 'image', 'lena.png')

# 画像を読み込む
img = cv2.imread(image_path)

#フィルタリング
dst = cv2.filter2D(img, -1, kernel)

# ウィンドウに表示する
cv2.imshow('image origin', img)
cv2.imshow('filtered image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
