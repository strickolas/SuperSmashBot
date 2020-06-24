import cv2

from matplotlib import pyplot as plt
from PIL import Image


class CannyEdgeDetection:
    def __init__(self):
        pass

    def __call__(self, image: Image) -> type(Image):
        return cv2.Canny(image, 100, 200)
