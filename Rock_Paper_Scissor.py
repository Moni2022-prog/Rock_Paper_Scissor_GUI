from tkinter import*
import random

#creating the window 

window = Tk()
window.title("RockPaperScissor_GUI")
window.geometry("460x300")
window.resizable(False,False)
window.config(bg="light pink")

#defining variables and dictionary
dict = {
    "0" : "Rock",
    "1" : "Paper",
    "2" : "Scissor"
}
your_choice = ""
comp_choice = ""
your_score = 0
comp_score = 0

#creating functions
def play_again():
    text_to_display.delete("1.0","end")

def points():
    text_to_scores.delete("1.0", "end")
    text_to_scores.insert(END, f"     {your_score}                                {comp_score}")

def rock():
    global comp_score
    global your_score

    your_choice = "Rock"
    comp_choice = dict[str(random.randint(0,2))]
    text_to_display.insert(END, f"    Your Choice:               {your_choice}\n    Computer's Choice:         {comp_choice}")
    if comp_choice == "Paper":
        comp_score += 1
    if comp_choice == "Scissor":
        comp_score += 1

    points()

def paper():
    global comp_score
    global your_score

    your_choice = "Paper"
    comp_choice = dict[str(random.randint(0,2))]
    text_to_display.insert(END, f"    Your Choice:               {your_choice}\n    Computer's Choice:         {comp_choice}")
    if comp_choice == "Rock":
        your_score += 1
    if comp_choice == "Scissor":
        comp_score += 1
    points()

def scissor():
    global comp_score
    global your_score

    your_choice = "Scissor"
    comp_choice = dict[str(random.randint(0,2))]
    text_to_display.insert(END, f"    Your Choice:               {your_choice}\n    Computer's Choice:         {comp_choice}")
    if comp_choice == "Paper":
        your_score += 1
    if comp_choice == "Rock":
        comp_score += 1
    points()


#Text box for displaying the choices
text_to_display = Text(window, width=55 , height=4)
text_to_display.grid(row=0, columnspan=5, padx=5, pady=8)

#Buttons and labels created
rock_button = Button(window, text="Rock", width= 15,command=rock)
rock_button.grid(row=2, column=0,padx=10)

paper_button = Button(window, text="Paper",width=15,command=paper)
paper_button.grid(row=2, column=1,padx=10)

Scissor_button = Button(window, text="Scissor",width=15,command=scissor)
Scissor_button.grid(row=2, column=2,padx=10)


score_label = Label(window,height=2,width=50,
text="Your Score                             vs                            Computer's Score")
score_label.grid(row=5,columnspan=5,pady=10)

text_to_scores = Text(window, height=2,width=45)
text_to_scores.grid(row=6, columnspan=5,padx=5,pady=5)

play_again_button = Button(window, text="Play Again",font=('Roboto',14),bg="light blue",
                           height=1,command=play_again)
play_again_button.grid(row=8, column=1,pady=8)

user_notes_label = Label(window, text="Press 'Play Again' after every choice ")
user_notes_label.grid(row=9,column=1,pady=8)



window.mainloop()