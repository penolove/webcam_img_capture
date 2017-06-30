import cv2
import time
cam = cv2.VideoCapture(0)


img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break
    time.sleep(1)
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

cam.release()

cv2.destroyAllWindows()
