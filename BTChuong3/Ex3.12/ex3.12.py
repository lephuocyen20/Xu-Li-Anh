import cv2
    
img = cv2.imread('D:/3/HK2/XLA/Giua_Ky/20133119_LePhuocYen_GiuaKy/BTChuong3/Ex3.12/images.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Goc', img)
output_sharpen = cv2.addWeighted(img, 1.2, img, 0.5, 0)
output_bilateral = cv2.bilateralFilter(output_sharpen, 5, 100, 6)
cv2.imshow('Ket qua', output_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()