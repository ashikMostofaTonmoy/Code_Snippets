import cv2
import os

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
name= 'VID_20211223_152545'
cap = cv2.VideoCapture(name+'.mp4')
nOfVidioFrame = float(cap.get(cv2.CAP_PROP_FRAME_COUNT))
nOfDesiredFrame = 50
print(nOfVidioFrame)
n_of_frame_interval = int(nOfVidioFrame/ nOfDesiredFrame)
print (n_of_frame_interval)



try:
    os.makedirs(name, exist_ok=True)
except OSError as error:
    print(error)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")


count = 0
num = 0
# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame
        count += 1

        if count == n_of_frame_interval:
            frame2 = cv2.resize(frame, dsize=(0, 0), fx= .5, fy= .5)
            cv2.imshow('Frame',frame2)
            #cv2.imwrite(name+"/"+"frame%d.jpg" % num, frame)
            count = count + 1
            num += 1
            count = 0

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
