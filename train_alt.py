import numpy as np
import tensorflow
import os
import tensorflow.keras as keras
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from PIL import Image
import sklearn

# Set up image paths
train_path = r"C:\Users\user\Desktop\finetune\train"
valid_path = r"C:\Users\user\Desktop\finetune\valid"
test_path = r"C:\Users\user\Desktop\finetune\test"

# Normalize pixel values. Resize images to 224x224
train_batches = keras.preprocessing.image_dataset_from_directory(
    train_path,
    image_size=(224, 224),
    batch_size=32,  # Reduce batch size if memory issues arise
    label_mode='categorical'
)
train_batches = train_batches.map(lambda x, y: (keras.applications.mobilenet.preprocess_input(x), y))

valid_batches = keras.preprocessing.image_dataset_from_directory(
    valid_path,
    image_size=(224, 224),
    batch_size=32,
    label_mode='categorical'
)
valid_batches = valid_batches.map(lambda x, y: (keras.applications.mobilenet.preprocess_input(x), y))

test_batches = keras.preprocessing.image_dataset_from_directory(
    test_path,
    image_size=(224, 224),
    batch_size=32,
    label_mode='categorical'
)
test_batches = test_batches.map(lambda x, y: (keras.applications.mobilenet.preprocess_input(x), y))

# Load and inspect pretrained MobileNet model
mobile = keras.applications.mobilenet.MobileNet(weights="imagenet", include_top=False)

# Add global average pooling and softmax layer
x = mobile.output
x = keras.layers.GlobalAveragePooling2D()(x)
predictions = Dense(2, activation='softmax')(x)

# Create the final model with the modified predictions layer
model = keras.models.Model(inputs=mobile.input, outputs=predictions)
model.summary()

# Freeze the layers except the last 3 layers
for layer in model.layers[:-4]:
    layer.trainable = False

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Callbacks: ModelCheckpoint and ReduceLROnPlateau
checkpointer = keras.callbacks.ModelCheckpoint(
    filepath=r"C:\Users\user\Desktop\ml\model_2e.keras",
    monitor='val_loss',
    verbose=1,
    save_best_only=True,
    save_weights_only=False,
    mode='auto',
    save_freq='epoch'
)

reduce_lr = keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=1, min_lr=0.000001)

# Fit the model
model.fit(
    train_batches,
    steps_per_epoch=len(train_batches),
    validation_data=valid_batches,
    validation_steps=len(valid_batches),
    epochs=3,
    verbose=1,
    callbacks=[checkpointer, reduce_lr]
)
