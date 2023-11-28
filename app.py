## pipe install pymongo

from tkinter import *
import register as r
import functions as f

root = Tk()
root.geometry("600x900")
root.config(bg="#006660")

canvas = Canvas(root, width = 310, height = 320)
canvas.config(bg="#006660", highlightthickness=0)
canvas.pack(pady=10)

img = PhotoImage(file="img/user.png")
canvas.create_image(8,10, anchor=NW, image=img)

title = Label(root, text="Login", font=('Candara', 34, 'bold'))
title.config(bg="#006660", fg="#fff")
title.pack(pady=30)
userLabel = Label(root, text="Usuário", font=("Lato", 24))
userLabel.config(bg="#006660", fg="#fff")
userLabel.pack()
userInput = Entry(root, font=('lato', 24))
userInput.pack(pady=10,ipadx=20, ipady=8)
passwordLabel = Label(root, text="Senha", font=("Lato", 24))
passwordLabel.config(bg="#006660", fg="#fff")
passwordLabel.pack()
passwordInput = Entry(root, show="*", font=('lato', 24))
passwordInput.pack(pady=10, ipadx=20, ipady=8)
buttonLogar = Button(root, text="Entrar", command=lambda: f.logar(userInput.get(), passwordInput.get()))
buttonLogar.config(bg="#003B7B", fg="#fff", font=("Lato", 17), cursor="target")
buttonLogar.pack(ipadx=60, ipady=10, pady=20)
buttonCadastrar = Button(root, text="Cadastrar Nova Conta", command=r.criarConta)
buttonCadastrar.config(bg="#006660", fg="#fff", borderwidth=0, font=('Candara', 22), cursor="hand2")
buttonCadastrar.pack(ipadx=30, pady=5)

root.mainloop()