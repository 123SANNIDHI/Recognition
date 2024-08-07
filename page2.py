import cv2
import test_mediapipe as mp
import pandas as pd
import os
import numpy as np

def show():
    def image_processed(hand_img):
        # Image processing
        # 1. Convert BGR to RGB
        img_rgb = cv2.cvtColor(hand_img, cv2.COLOR_BGR2RGB)

        # 2. Flip the img in Y-axis
        img_flip = cv2.flip(img_rgb, 1)

        # accessing MediaPipe solutions
        mp_hands = mp.solutions.hands

        # Initialize Hands
        hands = mp_hands.Hands(static_image_mode=True,
                               max_num_hands=1, min_detection_confidence=0.7)

        # Results
        output = hands.process(img_flip)

        hands.close()

        try:
            data = output.multi_hand_landmarks[0]
            data = str(data)

            data = data.strip().split('\n')

            garbage = ['landmark {', '  visibility: 0.0', '  presence: 0.0', '}']

            without_garbage = []

            for i in data:
                if i not in garbage:
                    without_garbage.append(i)

            clean = []

            for i in without_garbage:
                i = i.strip()
                clean.append(i[2:])

            for i in range(0, len(clean)):
                clean[i] = float(clean[i])
            return clean
        except:
            return np.zeros([1, 63], dtype=int)[0]

    import pickle
    # load model
    with open('model.pkl', 'rb') as f:
        svm = pickle.load(f)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Create or append to the CSV file
    csv_filename = 'data.csv'
    csv_exists = os.path.isfile(csv_filename)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        data = image_processed(frame)

        data = np.array(data)
        y_pred = svm.predict(data.reshape(-1, 63))
        print(y_pred)

        # Add predicted label to the frame
        label = str(y_pred[0])
        cv2.putText(frame, label, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5, cv2.LINE_AA)

        # Add quit message
        cv2.putText(frame, "Press 'q' to quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow('frame', frame)

        # Append data to the CSV file
        data_dict = {'Label': label}
        data_df = pd.DataFrame(data_dict, index=[0])
        data_df.to_csv(csv_filename, mode='a', header=not csv_exists, index=False)

        csv_exists = True

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

