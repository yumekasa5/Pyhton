"""Image Processing"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

#エッジ検出
def detect_edges(image_path):
    """入力画像のエッジを検出する

    Parameters
    ----------
    image_path : str
        入力画像のパス

    Returns
    -------
    edges
        エッジ検出後の画像
    """
    image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
    edges = cv2.Canny(image, 100, 200)
    return edges


def plot_histogram(image, title='Image Histogram'):
    """画像のヒストグラムを表示"""

    # 画像のヒストグラムを計算
    histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

    # ヒストグラムをプロット
    plt.figure()
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.plot(histogram, color='blue')
    plt.xlim([0, 256])
    plt.show()

def percentile_thresholding(img, p=95):
    """p-タイル法による2値化閾値算出

    Parameters
    ----------
    img : Any
        入力画像
    p : int, optional
        画像占有率, by default 95

    Returns
    -------
    bin_img : Any
        2値化画像
    """
    # 画像のピクセル値を1次元配列に変換
    pixels = img.flatten()
    
    # pパーセンタイルの計算
    bin_threshold = np.percentile(pixels, p)

    bin_img = np.where(img >= bin_threshold, 255, 0).astype(np.uint8)
    return bin_img

    
    
def otsu_threshold(image):
    # 画像のヒストグラムを計算
    histogram, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])

    # 画像全体のピクセル数
    total_pixels = image.shape[0] * image.shape[1]

    # 初期値
    best_threshold = 0
    best_variance = 0

    # 閾値の評価
    for threshold in range(256):
        # クラス1のピクセル数とクラス2のピクセル数を計算
        class1_pixels = np.sum(histogram[:threshold])
        class2_pixels = np.sum(histogram[threshold:])

        # クラス1とクラス2の平均値を計算
        class1_mean = np.sum(histogram[:threshold] * np.arange(threshold)) / class1_pixels
        class2_mean = np.sum(histogram[threshold:] * np.arange(threshold, 256)) / class2_pixels

        # クラス1とクラス2の分散を計算
        class1_variance = np.sum(((np.arange(threshold) - class1_mean) ** 2) * histogram[:threshold]) / class1_pixels
        class2_variance = np.sum(((np.arange(threshold, 256) - class2_mean) ** 2) * histogram[threshold:]) / class2_pixels

        # クラス内分散とクラス間分散の合計を計算
        within_class_variance = (class1_pixels / total_pixels) * class1_variance + (class2_pixels / total_pixels) * class2_variance
        between_class_variance = (class1_pixels / total_pixels) * (class2_pixels / total_pixels) * ((class1_mean - class2_mean) ** 2)

        # クラス間分散が最大の場合、閾値を更新
        if between_class_variance > best_variance:
            best_variance = between_class_variance
            best_threshold = threshold

    return best_threshold