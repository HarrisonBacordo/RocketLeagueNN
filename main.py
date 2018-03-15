import numpy as np
from PIL import ImageGrab
import cv2
import time

start_time = time.time()
while True:
    screengrab = np.array(ImageGrab.grab(bbox=(0, 30, 1024, 790)))
    print("time took {} seconds".format(time.time() - start_time))
    start_time = time.time()
    cv2.imshow('window', cv2.cvtColor(screengrab, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
