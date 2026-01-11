from tkinter import *
import os
from PIL import Image, ImageTk
import random
def change_photo():
    def tru_pic(event):
        button=event.widget
        
    anim=random.sample(list_animal, 4)
    find_photo=random.choice(anim)
    buttons=[]
    for i, img in enumerate(anim):
        img= PhotoImage(file=dir_animal+anim[i]).subsample(4,4)
        lab_anim=Button(image=img, highlightthickness=0)
        lab_anim.bind('<Button-1>', lambda: tru_pic(anim[i]) )
        lab_anim.image=img
        lab_anim.grid(column=i, row=1, padx=5)
        buttons.append(lab_anim)
   
        
    lbl_find.configure(text=find_photo.replace(".png",""))
    next_btn.configure(text="Следующий слайд")
        
    '''img0= PhotoImage(file=dir_animal+anim[0]).subsample(4,4)
    lab_anim0=Button(image=img0, highlightthickness=0)
    lab_anim0.image=img0
    lab_anim0.grid(column=0, row=1, padx=5)
    print(id(lab_anim0))
    img1= PhotoImage(file=dir_animal+anim[1]).subsample(4,4)
    lab_anim1=Button(image=img1, highlightthickness=0)
    lab_anim1.image=img1
    lab_anim1.grid(column=1, row=1, padx=5)
   
    img2= PhotoImage(file=dir_animal+anim[2]).subsample(4,4)
    lab_anim2=Button(image=img2, highlightthickness=0)
    lab_anim2.image=img2
    lab_anim2.grid(column=2, row=1, padx=5)
  
    img3= PhotoImage(file=dir_animal+anim[3]).subsample(4,4)
    lab_anim3=Button(image=img3, highlightthickness=0)
    lab_anim3.image=img3
    lab_anim3.grid(column=3, row=1, padx=5)
    lbl_find.configure(text=find_photo.replace(".png",""))
    next_btn.configure(text="Следующий слайд")
    lab_anim0.bind("<Enter>", lambda event:lab_anim0.configure(background='red'))
    lab_anim0.bind("<Leave>", lambda event:lab_anim0.configure(background='lightgray'))
    lab_anim1.bind("<Enter>", lambda event:lab_anim1.configure(background='red'))
    lab_anim1.bind("<Leave>", lambda event:lab_anim1.configure(background='lightgray'))
    lab_anim2.bind("<Enter>", lambda event:lab_anim2.configure(background='red'))
    lab_anim2.bind("<Leave>", lambda event:lab_anim2.configure(background='lightgray'))
    lab_anim3.bind("<Enter>", lambda event:lab_anim3.configure(background='red'))
    lab_anim3.bind("<Leave>", lambda event:lab_anim3.configure(background='lightgray'))'''
    return find_photo, anim
    
tk = Tk()
tk.title('Обучение по картинкам')
tk.geometry('1240x600')
tk.resizable(0,0)

dir_animal='C:\\PyProject\\test\\alenv\\animal\\'
#получаем список всех фото из папки
list_animal=os.listdir(dir_animal)
random.shuffle(list_animal)
animal_list=random.sample(list_animal, 4)

lbl0 = Label( text='Найди картинку: ', font='Gabriola 30',fg='red')
lbl0.grid(column=0, row=0)
lbl_find = Label(text ="имя картинки" ,font='Gabriola 35',fg='blue')
lbl_find.grid(column=1, row=0)



#img0= PhotoImage(file=dir_animal+animal_list[0]).subsample(4,4)
lab_anim0=Button()
#lab_anim0.image=img0
#lab_anim0.grid(column=0, row=1)

#img1= PhotoImage(file=dir_animal+animal_list[1]).subsample(4,4)
lab_anim1=Button()#image=img1)
#lab_anim1.image=img1
#lab_anim1.grid(column=1, row=1)

#img2= PhotoImage(file=dir_animal+animal_list[2]).subsample(4,4)
lab_anim2=Button()#image=img2)
#lab_anim2.image=img2
#lab_anim2.grid(column=2, row=1)

#img3= PhotoImage(file=dir_animal+animal_list[3]).subsample(4,4)
lab_anim3=Button()#image=img3)
#lab_anim3.image=img3
#lab_anim3.grid(column=3, row=1)



next_btn=Button(text="начать", font='Gabriola 15', command=change_photo)
next_btn.grid(column=0, row=2)

#поиск искомого фото

taget_photo, list_taget=change_photo()
print(taget_photo,list_taget)

tk.mainloop()