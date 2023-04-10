import tkinter as tk
from tkinter import *

start_window = tk.Tk()
start_window.title("Этажи")
start_window.geometry('500x500')
frame_l = tk.Frame(master=start_window, relief=tk.RAISED, borderwidth=10).pack()
label_info = tk.Label(master=frame_l, text="Привет, меня зовут Еркын, я твой виртуальный консультант. Введи этаж дома:\n Выбири этаж дома",
                      bg="light gray", width=200, height=3).pack()
frame_b = tk.Frame(master=start_window, relief=tk.RAISED, borderwidth=5).pack()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def first_fee():
    """Функция первоначального взноса"""

    window_ff = tk.Toplevel()
    window_ff.title("Первоначальный взнос")
    window_ff.geometry('500x500')

    frame_l = tk.Frame(master=window_ff, relief=tk.RAISED, borderwidth=10)
    frame_l.pack()
    label_info = tk.Label(master=frame_l,
                          text="Выбери процент первоначального взноса\n Примечание: чем меньше первоначальный взноса тем больше стоимость кв/м",
                          bg="light gray", width=200, height=3).pack()
    frame_b = tk.Frame(master=window_ff, relief=tk.RAISED, borderwidth=5)
    frame_b.pack()

    btm_30 = tk.Button(master=frame_b, text='30% +15000тг',
                             width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_50 = tk.Button(master=frame_b, text='50% +10000тг',
                             width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_70 = tk.Button(master=frame_b, text='70% +5000тг',
                             width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_100 = tk.Button(master=frame_b, text='100% +0тг',
                             width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def floor_5():
    """" Функция вызывается при нажатии на Этаж 5"""

    window_floor = tk.Toplevel()
    window_floor.title("Этаж 5 Комнаты")
    window_floor.geometry('500x500')

    frame_l = tk.Frame(master=window_floor, relief=tk.RAISED, borderwidth=10)
    frame_l.pack()
    label_info = tk.Label(master=frame_l, text="Выбери кол-во комнат и желаемый метраж",
                          bg="light gray", width=200, height=3).pack()
    frame_b = tk.Frame(master=window_floor, relief=tk.RAISED, borderwidth=5)
    frame_b.pack()

    list_m2345 = [44.5, 59.49, 81.5, 75.43, 120.81]
    btm_rooms1 = tk.Button(master=frame_b, text=f'Комнат 1 : {list_m2345[0]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5, command=first_fee).pack()
    btm_rooms2_2 = tk.Button(master=frame_b, text=f'Комнат 2 : {list_m2345[3]}m',
                             width=14, height=3, bg="saddle brown", fg="white", borderwidth=5, command=first_fee).pack()
    btm_rooms2 = tk.Button(master=frame_b, text=f'Комнат 2 : {list_m2345[1]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5, command=first_fee).pack()
    btm_rooms3 = tk.Button(master=frame_b, text=f'Комнат 3 : {list_m2345[2]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5, command=first_fee).pack()
    btm_rooms4 = tk.Button(master=frame_b, text=f'Комнат 4 : {list_m2345[4]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5, command=first_fee).pack()


def floor_4():
    """" Функция вызывается при нажатии на Этаж 4"""

    window_floor = Toplevel()
    window_floor.title("Этаж 4 Комнаты")
    window_floor.geometry('500x500')

    frame_l = tk.Frame(master=window_floor, relief=tk.RAISED, borderwidth=10)
    frame_l.pack()
    label_info = tk.Label(master=frame_l, text="Выбери кол-во комнат и желаемый метраж",
                          bg="light gray", width=200, height=3).pack()
    frame_b = tk.Frame(master=window_floor, relief=tk.RAISED, borderwidth=5)
    frame_b.pack()

    list_m2345 = [44.5, 59.49, 81.5, 75.43, 120.81]
    btm_rooms1 = tk.Button(master=frame_b, text=f'Комнат 1 : {list_m2345[0]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms2_2 = tk.Button(master=frame_b, text=f'Комнат 2 : {list_m2345[3]}m',
                             width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms2 = tk.Button(master=frame_b, text=f'Комнат 2 : {list_m2345[1]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms3 = tk.Button(master=frame_b, text=f'Комнат 3 : {list_m2345[2]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms4 = tk.Button(master=frame_b, text=f'Комнат 4 : {list_m2345[4]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()

def floor_1():
    """" Функция вызывается при нажатии на Этаж 1"""

    window_floor = Toplevel()
    window_floor.title("Этаж 1 Комнаты")
    window_floor.geometry('500x500')

    frame_l = tk.Frame(master=window_floor, relief=tk.RAISED, borderwidth=10)
    frame_l.pack()
    label_info = tk.Label(master=frame_l, text="Выбери кол-во комнат и желаемый метраж",
                          bg="light gray", width=200, height=3).pack()
    frame_b = tk.Frame(master=window_floor, relief=tk.RAISED, borderwidth=5)
    frame_b.pack()

    list_m1 = [41.55, 56.28, 76.71, 72.25, 89.01]
    btm_rooms1 = tk.Button(master=frame_b, text=f'Комнат 1 : {list_m1[0]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms2_2 = tk.Button(master=frame_b, text=f'Комнат 2 : {list_m1[3]}m',
                             width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms2 = tk.Button(master=frame_b, text=f'Комнат 2 : {list_m1[1]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms3 = tk.Button(master=frame_b, text=f'Комнат 3 : {list_m1[2]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms4 = tk.Button(master=frame_b, text=f'Комнат 4 : {list_m1[4]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()


def floor_2_3():
    """" Функция вызывается при нажатии на Этаж 2 и 3"""

    window_floor = Toplevel()
    window_floor.title("Этаж 2, 3, 4 Комнаты")
    window_floor.geometry('500x500')

    frame_l = tk.Frame(master=window_floor, relief=tk.RAISED, borderwidth=10)
    frame_l.pack()
    label_info = tk.Label(master=frame_l,text="Выбери кол-во комнат и желаемый метраж",
                          bg="light gray", width=200, height=3).pack()
    frame_b = tk.Frame(master=window_floor, relief=tk.RAISED, borderwidth=5)
    frame_b.pack()

    list_m2345 = [44.5, 59.49, 81.5, 75.43, 120.81]
    btm_rooms1 = tk.Button(master=frame_b, text=f'Комнат 1 : {list_m2345[0]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms2_2 = tk.Button(master=frame_b, text=f'Комнат 2 : {list_m2345[3]}m',
                             width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms2 = tk.Button(master=frame_b, text=f'Комнат 2 : {list_m2345[1]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms3 = tk.Button(master=frame_b, text=f'Комнат 3 : {list_m2345[2]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()
    btm_rooms4 = tk.Button(master=frame_b, text=f'Комнат 4 : {list_m2345[4]}m',
                           width=14, height=3, bg="saddle brown", fg="white", borderwidth=5).pack()


btm_floor1 = tk.Button(master=frame_b, text='Этаж 1', width=7, height=3, bg="saddle brown", fg="white", borderwidth=5, command=floor_1).pack()
btm_floor2 = tk.Button(master=frame_b, text='Этаж 2', width=7, height=3, bg="saddle brown", fg="white", borderwidth=5, command=floor_2_3).pack()
btm_floor3 = tk.Button(master=frame_b, text='Этаж 3', width=7, height=3, bg="saddle brown", fg="white", borderwidth=5, command=floor_2_3).pack()
btm_floor4 = tk.Button(master=frame_b, text='Этаж 4', width=7, height=3, bg="saddle brown", fg="white", borderwidth=5, command=floor_4).pack()
btm_floor5 = tk.Button(master=frame_b, text='Этаж 5', width=7, height=3, bg="saddle brown", fg="white", borderwidth=5, command=floor_5).pack()



start_window.mainloop()