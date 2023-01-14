import tkinter as tk
from numpy import random

#window
root = tk.Tk()
root.title("Challenge Generator")
root.geometry("400x300")

#label to display challenge
challenge_label = tk.Label(root, text="Challenge goes here", font=("Arial", 20))
challenge_label.pack()

#challenge generator
def generate_challenge():
    #insert database below for challenges
    challenges = ["Take a walk", "Compliment 5 strangers", "Thank a loved one", "Read 10 pages"]
    challenge = random.choice(challenges)
    challenge_label.config(text=challenge)

#button
new_challenge_button = tk.Button(root, text="New Challenge", command=generate_challenge)
new_challenge_button.pack()

#run app
root.mainloop()