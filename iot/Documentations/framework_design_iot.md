
Camera price cheaper in arduino.

ESP32 CAM -> livestream -> Amazon Kinesis -> EC3 instance -> S3 bucket depending on detection 

Cheap ESP32 Camera 
- streams the video footage

Amazon Kinesis
- connects the stream to the network
- can also be direct to the ESP32

EC3 Instance
- captures livestream
- runs the facial recognition on the video stream  (cv2, opencv, dlib )
- if detects face
- stores the footage to an S3 bucket and trigger api call
- stores face metadata in the database

S3 Bucket
- stores the data / frames necessary



https://stackoverflow.com/questions/55828451/video-streaming-from-ip-camera-in-python-using-opencv-cv2-videocapture

https://github.com/aws-samples/aws-end-to-end-iot-amplify-demo#Setting-Up-Your-Device-in-AWS-IoT-Core

https://aws.amazon.com/kinesis/video-streams/pricing/




