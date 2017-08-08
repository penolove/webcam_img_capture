import os
import sys
import cv2
import time
from datetime import datetime
import requests
Debug = True

Dbwrite = True
if Dbwrite:
    import sqlite3
    conn = sqlite3.connect('webcam.db')

def get_img_write_webcam(cam, path , img_name, interval=5):
    ret, frame = cam.read()
    if not ret:
        print("frame not get properly")
        return None
    
    img_path = "{}.jpg".format(os.path.join(path,img_name))
    if Debug: print("current writing to", img_path)
    cv2.imwrite(img_path, frame)
    
    if Dbwrite:
        if Debug : print("current writing to DB with ", img_path)
        conn.execute("insert into images (name,time_folder) \
                      values ('{}','{}')".format(img_name+'.jpg',path));
        conn.commit()
    time.sleep(interval)

def check_path_create(target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        return True
    return False


dir_queue=[]
def post_yolo(prefix,min_path):
    dir_queue.insert(0,min_path)
    if len(dir_queue)>1:
        try:
            dir_path = dir_queue.pop()                                                                 
            r = requests.post("http://localhost:5566/home", data='{"dir_path": "'+prefix+dir_path+'"}')
        except Exception as e:        
            print("====[file monitor] post somewhat fails===") 
            print(e)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage : python capture_SAM.py target_dir")
        sys.exit()
    _, target_dir = sys.argv

    # create/check Folder A : target dir to monitor, contain lots of folder B(date)
    check_path_create(target_dir)
    if not os.path.isdir(target_dir):
        print("given path is not a vaild folder")
        sys.exit()
    
    cam = cv2.VideoCapture(0) # used in webcam
    while True:
        current_time = datetime.now()
        # create folder B for different date
        date_path = os.path.join(target_dir,current_time.strftime("%Y_%m_%d"))
        check_path_create(date_path)
        # create folder C for different hour
        hour_path = os.path.join(date_path,current_time.strftime("%H"))
        check_path_create(hour_path)
        # create folder D for each ten minutes
        min_path = os.path.join(hour_path,current_time.strftime("%M"))
        min_created = check_path_create(min_path)
        if min_created:
            #post previous dir to yolo server
            prefix='../webcam_img_capture/'
            post_yolo(prefix,min_path) 

        # capture images for each interval(default 5s)
        img_name = current_time.strftime("%S")

        ##########################
        # write to images webcam #
        get_img_write_webcam(cam, min_path, img_name)
        ##########################

    cam.release()
    cv2.destroyAllWindows()

