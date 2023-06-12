import os
import argparse
import cv2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove small images from a folder')
    parser.add_argument('--input', type=str, default='photos', help='input directory path')
    parser.add_argument('--size_threshold', type=int, default=512, help='size threshold')
    args = parser.parse_args()

    counter = 0
    for file_name in os.listdir(args.input):
        try:
            file_path = os.path.join(args.input, file_name)
            img = cv2.imread(file_path)
            if img.shape[0] < args.size_threshold and img.shape[1] < args.size_threshold:
                os.remove(file_path)
                print("image removed")
                counter += 1

        except Exception as e:
            print("Error:", e)
            os.remove(file_path)
            print("image removed")

    print(counter, "images removed")
