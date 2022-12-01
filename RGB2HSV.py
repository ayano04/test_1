import cv2
import matplotlib.pyplot as plt

#画像の読み込み
img = cv2.imread("robot_test_4_1.jpg")

#BGRからRGBに変換
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#画像のサイズを変更
img = cv2.resize(img, (640, 480))

X_start = int(input("開始位置のX座標の値を入力してください>>"))
Y_start = int(input("開始位置のY座標の値を入力してください>>"))
X_end = int(input("終了位置のX座標の値を入力してください>>"))
Y_end = int(input("終了位置のY座標の値を入力してください>>"))

#指定した範囲（yの始まり:yの終わり,xの始まり:xの終わり）
img_box = img[Y_start:Y_end, X_start:X_end]

#RGB値を取得
#flattenで値を一列に並べ，minで最小値を取得し，maxで最大値を取得する
r_min = img_box.T[0].flatten().min()
r_max = img_box.T[0].flatten().max()

g_min = img_box.T[1].flatten().min()
g_max = img_box.T[1].flatten().max()

b_min = img_box.T[2].flatten().min()
b_max = img_box.T[2].flatten().max()


#表示
print("R_min {:.2f}    R_max {:.2f}".format(r_min, r_max))
print("G_min {:.2f}    G_max {:.2f}".format(g_min, g_max))
print("B_min {:.2f}    B_max {:.2f}".format(b_min, b_max))

#RGBからHSVに変換
img_box_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#flattenで値を一列に並べ，minで最小値を取得し，maxで最大値を取得する
h_min = img_box_hsv.T[0].flatten().min()
h_max = img_box_hsv.T[0].flatten().max()

s_min = img_box_hsv.T[1].flatten().min()
s_max = img_box_hsv.T[1].flatten().max()

v_min = img_box_hsv.T[2].flatten().min()
v_max = img_box_hsv.T[2].flatten().max()    


#表示
print("H_min {:.2f}    H_max {:.2f}".format(h_min, h_max))
print("S_min {:.2f}    S_max {:.2f}".format(s_min, s_max))
print("V_min {:.2f}    V_max {:.2f}".format(v_min, v_max))

#指定した範囲を枠で囲む
cv2.rectangle(img, (X_start,Y_start), (X_end,Y_end), (255,0,0), 2)

#描写
plt.imshow(img)
plt.show()