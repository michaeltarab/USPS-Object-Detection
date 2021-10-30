# USPS-Object-Detection
* Yolo4 model trained with Darknet that detects the USPS logo in images. 
* Keep in mind, this is not the strongest model as it was trained with no validation however it works very well with only 2000 iterations.

# Requirements
* The only requirement is that you have darknet (From AlexeyAB) compiled
* Refer to darknet's repository for recommended specs. I attempted this on my Pi 4, and it took over a minute to predict correctly.

# How to use:
* Make sure you have downloaded the [files](https://drive.google.com/drive/folders/1e1wAt8KT7OssTvF09YhJNGCRS4mwyoXu?usp=sharing): yolo-obj_final.weights, yolo-obj.cfg, obj.data, obj.names
* Put them in their corresponding locations
  * Put obj.data in darknet/build/darknet/x64/data
  * Put yolo-obj_final.weights in darknet/backup (OR Wherever you want the weights file located, mine is located in a folder I made called backup)
  * Put obj.data in darknet/build/darknet/x64/data
  * In obj.data, make sure you have renamed the path of the obj.names to the correct path on your system.


![Alt Text](https://thumbs.gfycat.com/ElderlyBleakDoctorfish-size_restricted.gif)

