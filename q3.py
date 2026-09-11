import cv2

def capture_video(save=False):
    camera = cv2.VideoCapture(0)
    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    recorded_video = None 
    if save:
        codec = cv2.VideoWriter_fourcc(*'XVID')
        recorded_video = cv2.VideoWriter('recorded_video.avi', codec, 20, (frame_width, frame_height))
          
    while True:
        success, image = camera.read()
    
        if not success:
            print("Failed to capture image")
            break

        if save and recorded_video is not None:
            recorded_video.write(image) 

        cv2.imshow('Recording', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('Quitting the recording')
            break

    camera.release()

    if recorded_video is not None:
        recorded_video.release()
        
    cv2.destroyAllWindows()

image_input = input("Do you want to record(r) or record and save the file(s)? : ")
if image_input.lower() == 'r':
    capture_video()
elif image_input.lower() == 's':
    capture_video(save=True)
    print("Video recorded and saved as 'recorded_video.avi'")
   