from tkinter import *
import Attendance as atten
import FaceRecognition as face

# **** Window initialization, sizing, and positioning
root = Tk()  # window render object
menu = Menu(root)
root.config(menu=menu)


def window(main):
    main.title("Home Security")
    main.update_idletasks()
    width = 500
    height = 200
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_height() // 2) + height
    main.geometry('{}x{}+{}+{}'.format(width, height, x, y))


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
labelIntro = Label(root, text="This program will use facial recognition with your webcam")
labelIntro.pack()
# ****

# **** Buttons
button1 = Button(root, text="Open WebCam", command=atten.runCamera)
button2 = Button(root, text="Picture Test", command=face.showImage)
button3 = Button(root, text="Exit", fg='red', command=quit)
button1.pack(pady=20, padx=2)
button2.pack(pady=20, padx=2)
button3.pack(padx=2)
# ****

# **** Status Bar
status = Label(root, text="Facial Recognition", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
# ****

window(root)
root.mainloop()  # loops the window
