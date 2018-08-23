#Introduction to AUV Systems

## Here's how the submarine works.

![sub architecture diagram](images/2018-sub-architecture.png)

### ncs-ros.py
1. Captures images with OpenCV
2. Processes the images and sends them to the Movidius with the MVNC API
3. Movidius processes results with neural network
4. Reads the result and sends it to execute.py

### SSD-Mobilenet

### execute.py
1. Reads bounding boxes from ncs-ros.py

Camera &rarr; Movidius &rarr; AI &rarr; Pixhawk

## Software we use
* Ubuntu 16.04
* Git
* ROS
* Caffe
* Movidius API