import cv2
import numpy as np

img = cv2.imread("D:/3/HK2/XLA/Giua_Ky/20133119_LePhuocYen_GiuaKy/BTChuong3/Ex3.19/cat.jpg")

# Gaussian Pyramid
l = img.copy()
gaussian_pyramid = [l]
for i in range(6):
    l = cv2.pyrDown(l)
    gaussian_pyramid.append(l)

# Laplacian Pyramid
l = gaussian_pyramid[5]
laplacian_pyramid = [l]
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i - 1].shape[1], gaussian_pyramid[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i - 1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)

anh_da_sua = laplacian_pyramid[0]
for i in range(1, 6):
    size = (laplacian_pyramid[i].shape[1], laplacian_pyramid[i].shape[0])
    anh_da_sua = cv2.pyrUp(anh_da_sua, dstsize=size)
    anh_da_sua = cv2.add(anh_da_sua, laplacian_pyramid[i])
    cv2.imshow(str(i), anh_da_sua)

cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()