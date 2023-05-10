import tkinter
import pandas
VOPROS=None
VERNO=0
NEVERNO=0
COUNTER=15
alldata=pandas.read_csv("bazafinal.csv",index_col= False)
alldata.columns=["Word", "Trans"]
TIMER=None


wondow=tkinter.Tk()

canvas=tkinter.Canvas(master=wondow,height=500,width=500,background="#999999")
canvas.place(x=0,y=0)
canvas2=tkinter.Canvas(master=canvas,width=400,height=250)
timeroncanvas2=tkinter.Label(master=canvas2,text="")
canvas2.create_window(200,10,window=timeroncanvas2)




galka = tkinter.PhotoImage(file="galka.png")
krest=tkinter.PhotoImage(file="krest.png")

def najatirenter(event):
    clickgalka()
    entryanswer.delete(0,tkinter.END)

def neznau():
    global NEVERNO
    poleotveta.config(text=VOPROS.iloc[0, 1])
    NEVERNO += 1
    otvechenoneverno.config(text=NEVERNO)
    wondow.after_cancel(TIMER)
    pushbuttonstart()

def clickgalka():
    global VOPROS
    global VERNO
    global NEVERNO
    if entryanswer.get()==VOPROS.iloc[0,1]:
        VERNO+=1
        otvechenoverno.config(text=VERNO)
        wondow.after_cancel(TIMER)
        entryanswer.delete(0, tkinter.END)
        pushbuttonstart()
    else:
        poleotveta.config(text=VOPROS.iloc[0, 1])
        NEVERNO+=1
        otvechenoneverno.config(text=NEVERNO)
        wondow.after_cancel(TIMER)
        entryanswer.delete(0, tkinter.END)
        pushbuttonstart()


def sledvopros():
    global VOPROS
    VOPROS=alldata.sample()
    voproslabel.config(text=VOPROS.iloc[0,0])



def schetvremeni(x):
    global TIMER
    global NEVERNO

    if x<0:
        NEVERNO+=1
        otvechenoneverno.config(text=NEVERNO)
        poleotveta.config(text=VOPROS.iloc[0, 1])
        wondow.after_cancel(TIMER)
        pushbuttonstart()

    else:
        timeroncanvas2.config(text=str(x))
        TIMER=wondow.after(1000,schetvremeni,x-1)


def pushbuttonstart():
    sledvopros()
    schetvremeni(COUNTER)


battungalka=tkinter.Button(master=canvas,width=50,height=50,image=galka,highlightthickness=0,command=clickgalka)

battungalka_win=canvas.create_window(400,400, window=battungalka)
battunkrest=tkinter.Button(master=canvas,width=50,height=50,image=krest,highlightthickness=0,command=neznau)

battunkrest_win=canvas.create_window(100,400,window=battunkrest)
entryanswer=tkinter.Entry(master=canvas,width=40)
entryanswer.bind('<Return>',najatirenter)
canvas.create_window(250,330,window=entryanswer)
holstvoprosa=canvas.create_window(250,150,window=canvas2)

battunstart=tkinter.Button(master=canvas,text="Start",command=pushbuttonstart)
canvas.create_window(250,300,window=battunstart)

voproslabel=tkinter.Label(font=("Arial",25,"bold"))
canvas2.create_window(200,100, window=voproslabel)
otvechenoverno=tkinter.Label(text=VERNO,background="#999999",font=("Arial, 25"))
canvas.create_window(400,450, window=otvechenoverno)
otvechenoneverno=tkinter.Label(text=NEVERNO,background="#999999",font=("Arial, 25"))
canvas.create_window(100,450, window=otvechenoneverno)
poleotveta=tkinter.Label(text="",font=("Arial, 25"), fg="red")
canvas2.create_window(200,200,window=poleotveta)
canvas.pack()








wondow.mainloop()