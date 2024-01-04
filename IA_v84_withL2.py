import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from keras.preprocessing.image import ImageDataGenerator
import os


base_dir = r'D:\ImageClassification\data'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# Carpeta con nuestras imágenes de entrenamiento de nevus benignos
train_nevus_dir = os.path.join(train_dir, 'nevus')

# Carpeta con nuestras imágenes de entrenamiento de melanomas
train_melanoma_dir = os.path.join(train_dir, 'melanoma')

# Carpeta con nuestras imágenes de validación de nevus benignos
validation_nevus_dir = os.path.join(validation_dir, 'nevus')

# Carpeta con nuestras imágenes de validación de melanomas
validation_melanoma_dir = os.path.join(validation_dir, 'melanoma')

# Configuramos matplotlib fig, dimensionándolo para que acomode imágenes en 4x4
import matplotlib.image as mpimg
nrows = 4
ncols = 4

fig = plt.gcf()
fig.set_size_inches(ncols*4, nrows*4)
pic_index = 100
train_nevus_fnames = os.listdir( train_nevus_dir )
train_melanoma_fnames = os.listdir( train_melanoma_dir )


next_nevus_pix = [os.path.join(train_nevus_dir, fname)
                for fname in train_nevus_fnames[ pic_index-8:pic_index]
               ]

next_melanoma_pix = [os.path.join(train_melanoma_dir, fname)
                for fname in train_melanoma_fnames[ pic_index-8:pic_index]
               ]

for i, img_path in enumerate(next_nevus_pix+next_melanoma_pix):
  # Configuramos subplot; índices de subplot comienzan en 1
  sp = plt.subplot(nrows, ncols, i + 1)
  sp.axis('Off') # Que no nos muestre los ejes o las líneas de la cuadrícula

  img = mpimg.imread(img_path)
  plt.imshow(img)

plt.show()

# Añadimos nuestros parámetros para aumentar el dataset artificialmente a ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255.,rotation_range = 40, width_shift_range = 0.2, height_shift_range = 0.2, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)

# OJO: El dataset para validación no debe aumentarse artificialmente
test_datagen = ImageDataGenerator( rescale = 1.0/255. )

# Flow training images en batches de 20 usando train_datagen generator
train_generator = train_datagen.flow_from_directory(train_dir, batch_size = 20, class_mode = 'binary', target_size = (224, 224))

# Flow validation images en batches de 20 usando test_datagen generator
validation_generator = test_datagen.flow_from_directory( validation_dir,  batch_size = 20, class_mode = 'binary', target_size = (224, 224))

from tensorflow.keras.applications.vgg16 import VGG16

base_model = VGG16(input_shape = (224, 224, 3), # Configuramos tamaño de imágenes
include_top = False, # Dejamos fuera del modelo base a nuestra última capa completamente conectada (la ReLU)
weights = 'imagenet')

for layer in base_model.layers:
    layer.trainable = False

# Compactamos la capa de salida a 1 dimensión
x = layers.Flatten()(base_model.output)

# Añadimos una capa completamente conectada con 512 neuronas en la capa oculta y activación ReLU
x = layers.Dense(512, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01))(x)

# Añadimos dropout rate de 0.5 (porcentaje de neuronas a las que daremos valor 0 aleatoriamente en cada iteración del entrenamiento)
x = layers.Dropout(0.5)(x)

# Añadimos capa final sigmoide con 1 neurona para el classification output
x = layers.Dense(1, activation='sigmoid', kernel_regularizer=tf.keras.regularizers.l2(0.01))(x)

model = tf.keras.models.Model(base_model.input, x)

model.compile(optimizer = tf.keras.optimizers.RMSprop(lr=0.0001), loss = 'binary_crossentropy',metrics = ['acc'])

# Revisamos que haya GPUs compatibles disponibles
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Entrenamos la red neuronal usando la GPU
with tf.device('/GPU:0'):
    vgghist = model.fit(train_generator, validation_data = validation_generator, steps_per_epoch = 93, epochs = 30)

print(vgghist.history.keys())

import matplotlib.pyplot as plt
plt.plot(vgghist.history["acc"])
plt.plot(vgghist.history['val_acc'])
plt.plot(vgghist.history['loss'])
plt.plot(vgghist.history['val_loss'])
plt.title("model accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(["Accuracy","Validation Accuracy","loss","Validation Loss"])
plt.show()


# Clasificamos imágenes específicas utilizando el modelo (para ejemplificar)
from tensorflow.keras.preprocessing import image

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.vgg16.preprocess_input(img)
    return img

# Lista de las rutas de las imágenes a clasificar
image_paths = ['path_to_image1.jpg', 'path_to_image2.jpg']  # Replace with your image file paths

for image_path in image_paths:
    preprocessed_img = preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)

    # Predecimos la clase de la imágen (0 or 1 en nuestro caso, al ser clasificación binaria)
    predicted_class_index = np.argmax(predictions)

    # Obtenemos la probabilidad de la predicción de la clase
    prediction_probability = predictions[0][predicted_class_index]

    if predicted_class_index == 0:
        predicted_class = 'nevus'
    else:
        predicted_class = 'melanoma'

    print(f"Image: {image_path} - Predicted Class: {predicted_class} - Prediction Probability: {prediction_probability:.4f}")