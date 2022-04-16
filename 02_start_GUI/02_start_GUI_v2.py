from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

             # Initial Instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                          "(between $5 and $50) in the box "
                                          "below. Then choose the stakes. "
                                          "The higher the stakes, the more "
                                          "you can win!", wrap=275, justify=LEFT,
                                          padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)

        # Entry box (row 2)
        self.start_amount_entry = Entry(self.entry_error_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=0)

        self.amount_error_label = Label(self.entry_error_frame, font="Arial 10 bold", fg="#ffafaf",
                                        wrap=275, justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # buttons go here...
        button_font = "Arial 12 bold"
        # Orange low stakes button...
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)",
                                      command=lambda: self.to_game(1),
                                       font=button_font, bg="#FF9933")
        self.low_stakes_button.grid(row=0, column=0, pady=10)

        # Yellow medium stakes button...
        self.medium_stakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="#FFFF33")
        self.medium_stakes_button.grid(row=0, column=1, padx=5, pady=10)

        # Green medium stakes button...
        self.high_stakes_button = Button(self.stakes_frame, text="High ($15)",
                                       command=lambda: self.to_game(3),
                                       font=button_font, bg="#99FF33")
        self.high_stakes_button.grid(row=0, column=2, padx=5, pady=10)

        # Help Button
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="black", font=button_font)
        self.help_button.grid(row=4, pady=10)



    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()

        # set error background colours (and assume that there are no errors at the start
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes)
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you " \
                                 "can play with is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! The most you can risk in "\
                                 "this game is $50"
            elif starting_balance < 10 and (stakes == 2 or stakes == 3):
                has_errors = "yes"
                error_feedback = "Sorry, you can only afford to "\
                                 "play a low stakes game."

            elif starting_balance < 15 and stakes == 3:
                has_errors = "yes"
                error_feedback = "Sorry, you can only afford to "\
                                 "play a low or medium stakes game."

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount ( not text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            Game(self, stakes, starting_balance)

        # hide start up window
        # root.withdraw()

class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)



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





