import os
import cv2


folder = "photos2"
size_threshold = 512
counter = 0

for file_name in os.listdir(folder):
    try:
        file_path = os.path.join(folder, file_name)
        img = cv2.imread(file_path)
        if img.shape[0] < size_threshold and img.shape[1] < size_threshold:
            os.remove(file_path)
            print("image removed")
            counter += 1

    except Exception as e:
        print("Error:", e)
        os.remove(file_path)
        print("image removed")

print(counter, "images removed")
