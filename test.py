from tkinter import Tk, ttk, CENTER, NO

from db_worker import Database

# def get_player_to_sort(player):
#     return player[3] if player[2] + player[3] == 0 else (player[3], player[3] / (player[2] + player[3]))

db = Database('users.db')
players = db.get_all_values()[:10]
players = sorted(players, key=lambda x: (x[3], x[3] / (x[2] + x[3] + 1)), reverse=True)

root = Tk()
root.geometry('500x500')

table = ttk.Treeview()
table['columns'] = (0, 1, 2, 3)

table.column('#0', width=0, stretch=NO)
table.column(0, anchor=CENTER)
table.column(1, anchor=CENTER)
table.column(2, anchor=CENTER)
table.column(3, anchor=CENTER)

table.heading('#0', text='', anchor=CENTER)
table.heading(0, text='id')
table.heading(1, text='user_name')
table.heading(2, text='wrong_answers')
table.heading(3, text='right_answers')

for player in players:
    table.insert(parent='', index='end', text='', values=player)

table.pack()

root.mainloop()
