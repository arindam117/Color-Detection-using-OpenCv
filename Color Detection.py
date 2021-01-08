import cv2 as cv
import numpy as np


# frameWidth = 360
# frameHeight = 480

cap = cv.VideoCapture(0)

# # 3 is for width and frameWidth = 640, we can directly put 360 as well in place of frameWidth in cap.set()
# cap.set(3, frameWidth)
# # 4 is for height and we already have made the frameHeight variable = 480
# cap.set(4, frameHeight)
# # 10 is the id for brightness and 130 is its parameter
# cap.set(10, 130)
while True:
    success, img = cap.read()
    # Creating a HSV frame, (Hue(H), Saturation(S), Values(V))
    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)


    # Creating mask for color RED (Low and High Values)

    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])

    # Creating a mask which will whiten only the red areas
    # DETECTING ONLY THE RED COLORS
    # Creating a range for the colors using the inRange function where we define the low and high values for (S,V)
    red_mask = cv.inRange(hsv_img,low_red,high_red)
    red = cv.bitwise_and(img,img,mask=red_mask)

# DETECTING ONLY THE BLUE COLORS

    # Creating masks for the BLUE color
    low_blue = np.array([94,80,2])
    high_blue = np.array([126,255,255])

    # Detecting only BLUE
    # Creating a range for the colors using the inRange function where we define the low and high values for (S,V)
    blue_mask = cv.inRange(hsv_img,low_blue,high_blue)
    blue = cv.bitwise_and(img,img,mask=blue_mask)


# DETECTING ONLY THE GREEN COLORS

    # Creating masks for Green
    low_green = np.array([25,52,72])
    high_green = np.array([102,255,255])

    # Detecting using inRange and Bitwise_and
    green_mask = cv.inRange(hsv_img,low_green,high_green)
    green = cv.bitwise_and(img,img,mask=green_mask)


    cv.imshow("Original",img) # Shows the original live feed

    cv.imshow("Red Detection", red) # Detects only RED in the live feed(This is not working on my PC)

    cv.imshow("Blue Detection",blue) # Detects only Blue in the live feed
    cv.imshow('Green Detection',green) #Detects only the green objects in the live feed

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.read()
cv.destroyAllWindows()