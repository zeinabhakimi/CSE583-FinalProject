# CSE583-FinalProject

## Abstract

Object detection is the problem of finding and classifying a variable number of objects on an image. This can be done by using Deep Learning method like DetectNet which is provided by Nvidia Digits. DetectNet uses single neural network architecture as Yolo for finding both classses and bounding boxes in images. 
Finding diffrent objects in KITTI dataset with DetectNet method is our goal in this project. The problem of using DetectNet to find multi class objects like Car plus Pedestrain in this datest is reported by other people in foroums, but I did not find any papers refering to this problem. Since Digits is a new good enviroment for uaing Deep Learning methoeds more efficient, I have been motivated to traget this issue. 

## FrameWork 

The main framework that I used was Nvidia Digits with Caffe in backend


## Dataset
### Train and Test dataset

I used [kitti dataset](http://www.cvlibs.net/datasets/kitti/). Please download the 12 GB images file from [images](http://www.cvlibs.net/download.php?file=data_object_image_2.zipand) and 5 MB labeles file from [labels](http://www.cvlibs.net/download.php?file=data_object_label_2.zip). Save both in a file kitti.

Then use the following code to unzip and split the data into train/val. This would craete 1180 validation and 6373 train images with their labels. Input-dir is a path to the dataset file craeted above.

``
python kitti_data.py -i input-dir -o output-dir
``

### Dataset used for transfer learning

I used [MS-COCO dataset](http://cocodataset.org/#home) for training my network. 
* Please download the 18 GB train images from [train_images](http://images.cocodataset.org/zips/train2017.zip). 
* Please download the 1 GB val images from [val_images](http://images.cocodataset.org/zips/val2017.zip). 
* Please download the tran/val annotation file from [train/val_annotation](http://images.cocodataset.org/annotations/annotations_trainval2017.zip)

