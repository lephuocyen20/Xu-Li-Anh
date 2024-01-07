import cv2
import numpy as np

anh1 = cv2.imread(
    "D:/3/HK2/XLA/Giua_Ky/20133119_LePhuocYen_GiuaKy/BTChuong3/Ex3.20/images_cat.jpg"
)
anh1 = cv2.resize(anh1, (500, 500))
anh2 = cv2.imread(
    "D:/3/HK2/XLA/Giua_Ky/20133119_LePhuocYen_GiuaKy/BTChuong3/Ex3.20/images_dog.jpg"
)
anh2 = cv2.resize(anh2, (500, 500))

footbase_ball = np.hstack((anh1[:, :250], anh2[:, 250:]))

# Gaussian Pyramid 1
l = anh1.copy()
gaussian_pyramid = [l]
for i in range(6):
    l = cv2.pyrDown(l)
    gaussian_pyramid.append(l)

# Laplacian Pyramid 1
l = gaussian_pyramid[5]
laplacian_pyramid = [l]
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i - 1].shape[1], gaussian_pyramid[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i - 1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)

# Gaussian Pyramid 2
l = anh2.copy()
gaussian_pyramid2 = [l]
for i in range(6):
    l = cv2.pyrDown(l)
    gaussian_pyramid2.append(l)

# Laplacian Pyramid 2
l = gaussian_pyramid2[5]
laplacian_pyramid2 = [l]
for i in range(5, 0, -1):
    size = (gaussian_pyramid2[i - 1].shape[1], gaussian_pyramid2[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid2[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid2[i - 1], gaussian_expanded)
    laplacian_pyramid2.append(laplacian)

# Laplacian Pyramid Footbase_ball
footbase_ball_pyramid = []
n = 0
for anh1_lap, anh2_lap in zip(laplacian_pyramid, laplacian_pyramid2):
    n += 1
    cols, rows, ch = anh1_lap.shape
    laplacian = np.hstack(
        (anh1_lap[:, 0 : int(cols / 2)], anh2_lap[:, int(cols / 2) :])
    )
    footbase_ball_pyramid.append(laplacian)

# Reconstructed Footbase_ball
footbase_ball_reconstructed = footbase_ball_pyramid[0]
for i in range(1, 6):
    size = (footbase_ball_pyramid[i].shape[1], footbase_ball_pyramid[i].shape[0])
    footbase_ball_reconstructed = cv2.pyrUp(footbase_ball_reconstructed, dstsize=size)
    footbase_ball_reconstructed = cv2.add(
        footbase_ball_pyramid[i], footbase_ball_reconstructed
    )

cv2.imshow("catdog reconstructed", footbase_ball_reconstructed)
cv2.imshow("catdog ", footbase_ball)
# cv2.imshow("anh1", anh1)
# cv2.imshow("anh2", anh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
