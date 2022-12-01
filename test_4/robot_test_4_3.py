#ライブラリインポート
import cv2
import numpy as np

#2枚の画像に対する繰り返し処理
for i in range(2):
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
    
    #ロボットとターゲットを別々に認識し，二値化画像を作成，重心を計算
    img_robot_test_4_[(h > 179) & (s > 100)& (v > 100)] = 255
    #二値化画像を作成
    cv2.imwrite(gray_pic,np.array(img_robot_test_4_))
    #作成した画像を読み込み
    img_gray_r = cv2.imread(gray_pic,cv2.IMREAD_GRAYSCALE)
    #読み込んだ画像の重心、輪郭を取得
    M_r = cv2.moments(img_gray_r, False)
    contours, hierarchy= cv2.findContours(img_gray_r, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x_r,y_r= int(M_r["m10"]/M_r["m00"]) , int(M_r["m01"]/M_r["m00"])
    print(x_r,y_r)
    cv2.circle(img, (x_r,y_r), 20, 100, 2, 4)
    cv2.drawContours(img, contours, -1, color=(0, 0, 0), thickness=5)
    cv2.imwrite(pic_name_out,np.array(img))
        
    img_robot_test_4_[(h > 70) & (h < 80) & (s > 100) & (v > 100)] = 255
    #二値化画像を作成
    cv2.imwrite(gray_pic,np.array(img_robot_test_4_))
    #作成した画像を読み込み
    img_gray_t = cv2.imread(gray_pic,cv2.IMREAD_GRAYSCALE)
    #読み込んだ画像の重心、輪郭を取得
    M_t = cv2.moments(img_gray_t, False)
    contours, hierarchy= cv2.findContours(img_gray_t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x_t,y_t= int(M_t["m10"]/M_t["m00"]) , int(M_t["m01"]/M_t["m00"])
    print(x_t,y_t)
    cv2.circle(img, (x_t,y_t), 20, 100, 2, 4)
    cv2.drawContours(img, contours, -1, color=(0, 0, 0), thickness=5)
    cv2.imwrite(pic_name_out,np.array(img))