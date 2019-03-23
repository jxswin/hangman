from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import wSelect

window=Tk()
window.title("Hangman.exe")
window.configure(bg='black',height=650,width=500)
window.iconbitmap('hmicon.jpg')

frame=Frame(window,bg='white')
frame.configure(height=640,width=490)
frame.place(x=5,y=5)

#importing a word
new_ip=get_word()
lenip=len(new_ip)
list1='_'
list2=[]
print(new_ip)

#set of characters in new_ip
list3=[]

#no repetition of letters
list4=[]

#sort image
img0=ImageTk.PhotoImage(Image.open("hm00.jpg"))
img1=ImageTk.PhotoImage(Image.open("hm01.jpg"))
img2=ImageTk.PhotoImage(Image.open("hm02.jpg"))
img3=ImageTk.PhotoImage(Image.open("hm03.jpg"))
img4=ImageTk.PhotoImage(Image.open("hm04.jpg"))
img5=ImageTk.PhotoImage(Image.open("hm05.jpg"))
img6=ImageTk.PhotoImage(Image.open("hm06.jpg"))
img7=ImageTk.PhotoImage(Image.open("hm07.jpg"))
img8=ImageTk.PhotoImage(Image.open("hm08.jpg"))
img9=ImageTk.PhotoImage(Image.open("hm09.jpg"))
img10=ImageTk.PhotoImage(Image.open("hm10.jpg"))
img11=ImageTk.PhotoImage(Image.open("hm11.jpg"))
img12=ImageTk.PhotoImage(Image.open("hm12.jpg"))
img13=ImageTk.PhotoImage(Image.open("hm13.jpg"))

img=[img0,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13]
i=0
#functions
def mkunder(new_ip):
    #printing underscores
    list2.clear()
    for i in range(0,len(new_ip)):
        list2.append(list1)
mkunder(new_ip)
 
def mkset(new_ip):
    list3.clear()
    for char in new_ip:
        list3.append(char)

mkset(new_ip)
    
def convert(l): 
    new = ""   
    for x in l: 
        new += x 
        new += ' '
    return new 

def click():
    global i
    if(i < 12):
        ip=tBox.get()
        if (len(ip)==0):
            messagebox.showinfo("OOPS","EMPTY TEXTBOX")
        else:
            tBox.delete(0,10)
            check(ip)
            v.set(convert(list2))
            print(list2)
            check_finish()
    else:
        change()
    

    
def check(ip):
    global i
    if ip in list3 and ip not in list4:
        list4.append(ip)
        for j in range(len(list3)):
            if ip==list3[j]:
                list2[j]=ip
    else:
        i+=1
        imag()
        if (i==12):
            messagebox.showinfo("OOPS","The correct word is  " +convert(list3))
        else:
            if ip in list3:
                messagebox.showinfo("OOPS","LETTER REPEATED")
            else:
                messagebox.showinfo("OOPS","LETTER NOT IN WORD")
    
            #flag increment
def check_finish():
    global i
    us='_'
    if us not in list2:
        i=13
        imag()
        
def change():
    global i
    i=0
    tBox.delete(0,3)
    new_ip=get_word()
    print(new_ip)
    mkunder(new_ip)
    print(list2)
    v.set(convert(list2))
    mkset(new_ip)
    print(list3)
    list4.clear()
    imag()
        
      
#functions_end
    



l1=Label(frame,text='HANGMAN',fg='black',bg='white',font='comicsans 20 bold')
l1.place(anchor=N,relx=0.5)

#image
def imag():
    global i
    l3=Label(frame,image=img[i],height=400,width=400)
    l3.place(anchor=CENTER,relx=0.5,rely=0.38)
imag()    

#output box
v=StringVar(value=list2)
l2=Label(frame,textvariable=v,fg='black',bg='white',font='times 20')
l2.place(anchor=CENTER,relx=0.5,rely=0.75)

#submit button
b1=Button(frame, text='SUBMIT',font='times 14',width=15,height=3,command=click)
b1.place(anchor=CENTER,relx=0.8,rely=0.87)

#change word button
b2=Button(frame, text='CHANGE',font='times 14',width=15,height=3,command=change)
b2.place(anchor=CENTER,relx=0.2,rely=0.87)

#input character box
tBox=Entry(frame,font='none 18', width=5, bg='white')
tBox.place(anchor=CENTER,relx=0.5,rely=0.87)


window.mainloop()
