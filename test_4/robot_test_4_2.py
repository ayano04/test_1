#ライブラリインポート
import cv2
import numpy as np
import matplotlib.pyplot as plt

#2枚の画像に対する繰り返し処理
for i in range(3):
    #画像の変数宣言
    pic_name="robot_test_4_"+str(i+1)+ ".jpg"
    pic_name_out="robot_test_4_"+str(i+1)+ "out.jpg"
    gray_pic="robot_test_4_"+str(i+1)+ "gray.jpg"
    
    #ベース画像の読み込み
    img = cv2.imread(pic_name,cv2.IMREAD_COLOR)
    
    #画像のサイズ情報取得
    height, width = img.shape[:2]
    
    #画像の色をHSV形式に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    
    #ベース画像と同じ大きさの配列を作成
    img_robot_test_4_=np.zeros((height,width,3),np.uint8)
    
    #紫色を指定（ロボット）
    img_robot_test_4_[(h > 179) & (s > 100)& (v > 100)] = 255
    
    #緑色を指定（ターゲット）
    img_robot_test_4_[(h > 70) & (h < 80) & (s > 100) & (v > 100)] = 255
    
    #ロボットとターゲットの領域だけの二値化画像を作成
    cv2.imwrite(gray_pic,np.array(img_robot_test_4_))
    
    #作成した画像を読み込み
    img_gray = cv2.imread(gray_pic,cv2.IMREAD_GRAYSCALE)
    
    M_robot = cv2.moments(img_gray, False)
    contours, hierarchy= cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, color=(255, 0, 0), thickness=5)
    
    M = cv2.moments(img_gray, False)
    x,y= int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"])
    plt.plot(x,y,marker='.')

    plt.imshow(img, cmap = "gray")
    plt.colorbar()
    plt.show()
    
    cv2.imwrite(pic_name_out,np.array(img))
    cv2.circle(img, (x,y), 20, 100, 2, 4)