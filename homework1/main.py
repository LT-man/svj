import cv2, os
Svj = cv2.imread("svj.jpg")
print(Svj.shape)
print(Svj[105, 110])
Svj[105, 110] = (0, 0, 255 )
cv2.imshow("screen", Svj)
cv2.waitKey(0)
b, g, r = cv2.split(Svj)
cv2.imshow("screen2", b)
cv2.waitKey(0)
cv2.imshow("screen3", g)
cv2.waitKey(0)
cv2.imshow("screen4", r)
cv2.waitKey(0)
path = "/Users/laury/Pictures/Saved Pictures"
os.chdir(path)
cv2.imwrite("svj.jpg", Svj)
