# imports

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

# window gui
win = tk.Tk()
win.title("HALLS OF RESIDENCE AUDIT FORM")

frame = tk.Frame(win)
frame.pack()

# Saving Resident Info Labels and geometry (Names and Room number)
resident_info_frame = tk.LabelFrame(frame,text="Residents Details")
resident_info_frame.grid(row=0,column=0,padx=20, pady=20)

name_label_1 = tk.Label(resident_info_frame,text="NAME: ", font=("Arial", 10, "bold"))
name_label_1.grid(row=0,column=0, sticky = "w")

name_label_2 = tk.Label(resident_info_frame,text="NAME: ", font=("Arial", 10, "bold"))
name_label_2.grid(row=1,column=0,sticky = "w")

name_label_2 = tk.Label(resident_info_frame,text="NAME: ", font=("Arial", 10, "bold"))
name_label_2.grid(row=2,column=0, sticky = "w")

room_number_label = tk.Label(resident_info_frame,text="ROOM NUMBER: ", font=("Arial", 10, "bold"))
room_number_label.grid(row=3,column=0,sticky = "w")

# (Saving) Resident Info Entry Boxes and geometry (Names and Room number)
name_entry_1 = tk.Entry(resident_info_frame, width=40)
name_entry_2 = tk.Entry(resident_info_frame, width=40)
name_entry_3 = tk.Entry(resident_info_frame, width=40)
room_number_entry = tk.Entry(resident_info_frame)

name_entry_1.grid(row=0,column=1)
name_entry_2.grid(row=1,column=1)
name_entry_3.grid(row=2,column=1)
room_number_entry.grid(row=3,column=1)


# Saving Resident Info Labels and geometry (REG NUMBER)
regno_label_1 = tk.Label(resident_info_frame,text="REGNO: ", font=("Arial", 10, "bold"))
regno_label_1.grid(row=0,column=2, sticky = "w")

regno_label_2 = tk.Label(resident_info_frame,text="REGNO: ", font=("Arial", 10, "bold"))
regno_label_2.grid(row=1,column=2,sticky = "w")

regno_label_3 = tk.Label(resident_info_frame,text="REGNO: ", font=("Arial", 10, "bold"))
regno_label_3.grid(row=2,column=2, sticky = "w")

# (Saving) Resident Info Entry Boxes and geometry (REG NUMBER)
regno_entry_1 = tk.Entry(resident_info_frame)
regno_entry_2 = tk.Entry(resident_info_frame)
regno_entry_3 = tk.Entry(resident_info_frame)

regno_entry_1.grid(row=0,column=3)
regno_entry_2.grid(row=1,column=3)
regno_entry_3.grid(row=2,column=3)

# Saving Resident Info Labels and geometry (COLLEGE)
college_label_1 = tk.Label(resident_info_frame,text="COLLEGE: ", font=("Arial", 10, "bold"))
college_label_1.grid(row=0,column=4, sticky = "w")

college_label_2 = tk.Label(resident_info_frame,text="COLLEGE: ", font=("Arial", 10, "bold"))
college_label_2.grid(row=1,column=4,sticky = "w")

college_label_3 = tk.Label(resident_info_frame,text="COLLEGE: ", font=("Arial", 10, "bold"))
college_label_3.grid(row=2,column=4, sticky = "w")

# (Saving) Resident Info Entry Boxes and geometry (COLLEGE)
college_entry_1 = tk.Entry(resident_info_frame)
college_entry_2 = tk.Entry(resident_info_frame)
college_entry_3 = tk.Entry(resident_info_frame)

college_entry_1.grid(row=0,column=5)
college_entry_2.grid(row=1,column=5)
college_entry_3.grid(row=2,column=5)

# For loop to pad multiple widgets in resident_info_frame
for widget in resident_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

# Conditions of room on Day of Occupation/Vacation
conditions_frame = tk.LabelFrame(frame, text="Conditions of Room on Day of Occupation/Vacation")
conditions_frame.grid(row=1,column=0, sticky = "news", padx=20, pady=20)

# items description list(Labels)
item_description_label = tk.Label(conditions_frame,text="ITEM DESCRIPTION", font=("Arial", 10, "bold"))
bed_label = tk.Label(conditions_frame,text="BED: single, 3/4, double")
mattress_label = tk.Label(conditions_frame,text="MATTRESS: single, 3/4, double")
study_table_label = tk.Label(conditions_frame,text="STUDY TABLE: fixed/movable")
book_shelf_label = tk.Label(conditions_frame,text="BOOKSHELF: fixed/movable")
wardrobe_label = tk.Label(conditions_frame,text="WARDROBE: fixed/movable")
wardrobe_key_label = tk.Label(conditions_frame,text="WARDROBE KEY")
chair_label = tk.Label(conditions_frame,text="CHAIR: Padded")
arm_chair_label = tk.Label(conditions_frame,text="ARM CHAIR")
curtains_label = tk.Label(conditions_frame,text="CURTAINS")
door_label = tk.Label(conditions_frame,text="DOOR")
litter_bin_label = tk.Label(conditions_frame,text="LITTER BIN")
dust_pan_label = tk.Label(conditions_frame,text="DUST PAN")
broom_label = tk.Label(conditions_frame,text="BROOM")
door_plaque_label = tk.Label(conditions_frame,text="DOOR PLAQUE")
door_key_n_lock_label = tk.Label(conditions_frame,text="DOOR KEY & LOCK")
curtain_rails_label = tk.Label(conditions_frame,text="CURTAIN RAILS")
floor_tiles_label = tk.Label(conditions_frame,text="FLOOR TILES")
light_switch_label = tk.Label(conditions_frame,text="LIGHT SWITCH")
study_lamp_holder_label = tk.Label(conditions_frame,text="STUDY LAMP HOLDER")
socket_outlet_label = tk.Label(conditions_frame,text="SOCKET OUTLET")
walls_label = tk.Label(conditions_frame,text="WALLS")
window_panes_label = tk.Label(conditions_frame,text="WINDOW PANES")
window_handle_label = tk.Label(conditions_frame,text="WINDOW HANDLE")
window_adjuster_label = tk.Label(conditions_frame,text="WINDOW ADJUSTER")

# items description list(Labels) (geometry)
item_description_label.grid(row=0,column=0,sticky = "w")
bed_label.grid(row=1,column=0,sticky = "w")
mattress_label.grid(row=2,column=0,sticky = "w")
study_table_label.grid(row=3,column=0,sticky = "w")
book_shelf_label.grid(row=4,column=0,sticky = "w")
wardrobe_label.grid(row=5,column=0,sticky = "w")
wardrobe_key_label.grid(row=6,column=0,sticky = "w")
chair_label.grid(row=7,column=0,sticky = "w")
arm_chair_label.grid(row=8,column=0,sticky = "w")
curtains_label.grid(row=9,column=0,sticky = "w")
door_label.grid(row=10,column=0,sticky = "w")
litter_bin_label.grid(row=11,column=0,sticky = "w")
dust_pan_label.grid(row=12,column=0,sticky = "w")
broom_label.grid(row=13,column=0,sticky = "w")
door_plaque_label.grid(row=14,column=0,sticky = "w")
door_key_n_lock_label.grid(row=15,column=0,sticky = "w")
curtain_rails_label.grid(row=16,column=0,sticky = "w")
floor_tiles_label.grid(row=17,column=0,sticky = "w")
light_switch_label.grid(row=18,column=0,sticky = "w")
study_lamp_holder_label.grid(row=19,column=0,sticky = "w")
socket_outlet_label.grid(row=20,column=0,sticky = "w")
walls_label.grid(row=21,column=0,sticky = "w")
window_panes_label.grid(row=22,column=0,sticky = "w")
window_handle_label.grid(row=23,column=0,sticky = "w")
window_adjuster_label.grid(row=24,column=0,sticky = "w")

# Quantity Label
quantity_label = tk.Label(conditions_frame,text="QUANTITY", font=("Arial", 10, "bold"))
bed_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
mattress_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
study_table_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
bookshelf_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
wardrobe_table_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
wardrobe_key_table_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
chair_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
arm_chair_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
curtains_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
door_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
litter_bin_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
dust_pan_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
broom_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
door_plaque_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
door_key_n_lock_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
curtain_rails_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
floor_tiles_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
light_switch_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
study_lamp_holder_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
socket_outlet_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
walls_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
window_panes_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
window_handle_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)
window_adjuster_spinbox = tk.Spinbox(conditions_frame,from_=0, to=100)

# Quantity label (geometry)
quantity_label.grid(row=0,column=1,sticky = "w")
bed_spinbox.grid(row=1,column=1,sticky = "w")
mattress_spinbox.grid(row=2,column=1,sticky = "w")
study_table_spinbox.grid(row=3,column=1,sticky = "w")
bookshelf_spinbox.grid(row=4,column=1,sticky = "w")
wardrobe_table_spinbox.grid(row=5,column=1,sticky = "w")
wardrobe_key_table_spinbox.grid(row=6,column=1,sticky = "w")
chair_spinbox.grid(row=7,column=1,sticky = "w")
arm_chair_spinbox.grid(row=8,column=1,sticky = "w")
curtains_spinbox.grid(row=9,column=1,sticky = "w")
door_spinbox.grid(row=10,column=1,sticky = "w")
litter_bin_spinbox.grid(row=11,column=1,sticky = "w")
dust_pan_spinbox.grid(row=12,column=1,sticky = "w")
broom_spinbox.grid(row=13,column=1,sticky = "w")
door_plaque_spinbox.grid(row=14,column=1,sticky = "w")
door_key_n_lock_spinbox.grid(row=15,column=1,sticky = "w")
curtain_rails_spinbox.grid(row=16,column=1,sticky = "w")
floor_tiles_spinbox.grid(row=17,column=1,sticky = "w")
light_switch_spinbox.grid(row=18,column=1,sticky = "w")
study_lamp_holder_spinbox.grid(row=19,column=1,sticky = "w")
socket_outlet_spinbox.grid(row=20,column=1,sticky = "w")
walls_spinbox.grid(row=21,column=1,sticky = "w")
window_panes_spinbox.grid(row=22,column=1,sticky = "w")
window_handle_spinbox.grid(row=23,column=1,sticky = "w")
window_adjuster_spinbox.grid(row=24,column=1,sticky = "w")

# Create a date entry (Date of issue Labels)
date_of_issue_label = tk.Label(conditions_frame,text="DATE OF ISSUE", font=("Arial", 10, "bold"))
bed_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
mattress_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
study_table_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
book_shelf_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
wardrobe_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
wardrobe_key_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
chair_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
arm_chair_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
curtains_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
door_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
litter_bin_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
dust_pan_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
broom_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
door_plaque_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
door_key_n_lock_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
curtain_rails_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
floor_tiles_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
light_switch_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
study_lamp_holder_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
socket_outlet_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
walls_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
window_panes_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
window_handle_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)
window_adjuster_date_entry = DateEntry(conditions_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=8, day=25)

# Create a date entry (Date of issue geometry)
date_of_issue_label.grid(row=0,column=2)
bed_date_entry.grid(row=1,column=2)
mattress_date_entry.grid(row=2,column=2)
study_table_date_entry.grid(row=3,column=2)
book_shelf_date_entry.grid(row=4,column=2)
wardrobe_date_entry.grid(row=5,column=2)
wardrobe_key_date_entry.grid(row=6,column=2)
chair_date_entry.grid(row=7,column=2)
arm_chair_date_entry.grid(row=8,column=2)
curtains_date_entry.grid(row=9,column=2)
door_date_entry.grid(row=10,column=2)
litter_bin_date_entry.grid(row=11,column=2)
dust_pan_date_entry.grid(row=12,column=2)
broom_date_entry.grid(row=13,column=2)
door_plaque_date_entry.grid(row=14,column=2)
door_key_n_lock_date_entry.grid(row=15,column=2)
curtain_rails_date_entry.grid(row=16,column=2)
floor_tiles_date_entry.grid(row=17,column=2)
light_switch_date_entry.grid(row=18,column=2)
study_lamp_holder_date_entry.grid(row=19,column=2)
socket_outlet_date_entry.grid(row=20,column=2)
walls_date_entry.grid(row=21,column=2)
window_panes_date_entry.grid(row=22,column=2)
window_handle_date_entry.grid(row=23,column=2)
window_adjuster_date_entry.grid(row=24,column=2)


# condition of item (GOOD/DAMAGED)
condition_of_item_label = tk.Label(conditions_frame,text="CONDITION OF ITEM", font=("Arial", 10, "bold"))
bed_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
mattress_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
study_table_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
bookshelf_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
wardrobe_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
wardrobe_key_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
chair_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
arm_chair_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
curtains_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
door_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
litter_bin_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
dust_pan_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
broom_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
door_plaque_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
door_key_n_lock_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
curtain_rails_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
floor_tiles_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
light_switch_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
study_lamp_holder_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
socket_outlet_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
walls_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
window_panes_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
window_handle_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])
window_adjuster_combobox = ttk.Combobox(conditions_frame, values = ["","Good", "Damaged"])

# condition of item (GOOD/DAMAGED) geometry
condition_of_item_label.grid(row=0, column=3)
bed_combobox.grid(row=1, column=3)
mattress_combobox.grid(row=2, column=3)
study_table_combobox.grid(row=3, column=3)
bookshelf_combobox.grid(row=4, column=3)
wardrobe_combobox.grid(row=5, column=3)
wardrobe_key_combobox.grid(row=6, column=3)
chair_combobox.grid(row=7, column=3)
arm_chair_combobox.grid(row=8, column=3)
curtains_combobox.grid(row=9, column=3)
door_combobox.grid(row=10, column=3)
litter_bin_combobox.grid(row=11, column=3)
dust_pan_combobox.grid(row=12, column=3)
broom_combobox.grid(row=13, column=3)
door_plaque_combobox.grid(row=14, column=3)
door_key_n_lock_combobox.grid(row=15, column=3)
curtain_rails_combobox.grid(row=16, column=3)
floor_tiles_combobox.grid(row=17, column=3)
light_switch_combobox.grid(row=18, column=3)
study_lamp_holder_combobox.grid(row=19, column=3)
socket_outlet_combobox.grid(row=20, column=3)
walls_combobox.grid(row=21, column=3)
window_panes_combobox.grid(row=22, column=3)
window_handle_combobox.grid(row=23, column=3)
window_adjuster_combobox.grid(row=24, column=3)


















'''# For loop to pad multiple widgets in resident_info_frame
for widget in conditions_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)'''

win.mainloop()





