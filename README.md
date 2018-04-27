# CSE583-FinalProject

## Abstract

Object detection is the problem of finding and classifying a variable number of objects on an image. This can be done by using Deep Learning method like DetectNet which is provided by Nvidia Digits. DetectNet uses single neural network architecture as Yolo for finding both classses and bounding boxes in images. 
Finding diffrent objects in KITTI dataset with DetectNet method is our goal in this project. The problem of using DetectNet to find multi class objects like Car plus Pedestrain in this datest is reported by other people in foroums, but I did not find any papers refering to this problem. Since Digits is a new good enviroment for uaing Deep Learning methoeds more efficient, I have been motivated to traget this issue. 

## FrameWork 

The main framework that I used was Nvidia Digits with Caffe in backend


## Dataset
### Train and Test dataset

I used [kitti dataset](http://www.cvlibs.net/datasets/kitti/) . You can download the 12 GB image files from [images](http://www.cvlibs.net/download.php?file=data_object_image_2.zipand) and 5 MB label files from  [labels](http://www.cvlibs.net/download.php?file=data_object_label_2.zip). Then put them in a same file. 

Then use the following code to unzip and split the data into train/val. Input-dir is a path to the dataset file created above.  

python kitti_data.py -i input-dir -o output-dir

### dataset used for transfer learning
