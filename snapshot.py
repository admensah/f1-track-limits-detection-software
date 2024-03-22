import cv2
import sys
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent
from videoplayer import VideoPlayer

def select_video():
    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4 *.avi *.mov")])
    print(f"Video selected path: {video_path}.")
    return video_path

def select_pause_time(video_path):
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))
    player.resize(640, 480)
    player.show()
    exit_code = app.exec_()

    filename = 'last_pause_time.txt'
    last_pause_time = None
    with open(filename, 'r') as file:
        last_pause_time =  float(file.readline().strip())
    return last_pause_time
    
def capture_snapshot(video_path, snapshot_time):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    cap.set(cv2.CAP_PROP_POS_MSEC, snapshot_time * 1000)
    
    success, frame = cap.read()
    if success:
        cv2.imshow('Snapshot (Press any key to continue)', frame)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
        
        snapshot_filename = "snapshot.jpg"
        cv2.imwrite(snapshot_filename, frame)
    else:
        print("Error: Could not read frame.")
    
    cap.release()

def edges():
    image = cv2.imread("snapshot.jpg")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('GreyScale (Press any key to continue)', gray)
    cv2.waitKey(0) 

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred,100,200)
    cv2.imshow('Edges (Press any key to continue)', edges)
    cv2.waitKey(0) 

    cv2.imwrite('edges.jpg', edges)

# Select Video
video_path = select_video()
# Get Last Pause Time
pause_time = select_pause_time(video_path)
# Get snapshot at that time
capture_snapshot(video_path, pause_time)
# Make edges
edges()
