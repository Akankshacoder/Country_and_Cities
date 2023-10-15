from tkinter import*
import random as r1
root= Tk()
root.title("Fibonacci")
root.geometry("400x400")

l1 = Label(root,text="Country Name: ")
l1.place(relx=0.5, rely=0.5, anchor=CENTER)

l2 = Label(root, text="City Name: ")
l2.place(relx=0.5, rely=0.6, anchor=CENTER)

l3 = Label(root, text="Random Country: ")
l3.place(relx=0.5, rely=0.8, anchor=CENTER)

l4 = Label(root, text="Random City: ")
l4.place(relx=0.5, rely=0.9, anchor=CENTER)


e1=Entry(root)
e1.place(relx=0.5, rely=0.2, anchor=CENTER)
list_1=[]

e2=Entry(root)
e2.place(relx=0.5, rely=0.3, anchor=CENTER)

list_1=[]
list_2=[]
def dis():
    inp= e1.get()
    list_2.append(inp)
    l1["text"]=+ str(list_1)
    l2["text"]=+ str(list_2)
    e1.delete(0,END)
    
def disrand():
    l= len(list_1)
    ltwo= len(list_2)
    rn = r1.randint(0,l-1)
    rn2 = r1.randint(0,ltwo-1)
    lthree = list_1[rn]
    lfour = list_2[rn2]
    l3["text"]=+ str(lthree)
    l4["text"]=+ str(lfour)
    

b1 = Button(root, text="Display Country And City Name", command= dis)
b1.place(relx=0.5,rely= 0.4, anchor=CENTER)

b2 = Button(root, text="Display Country And City Name Randomly", command= disrand)
b2.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()