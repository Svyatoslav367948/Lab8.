import cv2

img=cv2.imread('variant-8.jpg', 1)
print(img)
print(img.shape)
# the_centre=((img.shape[0])/2, (img.shape[1])/2)
# print(the_centre)
# dlina1 = 387.5-200
# dlina2 = 387.5+200
# shirina1 = 600+200
# shirina2 = 600-200
# print(dlina1, dlina2, shirina1, shirina2)
photo = img[188:588, 400:800]
cv2.imshow('original', img)
cv2.imshow('cropped', photo)
cv2.waitKey(0)
cv2.imwrite("photo.400x400.png", photo)

