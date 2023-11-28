import pymongo
from pymongo import MongoClient

server = MongoClient("mongodb://localhost:27017/")
db = server.pythonBD

users = db.users

def criarUser(nome, cpf, email, senha):
    post = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha
    }
    
    users.insert_one(post).inserted_id

def login(user, senha):
    user = users.find_one({"nome": user, "senha": senha})
    return user
    
def updateUser(id, nome, documento, email, senha):
    userId = users.update_one({"_id": id}, {"$set":{"nome": nome, "cpf": documento, "email": email, "senha":senha}}).upserted_id
    return users.find_one({"_id": id})

def deleteUser(user):
    users.delete_one({"_id": user.id})