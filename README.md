# USPS-Object-Detection
* Yolo4 model trained with Darknet that detects the USPS logo in images and alerts you through email.
* Keep in mind, this is not the strongest model as it was trained with no validation however it works very well with only 2000 iterations.

# Requirements
* Have darknet (From AlexeyAB) compiled with OPENCV and LIBSO enabled in Makefile
* If using python code, see required modules
# How to use:
* Make sure you have downloaded the [files](https://drive.google.com/drive/folders/1e1wAt8KT7OssTvF09YhJNGCRS4mwyoXu?usp=sharing): yolo-obj_final.weights, yolo-obj.cfg, obj.data, obj.names
* Make sure OpenCV knows where your own files are (weights,cfg,data) 
  * In obj.data, make sure you have renamed the path of the obj.names to the correct path on your system.


![Alt Text](https://thumbs.gfycat.com/ElderlyBleakDoctorfish-size_restricted.gif)

