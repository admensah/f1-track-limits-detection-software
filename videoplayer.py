from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import asyncio
event = asyncio.Event()

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("F1 Stewards Player")
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        self.videoWidget = QVideoWidget()
        self.playButton = QPushButton('Play')
        self.playButton.clicked.connect(self.toggle_play_pause)
        
        self.exitButton = QPushButton('Exit and Save Last Pause Time')
        self.exitButton.clicked.connect(self.exit_and_save_last_time)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.videoWidget)
        self.layout.addWidget(self.playButton)
        self.layout.addWidget(self.exitButton)
        
        self.setLayout(self.layout)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        self.lastPauseTime = None  # Variable to store the last pause time

    def toggle_play_pause(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.playButton.setText('Play')
            self.lastPauseTime = self.mediaPlayer.position()
            print(f"Video paused at {self.lastPauseTime / 1000} seconds.")
        else:
            self.mediaPlayer.play()
            self.playButton.setText('Pause')

    def exit_and_save_last_time(self):
        if self.lastPauseTime is not None:
            with open('last_pause_time.txt', 'w') as file:
                file.write(f"{self.lastPauseTime / 1000}\n")  # Save the last pause time in seconds
            print(f"Last pause time saved to last_pause_time.txt: {self.lastPauseTime / 1000} seconds.")
        self.close()  # Close the application
        event.set()
