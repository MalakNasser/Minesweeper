from tkinter import *
from Cell import Cell
import Settings
import Utilities

root = Tk()

#Override the settings of the window
root.configure(bg="green")
root.geometry(f'{Settings.WIDTH}x{Settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='darkgreen',
    width=Settings.WIDTH,
    height=Utilities.height_prct(20)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='darkgreen',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)
game_title.place(
    x=Utilities.width_prct(13), y = 20
)

left_frame = Frame(
    root,
    bg='darkgreen',
    width=Utilities.width_prct(20),
    height=Utilities.height_prct(80)
)
left_frame.place(x=0, y=120)

left_lable = Label(
    left_frame,
    bg='darkgreen',
    fg='white',
    text=f'Total mines: {Settings.MINES_COUNT}',
    font=('', 15)
)
left_lable.place(
    x=14, y = 60
)

middle_frame = Frame(
    root,
    bg='black',
    width=Utilities.width_prct(80),
    height=Utilities.height_prct(80)
)
middle_frame.place(x=Utilities.width_prct(25),
                   y=Utilities.height_prct(25)
)

for i in range(Settings.GRID_SIZE):
    for j in range(Settings.GRID_SIZE):
        c = Cell(i, j)
        c.create_btn_object(middle_frame)
        c.cell_btn_object.grid(
            column=i, row=j
        )

#Call the lable from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=18, y=20)

Cell.randomize_mines()

#Run the window
root.mainloop()