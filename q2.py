import cv2
user_file = input("Enter the path of the image: ")
user_input = input("Do you want to draw a: line(l), circle(c), rectangle(r) or add a text(t):  ")
user_input = user_input.lower()
with open(user_file, 'rb') as f:
    image = cv2.imread(user_file, 1)
    x1 = int(input("Enter x coordinate of the first point: "))
    y1 = int(input("Enter y coordinate of the first point: "))
    x2 = int(input("Enter x coordinate of the second point: "))
    y2 = int(input("Enter y coordinate of the second point: "))
    if user_input == 'l':
        output = cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
    elif user_input == 'r':
        output = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
    elif user_input == 'c':
        radius = int(input("Enter the radius of the circle: "))
        output = cv2.circle(image, (x1, y1), radius, (255, 0, 0), 3)
    elif user_input == 't':
        output = cv2.putText(image, "Hey guys!", (x1, y1), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 3)
    else:
        print("Invalid input. Please enter 'l', 'c', 'r', or 't'.")

    

    cv2.imshow('User input image', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    output_file = cv2.imwrite('output_image.png', output)

