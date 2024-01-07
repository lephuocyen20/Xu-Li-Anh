import cv2 
import matplotlib.pyplot as plt
import numpy as np
import copy

class contrastStretch:
    def __init__(self):
        self.i="";
        self.anh_goc="";
        self.cuoiDS=[]
        self.rem=0
        self.L=256
        self.sk=0
        self.k=0
        self.so_dong=0;
        self.so_cot=0;
        
    
    def stretch(self,input_image):
        self.i=cv2.imread(input_image,0);
        self.anh_goc=copy.deepcopy(self.i);
        x,y,z=plt.hist(self.i.ravel(),256,[0,256],label='x')
        self.k=np.sum(x)
        for i in range(len(x)):
            prk=x[i]/self.k
            self.sk+=prk
            last=(self.L-1)*self.sk        
            if self.rem!=0:
                self.rem=int(last % last)
            last = int(last + 1 if self.rem >=0.5 else last)
            self.cuoiDS.append(last)
            self.so_dong=(int(np.ma.count(self.i)/self.i[1].size))
            self.so_cot=self.i[1].size
        for i in range(self.so_cot):
            for j in range(self.so_dong):
                num=self.i[j][i]
                if num != self.cuoiDS[num]:
                    self.i[j][i]=self.cuoiDS[num]
        cv2.imwrite('output_data/ouputImage.jpg',self.i)

    def plotHistogram(self):
        plt.hist(self.i.ravel(),256,[0,256])
        
    def showImage(self):
        cv2.imshow("Ket qua",self.i);
        cv2.imshow("Anh goc",self.anh_goc);
        cv2.waitKey(100000)
        cv2.destroyAllWindows()

stretcher=contrastStretch();
stretcher.stretch("D:/3/HK2/XLA/Giua_Ky/20133119_LePhuocYen_GiuaKy/BTChuong3/Ex3.7/lion.jpg");
stretcher.plotHistogram();
stretcher.showImage();