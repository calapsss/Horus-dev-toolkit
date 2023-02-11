# Eyes v1
 Face Detection from Raspberry Pi 4 to S3 Bucket 

## Description
Raspberrypi data collector for Horus
- Built in facial detection 
- Automatic data transfer to s3 bucket


## Installation
Check that your Picamera is working properly by running the following command:
```
libcamera-hello
```

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

Install boto3 Library
```
pip install boto3
```

Install pyyaml Library
```
pip install pyyaml
```

## Configuration

Update the config.yml and provide AWS S3 Credentials and bucket name
- The yml file will contain information that you will input yourself
- Add the proper folder path remove the / in the end since it is already in the amazon_path variable

Update the aws-access.txt file
- Add your AWS Access Key ID, AWS Access Key Secret, and preferred region
- Make sure to follow the format in the file

## Usage

Initial Setup in commandline
```
chmod u+x setup.sh
./setup.sh
```

Run file in commandline
```
python3 main.py
```


## References
- https://github.com/calapsss/face_detection_tutorial
- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_file

