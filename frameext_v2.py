import cv2
import os

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
path = 'Data/'

name = 'Kentucky Derby 2022 (FULL RACE) - NBC Sportsasjdfhasdjh'

outPath = 'Data/results/'+name
cap = cv2.VideoCapture(path+name+'.mp4')
nOfVidioFrame = float(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# nOfDesiredFrame = 3000
# print(f"nOfVidioFrame: {nOfVidioFrame}")
# n_of_frame_interval = int(nOfVidioFrame / nOfDesiredFrame)
n_of_frame_interval = 5
print(f"n_of_frame_interval: {n_of_frame_interval}")


try:
    os.makedirs(outPath, exist_ok=True)
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
            # frame2 = cv2.resize(frame, dsize=(0, 0), fx=.5, fy=.5)
            # cv2.imshow('Frame',frame2)
            zerofills = str(num).zfill(6)
            name = f"{outPath}/frame_{zerofills}.jpg"
            # cv2.imwrite(outPath+"/"+"frame_%d.jpg" % num, frame)
            cv2.imwrite(name, frame)
            count = count + 1
            print(f"processing frame no: {zerofills}")
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
