from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap('landscape.ico')


# Import an image 
myImage1 = ImageTk.PhotoImage(Image.open('funnycats/cat1.jpg'))
myImage2 = ImageTk.PhotoImage(Image.open('funnycats/cat2.jpg'))
myImage3 = ImageTk.PhotoImage(Image.open('funnycats/cat3.jpg'))
myImage4 = ImageTk.PhotoImage(Image.open('funnycats/cat4.jpg'))
myImage5 = ImageTk.PhotoImage(Image.open('funnycats/cat5.jpg'))

imagesList = [myImage1, myImage2, myImage3, myImage4, myImage5]

index = 0
myLabel = Label(image=imagesList[index])
myLabel.grid(row=0, column=0, columnspan=3)


def forward():
    # Creating global variables accessible from outside of this function
    global myLabel
    global index 
    global buttonForward

    buttonBack.config(state="normal")
    # This is checking if we are at the end of the slideshow
    if index == len(imagesList)-2:
        # If we are, disable the forward button
        buttonForward.config(state="disabled")
        
    # If more pictures available, erase old picture and grid the next picture
    myLabel.grid_forget()
    index += 1
    myLabel = Label(image=imagesList[index])
    myLabel.grid(row=0, column=0, columnspan=3)
        
    statusText = f'Image {index+1} of {len(imagesList)}'
    status = Label(root, text=statusText, bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)

def back():
    global myLabel
    global index

    buttonForward.config(state="normal")
    if index == 1:
        buttonBack.config(state="disabled")

    myLabel.grid_forget()
    index -= 1
    myLabel = Label(image=imagesList[index])
    myLabel.grid(row=0, column=0, columnspan=3)

    statusText = f'Image {index+1} of {len(imagesList)}'
    status = Label(root, text=statusText, bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)

# Button of the program
buttonBack = Button(root, text="<<", command=back, state=DISABLED)
buttonQuit = Button(root, text="Exit", command=root.quit, padx=15)
buttonForward = Button(root, text=">>", command=forward)

buttonBack.grid(row=1, column=0)
buttonQuit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)

statusText = f'Image {index+1} of {len(imagesList)}'
status = Label(root, text=statusText, bd=1, relief=SUNKEN, anchor=W)
status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)

root.mainloop()