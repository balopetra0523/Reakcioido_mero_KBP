import tkinter as tk
from tkinter import ttk
import random
import time
import sajat_KBP
def jelzes():
    global kezdet
    uzenet_cimke.config(text= "Most kattinthatsz!")
    kezdet = time.perf_counter()
    reakcio_gomb.config(state="normal")

def inditas():
    inditas_gomb.config(state="disabled")
    print("Reakcióidő-mérés elindult!")
    uzenet_cimke.config(text="Várj a jelzésre...")
    varakozas= random.randint(2,5)
    root.after( varakozas * 1000, jelzes )

def kattintas():
    veg= time.perf_counter()
    reakcioido = veg - kezdet
    reakcioido_ms = sajat_KBP.KBP_masodpercbol_ms(reakcioido)
    app.legutobbi_eredmeny = reakcioido_ms
    meres_ideje = time.localtime()
    idobelyeg = time.time()
    print(" A mérés időbélyege:", idobelyeg)
    uzenet_cimke.config(text=f"Reakcióidőd: {app.legutobbi_eredmeny:.0f} ms\nMérve:{meres_ideje.tm_hour:02d}:{meres_ideje.tm_min:02d} : {meres_ideje.tm_sec:02d}")
    reakcio_gomb.config(state="disabled")
    inditas_gomb.config(state="normal")

app= sajat_KBP.KBP_ReakcioMeres()
root = tk.Tk()
root.geometry("500x350")
root.title("Reakcióidő-mérő")
root.resizable(False,False)

cim_cimke= ttk.Label(root, text="Reakcióidő-mérő", font=("Arial", 16,"bold"))
cim_cimke.grid(column=0,row=0,padx=20,pady=20)

inditas_gomb = ttk.Button(root, text="Inditás", command=inditas)
inditas_gomb.grid(column=0,row=1,padx=20,pady=20)


uzenet_cimke=ttk.Label(root, text="Nyomd meg az Indítás gombot!")
uzenet_cimke.grid(column=0,row=2,padx=20,pady=20)

reakcio_gomb= ttk.Button(root, text="Kattints ide!", command=kattintas)
reakcio_gomb.config(state="disabled")
reakcio_gomb.grid(column=0,row=3,padx=20,pady=20)


root.mainloop()


