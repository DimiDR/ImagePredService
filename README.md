# ImagePredService
Django Web Service with Tensorflow Image prediction

# Installation
## Framework
Python 3.6  
$ pip install django  
$ pip install djangorestframework

## Machine Learning
$ pip install tensorflow==2.0.0  
$ pip install keras==2.1.5  
$ pip install pillow==7.0.0

Make sure the Tensorflow Version 2.0.0 is installed. Other Versions cause different errors.  
New TF versions could be more stabe in the future (Today: 29.01.2020).  

# Usability
## Model Training
Check the tutorials to train your model.  
Create two files "labels.txt" and "saved_model.pb" and copy into this project.  

## Run Django
Install the prerequisites.  
Run in virtual environment.  
$ cd "cloned directory"  
$ python manage.py runserver  
Settings for postman:  
[Postman](postman.jpg)  
Recreate Postman in application.  
Response:  
"predicted" - label from "labels" with highest probability  
"defect" - first entry in "labels" and its probability  
"ok" - seccond  entry in "labels" and its probability  
"robotarm" - third entry in "labels" and its probability  
"id" - ID fron Django DB  
"file" - Link to file  

# Additional informations
There is no picture segmentation only picture classification.  
The uploaded picture will get an ID.  
Only the current picture exists in Database and File Server.  
Old picture will be deleted when uploading the new picture to save space on server.  

# Links to Tutorials
## Rest Framework
https://www.techiediaries.com/django-rest-image-file-upload-tutorial/

## Machine Learning
Tensorflow Model was trained using this sources. The Model was trained in Colab (Google Drive).  
https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/tf2_image_retraining.ipynb#scrollTo=FlsEcKVeuCnf    https://github.com/tensorflow/hub  

## Deployment to PYTHONANYWHERE
https://www.youtube.com/watch?v=Y4c4ickks2A  