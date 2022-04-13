from tkinter import *
from functools import partial   # To prevent unwanted windows
import re
import random

class Game:
    def __init__(self):

        # Formatting variables...
        self.game_stats_list = [50, 6]

        # In actual program this is blank and is populated with user calculations
        self.round_stats_list = ['silver ($4) | silver ($4) | lead ($0)- Cost: $10 | Payback: $8 | Current Balance:$48',
                                 'lead ($0) | silver ($4) | gold ($0)- Cost: $10 | Payback: $14 | Current Balance:$52',
                                 'lead ($0) | lead ($0) | copper ($2)- Cost: $10 | Payback: $2 | Current Balance:$44',
                                 'copper ($2) | lead ($0) | copper ($2)- Cost: $10 | Payback: $4 | Current Balance:$38'
                                 'lead ($0) | lead ($0) | lead ($0)- Cost: $10 | Payback: $0 | Current Balance:$28']
        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label =Label(self.game_frame, text="Play...",
                                  font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # History Button (row 1)
        self.stats_button = Button(self.game_frame, text="Game Stats",
                                   font="Arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

class GameStats:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading="Arial 12 bold"
        content="Areal 12"

        # sets up child window
        self.stats_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # set up Gui frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # set up help heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # to export <instructions>
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Game Statistics."
                                             "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green", padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Starting Balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Starting balance (row 2.0)
        self.start_balance_label = Label(self.details_frame, text="Starting Balance:",
                                         font=heading, anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                               text="${}".format(game_stats[0]),
                                               anchor="w")
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # Current Balance(row 2.2)
        self.current_balance_label = Label(self.details_frame, text="Current Balance:",
                                         font=heading, anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                               text="${}".format(game_stats[1]),
                                               anchor="w")
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        if game_stats[1] >game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost(2.3)
        self.wind_loss_label = Label(self.details_frame,
                                     text=win_loss, font=heading,
                                     anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.details_frame,
                                      font=content, text="${}".format(amount),
                                      fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2, column=1, padx=0)

        self.games_played_label = Label(self.details_frame,
                                     text="Rounds Played:", font=heading,
                                     anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame,
                                      font=content, text=len(game_history),
                                      anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        # Export Button
        self.export_button = Button(self.details_frame, text="Export",
                                    width=10, bg="#660000", fg="white",
                                    font="arial 15 bold",
                                    command=lambda: self.export(game_history, game_stats))
        self.export_button.grid(row=5, column=0)
        # Dismiss Button
        self.dismiss_btn = Button(self.details_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold",command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=5, column=1)

    def close_stats(self, partner):
        # put help button back to normal...

        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, game_history, game_stats):
        Export(self, game_history, game_stats)

class Export:
    def __init__(self, partner, game_history, all_game_stats):
        print(game_history)

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'release' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # set up child GUI Frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions", font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Export instructions(label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                 "in the box below "
                                 "and press the Save "
                                 "button to save your "
                                 "stats history "
                                 "to a text file.",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label,row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                 "you enter below "
                                 "already exists, "
                                 "its contents will "
                                 "be replaced with "
                                 "your stats "
                                 "history", justify=LEFT, bg="#ffafaf", fg="maroon", font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2,pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

         # Error Message Labels
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons(row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, game_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#003366", fg="white",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, game_history, game_stats):
        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename -{}".format(problem))
            # change the entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file and then clost
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # heading for stats
            f.write("Game Statistics\n\n")

            # add new line at end of each item
            for round in game_stats:
                f.write(str(round) + "\n")

            # heading for stats
            f.write("\nRound Details\n\n")

            # add new line at end of each item
            for item in game_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)


    def close_export(self, partner):
        #put export button back to normal...

        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game!!")
    something = Game()
    root.mainloop()
