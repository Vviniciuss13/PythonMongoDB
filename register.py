import functions as f
from tkinter import *

def criarConta():
    telaCriar = Tk()
    telaCriar.geometry("600x900")
    telaCriar.config(bg="#006660")
    titleCadastrar = Label(telaCriar, text="Cadastrar Usuário", font=('Candara', 34, 'bold'))
    titleCadastrar.config(bg="#006660", fg="#fff")
    titleCadastrar.pack(pady=20)
    
    nameLabel = Label(telaCriar, text="Nome: ", font=("Lato", 24))
    nameLabel.config(bg="#006660", fg="#fff")
    nameLabel.pack()
    nameInput = Entry(telaCriar, font=("Lato", 24))
    nameInput.pack(pady=10, ipadx=20, ipady=8)
    
    documentLabel = Label(telaCriar, text="CPF: ", font=("Lato", 24))
    documentLabel.config(bg="#006660", fg="#fff")
    documentLabel.pack()
    documentInput = Entry(telaCriar, font=("Lato", 24))
    documentInput.pack(pady=10, ipadx=20, ipady=8)
    
    emailLabel = Label(telaCriar, text="Email: ", font=("Lato", 24))
    emailLabel.config(bg="#006660", fg="#fff")
    emailLabel.pack()
    emailInput = Entry(telaCriar, font=("Lato", 24))
    emailInput.pack(pady=10, ipadx=20, ipady=8)
    
    passwordCadastrarLabel = Label(telaCriar, text="Senha: ", font=("Lato", 24))
    passwordCadastrarLabel.config(bg="#006660", fg="#fff")
    passwordCadastrarLabel.pack()
    passwordCadastrarInput = Entry(telaCriar, show="*", font=("Lato", 24))
    passwordCadastrarInput.pack(pady=10, ipadx=20, ipady=8)
    
    buttonInserir = Button(telaCriar, text="Cadastrar", command=lambda: f.createUser(telaCriar, nameInput.get(), documentInput.get(), emailInput.get(), passwordCadastrarInput.get()))
    buttonInserir.config(bg="#003B7B", fg="#fff", font=("Lato", 17), cursor="hand2")
    buttonInserir.pack(ipadx=30, ipady=10, pady=10)