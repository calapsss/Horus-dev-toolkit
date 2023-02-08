# Eyes v1

## Description
Raspberrypi data collector for Horus
- Built in facial detection 
- Automatic data transfer to s3 bucket



## Installation
Check that your Picamera is working properly by running the following command:
```libcamera-hello```

Update and upgrade your Raspberry Pi by running the following commands:
```
sudo apt-get update
sudo apt-get upgrade
```

Install the required libraries by running the following command:
```
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install qt4-dev-tools
```
Install OpenCV by running the following command:
```
pip install opencv-python
```

Install tinys3 Library
```
pip install tinys3
```

Install pyyaml Library
```
pip install pyyaml
```

Update the config.yml and provide AWS S3 Credentials and bucket name

## Usage

Run
```
python3 main.py
```


## References
[] https://github.com/rob5standingby/raspberry-pi-s3-cam/blob/master/s3cam.py
[] https://github.com/calapsss/face_detection_tutorial
[] https://github.com/smore-inc/tinys3

