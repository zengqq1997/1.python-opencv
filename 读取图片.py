import cv2 as cv
img = cv.imread("C:/Users/ZQQ/Desktop/0132.jpg")
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
cv2.destroyAllWindows() 
