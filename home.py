import functions as f
from tkinter import *

def telaHome(user):
    def editMode():
        nomeLabel.config(text="Nome")
        documentoLabel.config(text="Documento")
        emailLabel.config(text="Email")
        senhaLabel.config(text="Senha")
        
        nomeInput.config(state="normal")
        documentoInput.config(state="normal")
        emailInput.config(state="normal")
        senhaInput.config(state="normal")
        buttonUpdate = Button(telaHome, text="Atualizar", command=lambda: f.edit(telaHome, user.id, nomeInput.get(), documentoInput.get(), emailInput.get(), senhaInput.get()))
        buttonUpdate.pack(ipadx=60, ipady=10, pady=20)
        buttonUpdate.config(bg="#003B7B", fg="#fff", font=("Lato", 17), cursor="target")
        
        frameButton.destroy()
    
    telaHome = Tk()
    telaHome.geometry("600x900")
    telaHome.config(bg="#006660")
    
    titleHome = Label(telaHome, text="Dados do Usuário", font=('Candara', 34, 'bold'), fg="#fff", bg="#006660")
    titleHome.pack(pady=10)
    
    frame = Frame(telaHome, bg="#006660")
    frameButton = Frame(telaHome, bg="#006660")
    
    nomeLabel = Label(frame, text="Nome: ", font=("Lato", 24))
    nomeLabel.config(bg="#006660", fg="#fff")
    nomeLabel.grid(column=0, row=0)
    nomeInput = Entry(frame, font=("Lato", 24))
    nomeInput.insert(0, user.nome)
    nomeInput.config(state="readonly")
    
    documentoLabel = Label(frame, text="Documento: ", font=("Lato", 24))
    documentoLabel.config(bg="#006660", fg="#fff")
    documentoLabel.grid(column=0, row=1)
    documentoInput = Entry(frame, font=("Lato", 24))
    documentoInput.insert(0,user.documento)
    documentoInput.config(state="readonly")
    
    emailLabel = Label(frame, text="Email: ", font=("Lato", 24))
    emailLabel.config(bg="#006660", fg="#fff")
    emailLabel.grid(column=0, row=2)
    emailInput = Entry(frame, font=("Lato", 24))
    emailInput.insert(0, user.email)
    emailInput.config(state="readonly")
    
    senhaLabel = Label(frame, text="Senha: ", font=("Lato", 24))
    senhaLabel.config(bg="#006660", fg="#fff")
    senhaLabel.grid(column=0, row=3)
    senhaInput = Entry(frame, font=("Lato", 24))
    senhaInput.insert(0, user.senha)
    senhaInput.config(state="readonly")
    
    nomeInput.grid(column=1, row=0, pady=10)
    documentoInput.grid(column=1, row=1, pady=10)
    emailInput.grid(column=1, row=2, pady=10)
    senhaInput.grid(column=1, row=3, pady=10)
    
    ButtonEdit = Button(frameButton, text="Editar Informações?", command=lambda: editMode(), font=("Candara", 16), fg="#fff", bg="#CFC736")
    ButtonEdit.grid(column=0, row=1, pady=10, padx=20, ipadx=10, ipady=20)
    
    ButtonDelete = Button(frameButton, text="Deletar Conta", command=lambda: f.deleteUser(telaHome, user), font=("Candara", 16), fg="#fff", bg="#7D1C16")
    ButtonDelete.grid(column=1, row=1, pady=10, padx=20, ipadx=10, ipady=20)
    
    frame.pack()
    frameButton.pack()