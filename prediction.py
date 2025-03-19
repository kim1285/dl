import numpy as np
from tensorflow import keras


model = keras.models.load_model(r"C:\Users\user\Desktop\ml\model_2e.keras")


def prepare_image(file):
    img_path = ''
    img = keras.preprocessing.image.load_img(img_path + file, target_size=(224, 224))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)


preprocessed_image = prepare_image(r"C:\Users\user\Desktop\finetune\train\nonfire\65a10dc9e3ca143b6b8649191b81f665.wix_mp_1024.jpg")
predictions = model.predict(preprocessed_image)
print(predictions)
print(type(predictions))
print(predictions.shape)

print("Fire :", str(predictions[0][0]*100)[:4] + "%"," |Not Fire:",str(predictions[0][1]*100)[:4]+"%")

if predictions[0][0] > 0.5:
    print("Fire detected")
else:
    print("No Fire detected")
