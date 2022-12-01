#ライブラリインポート
import cv2
import numpy as np

#画像の変数宣言
pic_name="robot_test_4_1"+ ".jpg"
pic_name_out="robot_test_4_1"+ "out.jpg"
gray_pic="robot_test_4_1"+"gray.jpg"
    
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
img_robot_test_4_1=np.zeros((height,width,3),np.uint8)
    
#ロボットとターゲットを別々に認識し，二値化画像を作成，重心を計算
img_robot_test_4_1[(h > 179) & (s > 100)& (v > 100)] = 255
#二値化画像を作成
cv2.imwrite(gray_pic,np.array(img_robot_test_4_1))
#作成した画像を読み込み
img_gray_r = cv2.imread(gray_pic,cv2.IMREAD_GRAYSCALE)
#読み込んだ画像の重心、輪郭を取得
M_r = cv2.moments(img_gray_r, False)
contours, hierarchy= cv2.findContours(img_gray_r, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
x_r,y_r= int(M_r["m10"]/M_r["m00"]) , int(M_r["m01"]/M_r["m00"])
print(x_r,y_r)
        
img_robot_test_4_1[(h > 70) & (h < 80) & (s > 100) & (v > 100)] = 255
#二値化画像を作成
cv2.imwrite(gray_pic,np.array(img_robot_test_4_1))
#作成した画像を読み込み
img_gray_t = cv2.imread(gray_pic,cv2.IMREAD_GRAYSCALE)
#読み込んだ画像の重心、輪郭を取得
M_t = cv2.moments(img_gray_t, False)
contours, hierarchy= cv2.findContours(img_gray_t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
x_t,y_t= int(M_t["m10"]/M_t["m00"]) , int(M_t["m01"]/M_t["m00"])
print(x_t,y_t)