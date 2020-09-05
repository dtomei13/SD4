from tkinter import *
import Attendance as atten
import FaceRecognition as face
import AddPhoto as photo
from PIL import Image, ImageTk

# **** Window initialization, sizing, and positioning
root = Tk()  # window render object
menu = Menu(root)
root.config(menu=menu)

cameraFeedButton = PhotoImage(file = 'Images/button.png')

def window(main):
    main.title("Home Security")
    main.update_idletasks()
    ws = main.winfo_screenwidth() # width of the screen
    hs = main.winfo_screenheight()
    w = 1050
    h = 500
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    main.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # width = 1050
    # height = 500
    # x = (main.winfo_screenwidth() // 2) - (width // 2)
    # y = (main.winfo_height() // 2) + height
    # main.geometry('{}x{}+{}+{}'.format(width, height, x, y))


# ****

# **** Menus
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open camera", command=atten.runCamera)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)
# ****
helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="I can't help", command=quit)

# Labels

# ****

# **** Buttons
button1 = Button(root, text = 'Live Feed', command=atten.runCamera)
button2 = Button(root, text="Picture Test", command=face.showImage)
button3 = Button(root, text="Exit", fg='red', command=quit)
button4 = Button(root, text="Add Photos", command=photo.showWindow)
button1.place(x = 300, y = 120)
button2.place(x = 600, y = 120)
button4.place(x = 300, y = 240)
button3.place(x = 600, y = 240)


# ****

# **** Status Bar
status = Label(root, text="Facial Recognition", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
# ****

window(root)
root.mainloop()  # loops the window
