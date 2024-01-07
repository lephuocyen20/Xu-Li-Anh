
import cv2

# Histogram Equalization function
def histo_equal(image_input: str, adjType: str = "local", colorInfo: str = "color"):

    # Load image_input
    anh = cv2.imread(image_input)
    # If user wants grayscale output, reload as grayscale image_input
    if(colorInfo == "gray"):
        anh = cv2.imread(image_input, 0)

    # If image_input number of dimensions is 2 perform grayscale operations
    if(anh.ndim == 2):
        # Perform global histogram equilazation
        if(adjType == 'global'):
            output = cv2.equalizeHist(anh)

        # Perform local adaptive histogram equilazation
        else:
            clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(10, 10))
            output = clahe.apply(anh)

    # If image_input dimension is not 2 it will be 3; perform color manipulations
    else:
        # Create HSI representation of image_input
        # Used to manipulate Intensity channel of image_input
        HSV = cv2.cvtColor(anh, cv2.COLOR_BGR2HSV)
        V = HSV[:, :, 2]

        # Perform global histogram equilazation
        if(adjType == 'global'):
            equalized = cv2.equalizeHist(V)

        # Perform local adaptive histogram equilazation
        else:
            clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(10, 10))
            equalized = clahe.apply(V)

        # Use new Intensity channel to form HSI image_input
        HSV[:, :, 2] = equalized

        # Return back to rgb space
        output = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)

    # Display input and output image_input
    cv2.imshow("Truoc", anh)
    cv2.imshow("Sau", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
histo_equal("D:/3/HK2/XLA/Giua_Ky/20133119_LePhuocYen_GiuaKy/BTChuong3/Ex3.8/lion.jpg")
