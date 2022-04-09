from tkinter import *
from functools import partial   # To prevent unwanted windows
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
                                  font="Arial 24 bold", padx=10, pady=10,
                                   command=self.to_help)
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

        # Dismiss Button
        self.dismiss_btn = Button(self.details_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold",command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=5)

    def close_stats(self, partner):
        # put help button back to normal...

        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game!!")
    something = Game()

    root.mainloop()
