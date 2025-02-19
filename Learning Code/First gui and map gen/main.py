import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        finishLabel.configure(text="", text_color="white")
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        video.download()
        finishLabel.configure(text="Download finished")
    except:
        finishLabel.configure(text="Download failed", text_color="red")

#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

#adding UI elements
title = customtkinter.CTkLabel(app, text="insert a youtube link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar();
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#finished downloading 
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(pady=10)

#progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

#progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400, height=40)
progressBar.set(0.5)
progressBar.pack(pady=10)

#download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(pady=10)


#run app
app.mainloop()