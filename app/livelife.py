import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
from numpy import random

bgcolour = "#13005A"
points = 0

#challenge generator
def generate_challenge():
    connection = sqlite3.connect("data/challenges.db")
    cur = connection.cursor()
    cur.execute("SELECT challenge FROM challenge;")
    chal = cur.fetchall()

    idx = random.randint(0, len(chal)-1)
    challenge = chal[idx]
    return str(challenge)[2:-3] #Removes unnecessary characters

def clear(f):
  for w in f.winfo_children():
    w.destroy()

def loadFrame():
  clear(frame2)
  clear(frame3)
  frame.tkraise()
  frame.pack_propagate(False)

  #Making Image Widget (Mountain)
  mountain = ImageTk.PhotoImage(file = "assets\mountain_fg.png")
  mountain_widget = tk.Label(frame, image= mountain, bg= bgcolour)
  mountain_widget.image = mountain
  mountain_widget.place(x= 0, y= 400)

  #image widget (challenge accepted)
  img = Image.open("assets\challenge_accepted.png")
  realLogo = img.resize((200,200), Image.LANCZOS)
  logo = (ImageTk.PhotoImage(realLogo))
  logo_widget = tk.Label(frame, image= logo, bg= bgcolour)
  logo_widget.image = logo
  logo_widget.pack()

  caption = tk.Label(
    frame,
    text= "Your Daily Challenge Awaits",
    bg= bgcolour,
    fg= "white",
    font=("Helvetica",18)
  )
  caption.pack()

  pointCount = tk.Label(
    frame,
    text = f"Your current points: {points}",
    bg= bgcolour,
    fg= "white",
    font=("Helvetica",18)
  )
  pointCount.pack()

  tk.Button(
    frame,
    text = "New Challenge",
    font = ("Helvetica", 20),
    bg="#FF6961",
    fg= "white",
    cursor= "hand2",
    activebackground="#c23b22",
    activeforeground="black",
    command=lambda:loadFrame2()).pack(padx= 20, pady= 20)


def loadFrame2():
  clear(frame)
  frame2.tkraise()
  frame2.pack_propagate(False)
  challenge = generate_challenge()

  background = Image.open("assets\moon.jpg")
  reBackground = background.resize((650, 1000), Image.LANCZOS)
  bkg = ImageTk.PhotoImage(reBackground)
  bkg_widget = tk.Label(frame2, image= bkg)
  bkg_widget.image = bkg
  bkg_widget.place(x=0, y= 0, relwidth= 1, relheight= 1)

  chalLabel = tk.Label(
    frame2,
    text= "Your Challenge Today is:",
    bg= bgcolour,
    fg= "white",
    font= ("Helvetica", 18)
  )
  chalLabel.pack(pady= 50)

  chalToday = tk.Label(
    frame2,
    text= challenge,
    bg= bgcolour,
    fg= "white",
    font= ("Helvetica", 18),
    wraplength= 450,
    justify="center"
  )
  chalToday.pack()

  backB = tk.Button(
    frame2,
    text = "Back",
    font = ("Helvetica", 18),
    bg="#FF6961",
    fg= "white",
    cursor= "hand2",
    activebackground="#c23b22",
    activeforeground="black",
    command= lambda:loadFrame()
  )

  checkB = tk.Button(
    frame2,
    text = "Challenge Success?",
    font = ("Helvetica", 18),
    bg="#03c03c",
    fg= "white",
    cursor= "hand2",
    activebackground="#2F4C39",
    activeforeground="black",
    command= lambda:loadFrame3(challenge)
  )

  backB.pack(pady= 20)
  checkB.pack()
  

def loadFrame3(c):
  global points
  points +=1 #increment points for each challenge succeeded
  clear(frame2)
  frame3.tkraise()
  frame3.pack_propagate(False)

  background = Image.open("assets\moon.jpg")
  reBackground = background.resize((650,1000), Image.LANCZOS)
  bkg = (ImageTk.PhotoImage(reBackground))
  bkg_widget = tk.Label(frame3, image= bkg)
  bkg_widget.image = bkg
  bkg_widget.place(x=0, y= 0, relwidth= 1, relheight= 1)

  congrats = tk.Label(
    frame3,
    text= "Great job, you completed the challenge:",
    bg= bgcolour,
    fg= "white",
    font= ("Helvetica", 18)
  )
  congrats.pack(pady = 50)

  chalToday = tk.Label(
    frame3,
    text= c,
    bg= bgcolour,
    fg= "white",
    font= ("Helvetica", 18),
    wraplength= 450,
    justify="center"
  )
  chalToday.pack()

  pointGained = tk.Label(
    frame3,
    text= f"You now have {points} point(s)",
    bg= bgcolour,
    fg= "white",
    font= ("Helvetica", 18)
  )
  pointGained.pack()

  backB = tk.Button(
    frame3,
    text = "Back",
    font = ("Helvetica", 18),
    bg="#FF6961",
    fg= "white",
    cursor= "hand2",
    activebackground="#c23b22",
    activeforeground="black",
    command= lambda:loadFrame()
  )  
  backB.pack(pady= 20)

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
frame2 = tk.Frame(root, width= 500, height= 700)
frame3 = tk.Frame(root, width= 500, height= 700)

frame.grid(row= 0, column= 0, sticky= "nesw")
frame2.grid(row= 0, column= 0, sticky= "nesw")
frame3.grid(row= 0, column= 0, sticky= "nesw")


loadFrame()


#run app
root.mainloop()