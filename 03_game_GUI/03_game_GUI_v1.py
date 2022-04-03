from tkinter import *
from functools import partial   # To prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)


    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes =1

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()

class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # disable low stakes button
        partner.lowstakes_button.config(state=DISABLED)

        # initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # balance
        self.balance_label = Label(self.game_frame, text="")
        self.balance_label.grid(row=1)

        self.gain_button = Button(self.game_frame, text="Gain",
                                  command=partial(self.reveal_boxes))
        self.gain_button.grid(row=2)

    def reveal_boxes(self):
        # retrieve the balance from the initial function
        current_balance = self.balance.get()

        # Adjust the balance (substract game cost and add pay out)
        # for testing purposes, just add 2
        current_balance += 2

        # set balance to adjusted balance
        self.balance.set(current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game!!")
    something = Start(root)

    root.mainloop()
