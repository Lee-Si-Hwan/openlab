from audioop import avg
import cv2
from matplotlib import pyplot as plt

def get_histogram(path):
    temp = list() #b, g, r
    img = cv2.imread(path,cv2.IMREAD_COLOR)
    histb = cv2.calcHist([img],[0],None,[256],[0,256])
    histg = cv2.calcHist([img],[1],None,[256],[0,256])
    histr = cv2.calcHist([img],[2],None,[256],[0,256])
    print(len(histb))
    print(sum(histb)/len(histb), sum(histg)/len(histg), sum(histr)/len(histr))
    return [sum(histb)/len(histb), sum(histg)/len(histg), sum(histr)/len(histr)]
    

