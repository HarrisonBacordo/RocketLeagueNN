import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D

# TODO: Identify ball, have car move only toward ball.

def process_screen(sc_grab):
    """
    Processes screen grab to make it more easily read by the computer
    :param sc_grab: img to process
    :return: processed img
    """
    processed_img = cv2.cvtColor(sc_grab, cv2.COLOR_BGR2GRAY)   # convert to gray
    processed_img = cv2.Canny(processed_img, threshold1=125, threshold2=200)    # edge detection only
    return processed_img


# countdown timer to prep game input
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

start_time = time.time()
while True:
    screengrab = np.array(ImageGrab.grab(bbox=(0, 30, 1024, 790)))
    new_sc_grab = process_screen(screengrab)
    # key input
    print('down')
    PressKey(W)
    time.sleep(3)
    print('down')
    ReleaseKey(W)
    # print time for testing purposes. restart start_time
    print("Loop took {} seconds".format(time.time() - start_time))
    start_time = time.time()
    # show screengrab. If q is held then break loop
    cv2.imshow('window', new_sc_grab)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
