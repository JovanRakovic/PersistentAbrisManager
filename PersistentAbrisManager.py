import ttkbootstrap as ttk
from tkinter import filedialog as fd
import os
import shutil

routes = "ROUTES.lua"
additional = "ADDITIONAL.lua"
navigation = "NAVIGATION.lua"

database_str = "Database"
dtb_path = "./ABRIS/Database/"

collection_list = []

def set_create_update_btn(update):
    if update:
        create_update_btn.config(text="Update")
    else:
        create_update_btn.config(text="Create")

def append_to_collection_display(col_name):
    r=a=n='-'
    col_dtb = os.listdir("./ABRIS/"+col_name+"/")
    if routes in col_dtb:
        r = '+' 
    if additional in col_dtb:
        a = '+' 
    if navigation in col_dtb:
        n = '+'
    collections_display_treeview.insert('','end',values=(col_name, r, a, n))
    collection_list.append(col_name)

def get_collections():
    collection_list.clear()
    collections_display_treeview.delete(*collections_display_treeview.get_children())
    path = "./ABRIS/"
    dir_list = os.listdir(path)
    append_to_collection_display(database_str)
    for col in dir_list:
        if col == database_str or col == "Loader" or "." in col:
            continue
        append_to_collection_display(col)

def selectedCollection(event):
    item = collections_display_treeview.focus()
    col_name_entry.delete(0, 'end')
    col_name_entry.insert(0, collections_display_treeview.item(item, option="values")[0])
    set_create_update_btn(True)

def check_for_collection_name_match(*args):
    col_name = col_name_string_var.get().strip()
    if col_name == database_str:
        col_name = ""
        col_name_string_var.set(col_name)
    if col_name in collection_list:
        set_create_update_btn(True)
    else:
        set_create_update_btn(False)

def create_update_collection():
    col_name = col_name_string_var.get().strip()
    if col_name == "":
        return

    path = "./ABRIS/" + col_name + "/"
    if not (col_name in collection_list):
        try:
            os.mkdir(path)
        except FileExistsError:
            print(f"Directory already exists.")
            return
        except PermissionError:
            print(f"Permission denied")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        
    dir_list = os.listdir(dtb_path)
    if check_routes_var.get() and routes in dir_list:
        shutil.copy(dtb_path+routes,path)
    if check_additinoal_var.get() and additional in dir_list:
        shutil.copy(dtb_path+additional,path)
    if check_nav_var.get() and navigation in dir_list:
        shutil.copy(dtb_path+navigation,path)
    get_collections()

def delete():
    col_name = col_name_string_var.get().strip()
    if not (col_name in collection_list):
        return
    
    path = "./ABRIS/" + col_name + "/"
    dir_list = os.listdir(path)
    if dir_list == []:
        os.rmdir(path)
    else:
        if check_routes_var.get() and routes in dir_list:
            os.remove(path+routes)
        if check_additinoal_var.get() and additional in dir_list:
            os.remove(path+additional)
        if check_nav_var.get() and navigation in dir_list:
            os.remove(path+navigation)
    get_collections()

def clear():
    dir_list = os.listdir(dtb_path)
    if check_routes_var.get() and routes in dir_list:
        os.remove(dtb_path+routes)
    if check_additinoal_var.get() and additional in dir_list:
        os.remove(dtb_path+additional)
    if check_nav_var.get() and navigation in dir_list:
        os.remove(dtb_path+navigation)
    get_collections()

def load():
    col_name = col_name_string_var.get().strip()
    if not (col_name in collection_list):
        return
    
    path = "./ABRIS/" + col_name + "/"
    dir_list = os.listdir(path)
    if check_routes_var.get() and routes in dir_list:
        shutil.copy(path+routes,dtb_path)
    if check_additinoal_var.get() and additional in dir_list:
        shutil.copy(path+additional,dtb_path)
    if check_nav_var.get() and navigation in dir_list:
        shutil.copy(path+navigation,dtb_path)
    get_collections()

def set_dcs_root_path():
    path = fd.askdirectory(title="Select DCS root directory")
    path = path+"/Mods/aircraft/Ka-50_3/Cockpit/Scripts/Devices_specs/"

    if not os.path.isdir(path):
        return

    dcs_root_string_var.set(path)

    file = open("./parameters.txt","w")
    file.write(path)
    file.close()

def load_file_parameters():
    try:
        file = open("./parameters.txt")
        dcs_root_string_var.set(file.read())
        file.close()
    except:
        return

def replace_abris_lua():
    path = dcs_root_entry.get()
    shutil.copy(path+"ABRIS.lua",path+"ABRIS_old.lua")
    shutil.copy("./ABRIS.lua",path+"ABRIS.lua")

root = ttk.Window(themename="darkly")
root.title("PAM - PersistentAbrisManager")
root.geometry('500x300')

padX = 5
padY = 5

btn_padX = 3
btn_padY = 3

label_padX = 7
label_padY = 2

ipadX = 0
ipadY = 0

for i in range(0,5):
    root.rowconfigure(i, weight=1)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

#Collection name lable and entry
col_name_label_frame = ttk.Labelframe(text="Collection Name", border=0)
col_name_label_frame.grid(column=0,row=0,padx=label_padX, pady=label_padY, ipadx=0, ipady=0, sticky="ew")
col_name_label_frame.columnconfigure(0, weight=1)

col_name_string_var = ttk.StringVar()
col_name_string_var.trace_add("write", check_for_collection_name_match)

col_name_entry = ttk.Entry(col_name_label_frame, textvariable=col_name_string_var)
col_name_entry.grid(column=0, row=0, padx=0, pady=0, sticky="ew")

#Check buttons for selecting which data to save(update)/load/unload/delete
data_files_label_frame = ttk.Labelframe(text="Database Files")
data_files_label_frame.grid(column=0,row=1, padx=label_padX, pady=label_padY, ipadx=ipadX, ipady=ipadY, sticky="ew")

check_routes_var = ttk.BooleanVar()
check_additinoal_var = ttk.BooleanVar()
check_nav_var = ttk.BooleanVar()

check_routes_var.set(False)
check_additinoal_var.set(False)
check_nav_var.set(False)

check_routes =      ttk.Checkbutton(data_files_label_frame, onvalue=True, offvalue=False, variable=check_routes_var, text="Routes")
check_additional =  ttk.Checkbutton(data_files_label_frame, onvalue=True, offvalue=False, variable=check_additinoal_var, text="Additional Inf.")
check_nav =         ttk.Checkbutton(data_files_label_frame, onvalue=True, offvalue=False, variable=check_nav_var, text="Navigation")

check_routes.grid       (column=0, row=0, padx=padX, pady=padY)
check_additional.grid   (column=1, row=0, padx=padX, pady=padY)
check_nav.grid          (column=2, row=0, padx=padX, pady=padY)

#Buttons for create(update)/unload/delete
manipulation_btns_label_frame = ttk.Labelframe(text="Collection and DTB control buttons")
manipulation_btns_label_frame.grid(column=0, row=2, padx=label_padX, pady=label_padY, ipadx=ipadX, ipady=ipadY, sticky="ew")
manipulation_btns_label_frame.rowconfigure(0, weight=1)
manipulation_btns_label_frame.rowconfigure(1, weight=1)
manipulation_btns_label_frame.columnconfigure(0, weight=3)
manipulation_btns_label_frame.columnconfigure(1, weight=3)
manipulation_btns_label_frame.columnconfigure(2, weight=1)

create_update_btn =     ttk.Button(manipulation_btns_label_frame, text="Create", command=create_update_collection, bootstyle="success")
unload_btn =            ttk.Button(manipulation_btns_label_frame, text="Load", command=load, bootstyle="info")
clear_btn =             ttk.Button(manipulation_btns_label_frame, text="Clear", command=clear, bootstyle="info")
delete_btn =            ttk.Button(manipulation_btns_label_frame, text="Delete", command=delete, bootstyle="danger")
refresh_btn =           ttk.Button(manipulation_btns_label_frame, text="Refresh", command=get_collections, bootstyle="info")

create_update_btn.grid      (column=0, row=0, padx=btn_padX, pady=btn_padY, sticky="ew")
unload_btn.grid             (column=1, row=0, padx=btn_padX, pady=btn_padY, sticky="ew")
clear_btn.grid              (column=1, row=1, padx=btn_padX, pady=btn_padY, sticky="ew")
delete_btn.grid             (column=0, row=1, padx=btn_padX, pady=btn_padY, sticky="ew")
refresh_btn.grid            (column=2, row=0, columnspan=2, rowspan=2, padx=btn_padX, pady=btn_padY, sticky="ewns")

#DCS root file label, entry and replace abris button
dcs_root_label_frame = ttk.Labelframe(text="DCS root directory")
dcs_root_label_frame.grid(column=0, row=3, padx=label_padX, pady=label_padY, ipadx=ipadX, ipady=ipadY, sticky="ew")
dcs_root_label_frame.columnconfigure(0,weight=1)
dcs_root_label_frame.columnconfigure(1,weight=1)

dcs_root_get_dir_btn = ttk.Button(dcs_root_label_frame, text="Select Directory", command=set_dcs_root_path, bootstyle="info")
dcs_root_apply_btn = ttk.Button(dcs_root_label_frame, text="Replace Abris.lua", command=replace_abris_lua, bootstyle="success")

dcs_root_get_dir_btn.grid(column=0, row=0, padx=padX, pady=padY, sticky="ew")
dcs_root_apply_btn.grid(column=1, row=0, padx=padX, pady=padY, sticky="ew")

dcs_root_string_var = ttk.StringVar()

dcs_root_entry = ttk.Entry(dcs_root_label_frame, textvariable=dcs_root_string_var)
dcs_root_entry.config(state="readonly")
dcs_root_entry.grid(column=0, columnspan=2, row=1, padx=padX, pady=padY, sticky="ew")

#Treeview for sellecting collections
collections_display_label_frame = ttk.Labelframe(text="Collections", border=0)
collections_display_label_frame.grid(column=1, row=0, rowspan=4, padx=label_padX, pady=label_padY, ipadx=ipadX, ipady=ipadY, sticky="ewns")
collections_display_label_frame.columnconfigure(0,weight=1)
collections_display_label_frame.rowconfigure(0,weight=1)

collections_display_treeview = ttk.Treeview(collections_display_label_frame, columns=[0,1,2,3], show="headings")
collections_display_treeview.heading(0, text="Name", anchor="w")
collections_display_treeview.column(0, width=120, minwidth=100, stretch=True)
collections_display_treeview.heading(1, text="R")
collections_display_treeview.heading(2, text="A")
collections_display_treeview.heading(3, text="N")
for i in range(1,4):
    collections_display_treeview.column(i, width=25,  minwidth=25, stretch=False, anchor="center")

collections_display_treeview.bind("<Double-1>", selectedCollection)

collections_display_treeview.grid(column=0, row=0, padx=padX, pady=padY, sticky="ewns")

get_collections()
load_file_parameters()

root.mainloop()