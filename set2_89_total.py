
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
#the path for the folder of the images
mypath='../new/80nm_dataset_2_mixedexperiments/80nm_dataset_2_mixedexperiments/test'
#the next counter is only for counting and and reg percantage
neg_count = 0
pos_count = 0
neg_total = 0
pos_total = 0
neg_hit = 0
neg_miss = 0
pos_hit = 0
pos_miss = 0
i=0
#the next following path for the annotations and open it
with open('../new/80nm_dataset_2_mixedexperiments/80nm_dataset_2_mixedexperiments/annotations_test.csv', 'r') as rf:
 reader = list(csv.reader(rf))
# # the following loop for counting the pos+ and neg- from the annotations  
for K in reader:
     if(str([K[1]])==str("['1']")):
       pos_total = pos_total+1
     else:
       neg_total = neg_total +1
#open the path for the image folder 
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
# the loop funtion for gurantee that the name of the images is inorder
for i in range (0, len(onlyfiles)):
  onlyfiles[i]= str(i)+'.png'
  print(str(onlyfiles[i])+"\t") # for debugging 
#list for images   
print(str(onlyfiles))
images = np.empty(len(onlyfiles), dtype=object)
#Algorithms 
for n in range(0, len(onlyfiles)):
            i=n
            #reading the image 
            images[n] = cv2.imread(join(mypath,onlyfiles[n]),0 )
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step0' , 'Image '+str(n)+'.png'), images[n]) 

            #histogram equaliztion just for the distiputed the image intinsity
            equ = cv2.equalizeHist(images[n])
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step1' , 'Image '+str(n)+'.png'), equ) 

            #log for increase the intisity level
            img_log = np.array(255*(equ/255)**0.55,dtype='uint8')
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step2' , 'Image '+str(n)+'.png'), img_log) 

            median = cv2.GaussianBlur(img_log, (3,3),0)
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step3' , 'Image '+str(n)+'.png'), median) 

            median2 = cv2.GaussianBlur(median, (3,3),0)
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step4' , 'Image '+str(n)+'.png'), median2) 

            median3 = cv2.GaussianBlur(median2, (3,3),0)
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step5' , 'Image '+str(n)+'.png'), median3)
            median5 = cv2.GaussianBlur(median3, (3,3),0)
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step6' , 'Image '+str(n)+'.png'), median5)
            


            #the threshold level spicified after cheking the GUI
            retval, the = cv2.threshold(median5,197,255,cv2.THRESH_BINARY)
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step8' , 'Image '+str(n)+'.png'), the)

            #to getred of the noise 
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
            opeee = cv2.erode(the,kernel,iterations =2)
            #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/steps/step9' , 'Image '+str(n)+'.png'), opeee2)

            #to connect the images if its so small 
            kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
            opeee2 = cv2.morphologyEx(opeee, cv2.MORPH_CLOSE, kernel2)
          
 
            # height, width, number of channels in image
            #draw rectangle on the image to getred of the noise in the surounding 
            height = opeee2.shape[0]
            width = opeee2.shape[1]        
            image = cv2.rectangle(opeee2,(0,0), (height,width), (0,0,0), 30)
            
            #our assumption that after our algorithn if thre's any pixel white, then it's positive 
            if cv2.countNonZero(image)<1: # negative image 

                      neg_count = neg_count +1
                      print(str(i)+" Neg")
                      cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/neg_output_all' , 'Image '+str(n)+'.png'), image)

                      #check if it's hit 
                      if(str([reader[i][1]])==str("['0']")): 
                        neg_hit = neg_hit +1
                        #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/neg_output' , 'Image '+str(n)+'.png'), image)

                        #if it should be pos but my algo said it's neg
                      else:
                        neg_miss = neg_miss +1
                        #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/NEG_OUT_WRONG' , 'Image '+str(n)+'.png'), image)

            else: #positive image
                    pos_count = pos_count +1
                    print(str(i)+" pos")
                    cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/pos_output_all' , 'Image '+str(n)+'.png'), image)

                    if(str([reader[i][1]])==str("['1']")):
                        pos_hit = pos_hit +1
                        #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/pos_output' , 'Image '+str(n)+'.png'), image)

                    else:
                        pos_miss = pos_miss +1
                        #cv2.imwrite(os.path.join('D:/edu/image/project/ubunto/POS_OUT_WORNG' , 'Image '+str(n)+'.png'), image)
           # for debugging 
            print(n)

cv2.waitKey(0) 

print("Pos: "+str(pos_count)) 						# total pos i predict
print("neg: "+str(neg_count)) 				 		# total neg i predict
print("Pos Total (actual): "+str(pos_total)) 		# total pos from annotation
print("neg Total (actual): "+str(neg_total)) 		# total neg from anotation
print("Pos hit (actual): "+str(pos_hit)) 	 		# pos hit-predict 
print("pos miss (actual): "+str(pos_miss))	 		# pos i miss-predict it 
print("neg hit (actual): "+str(neg_hit))	 		# neg hit-predict 
print("neg miss (actual): "+str(neg_miss))   		# pos i miss-predict it
print("pos % :"+str(((pos_hit)/(pos_total))*100))	# pos % prediction
print("neg % : "+str(((neg_hit)/(neg_total))*100))  # neg % predection
print("total reg % :"+str((((pos_hit)+(neg_hit))/(pos_total+neg_total))*100)) # total reg % 

cv2.destroyAllWindows() 
