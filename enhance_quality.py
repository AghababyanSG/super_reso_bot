import cv2
from time import time
from selenium.common.exceptions import TimeoutException

# from cv2 import UMat

# import numpy as np

def enhance():
    try:
        path_pic = "test"  # example: "Textures/photo_2022-10-08_22-39-53.jpg"


        img = cv2.imread(path_pic)

        path = "EDSR_x4.pb"
        sr = cv2.dnn_superres.DnnSuperResImpl_create()

        sr.readModel(path)
        print("0")

        # sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        # sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        sr.setModel("edsr", 4)
        print("1")

        start = time()
        result = sr.upsample(img)
        cv2.imwrite('your_pic_enhanced.jpg', result)
        print("with CPU:", time() - start)
    except TimeoutException:
        pass
if __name__ == '__main__':
    enhance()
