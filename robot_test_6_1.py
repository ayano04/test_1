#ライブラリインポート
import cv2
import numpy as np
import math

#2枚の画像に対する繰り返し処理
for i in range(3):
    #画像の変数宣言
    pic_name="robot_test_6_"+str(i+1)+ ".jpg"
    pic_name_out="robot_test_6_"+str(i+1)+ "out.jpg"
    gray_pic="robot_test_6_"+str(i+1)+ "gray.jpg"
    
    #ベース画像の読み込み
    img = cv2.imread(pic_name,cv2.IMREAD_COLOR)
    
    #画像のサイズ情報取得
    height, width = img.shape[:2]
    print(height, width)
    
    #画像の色をHSV形式に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    
    #ベース画像と同じ大きさの配列を作成
    img_robot_test_6_=np.zeros((height,width,3),np.uint8)
    
    #ロボットを認識
    img_robot_test_6_[(h > 179) & (s > 100)& (v > 100)] = 255
    #二値化画像を作成
    cv2.imwrite(gray_pic,np.array(img_robot_test_6_))
    #作成した画像を読み込み
    img_gray_r = cv2.imread(gray_pic,cv2.IMREAD_GRAYSCALE)
    #読み込んだ画像の重心、輪郭を取得
    M_r = cv2.moments(img_gray_r, False)
    contours, hierarchy= cv2.findContours(img_gray_r, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x_r,y_r= int(M_r["m10"]/M_r["m00"]) , int(M_r["m01"]/M_r["m00"])
    print(x_r,y_r)
    #画像にロボットの重心をプロット
    cv2.circle(img, (x_r,y_r), 20, 100, 2, 4)
    cv2.drawContours(img, contours, -1, color=(0, 0, 0), thickness=5)
    cv2.imwrite(pic_name_out,np.array(img))
    
    #ターゲットを認識
    img_robot_test_6_[(h > 70) & (h < 80) & (s > 100) & (v > 100)] = 255
    #二値化画像を作成
    cv2.imwrite(gray_pic,np.array(img_robot_test_6_))
    #作成した画像を読み込み
    img_gray_t = cv2.imread(gray_pic,cv2.IMREAD_GRAYSCALE)
    #読み込んだ画像の重心、輪郭を取得
    M_t = cv2.moments(img_gray_t, False)
    contours, hierarchy= cv2.findContours(img_gray_t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x_t,y_t= int(M_t["m10"]/M_t["m00"]) , int(M_t["m01"]/M_t["m00"])
    print(x_t,y_t)
    #画像にターゲットの重心をプロット
    cv2.circle(img, (x_t,y_t), 20, 100, 2, 4)
    cv2.drawContours(img, contours, -1, color=(0, 0, 0), thickness=5)
    cv2.imwrite(pic_name_out,np.array(img))
    
    a = x_t - x_r
    b = y_r - y_t
    rad = math.atan(b/a)
    print(rad)
    
    #ロボットの正面を認識
    img_robot_test_6_[(h > 20) & (h < 30) & (s > 100) & (v > 100)] = 255
    #二値化画像を作成
    cv2.imwrite(gray_pic,np.array(img_robot_test_6_))
    #作成した画像を読み込み
    img_gray_f = cv2.imread(gray_pic,cv2.IMREAD_GRAYSCALE)
    #読み込んだ画像の重心、輪郭を取得
    M_f = cv2.moments(img_gray_f, False)
    contours, hierarchy= cv2.findContours(img_gray_f, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x_f,y_f= int(M_f["m10"]/M_f["m00"]) , int(M_f["m01"]/M_f["m00"])
    print(x_f,y_f)
    #画像にターゲットの重心をプロット
    cv2.circle(img, (x_f,y_f), 20, 100, 2, 4)
    cv2.drawContours(img, contours, -1, color=(0, 0, 0), thickness=5)
    cv2.imwrite(pic_name_out,np.array(img))