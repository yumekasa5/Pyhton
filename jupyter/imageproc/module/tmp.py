import cv2
import numpy as np

def elastic_matching(template, input_image):
    # テンプレート画像の特徴点を検出
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(template, None)

    # 入力画像の特徴点を検出
    kp2, des2 = orb.detectAndCompute(input_image, None)

    # 特徴点のマッチングを行う
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # マッチングした特徴点を使用して変換行列を推定
    src_points = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_points = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)

    # テンプレート画像のサイズを取得
    h, w = template.shape[:2]

    # 入力画像を変換してテンプレート画像に近づける
    transformed_image = cv2.warpPerspective(input_image, M, (w, h))

    # 回転角度と拡大縮小倍率の計算
    rotation_matrix = M[:2, :2]
    scale_x = np.linalg.norm(rotation_matrix[0, :])
    scale_y = np.linalg.norm(rotation_matrix[1, :])
    rotation_angle = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0]) * 180 / np.pi

    return transformed_image, rotation_angle, scale_x, scale_y

# テンプレート画像と入力画像の読み込み
template_image = cv2.imread('template.jpg', 0)
input_image = cv2.imread('input.jpg', 0)

# 弾性マッチングの実行
transformed_image, rotation_angle, scale_x, scale_y = elastic_matching(template_image, input_image)

# 結果の表示
cv2.imshow('Input Image', input_image)
cv2.imshow('Template Image', template_image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 回転角度と拡大縮小倍率の表示
print('Rotation Angle:', rotation_angle)
print('Scale X:', scale_x)
print('Scale Y:', scale_y)

