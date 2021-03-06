# CSE583-Final-Project

## Abstract

Object detection is the problem of finding and classifying a variable number of objects on an image. This can be done by using Deep Learning method like DetectNet which is provided by Nvidia Digits. DetectNet uses single neural network architecture as Yolo for finding both classses and bounding boxes in images. 
Finding diffrent objects in KITTI dataset with DetectNet method is our goal in this project. The problem of using DetectNet to find multi class objects like Car plus Pedestrain in this dataset is reported by other people in foroums, but I did not find any papers refering to this problem. Since Digits is a new good enviroment for using Deep Learning methodes more efficient, I have been motivated to target this issue. 

## FrameWork 

The main framework that I used was Nvidia Digits with Caffe in backend. Here is the link for [Digit](https://github.com/zeinabhakimi/DIGITS) instalation guide.


## Dataset
### For Training and Testing

I used [kitti dataset](http://www.cvlibs.net/datasets/kitti/). Please download the 12 GB images file from [images](http://www.cvlibs.net/download.php?file=data_object_image_2.zipand) and 5 MB labeles file from [labels](http://www.cvlibs.net/download.php?file=data_object_label_2.zip). Save both in a file kitti.

Then use the following code to unzip and split the data into train/val. Input-dir is a path to the dataset file created above.

``
python kitti_data.py -i input-dir -o output-dir
``

### For Transfer Learning

I used [MS-COCO dataset](http://cocodataset.org/#home) for training my network. 
* Please download the 18 GB train images from [train_images](http://images.cocodataset.org/zips/train2017.zip). Extract them to train2017. 
* Please download the 1 GB val images from [val_images](http://images.cocodataset.org/zips/val2017.zip). Extract them to val2017.
* Please download the tran/val_annotation file from [train/val_annotation](http://images.cocodataset.org/annotations/annotations_trainval2017.zip). Extract them to annotations_trainval2017. 
* Please clone  [COCO API](https://github.com/cocodataset/cocoapi) to work with data. 
To install PythonApi run following command under cocoapi-master/PythonAPI :
````
python setup.py build_ext --inplace
rm -rf build
````

To preprocess train dataset and its annotation save prepare.py under cocoapi-master/PythonAPI.
Then make new files: train,train_label,val, val_label in which you want to save your output.
Then run following command:
 
```
python prepare.py input-path-train  input-path-train-labels out-path-trainimages out-path-trainlabels 'train'
```

To preprocess val dataset run following:
 
```
python prepare.py input-path-val  input-path-val-labels out-path-valimages out-path-vallabels 'val'
```
To attach KITTI dataset and create COCO+KITTI dataset please run:

```
python attach.py input-path-kitti-train input-path-kitti-train-labels path-to-createdtrain path-to-created-trainlabels 'train'
```
And for attaching validation data:

```
python attach.py input-path-kitti-val input-path-kitti-val-labels path-to-created-val path-to-created-val-labels 'val'
```
### Training
I used diffrent hyperparmaetrs for each training in digits.
For training multi class detection car and pedesrtian following parametrs give the best results:
learning rate: 0.0001
learning rate function: Exponetial Decay
solver type: Adam

### Pretrained models

* Car-Detection caffe model using KITTI dataset : 20180323-143850-955b_epoch_30.0.tar.gz
* Pedestrian-Detection caffe model using KITTI dataset: 20180321-152256-30b3_epoch_30.0.tar.gz
* Car-Van-Detection caffe model using KITTI dataset:20180328-113456-7bcf_epoch_60.0.tar.gz
* Car-Pedestrian-Detection caffe model using KITTI dataset for 60 and 600 epochs:
 	  20180328-170321-80ae_epoch_60.0.tar.gz
    20180403-173721-8303_epoch_600.0.tar.gz
* Car-Pedestrian caffe model using COCO+KITTI dataset: 20180424-145615-eed4_epoch_100.0.tar.gz

## Evaluating 
```
python test.py 20180323-143850-955b_epoch_30.0.tar.gz car-deploy.prototxt 000023.png
```
## Tested Results
![pic1](images/test-1.png)
![pic2](images/test2.png)
