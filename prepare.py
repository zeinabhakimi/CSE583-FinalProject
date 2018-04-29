import matplotlib
matplotlib.use('Agg')
from PIL import Image
import sys
import os
import numpy as np
from os import walk
from pycocotools.coco import COCO
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

def resize(dataDir1, dataDir2, out_dir, out_dir_label , x, ch):

        new_height = 384
      
        #annFile = '%s/annotations/instances_%s.json' % (dataDir1, dataType)
        annFile=dataDir1
        catNms = [ch]
        coco=COCO(annFile)
        cats = coco.loadCats(coco.getCatIds())
        cat_idx = {}
        for c in cats:
            cat_idx[c['id']] = c['name']
        catIds = coco.getCatIds(catNms=catNms)
        imgIds = coco.getImgIds(catIds=catIds );
        imgs=coco.loadImgs(imgIds)
        for img in imgs:
            I = Image.open('%s/%s'%(dataDir2,img['file_name']))
            width, height=float(I.size[0]),float(I.size[1])
            aspect_ratio=width/height
            new_width=int(aspect_ratio* new_height)
            if height > 384:
                image = I.resize((new_width ,new_height), Image.ANTIALIAS)
            else:
                image=I
            x=x+1
            #b=str(x)
            path=str(x).zfill(6) +'.png'
            print (path)
            if not os.path.exists(os.path.join(out_dir,path )):
                #resized_image, aspect_ratio=resize(I, 384)
                image.save(os.path.join(out_dir,path))
            annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
            anns = coco.loadAnns(annIds)
            path_out=os.path.join(out_dir_label,str(x).zfill(6) + '.txt')
            if not os.path.exists(path_out):
                with open(path_out ,'w') as label_file:
                    #print (anns)
                    for a in anns:
                        bbox = a['bbox']
                        if height > 384:
                            print (img['file_name'])
                            bbox[0]=(new_width/width)*bbox[0]
							bbox[1]=(new_height/height)*bbox[1]
                            bbox[2]=(new_width/width)*bbox[2]
                            bbox[3]=(new_height/height)*bbox[3]
                        #a['bbox']= bbox
                        bbox = [bbox[0], bbox[1], bbox[2] + bbox[0], bbox[3] + bbox[1]]
                        bbox = [str(b) for b in bbox]
                        catname = cat_idx[a['category_id']]
                        if catname=="truck":
                           catname=catname.replace('truck', 'Truck')
                        if catname=="person":
                            print (catname)
                            print (catname.replace(" ",""))
                            catname=catname.replace('person', 'Pedestrain')
                        # Format line in label file
                        # Note: all whitespace will be removed from class names
                        #label_file=open('./labels/' + img['file_name'].split('.')[0] + '.txt','w')
                        out_str = [catname.replace(" ","")
                                  + ' ' + ' '.join(['0']*3)
                                  + ' ' + ' '.join([b for b in bbox])
                                  + ' ' + ' '.join(['0']*8)
                                  +'\n']
                        label_file.write(out_str[0])
                        print (out_str[0])
                        
if __name__ == '__main__':
    var1 = sys.argv[1]
    var2 = sys.argv[2]
    var3 = sys.argv[3]
    var4 = sys.argv[4]
    var5 = sys.argv[5]
    if var5 =='train':
        print ('start preparing train data')
        resize(var1,var2, var3 , var4 , 7481, 'person')
        resize(var1,var2, var3 ,var4,  71595, 'truck')

    if var5=='val':
        print ('start preparing val data')
        resize(var1,var2, var3, var4,  77722, 'person')
        resize(var1,var2, var3, var4,  80415, 'truck')

                                                                                                                                                                 
