import numpy as np
import pandas as pd
import cv2
import imutils

def show():
    camera = cv2.VideoCapture(0)
    r = g = b = xpos = ypos = 0
    index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
    df = pd.read_csv("D:\gui2\colors.csv", names=index, header=None, encoding='utf-8')

    # Create or append to the CSV file
    csv_filename = 'color_data.csv'
    csv_exists = False

    def getColorName(R, G, B):
        minimum = 10000
        for i in range(len(df)):
            d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
            if d <= minimum:
                minimum = d
                cname = df.loc[i, 'color_name'] + '   Hex=' + df.loc[i, 'hex']
        return cname

    def identify_color(event, x, y, flags, param):
        nonlocal b, g, r, xpos, ypos, csv_exists
        xpos = x
        ypos = y
        b, g, r = frame[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

        # Append data to the CSV file
        data_dict = {'Color': getColorName(r, g, b), 'R': r, 'G': g, 'B': b}
        data_df = pd.DataFrame(data_dict, index=[0])
        data_df.to_csv(csv_filename, mode='a', header=csv_exists, index=False)

        csv_exists = True

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', identify_color)

    while True:
        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=900)
        kernal = np.ones((5, 5), "uint8")
        cv2.rectangle(frame, (20, 20), (800, 60), (b, g, r), -1)
        text = getColorName(b, g, r) + '   R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        # Add quit message at the bottom left corner
        cv2.putText(frame, "Press 'q' to quit", (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow('image', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

