# -*- coding: utf-8 -*-
"""Copy of Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OeOuGEaEHL2SiosFHX5e_tjvlz9brLug
"""

# Commented out IPython magic to ensure Python compatibility.
# pip3 install openmim
# mim install mmengine
# mim install mmdet
# mim install "mmcv>=2.0.0"
# pip install gradio
# pip install numpy
# # !pip install -U numpy
# # !pip install numpy --upgrade
# git clone https://github.com/open-mmlab/mmpose.git
# # %cd mmpose
# pip install -e .

# !cp -r '/content/drive/MyDrive/CLPS 0950 Python/new_data' 'new_data/'

import glob 
from pathlib import Path 

images = Path('/content/drive/MyDrive/CLPS 0950 Python/new_data').rglob('*.png')
images =[ str(im) for im in images]

from mmpose.apis import MMPoseInferencer

import numpy
import matplotlib.pyplot as plt 
import cv2
import gradio as gr

if __name__ == "__main__":
   print("hi")


    inferencer = MMPoseInferencer(
        pose2d='/content/mmpose/configs/hand_2d_keypoint/topdown_heatmap/onehand10k/td-hm_res50_8xb32-210e_onehand10k-256x256.py',
        pose2d_weights='https://download.openmmlab.com/mmpose/top_down/resnet/res50_onehand10k_256x256-e67998f6_20200813.pth'
    )

    #y_data
    inferencer = MMPoseInferencer('hand')
    image = images[0]

    x_data = []
    y_data = []
    for image in images:
    label = image.split('/')[-2]
    img = cv2.imread(image)
    # The MMPoseInferencer API employs a lazy inference approach,
    # creating a prediction generator when given input
    result_generator = inferencer(image)
    result = next(result_generator)
    #plt.imshow(img)
    x = [a[0] for a in result['predictions'][0][0]['keypoints']]
    y = [a[1] for a in result['predictions'][0][0]['keypoints']]
    x1 = min(x)
    x2 = max(x)
    y1= min(y)
    y2 = max(y)

    newx = [(x-x1)/(x2-x1) for x in x]
    newy = [(y-y1)/(y2-y1) for y in y]
    X = newx + newy 
    y = label 
    #plt.scatter(x,y)
    #plt.plot(x1-10,y1-10,'o',color='orange')
    #plt.plot(x2+10,y2+10,'o',color='orange')
    x_data.append(X)
    y_data.append(y)
    plt.scatter(newx,newy)
    img=plt.show()

    from sklearn import svm
    import numpy as np

    clf = svm.SVC(decision_function_shape='ovo')
    x_data = np.array(x_data)
    clf.fit(x_data, y_data)

    np.shape(x_data[29])

    clf.predict([x_data[29]])[0]

    y_data[29]

    img

    !python demo/topdown_demo_with_mmdet.py \
        demo/mmdetection_cfg/cascade_rcnn_x101_64x4d_fpn_1class.py \
        https://download.openmmlab.com/mmpose/mmdet_pretrained/cascade_rcnn_x101_64x4d_fpn_20e_onehand10k-dac19597_20201030.pth \
        configs/hand_2d_keypoint/topdown_heatmap/onehand10k/td-hm_hrnetv2-w18_8xb64-210e_onehand10k-256x256.py \
        https://download.openmmlab.com/mmpose/hand/hrnetv2/hrnetv2_w18_onehand10k_256x256-30bc9c6b_20210330.pth \
        --input tests/data/onehand10k/9.jpg \
        --show --draw-heatmap

    
    inferencer = MMPoseInferencer('hand')
    def flip(im):
        result_generator = inferencer(im)
        result = next(result_generator)
        x = [a[0] for a in result['predictions'][0][0]['keypoints']]
        y = [a[1] for a in result['predictions'][0][0]['keypoints']]
        x1 = min(x)
        x2 = max(x)
        y1= min(y)
        y2 = max(y)

        newx = [(x-x1)/(x2-x1) for x in x]
        newy = [(y-y1)/(y2-y1) for y in y]
        sample = newx+newy 
        pred = clf.predict([x_data[0]])[0]
        
        # print(type(im))
        # for x,y in zip(detx,dety):
        #   im = cv2.circle(im,(int(x),int(y)),10,(255, 0, 0))
        font = cv2.FONT_HERSHEY_SIMPLEX
    
        # org
        org = (50, 50)
        
        # fontScale
        fontScale = 1
        
        # Blue color in BGR
        color = (255, 0, 0)
        
        # Line thickness of 2 px
        thickness = 2
        
        # Using cv2.putText() method
        im = cv2.putText(im, pred, org, font, 
                        fontScale, color, thickness, cv2.LINE_AA)
        return im

    demo = gr.Interface(
        flip, 
        gr.Image(source="webcam", streaming=True), 
        "image",
        live=True
    )
    demo.launch(debug=True)

    img = cv2.imread('/content/drive/MyDrive/CLPS 0950 Python/new_data/test.png')
    # The MMPoseInferencer API employs a lazy inference approach,
    # creating a prediction generator when given input
    result_generator = inferencer('/content/drive/MyDrive/CLPS 0950 Python/new_data/test.png')
    result = next(result_generator)

    x = [a[0] for a in result['predictions'][0][0]['keypoints']]
    y = [a[1] for a in result['predictions'][0][0]['keypoints']]
    x1 = min(x)
    x2 = max(x)
    y1= min(y)
    y2 = max(y)

    newx = [(x-x1)/(x2-x1) for x in x]
    newy = [(y-y1)/(y2-y1) for y in y]
    X = newx + newy 

    clf.predict([X])[0]

    # from PIL import Image

    test_images = Path('/content/drive/MyDrive/CLPS 0950 Python/asl-alphabet-test').rglob('*.jpg')
    test_images =[ str(im) for im in test_images]
    print(np.shape(test_images))

    inferencer = MMPoseInferencer('hand')
    # image = test_images[0]

    x_data = []
    y_data = []
    accuracy = 0
    for image in test_images:
    label = image.split('/')[-2]
    img = cv2.imread(image)
    # The MMPoseInferencer API employs a lazy inference approach,
    # creating a prediction generator when given input
    result_generator = inferencer(image)
    result = next(result_generator)
    #plt.imshow(img)
    x = [a[0] for a in result['predictions'][0][0]['keypoints']]
    y = [a[1] for a in result['predictions'][0][0]['keypoints']]
    x1 = min(x)
    x2 = max(x)
    y1= min(y)
    y2 = max(y)

    newx = [(x-x1)/(x2-x1) for x in x]
    newy = [(y-y1)/(y2-y1) for y in y]
    X = newx + newy
    
    pred = clf.predict([X])[0]
    if (pred == label):
        accuracy += 1
    
    accuracy / len(test_images) 