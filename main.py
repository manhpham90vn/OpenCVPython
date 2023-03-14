import cv2

# read img
path = r'assets/imgs/img.png'
img = cv2.imread(path)

# split chanel from img
B, G, R = cv2.split(img)

# show img
cv2.imshow('Demo', img)

# write img with chanel
pathB = r'assets/imgs/imgB.png'
pathG = r'assets/imgs/imgG.png'
pathR = r'assets/imgs/imgR.png'
cv2.imwrite(pathB, B)
cv2.imwrite(pathG, G)
cv2.imwrite(pathR, R)

# bitwise
pathTest = r'assets/imgs/imgT.png'
and_img = cv2.bitwise_and(B, G)
cv2.imwrite(pathTest, and_img)

# Esc key
if cv2.waitKey() & 0xff == 27:
    cv2.destroyAllWindows()