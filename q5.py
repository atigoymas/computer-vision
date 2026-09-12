import cv2

user_input = input("Do you want to do: \n1. Canny Edge Detection    \n2. Image Thresholding     \n3. Bitwise operations \nEnter your choice (1-3): ")
file_input = input("Enter the name of the image file with extension: ")
with open(file_input, 'rb') as f:
    image1 = cv2.imread(file_input, 0)
    h, w = image1.shape[:2]

if user_input == '1':
    canny_img = cv2.Canny(image1, 100, 200)
    cv2.imshow('Canny Edge Detection', canny_img)
    cv2.imwrite('canny_edge_detection.png', canny_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if user_input == '2':
    ret, thres_img = cv2.threshold(image1, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow('Image Thresholding', thres_img)
    cv2.imwrite('image_thresholding.png', thres_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if user_input == '3':
    file_input2 = input("Enter the name of the second image file with extension: ")
    with open(file_input2, 'rb') as f:
        image2_diff_size = cv2.imread(file_input2, 0)
        image2 = cv2.resize(image2_diff_size, (w, h),  interpolation=cv2.INTER_AREA)

    bitwise_and = cv2.bitwise_and(image1, image2)
    bitwise_or = cv2.bitwise_or(image1, image2)
    bitwise_not = cv2.bitwise_not(image1)
    cv2.imshow('Bitwise AND', bitwise_and)
    cv2.imshow('Bitwise OR', bitwise_or)
    cv2.imshow('Bitwise NOT', bitwise_not)
    cv2.imwrite('bitwise_and.png', bitwise_and)
    cv2.imwrite('bitwise_or.png', bitwise_or)
    cv2.imwrite('bitwise_not.png', bitwise_not)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Enter a number between 1 and 3")
    
    