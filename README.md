# Nanoparticle Detection

### Ali Abu Saleh Dania Tubaileh

#### An-Najah National University An-Najah National University

#### Computer Engineering department Computer Engineering department



## 1.Abstract

In this project, we will use image processing to detect nanoparticles (e.g., bacteria and fine
dust) in Surface Plasmon Resonance (SPR) images. SURFACE PLASMON RESONANCE (SPR)
imaging for quantification and analysis of nanoparticles in liquid or air samples. This
the project aims to detect the nanoparticles using an application which will be used to get the
the primary situation of samples either it’s infected by the virus or not instead of using neural
network which requires super-computer and consume a massive amount of power
compared to the normal application, using the spatial domain for detection was the
the solution we used to get the 89% detection.

## 2.0 Introduction

Nanoparticles samples in liquid or air samples detecting have been tried over many years
to get the best detection, with this project which has two sets that include over 8000
images with nanoparticle object,  we will use spatial domain analysis with image processing
technique to get efficiency over than (95%) which has been achieved by neural network
and Develop an accessible mobile real-time virus detection that can be used in our daily life
with ne need for a supercomputer, with image processing operation in spatial domain, it will
create the good algorithm to have a clear recognition of the nanoparticle samples in sets of
train and test.

## 2.1 Motivation

In this project, our motivate is to work out the techniques with CVIPTOOLS to find the best
operations in our problem which is the recognition of nanoparticle object(virus),  The
operations to highlight and isolate the nanoparticles in the input image to be more visible
that you can see it with eye human, to get that point many Filters may use.


## 2.2 Background

“ Due to the evolution and emergence of viruses, together with increasing global travel and
transport, there is the risk of spreading epidemic diseases. Therefore, an accessible mobile
the real-time virus detection device is needed” [1] many reasons lead to search for an
the algorithm from image processing techniques to get a clear object in images that is the size
approximately to nano which means a hard size to detect,”Manually analyzing the sensor
data and quantify the particles is a time-consuming task. An evaluation of a single data set
by an expert with a few hundred particles can take several hours” [2] so to find the best
operations will be limit it to get the best percentage of success.


## 3.0 problem definition

##### Detect nanoparticles (e.g., bacteria and fine dust) in Surface Plasmon Resonance

## (SPR) images.

As mentioned before the aim to detect the infected samples, as shown in the figure below
in figure 1
We are working with samples where the virus size is 80nm.

## 3.1 Challenges

1. Find the best technique to detect the virus in a spatial domain without using neural network
2. ​Different images with a variety of intensity levels in each dataset.
3. Determine the next step to get accurate recognition for all images in each dataset.
5.​the CVIPTOOLS doesn't deal with the samples and datasets given on MOODLE unless if we open
the image using the Paint in windows then and re-save the image
6. reading images using the function [ with open (‘path)’ ] reads the images out of order (randomly).
7. Choosing the different parameters for each dataset depends on the images in each one.
8. Choosing the best structuring element for the morphological processing as the virus size is similar
to the noise size with a very tiny different.
9. Intensity level for the virus is similar to the noise’s pixels.
10. Get rid of the Paper and salt noise in the surrounding borders.
11. Using the CVIPTools as GUI and find the same function in OpenCV.


## 4.0 Implementation

The programming language that was used is python , then link the libraries​ ​(Numpy
, glob, os and cv (open cv) to the program and using test application which is CVIPTOOLS
that have GUI image processing operation to test the samples to know the order of
techniques that will be implemented using opencv functions in python.

## 4.1 Project stages

### Stage 1: System setup

After reading the problem and consider it, we first decided to use CVIPTools which provides
GUI ( Graphical user interface) to test out solution approach, then change it to a code which
will take a huge amount of images automatically, the following image represents the


testing for our approach using the CVIPTools GUI in Figure 2.
**Figure 2.​ ​** Positive sample (left), negative sample (right) using CVIPTools GUI.
While using the CVIPTools GUI, we had a problem that the application doesn't deal with the
samples given on MOODLE unless if we open the image using the Paint in windows then
and re-save the image, as shown in the following figure 3.


**Figure 3.​** After re-save the image using paint( left image), direct opening with CVIPTools
without using paint ( right image).
Unfortunately, after trying to use the CVIPTools as a coding and try to link to the Visual
studio, we tried but we didn’t manage to do that, we decided to use OpenCV as a library
with Python language and the CVIPTools as testing by using the GUI.

## Stage 2: Image processing

## Part one: Project Handshake

In this part, we worked on the given database, which is 10 images for testing, and in this
stage, we managed to get 100% efficiency on the given samples as following
Sequence Image Number Class Input Preprocessing,
filtering and
thresholding
0  0  Negative
1  5  Negative


2  50  Negative
3  51  Negative
4  52  Negative
5  12912  Negative
6  12915  Negative
7  1  Positive
8  4  Positive
9  53  Positive
10  12913  Positive
11  12914  Positive
**Table 1.​** The output for our first technique.


## 4.1 Implementation of Algorithm

The code was as follows , followed by our approach.
The algorithm whereas follows



## 5.0 Algorithm Design

## Part one approach.

As the varuis is not visible to the human eye, we had to use the histogram equalization 3
times which increase the contrast of the image ,then MedianBlur function to removing
noise in edges ( same as average technique).
In order to handle the whole dataset given we used a function provided by python to open
the folder and read each image and store it in an array ( line 10,11, 12, 13 & 14), the
function used in line 11 require the library OS, and function used at same line (isFile &
listDir) also the same, that’s why we put the following import statements

## Problems in part one approach.

In our first try, we have a problem that we have to count the positive image manually and
compare it to the given dataset, also the program itself can’t decide which one is positive
and which one is negative.
Also, the multistage median creates a new problem which is bridging the gaps between the
noise dots and create an object then convert the negative image into a positive one.
We were unable to test this approach on the training set due to the lack of function which
calculate the positive and negative images.


## Part two: Counter and detection added

In this part, we worked on the problems we faced on the first part, and the code became as
follow,
The first enhancement was to remove the noise without bridging between the gabs, so in
that case we decided to use the morphological technique, which is Erosion followed by
Dilation, the kernel ( mask) was size of 1*3.
The second enhancement was to provide a function that decides which the processed image
either positive or negative, so we used function (CountNonZero), which count the pixels
with their intensity value > 0, which represent the object in our case.
Hypothesis: if the image after the processing contains white pixels → positive, else →
negative.
And the counter added to this stage so we can figure out the accuracy in our techniques.
The output for the negative images whereas follows


, the problems that it contains noise on the edges, and in this case we have to change the
method of detection,
The testing was like follow
Classes
Predicted class Total Recognations
(%)
Positive Negative
Actual
class
positive 6456  2  6458  99.
Negative 1364  5094  6458  78.
Total 7820  5096  12916  89.
We had problems in the thresholding value, noise around edges and the technique we use.

## Part two approach.

In this part, we assume the opening method will not cause a gap bridging, also the
histogram equalization should not be more than 1, also the thresholding value was
selected based on the processing which came up with the middle of the object is 225
( intensity value ), and throw the edges it’s 193, but there's some noise with intensity value
between 193-197, so we decided to select 200 as the cutting edge.


## Problems in part two approach.

The noise around the edges made the negative sample to be determined as positive
sample, the code doesn't give a real percentage, it only gives numbers for each class, the
technique used must be improved to achieve a higher percentage.

## Part Three: final step.

We need to remove the noise around the border because the problem as we mentioned
above that, it doesn't give a real result for negative, so we use Rectangle method to draw
above the borders to hide noise around it, by taking the height and width of the image. In
this case we test code by the train and test Dataset, it disguises noises on the tips of
borders to have a clear result for negative images, after that we repeat the calculation to
ensure that it recognizes the negative image (didn't make the noises around as positive).
Finally ,Achieved a good percentage.
**The code below shows the final image processing technique to detect all viruses
founded on dataset.**


**Set 1:
Set 2:**
Note: the description for each step is on the code comments sections


**Steps for the algorithm:**

1. reading the image
2. histogram equalization just for the distributed the image intensity
3. log for increase the intensity level
4. Smoothing
    a. GaussianBlur for set 2, which does not affect the shape of the noise)


```
b. MedianBlur for set 1, because the virus is bigger so it will not disappear
```
5. Thresholding (the threshold level specified after checking the GUI)
6. Erosion (to get rid of the noise)
7. To connect the remaining white pixels we used the closing method
8. draw a rectangle on the image to get rid of the noise in the surrounding
9. CountNonZero, will return the number of white pixels (our assumption that after
    our algorithm if there's any pixel white, then it's positive)
10.Count the positive and negative images
The main difference between the two algorithms is that in the first dataset the virus is
bigger than the one in the second set, so we have to choose a different value for the “log”
function, also the smoothing function is different as described in step 4.
This is the final code to detect nanoparticles varius using spatial domain analysis , after
these calculations we get a good percentage of detecting that is allowed in our project.


Classes
Experiment Total Recognations
(%)
Positive / actual Negative / actual
Dataset Set 1 1554/ 1850 1560/ 1850 3700  84.
Set 2 3688/ 4154 3725 / 4154 8308  89.
In Details:
**Set1​** :
Positive output from our algorithm: 1844
Negative Output from our algorithm: 1856
Positive Total (Annotation): 1850 Negative Total (Annotation): 1850
Positive hit (actual): 1554 Positive miss (actual): 290
Negative hit (actual): 1560 Negative miss (actual): 296
Positive % of Recognition = 1557/1850 = 84.00%
Negative % of Recognition = 1560/1850 = 84.3243%
Total % of recognition = (1557+1560) / (1850+1850) = 84.16216216216216%
**Set2​** :
Positive output from our algorithm: 4117
Negative Output from our algorithm: 4191
Positive Total (Annotation): 4154 Negative Total (Annotation): 4154
Positive hit (actual): 3688 Positive miss (actual): 429
Negative hit (actual): 3725 Negative miss (actual): 466
Positive % of Recognition = 3688/4154 = 88.781896966779%
Negative % of Recognition = 3725/4154 = 89.
Total % of recognition = (3688+3725) / (4154+4154) = 89.22725084256139%


**Set1 :**
● **sensitivity ​** =(true_positive)/positive
=1554/1850=0.
● **specificity​** =(true_negative)/negative
=1560/1850=0.
● **precision​** =(true_positive)/(((true_positive)+(false_positive))
=1554/(1557+296)= 0.
.
● **Accuracy​** =((true_positive)+(true_negative))/(positive+negative)
=(1554+1560)/(1850+1850)=0.
**Set2:**
● **sensitivity ​** =(true_positive)/positive
=3688/4154=0.
● **specificity​** =(true_negative)/negative
= 3725/4154 = 0.
● **precision​** =(true_positive)/(((true_positive)+(false_positive))
` = (3688/(3688+466))= 0.
● **Accuracy​** =((true_positive)+(true_negative))/(positive+negative)
=(3688+3725)/(4154+4154)= 0.


## 7.0 Summary

Our project about detect nanoparticles (e.g., bacteria and fine dust) in Surface Plasmon
Resonance (SPR) images , we try to solve the problem that is small size of object with image
processing operation to get a good recognition for the object , applying these operation require
accuracy analysis to get a high percentage, we used python language that help getting a good
functions,there was two set to try our algorithms on it,train set which contains images with

##### positive and negative image result,​ ​second set have complex images with mixed positive and

negative results ,so the parameters of the operation will be different from set1,after applying
these techniques there is a percentage to calculate to know the success of recognition if its true
as the result mentioned in sheet or not.


