import cv2

#Black & white Image (Gray Scale)
# img = cv2.imread("Tulips.jpg",0)
#Coloured Image
img = cv2.imread("Tulips.jpg",1)

print(img)
print(img.shape)    #Image Size

resized_image = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
# cv2.imwrite("Tulips_resized.jpg",resized_image)

cv2.imshow("Resized Image",resized_image)
cv2.waitKey()
cv2.destroyAllWindows()