import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
import youtube_dl


def download(link, opts):
    ydl_opts = opts
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x600')
        self.root.resizable(False, False)
        self.root.title('YouTube Downloader')

        self.loadGUI()

    def loadGUI(self):
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack()

        self.dlNewVideoButton = tk.Button(self.root, text='Download new video', command=self.downloadNewVideo)  
        self.dlNewVideoButton.pack()

    def downloadNewVideo(self):
        self.newVideoWin = tk.Tk()
        self.newVideoWin.title('Download new video')
        self.newVideoWin.resizable(False, False)
        self.newVideoWin.geometry('300x400')

        self.linkLabel = tk.Label(self.newVideoWin, text='Link to your video')
        self.linkLabel.pack()

        self.linkEntry = tk.Entry(self.newVideoWin)
        self.linkEntry.pack()

        self.r_var = tk.IntVar()

        self.Radio1 = tk.Radiobutton(self.newVideoWin, text='Video', variable=self.r_var, value=1, command=lambda:self.r_var.set(1))
        self.Radio2 = tk.Radiobutton(self.newVideoWin, text='Audio', variable=self.r_var, value=2, command=lambda:self.r_var.set(2))
        self.Radio1.pack()
        self.Radio2.pack()
    
        self.dlButton = tk.Button(self.newVideoWin, text='Download your video', command=self.dlFunc)
        self.dlButton.pack()
   
    def dlFunc(self):
        print(self.r_var.get())
        path = fd.askdirectory(title="Select directory")
        link = self.linkEntry.get()

        opts = {'outtmpl': path+'/'+u'%(id)s.%(ext)s'}

        if self.r_var.get() == 1:
            pass
        elif self.r_var.get() == 2:
            opts['format'] = 'bestaudio/best'
            opts['extractaudio'] = True
            opts['audioformat'] = 'mp3'
            opts['postprocessors'] = [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}]

        download(link, opts)
        messagebox.showinfo(title="Complete", message="Video has been downloaded\npath: "+path)
        self.newVideoWin.destroy()

    def start(self):
        self.root.protocol("WM_DELETE_WINDOW", self.__exit)
        self.root.mainloop()
    def __exit(self):
        self.root.destroy()

if __name__ == '__main__':
    gui = GUI()
    gui.start()
