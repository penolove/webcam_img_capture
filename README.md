# webcam_img_capture

# naive examples of webcam
capture.py
capture_img_duration.py

[Monitor and Summary]

require oslo.config with
```
 pip install 'oslo.config<2.0.0' 
```

and put your setting in app.conf (cate list, target path to save images)
(the category list can't be in two lines, due to some django issues)

# clean files first
./clean_data.sh
# creating a db with sqlite (will create a db with Images table)
./sqlite.sh 

# Monitor and Summary , saving images to target folder from web cam 
python capture_MAS_webcam.py [target]

## my home DVR example

python capture_MAS_DVR.py [target]
