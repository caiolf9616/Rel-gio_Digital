import tkinter as tk 
import time 

def atualizar_horario():
    hora_atual = time.strftime('%H:%M:%S')
    label_horario.config(text=hora_atual)
    root.after(1000, atualizar_horario)
    
root = tk.Tk()
root.title("Relógio Digital")

label_horario = tk.Label(root,font=('Arial',30),fg='red')
label_horario.pack()

atualizar_horario()

root.mainloop()   