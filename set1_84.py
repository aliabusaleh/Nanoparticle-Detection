
from os import listdir
from os.path import isfile, join
import os
import glob
import numpy as np 
import cv2
from skimage import data
from skimage.morphology import disk
from skimage.filters.rank import equalize
import csv

mypath='../new/80nm_dataset_1_splitbyexperiment/80nm_dataset_1_splitbyexperiment/test'
neg_count = 0
pos_count = 0
neg_total = 0
pos_total = 0
neg_hit = 0
neg_miss = 0
pos_hit = 0
pos_miss = 0
i=0
with open('../new/80nm_dataset_1_splitbyexperiment/80nm_dataset_1_splitbyexperiment/annotations_test.csv', 'r') as rf:
 reader = list(csv.reader(rf))
for K in reader:
     if(str([K[1]])==str("['1']")):
       pos_total = pos_total+1
     else:
       neg_total = neg_total +1

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
for i in range (0, len(onlyfiles)):
  onlyfiles[i]= str(i)+'.png'
  print(str(onlyfiles[i])+"\t")
print(str(onlyfiles))
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
            i=n
            images[n] = cv2.imread(join(mypath,onlyfiles[n]),0 )
            equ = cv2.equalizeHist(images[n]) 
            img_log = np.array(255*(equ/255)**0.70,dtype='uint8')
            #########################
            median5 = cv2.bilateralFilter(img_log,3,85,85)
            median = cv2.medianBlur(median5,3)
            median3 = cv2.medianBlur(median, 3)
            median4 = cv2.GaussianBlur(median3, (5,5),0)
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step_1' , 'Image '+str(n)+'.png'), median4) 
            retval, the = cv2.threshold(median4,196,255,cv2.THRESH_BINARY)
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step_2' , 'Image '+str(n)+'.png'), the) 
            kernel = np.ones((3,3), np.uint8)
            CLOSEING = cv2.erode(the,kernel,iterations =1)
 
            # height, width, number of channels in image
            height = CLOSEING.shape[0]
            width = CLOSEING.shape[1]        
            image = cv2.rectangle(CLOSEING,(0,0), (height,width), (0,0,0), 30) 
            if cv2.countNonZero(image)<4:
                      neg_count = neg_count +1
                      print(str(i)+" Neg")
                      if(str([reader[i][1]])==str("['0']")):
                        neg_hit = neg_hit +1
                        #cv2.imwrite(os.path.join('C:/Users/Ali Gh AbuSaleh/Desktop/edu/image/project/ubunto/neg_output' , 'Image '+str(n)+'.png'), image)
                      else:
                        neg_miss = neg_miss +1
                        #cv2.imwrite(os.path.join('C:/Users/Ali Gh AbuSaleh/Desktop/edu/image/project/ubunto/NEG_OUT_WRONG' , 'Image '+str(n)+'.png'), image)
            else:
                    pos_count = pos_count +1
                    print(str(i)+" pos")
                    if(str([reader[i][1]])==str("['1']")):
                        pos_hit = pos_hit +1
                        #cv2.imwrite(os.path.join('C:/Users/Ali Gh AbuSaleh/Desktop/edu/image/project/ubunto/pos_output' , 'Image '+str(n)+'.png'), image)
                    else:
                        pos_miss = pos_miss +1
                        #cv2.imwrite(os.path.join('C:/Users/Ali Gh AbuSaleh/Desktop/edu/image/project/ubunto/POS_OUT_WORNG' , 'Image '+str(n)+'.png'), image)
          
            print(n)

cv2.waitKey(0) 
print("Pos: "+str(pos_count))
print("neg: "+str(neg_count))
print("Pos Total (actual): "+str(pos_total))
print("neg Total (actual): "+str(neg_total))
print("Pos hit (actual): "+str(pos_hit))
print("pos miss (actual): "+str(pos_miss))
print("neg hit (actual): "+str(neg_hit))
print("neg miss (actual): "+str(neg_miss))
print("pos % :"+str(((pos_hit)/(pos_total))*100))
print("total reg % :"+str((((pos_hit)+(neg_hit))/(pos_total+neg_total))*100))
print("neg % : "+str(((neg_hit)/(neg_total))*100))
cv2.destroyAllWindows() 
