#  https://mmpose.readthedocs.io/en/latest/overview.html
#MMLab--MMPose package notes (Stella read documentation, introduction, installment instructions)
# 2d hand pose estimation, consists of 8 main components that do important things for detection including datasets

#Ivan Tips (office hours on 04/25/2023)
#Stella's Tasks:
# start woth installing and running MMPose detector
#classifiers to recognize our pistures as their letters
#Stella's and Camille's Tasks:
# take 10 pictures of our hands for each letter (create our dataset)
#Camille's tasks:
#start working on the interface of the game (interactive aspects, presenting random letters of the english alphabet)

#to do with Ivan in class:
#help with classification and connecting pose detection to our dataset

#final step:
#connect game aspect made by Camille to detection aspect made by Stella= project :)

#notes for MMLab 
# 1. download and install miniconda-- done 04/28
# 2. create conda environment and activate it? --done 04/28
# 3. install pytorch-- done 04/28
# 4. Install MMEngine and MMCV using MIM


#To use a custom dataset in MMPose, you need to add a new config file of the dataset meta information
#$MMPOSE/configs/_base_/datasets/

#example of custon dataset (like the one we are trying to build with the pictures of the letters of the ASL alphabet)
dataset_info = dict(
    dataset_name='mpii',
    paper_info=dict(
        author='Mykhaylo Andriluka and Leonid Pishchulin and '
        'Peter Gehler and Schiele, Bernt',
        title='2D Human Pose Estimation: New Benchmark and '
        'State of the Art Analysis',
        container='IEEE Conference on Computer Vision and '
        'Pattern Recognition (CVPR)',
        year='2014',
        homepage='http://human-pose.mpi-inf.mpg.de/',
    ),
    keypoint_info={
        0:
        dict(
            name='right_ankle',
            id=0,
            color=[255, 128, 0],
            type='lower',
            swap='left_ankle'),
        ## omitted
    },
    skeleton_info={
        0:
        dict(link=('right_ankle', 'right_knee'), id=0, color=[255, 128, 0]),
        ## omitted
    },
    joint_weights=[
        1.5, 1.2, 1., 1., 1.2, 1.5, 1., 1., 1., 1., 1.5, 1.2, 1., 1., 1.2, 1.5
    ],
    # Adapted from COCO dataset.
    sigmas=[
        0.089, 0.083, 0.107, 0.107, 0.083, 0.089, 0.026, 0.026, 0.026, 0.026,
        0.062, 0.072, 0.179, 0.179, 0.072, 0.062
    ])


#In the model config, the user needs to specify the metainfo path of the custom dataset (e.g. $MMPOSE/configs/_base_/datasets/custom.py) as follows:
# dataset and dataloader settings
dataset_type = 'MyCustomDataset' # or 'CocoDataset'

train_dataloader = dict(
    batch_size=2,
    dataset=dict(
        type=dataset_type,
        data_root='root/of/your/train/data',
        ann_file='path/to/your/train/json',
        data_prefix=dict(img='path/to/your/train/img'),
        # specify the new dataset meta information config file
        metainfo=dict(from_file='configs/_base_/datasets/custom.py'),
        ...),
    )

val_dataloader = dict(
    batch_size=2,
    dataset=dict(
        type=dataset_type,
        data_root='root/of/your/val/data',
        ann_file='path/to/your/val/json',
        data_prefix=dict(img='path/to/your/val/img'),
        # specify the new dataset meta information config file
        metainfo=dict(from_file='configs/_base_/datasets/custom.py'),
        ...),
    )

test_dataloader = val_dataloader

#datasets: many option in the MMPose detector, recommended is COCO, which I would have to download and train to apply to the hand signals
#https://mmpose.readthedocs.io/en/v0.29.0/demo.html#d-hand-keypoint-demo


#05/01/2023
#problem that Stella has been facing:
# the miniconda installed but maybe not in the right directory? it is in my computer but won't listen to python and install the rest of the things I need 
# maybe need to uninstall and install again, have been stuck on that for the entire weekend
#

#05/03/2023
#preparing my dataset and introducing it to MMPose:

#1. dataset should be in a specific format, such as COCO or MPII. Each image should be annotated with the corresponding keypoints for the pose estimation task. 
# use tools such as LabelImg or COCO Annotator to annotate your dataset.

#2. Convert dataset to the MMPose format: MMPose requires the dataset to be in a specific format. 
# use the tools/convert_datasets.py script in the MMPose repository to convert dataset.

#3. Create a data loader: MMPose uses data loaders to load the dataset during training and evaluation. 
# create a data loader for dataset by creating a new file in the mmpose/datasets directory. use the existing data loaders as a reference.

#4. Register dataset with MMPose by adding it to the DATASET_REGISTRY dictionary in the mmpose/datasets/__init__.py file.

#5. Train the model: Once dataset is registered, use the tools/train.py script. 
# use the --config argument to specify the configuration file for the model. The configuration file should include the name of your dataset and the path to the data.

#6. Evaluate the model: After training, evaluate the model using the tools/test.py script. 
#  use the --config argument to specify the configuration file for your model.

#COCO annotator- downloaded on 05/03 and started uploading images on the online platform to annotate
#labelImg downloaded and installed on 05/03

#got labelImg to open but it quits every time I try to label and image. I will ask Ivan for help