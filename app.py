from tkinter import *
from tkinter import filedialog
import vlc

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        self.root.geometry("800x600")

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.canvas = Canvas(root, bg="black", width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        self.play_button = Button(root, text="Play", command=self.play_video)
        self.play_button.pack()

        self.stop_button = Button(root, text="Stop", command=self.stop_video)
        self.stop_button.pack()

    def play_video(self):
        file_path = filedialog.askopenfilename()
        media = self.instance.media_new(file_path)
        self.player.set_media(media)
        self.player.set_xwindow(self.canvas.winfo_id())
        self.player.play()

    def stop_video(self):
        self.player.stop()

if __name__ == "__main__":
    root = Tk()
    app = VideoPlayer(root)
    root.mainloop()
