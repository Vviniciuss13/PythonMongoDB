import mongodb as m
from tkinter import *
import home as h
import register as r
from classes import User

def showError():
    telaErro = Tk()
    telaErro.geometry("550x200")
    telaErro.config(bg="#006660")
    errorLabel = Label(telaErro, text="Usuario ou Login inválido/errado!", font=("Gill Sans MT", 20, "bold"), bg="#006660", fg="#fff")
    errorLabel.pack(pady=15)
    buttonOk = Button(telaErro, text="Ok", command=telaErro.destroy, font=("Candara", 20), fg="#fff", bg="#A9251E")
    buttonOk.pack(ipadx=100, ipady=0,pady=10, padx=100)

def createUser(tela, nome, documento, email, password):
    if(nome == "" or documento == "" or email == "" or password == ""):
        telaFailed = Tk()
        telaFailed.geometry("550x200")
        telaFailed.config(bg="#006660")
        
        FailedLabel = Label(telaFailed, text="Campos Vazios!!", font=("Gill Sans MT", 20, "bold"), bg="#006660", fg="#fff")
        
        FailedLabel.pack(pady=15)
        buttonOk = Button(telaFailed, text="Ok", command=telaFailed.destroy, font=("Candara", 20), bg="#003B7B", fg="#fff")
        buttonOk.pack(ipadx=100, ipady=0,pady=10, padx=100)
    else:
        m.criarUser(nome, documento, email, password)
        telaSuccess = Tk()
        telaSuccess.geometry("550x200")
        telaSuccess.config(bg="#006660")
        
        successLabel = Label(telaSuccess, text="Usuário Cadastrado", font=("Gill Sans MT", 20, "bold"), bg="#006660", fg="#fff")
        
        successLabel.pack(pady=15)
        buttonOk = Button(telaSuccess, text="Ok", command=telaSuccess.destroy, font=("Candara", 20), bg="#29A973", fg="#fff")
        buttonOk.pack(ipadx=100, ipady=0,pady=10, padx=100)

def logar(user, password):
    entry = m.login(user, password)
    print(entry)
    if(entry == None):
        showError()
    else:
        user = User(entry['_id'], entry['nome'], entry['cpf'], entry['email'], entry['senha'])
        h.telaHome(user)
        
def edit(tela, id, nome, documento, email, senha):
    updateUser = m.updateUser(id, nome, documento, email, senha)
    tela.destroy()
    user = User(updateUser['_id'], updateUser['nome'], updateUser['cpf'], updateUser['email'], updateUser['senha'])
    h.telaHome(user)
    
def deleteUser(tela, user):
    telaDelete = Tk()
    telaDelete.geometry("550x200")
    telaDelete.config(bg="#006660")
    
    frameYesNo = Frame(telaDelete, bg="#006660")
    
    titleDelete = Label(telaDelete, text="Deseja Deletar a Conta?", font=("Gill Sans MT", 20, "bold"), bg="#006660", fg="#fff")
    titleDelete.pack(pady=10)
    
    buttonYes = Button(frameYesNo, text="Sim", command=lambda: delete('yes'), font=("Candara", 20), bg="#29A973", fg="#fff")
    buttonYes.grid(column=0, row=0, padx=20, ipadx=20, ipady=10, pady=10)
    
    buttonNo = Button(frameYesNo, text="Não", command=lambda: delete('no'), font=("Candara", 20), fg="#fff", bg="#A9251E")
    buttonNo.grid(column=1, row=0, padx=20, ipadx=20, ipady=10, pady=10)
    
    frameYesNo.pack()
    
    def delete(choice):
        if(choice == 'yes'):
            m.deleteUser(user)
            tela.destroy()
        telaDelete.destroy()    