import numpy as np
import scipy
import scipy.signal
from skimage.color import rgb2gray
from imageio import imread
from scipy import linalg as linalg
import matplotlib.pyplot as plt

deriv_vec = np.array([[0, 0, 0], [1, 0, -1], [0, 0, 0]])


def read_image(filename, representation):
    im = imread(filename)
    if representation == 1:
        # converting to gray
        im = rgb2gray(im) / 255
    else:
        if representation == 2:
            im = im.astype(np.float64)
            # setting the image's matrix to be between 0 and 1
            im = im / 255
    return im


def get_fft_coef(N):
    n = np.arange(N)
    k = n.reshape((N, 1))
    return np.exp(-2j * np.pi * k * n / N)


def DFT(signal):
    N = signal.shape[0]
    fft_coef = get_fft_coef(N)
    return np.dot(fft_coef, signal)


def IDFT(fourier_signal):
    N = fourier_signal.shape[0]
    fft_coef = np.linalg.inv(linalg.dft(N))
    out_vec = (1/N) * fft_coef.dot(fourier_signal)
    return out_vec


def DFT2(image):
    DFT_mat_cols = get_fft_coef(image.shape[1])
    DFT_mat_rows = get_fft_coef(image.shape[0])
    DFT_cols = np.dot(DFT_mat_cols, image.T).T
    final_DFT = np.dot(DFT_mat_rows, DFT_cols)
    return final_DFT

def IDFT2(image):
    DFT_mat_cols = get_fft_coef(image.shape[1])
    DFT_mat_rows = get_fft_coef(image.shape[0])
    DFT_cols = np.dot(np.linalg.inv(DFT_mat_cols), image.T).T
    final_DFT = np.dot(np.linalg.inv(DFT_mat_rows), DFT_cols)
    # normalizing the result with 1/N*M
    return 1/(image.shape[0] * image.shape[1]) * final_DFT


def conv_der(im):
    dx = scipy.signal.convolve2d(im, deriv_vec, mode='same')
    dy = scipy.signal.convolve2d(im, np.transpose(deriv_vec), mode='same')
    magnitude = np.zeros(shape=(im.shape[0], im.shape[1]))
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            magnitude[x][y] = np.sqrt(np.abs(dx[x][y])**2 + np.abs(dy[x][y])**2)
    return magnitude


def fourier_der(im):
    im_dft = DFT2(im)
    im = np.fft.fftshift(im_dft)
    # initializing arrays for derivatives and the magnitude matrices
    dx = np.zeros(shape=(im.shape[0], im.shape[1]), dtype=np.complex64)
    dy = np.zeros(shape=(im.shape[0], im.shape[1]), dtype=np.complex64)
    magnitude = np.zeros(shape=(im.shape[0], im.shape[1]))
    for u in range(im.shape[0]):
        for v in range(im.shape[1]):
            dx[u][v] = im[u][v] * (u - im.shape[1]/2)
            dy[u][v] = im[u][v] * (v - im.shape[0]/2)
    # shifting and converting the fourier matrices of the derivatives
    dx = np.fft.ifftshift(dx)
    dy = np.fft.ifftshift(dy)
    dx = IDFT2(dx)
    dy = IDFT2(dy)
    # calculating magnitude using the mean square function
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            magnitude[x][y] = np.sqrt(np.abs(dx[x][y])**2 + np.abs(dy[x][y])**2)
    return magnitude


def create_gaussian_kernel(size):
    bin_arr = np.array([1, 1])
    org_arr = np.array([1, 1])
    sum = 0
    gaussian_matrix = np.zeros(shape=(size, size))
    # TODO: what if size==1 - should return kernel with [1] ?
    if (size == 1):
        # special case, returning a [1] matrix
        return np.array([1])
    for i in range(size-2):
        # iterating to create the initial row of the kernel
        bin_arr = scipy.signal.convolve(bin_arr, org_arr)
    # calculating values on each entry in matrix
    for x in range(size):
        for y in range(size):
            gaussian_matrix[x][y] = bin_arr[x] * bin_arr[y]
            sum += gaussian_matrix[x][y]
    # TODO: search for element-wise multiplication for vector*vector=matrix
    # TODO: maybe create a matrix from repeated row vector
    # normalizing matrix to 1
    for x in range(size):
        for y in range(size):
            gaussian_matrix[x][y] /= sum
    return gaussian_matrix

def blur_spatial(im, kernel_size):
    # assuming kernel_size is odd
    gaussian_kernel = create_gaussian_kernel(kernel_size)
    conv_im = scipy.signal.convolve2d(im, gaussian_kernel, mode='same')
    return conv_im


def blur_fourier(im, kernel_size):
    # initializing vars
    kernel = create_gaussian_kernel(kernel_size)
    padded = np.zeros(im.shape).astype(complex)
    rows = im.shape[0] - kernel.shape[0]
    # calculating dimensions for top/bottom size
    bottom = int(np.floor(rows / 2)) + kernel.shape[0] + 1
    top = int(np.floor(rows / 2)) + 1
    columns = im.shape[1] - kernel.shape[1]
    # calculating dimensions for left/right sizes
    left = int(np.floor((columns / 2))) + 1
    right = int(np.floor(columns / 2)) + kernel.shape[1] + 1
    # adding the kernel to the padded matrix
    padded[top:bottom, left:right] += kernel
    shifted_ker = np.fft.ifftshift(padded)
    dft_shifted_ker = DFT2(shifted_ker)
    dft_im = DFT2(im)
    # multiplying pointwise elements
    updated = dft_im * dft_shifted_ker
    return np.real(IDFT2(updated))

def display_fourier(im):
    im = np.log(1+np.abs(im))
    plt.imshow(im, cmap='gray')
    plt.show()

pic = read_image("D:/3/HK2/XLA/Giua_Ky/20133119_LePhuocYen_GiuaKy/BTChuong3/Ex3.17/cat.jpg",1)
plt.imshow(pic)
plt.show()
pic = blur_spatial(pic, 10,)
display_fourier(pic)
plt.pause(3)
plt.close()