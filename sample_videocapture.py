import cv2

# カメラをキャプチャする
cap = cv2.VideoCapture(1)   #0:内臓カメラ, 1:外部カメラ

# キャプチャが成功したかどうかをチェックする
if not cap.isOpened():
    print("カメラが接続されていません")
    exit()

# キャプチャした映像をウィンドウに表示する
while True:
    # 映像をキャプチャする
    ret, frame = cap.read()

    # 映像がキャプチャできなかった場合は終了する
    if not ret:
        break

    # 映像をウィンドウに表示する
    cv2.imshow('Camera', frame)

    # キー入力を待機する
    if cv2.waitKey(1) == ord('q'):
        break

# キャプチャした映像を解放する
cap.release()

# ウィンドウを閉じる
cv2.destroyAllWindows()
