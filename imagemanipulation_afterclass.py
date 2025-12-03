import cv2
import matplotlib. pyplot as plt
image = cv2. imread ("dog.avif")
image_rgb = cv2. cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title ("RGB Image")
plt.show()
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap = "gray")
plt.title ("Grayscale Image")
plt.show
cropped_image = image[100: 300, 200: 400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()
cropped_image = cv2. getRotationMatrix2D(+45)
cv2.warpAffine
np.ones = (50)
cv2.add()
cv2.imwrite("output_images" )
