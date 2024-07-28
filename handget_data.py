import cv2
import mediapipe as mp
import pandas as pd  
import os
import numpy as np 
def image_processed(file_path):
    try:
        # reading the static image
        hand_img = cv2.imread(file_path)

        if hand_img is None:
            print("Failed to load image:", file_path)
            return np.zeros([1, 63], dtype=int)[0]

        # Rest of your image processing code...

    except Exception as e:
        print("Error processing image:", e)
        return np.zeros([1, 63], dtype=int)[0]
    file_path=("D:\hand4\DATASET")


def make_csv():
    
    mypath = 'DATASET/'
    file_name = open('dataset.csv', 'a')

    for each_folder in os.listdir(mypath):
        if '._' in each_folder:
            pass

        else:
            for each_number in os.listdir(mypath + '/' + each_folder):
                if '._' in each_number:
                    pass
                
                else:
                    label = each_folder

                    file_loc = mypath + '/' + each_folder + '/' + each_number

                    data = image_processed(file_loc)
                    try:
                        for id,i in enumerate(data):
                            if id == 0:
                                print(i)
                            
                            file_name.write(str(i))
                            file_name.write(',')

                        file_name.write(label)
                        file_name.write('\n')
                    
                    except:
                        file_name.write('0')
                        file_name.write(',')

                        file_name.write('None')
                        file_name.write('\n')
       
    file_name.close()
    print('Data Created !!!')

if __name__ == "__main__":
    make_csv()

