#a app that record al stock that is in the shelfs and as stock is sold it is deducted from stock,
# keep record from all stockthat is sold



from tkinter import *

import tkinter


import _cffi_backend


from numpy import delete, row_stack

def get_sellected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in _cffi_backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in _cffi_backend.search(Description_text.get(),Code_text.get(),Quantity_text.get(),Supplier_text.get()):
        list1.insert(END,row)

def add_command():
    _cffi_backend.insert(Description_text.get(),Code_text.get(),Quantity_text.get(),Supplier_text.get())
    list1.delete(0,END)
    list1.insert(END,(Description_text.get(),Code_text.get(),Quantity_text.get(),Supplier_text.get()))

def delete_command():
    _cffi_backend.delete(get_sellected_row()[0])

def update_command():
    _cffi_backend.update(selected_tuple[0],Description_text.get(),Code_text.get(),Quantity_text.get(),Supplier_text.get())
     
#def total out function


top=tkinter.Tk()

top.wm_title("Stock Control App")

l1=Label(top,text="Description")
l1.grid(row=0,column=0)

l2=Label(top,text="Code")
l2.grid(row=0,column=2)

l3=Label(top,text="Quantity")
l3.grid(row=1,column=0)

l4=Label(top,text="Supplier")
l4.grid(row=1,column=2)

Description_text=StringVar()
e1=Entry(top,textvariable=Description_text)
e1.grid(row=0,column=1)

Code_text=StringVar()
e2=Entry(top,textvariable=Code_text)
e2.grid(row=0,column=3)

Quantity_text=StringVar()
e3=Entry(top,textvariable=Quantity_text)
e3.grid(row=1,column=1)

Supplier_text=StringVar()
e4=Entry(top,textvariable=Supplier_text)
e4.grid(row=1,column=3)

list1=Listbox(top,height=6,width=35)
list1.grid(row=3,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(top)
sb1.grid(row=3,column=2,rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSellect>>',get_sellected_row)

b1=Button(top,text="View All",width=12)
button_command=view_command
b1.grid(row=3,column=3)

b2=Button(top,text="Stock IN",width=12)
button_command=add_command
b2.grid(row=4,column=3)

b3=Button(top,text="Stock OUT",width=12)
button_command=update_command
b3.grid(row=5,column=3)

b4=Button(top,text="Search",width=12)
button_command=search_command
b4.grid(row=6,column=3)

b5=Button(top,text="Total OUT",width=12)
b5.grid(row=7,column=3)

top.mainloop()