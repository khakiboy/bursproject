from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox

f = open("data.txt", "r")
sahamdaran={}
sa=[]
for x in f:
    a=x.split()
    sahamdaran[a[0]]=float(a[1])
    sa.append([a[0]])
f.close()






window = Tk()
window.title("Bakhshizade Burs Application")
window.geometry('300x200')
tab_control = ttk.Notebook(window)

#add_money_page
addmoney_tab = ttk.Frame(tab_control)
tab_control.add(addmoney_tab, text='Add money')
choice_person_label = Label(addmoney_tab, text= 'Choice the person:')
choice_person_label.grid(column=0, row=0)
combo = Combobox(addmoney_tab)
combo['values']= sa
combo.grid(column=1, row=0)
added_value_label = Label(addmoney_tab, text= 'Added value:')
added_value_label.grid(column=0, row=1)
added_value = Entry(addmoney_tab,width=30)
added_value.grid(column=1, row=1)
current_value_label = Label(addmoney_tab, text= 'Current value:')
current_value_label.grid(column=0, row=2)
current_value = Entry(addmoney_tab,width=30)
current_value.grid(column=1, row=2)
show_result_lable=Label(addmoney_tab)
show_result_lable.grid(column=0, row=4)
def clicked():
    f = open("data.txt", "r")
    for x in f:
        a=x.split()
        sahamdaran[a[0]]=float(a[1])
    f.close()
    darayi={}
    for i in sahamdaran.keys():
        darayi[i]=(sahamdaran[i]/100)*int(current_value.get())
    darayi[combo.get()]+=int(added_value.get())
    newbalance=int(current_value.get())+int(added_value.get())
    newdarsad={}
    for i in darayi.keys():
        newdarsad[i]=(darayi[i]/newbalance)*100
    print(newdarsad)
    f = open("data.txt", "w").close()
    f = open("data.txt", "a")
    for i in newdarsad.keys():
        f.write(i+" "+str(newdarsad[i])+'\n')
    f.close()
        

    
btn = Button(addmoney_tab, text="Submit", command=clicked)
btn.grid(column=1, row=3)




#get_money_page
getmoney_tab = ttk.Frame(tab_control)
tab_control.add(getmoney_tab, text='Get money')
choice_person_label1 = Label(getmoney_tab, text= 'Choice the person:')
choice_person_label1.grid(column=0, row=0)
combo1 = Combobox(getmoney_tab)
combo1['values']= sa
combo1.grid(column=1, row=0)
added_value_label1 = Label(getmoney_tab, text= 'Getted value:')
added_value_label1.grid(column=0, row=1)
added_value1 = Entry(getmoney_tab,width=30)
added_value1.grid(column=1, row=1)
current_value_label1 = Label(getmoney_tab, text= 'Current value:')
current_value_label1.grid(column=0, row=2)
current_value1 = Entry(getmoney_tab,width=30)
current_value1.grid(column=1, row=2)
show_result_lable1=Label(getmoney_tab)
show_result_lable1.grid(column=0, row=4)
def clicked():
    f = open("data.txt", "r")
    for x in f:
        a=x.split()
        sahamdaran[a[0]]=float(a[1])
    f.close()
    darayi={}
    for i in sahamdaran.keys():
        darayi[i]=(sahamdaran[i]/100)*int(current_value1.get())
    darayi[combo1.get()]-=int(added_value1.get())
    newbalance=int(current_value1.get())-(int(added_value1.get()))
    newdarsad={}
    for i in darayi.keys():
        newdarsad[i]=(darayi[i]/newbalance)*100
    print(newdarsad)
    f = open("data.txt", "w").close()
    f = open("data.txt", "a")
    for i in newdarsad.keys():
        f.write(i+" "+str(newdarsad[i])+'\n')
    f.close()
        

    
btn = Button(getmoney_tab, text="Submit", command=clicked)
btn.grid(column=1, row=3)

tab_control.pack(expand=1, fill='both')



window.mainloop()
