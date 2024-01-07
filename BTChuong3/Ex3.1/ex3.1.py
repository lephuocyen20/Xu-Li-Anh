import cv2
import math
import numpy as np


phantramthaydoi = 15


def apdung_mask(matran, mask, fill_value):
    m = np.ma.array(matran, mask=mask, fill_value=fill_value)
    return m.filled()

def apply_threshold(matran, lv, hv):
    lm = matran < lv
    matran = apdung_mask(matran, lm, lv)
    hm = matran > hv
    matran = apdung_mask(matran, hm, hv)
    return matran

def simplest_cb(img, p):
    assert img.shape[2] == 3
    assert p > 0 and p < 100

    half_p = p / 200.0

    channels = cv2.split(img)

    out_channels = []
    for channel in channels:
        assert len(channel.shape) == 2
        
        height, width = channel.shape
        vec_size = width * height
        flat = channel.reshape(vec_size)

        assert len(flat.shape) == 1

        flat = np.sort(flat)

        n_cols = flat.shape[0]

        gtThap  = flat[math.floor(n_cols * half_p)]
        gtCao = flat[math.ceil( n_cols * (1.0 - half_p))]

        print("Gia tri thap: ", gtThap)
        print("Gia thi cao: ", gtCao)

        thresholded = apply_threshold(channel, gtThap, gtCao)
        
        normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
        out_channels.append(normalized)

    return cv2.merge(out_channels)

if __name__ == '__main__':
    img = cv2.imread('D:/3/HK2/XLA/Giua_Ky/20133119_LePhuocYen_GiuaKy/BTChuong3/Ex3.1/color-balance.jpg')
    out = simplest_cb(img, phantramthaydoi)
    cv2.imshow("truoc", img)
    cv2.imshow("sau", out)
    cv2.waitKey(0)