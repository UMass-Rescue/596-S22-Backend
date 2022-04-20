import cv2

img = cv2.imread('imgs/doorbellDay.jpg')

x = 331
y = 103
w = 230
h = 292

cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0))

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()