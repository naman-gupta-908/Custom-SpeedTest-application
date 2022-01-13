import cv2
import speedtest
from tkinter.ttk import *
from tkinter import *
import threading

download_speed=0
upload_speed=0
root = Tk()
root.title("Internet Speed Test")
root.geometry('400x250')
root.resizable(False, False)
root.configure(bg="#9ed1e1")
root.iconbitmap('speed.ico')
pg=0
# design Label
Label(root, text ='INTERNET SPEED', bg='#9ed1e1', fg='#404042', font = 'arial 25 bold').pack()

# making label for show internet speed
down_label = Label(root, text="Download Speed - ", bg='#9ed1e1',fg='#404042', font = 'arial 15 bold')
down_label.place(x = 80, y= 50)
up_label = Label(root, text="Upload Speed - ", bg='#9ed1e1',fg='#404042', font = 'arial 15 bold')
up_label.place(x = 80, y= 80)
ping = Label(root, text="Ping - ", bg='#9ed1e1',fg='#404042', font = 'arial 15 bold')
ping.place(x = 80, y= 110)

# function for check speed
def check_speed():
    global download_speed, upload_speed, pg, img
    speed_test= speedtest.Speedtest()
    speed_test.get_best_server()
    speed_test.download()
    speed_test.upload()
    res = speed_test.results.dict()
    download_speed = round(res["download"] / (10 ** 6), 2)
    upload_speed = round(res["upload"] / (10 ** 6), 2)
    pg=res["ping"]

# function for progress bar and update text
def update_text():
    thread=threading.Thread(target=check_speed, args=())
    thread.start()
    progress=Progressbar(root, orient=HORIZONTAL,length=200, mode='indeterminate')
    progress.place(x = 85, y = 140)
    progress.start()
    while thread.is_alive():
        root.update()
        pass
    down_label.config(text="Download Speed - "+str(download_speed)+"Mbps")
    up_label.config(text="Upload Speed - "+str(upload_speed)+"Mbps")
    ping.config(text="Ping - "+str(pg)+"ms")
    
    progress.stop()
    progress.destroy()

# button for call to function
button = Button(root, text="Check Speed", width=30, bd = 0, bg = '#399cbd', fg='#fff', pady = 5, command=update_text)
button.place(x=85, y = 170)
root.mainloop()
