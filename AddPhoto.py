from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk



def window(main):
    main.title("Add Photo")
    main.update_idletasks()
    main.update_idletasks()
    ws = main.winfo_screenwidth() # width of the screen
    hs = main.winfo_screenheight()
    w = 500
    h = 200
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    main.geometry('%dx%d+%d+%d' % (w, h, x, y))

fileName = None

def uploadFile():
   filename = filedialog.askopenfilename(initialdir = "/", title = "Select Image")
   fileName = "yo"





def showWindow():
    # **** Window initialization, sizing, and positioning
    root = Tk()  # window render object
    menu = Menu(root)
    root.config(menu=menu)
    textVar = StringVar()
   

    uploadLabel = Label(root, text = "File Path", textvariable = textVar)
    uploadLabel.place(x = 75, y = 50)
    
    uploadPath = Label(root,text = fileName, width = 20)
    uploadPath.place(x = 150, y = 50)
   
    

    uploadButton = Button(root, text = 'Upload Image', command=uploadFile)
    uploadButton.place(x = 100, y = 150)

    cancelButton = Button(root, text = 'Cancel', command=root.destroy)
    cancelButton.place(x = 350, y = 150)

    window(root)
    root.update
   




