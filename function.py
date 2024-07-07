from tkinter import *
import random

root = Tk()

root.geometry('700x450')
root.title("Rock| Paper| Scissors Game")
root.resizable(0,0)
root.config(bg='seashell3')

Label(root, text='Rock| Paper | Scissors', font='arial 15 bold', bg ='seashell2').pack()

user_choice = StringVar()

Label(root, text="Type one in the immediate Text box: Rock | Paper | Scissors", font='arial 12', bg='seashell2').place(x=20, y = 70)
Entry(root, font='arial 12', textvariable=user_choice, bg='antiquewhite2').place(x=90, y=130)


computer_select = random.randint(1, 3)
if computer_select == 1:
    computer_select = "Rock"
elif computer_select == 2:
    computer_select = "Paper"
else:
    computer_select = "Scissors"

Results = StringVar()

def play():
    picked_by_user = user_choice.get()
    if picked_by_user == computer_select:
        Results.set(f"That was a draw, you both selected {picked_by_user}")
    elif picked_by_user == "Rock" and computer_select == "Paper":
        Results.set(f"Yos loose, {computer_select}, was computers choice which covers {picked_by_user}")
    elif picked_by_user == "Rock" and computer_select == "Scissors":
        Results.set(f"You win, {picked_by_user} was your choices which cant be cut by {computer_select}")
    elif picked_by_user == "Paper" and computer_select == "Scissors":
        Results.set(f"You loose, {computer_select} was computers choice which can cut through {picked_by_user}")
    elif picked_by_user == "Paper" and computer_select == "Rock":
        Results.set(f"You win, {picked_by_user} was your selection which can cover {computer_select}")
    elif picked_by_user == "Scissors" and computer_select == "Rock":
        Results.set(f"You loose, {picked_by_user} was your selction which cant cut through {computer_select}")
    elif picked_by_user == "Scissors" and computer_select == "Paper":
        Results.set(f"You win, {picked_by_user} was your selection which can cut through {computer_select}")
    elif picked_by_user == "" and computer_select == "":
        Results.set("You never selected, which is an invalid selection, please select Rock| Paper| Scissor, first letter should be uppercase ")

    else:
        Results.set(f"{picked_by_user} is an invalid selection, please select Rock| Paper| Scissor, first letter should be uppercase")

def Reset():
    Results.set("")
    user_choice.set("")

def Exit():
    root.destroy()

Entry(root, font='arial 10 bold', textvariable=Results, bg='antiquewhite2', width= 90).place(x=25, y = 250)
Button(root, font='arial 13 bold', text="PLAY", command=play, padx=5, bg = 'seashell4').place(x=350, y = 310)
Button(root, font='arial 13 bold', text="RESET", padx=5, bg= 'seashell4', command=Reset).place(x=250, y =310)
Button(root, font='arial 13 bold', text='EXIT', padx=5, bg= 'seashell4', command=Exit).place(x=450, y =310)


root.mainloop()