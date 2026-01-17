from tkinter import *
from os import path
import os
from PIL import Image, ImageTk
import random
import time
#цикл обработки нажатия кнопки следующее фото для смены картинок
def change_photo():
    anim=random.sample(list_image, 4)
    
    find_photo=random.choice(anim)
    for i, but in enumerate(all_button):
        img_p= PhotoImage(file=directory+anim[i]).subsample(4,4)
        but.configure(image=img_p)
        but.image=img_p   
        lbl_find.configure(text=find_photo.replace(".png",""))  
    global animal_list, target_photo
    animal_list=anim
    target_photo=find_photo
    

def find_img (list,foto):
    if list==foto:
        tk.configure(background='green')
        tk.after(400,lambda: tk.configure(background='SystemButtonFace'))
        
    else:
        tk.configure(background='red')
        tk.after(400,lambda: tk.configure(background='SystemButtonFace'))
        
        
tk = Tk()
tk.title('Обучение по картинкам')
tk.geometry('1245x600')
tk.resizable(0,0)
directory='C:\\PyProject\\test\\alenv\\animal\\'
#получаем список всех фото из папки
fr1=Frame(tk)
fr2=Frame(tk)
fr3=Frame(tk)
fr1.pack(fill=X,padx=10,pady=20)
fr2.pack()
fr3.pack(fill=X, padx=10,pady=35)
list_image=os.listdir(directory)
random.shuffle(list_image)
animal_list=random.sample(list_image, 4)
target_photo=random.choice(animal_list)

lbl0 = Label(fr1, text='Найди картинку: ', font='Gabriola 30',fg='blue')
#lbl0.grid(column=0, row=0)
lbl0.pack(side=LEFT, expand=0, padx=10, fill=X)
lbl_find = Label(fr1, text ="имя картинки" ,font='Gabriola 35',fg='red')
lbl_find.pack(side=LEFT, padx=10, expand=0, fill=X)
#lbl_find.grid(column=1, row=0)

img0= PhotoImage(file=directory+animal_list[0]).subsample(4,4)
lab_anim0=Button(fr2, image=img0, highlightthickness=0)
lab_anim0.image=img0
lab_anim0.bind("<Enter>", lambda event:lab_anim0.configure(background='blue'))
lab_anim0.bind("<Leave>", lambda event:lab_anim0.configure(background='lightgray'))
lab_anim0.grid(column=0, row=1, padx=3)

img1= PhotoImage(file=directory+animal_list[1]).subsample(4,4)
lab_anim1=Button(fr2,image=img1, highlightthickness=0)
lab_anim1.image=img1
lab_anim1.bind("<Enter>", lambda event:lab_anim1.configure(background='blue'))
lab_anim1.bind("<Leave>", lambda event:lab_anim1.configure(background='lightgray'))
lab_anim1.grid(column=1, row=1, padx=3)
   
img2= PhotoImage(file=directory+animal_list[2]).subsample(4,4)
lab_anim2=Button(fr2,image=img2, highlightthickness=0)
lab_anim2.image=img2
lab_anim2.bind("<Enter>", lambda event:lab_anim2.configure(background='blue'))
lab_anim2.bind("<Leave>", lambda event:lab_anim2.configure(background='lightgray'))
lab_anim2.grid(column=2, row=1, padx=3)

img3= PhotoImage(file=directory+animal_list[3]).subsample(4,4)
lab_anim3=Button(fr2, image=img3, highlightthickness=0)
lab_anim3.image=img3
lab_anim3.bind("<Enter>", lambda event:lab_anim3.configure(background='blue'))
lab_anim3.bind("<Leave>", lambda event:lab_anim3.configure(background='lightgray'))
lab_anim3.grid(column=3, row=1, padx=3)
lbl_find.configure(text=target_photo.replace(".png",""))

all_button=[lab_anim0,lab_anim1,lab_anim2,lab_anim3]

next_btn=Button(fr3,text="далее", font='Gabriola 45', background='yellow', command=change_photo)
next_btn.pack(side=LEFT, expand=1, fill=X)
lab_anim0.configure(command=lambda: find_img(animal_list[0],target_photo))
lab_anim1.configure(command=lambda: find_img(animal_list[1],target_photo))
lab_anim2.configure(command=lambda: find_img(animal_list[2],target_photo))
lab_anim3.configure(command=lambda: find_img(animal_list[3],target_photo))
tk.mainloop()