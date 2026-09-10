import cv2
image_input = input("Do you want to show the image or save it? (show/save): ")
image = cv2.imread('input_image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
if image_input.lower() == 'show':
    cv2.imshow('Screenshot image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif image_input.lower() == 'save':
    output = cv2.imwrite('Output_image.png', image)
