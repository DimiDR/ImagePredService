import os
from django.conf import settings
import numpy as np
import tensorflow as tf
#import tensorflow_hub as hub
from keras.preprocessing import image

#from keras.models import load_model
import ntpath

class ImageRecognition():
    #Model
    model_path = os.path.join(settings.STATIC_ROOT, "imagerec")
    model = tf.keras.models.load_model(model_path)
    #Labels
    labels_path = os.path.join(settings.STATIC_ROOT, "imagerec\labels.txt")
    imagenet_labels = np.array(open(labels_path).read().splitlines())

    def classifyImage(self, image_path):
        # dimensions of our images
        image_path_full = os.path.join(settings.MEDIA_ROOT, ntpath.basename(image_path))
        img_width, img_height = 224, 224
        img = image.load_img(image_path_full, target_size=(img_width, img_height))
        img_n = np.array(img)/255.0
        result = self.model.predict(img_n[np.newaxis, ...])
        print('Class and Number of Classes: ', result.shape, 'Probability of Classses: ', np.around(result * 100, decimals=1) )
        #top probability class
        predicted_class = np.argmax(result[0], axis=-1)
        predicted_class_name = self.imagenet_labels[predicted_class]
        print('Predicted Class Name: ', predicted_class_name)

        parameter = {"predicted": predicted_class_name}
        for i in range(len(self.imagenet_labels)):
            parameter[self.imagenet_labels[i]] = np.around(result * 100, decimals=1)[0][i]

        # return predicted class and the probabilities for the classes
        return parameter