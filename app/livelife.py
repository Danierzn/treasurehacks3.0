import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
from numpy import random

bgcolour = "#13005A"

#challenge generator
def generate_challenge():
    #insert database below for challenges
    challenges = ["Take a walk", "Compliment 5 strangers", "Thank a loved one", "Read 10 pages"]
    challenge = random.choice(challenges)
    challenge_label.config(text=challenge)

def clear(f):
  pass

def loadFrame():
  clear(frame2)
  frame.tkraise()
  frame.pack_propagate(False)

  #Making Image Widget (Mountain)
  mountain = ImageTk.PhotoImage(file = "assets\mountain_fg.png")
  mountain_widget = tk.Label(frame, image= mountain, bg= bgcolour)
  mountain_widget.image = mountain
  mountain_widget.place(x= 0, y= 400)

  #image widget (challenge accepted)
  img = Image.open("assets\challenge_accepted.png")
  realLogo = img.resize((200,200), Image.ANTIALIAS)
  logo = (ImageTk.PhotoImage(realLogo))
  logo_widget = tk.Label(frame, image= logo, bg= bgcolour)
  logo_widget.image = logo
  logo_widget.pack()

  tk.Label(
    frame,
    text= "Your Daily Challenge Awaits",
    bg= bgcolour,
    fg= "white",
    font="Helvetica"
  )

  tk.Button(
    frame,
    text = "New Challenge",
    font = ("TkHeadingFont", 20),
    bg="#FF6961",
    fg= "white",
    cursor= "hand2",
    activebackground="#c23b22",
    activeforeground="black",
    command=lambda:loadFrame2()).pack(padx= 20, pady= 20)


def loadFrame2():
  pass
  

#button
#new_challenge_button = tk.Button(root, text="New Challenge", command=generate_challenge, font= "Helvetica")
#new_challenge_button.pack()

#label to display challenge
#challenge_label = tk.Label(root, text="Challenge goes here", font=("Helvetica", 20))
#challenge_label.pack()



#window
root = tk.Tk()
root.title("Live Your Life")
root.eval("tk::PlaceWindow . center")


#Menu Frame
frame = tk.Frame(root, width= 500, height= 700, bg= bgcolour)
frame2 = tk.Frame (root, bg= bgcolour)

frame.grid(row= 0, column= 0, sticky= "nesw")
frame2.grid(row= 0, column= 0, sticky= "nesw")


loadFrame()


#run app
root.mainloop()