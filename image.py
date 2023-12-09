import cv2
import argparse
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array



import cv2
import os

class generate_result():
    
    def predict_image(self):

        if not os.path.exists("images"):
            os.mkdir("images")

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Camera not found or could not be opened.")
        else:
            ret, frame = cap.read()

            if ret:
                image_path = os.path.join("images", "snapshot.jpg")
                cv2.imwrite(image_path, frame)
                print(f"Snapshot saved as {image_path}")
            else:
                print("Error: Failed to capture an image.")


            cap.release()

        cv2.destroyAllWindows()

        json_file = open('top_models\\fer.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)

        model.load_weights('top_models\\fer.h5')

        classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        img = cv2.imread("images/snapshot.jpg")
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_detected = classifier.detectMultiScale(gray_img, 1.18, 5)
        predicted_emotion = ""
        if len(faces_detected) == 0:
            return "No faces Detected"
        # print(faces_detected)
        # if cv2.waitKey(0) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray_img[y:y + w, x:x + h]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            img_pixels = image.img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255.0

            predictions = model.predict(img_pixels)
            max_index = int(np.argmax(predictions))

            emotions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear']
            predicted_emotion = emotions[max_index]
            if predicted_emotion == "":
                print("Failed to capture the emotion")
            else: 
                print("the Emotion detected is ", predicted_emotion)
        
        return predicted_emotion


if __name__ == '__main__':
    x = generate_result()
    x.predict_image()



