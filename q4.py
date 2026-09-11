import cv2
import numpy as np

sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])

user_input = input("Do you want to use: \n1. Sharpening filter\n2. Gaussian Blur filter\n3. Median Blur filter\nEnter your choice (1-3): ")
file_name = input("Enter the name of the image file (with extension): ")
with open(file_name, 'rb') as f:
    image = cv2.imread(file_name, cv2.IMREAD_COLOR)

if user_input =='1':
    sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.imwrite('sharpened_image.png', sharpened_image)
elif user_input == '2':
    gaussian_blur_image = cv2.GaussianBlur(image, (3, 3), 0)
    cv2.imshow('Gaussian Blurred Image', gaussian_blur_image)
    cv2.imwrite('gaussian_blurred_image.png', gaussian_blur_image)
elif user_input == '3':
    median_blur = cv2.medianBlur(image, 5)
    cv2.imshow('Median Blurred Image', median_blur)
    cv2.imwrite('median_blurred_image.png', median_blur)
else:
    print("Enter a number between 1 and 3")
cv2.waitKey(0)
cv2.destroyAllWindows() 