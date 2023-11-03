import customtkinter
import tkinter
from pytube import YouTube
import os
folder_path = os.path.expanduser('/Downloads')

def start_download():
    try:
        ylink = link.get()
        yObject = YouTube(ylink)
        video = yObject.streams.get_lowest_resolution()
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        output_path = os.path.join(folder_path, yObject.title + ".mp4")
        video.download(output_path=output_path)
        print("Download complete")
    except:
        print("Download Failed")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=start_download())
download.pack(padx=10, pady=10)

app.mainloop()
