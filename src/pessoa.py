"""Classe que representa uma pessoa."""
class Pessoa:
    """"Definição de metodos de acesso e modificadores de atributos da classe Pessoa."""
    def __init__(self, nome, idade, email):
        self._nome = nome
        self._idade = idade
        self._email = email

    def getNome(self):
        return self._nome

    def getIdade(self):
        return self._idade

    def getEmail(self):
        return self._email

    def setNome(self, nome):
        self._nome = nome

    def setIdade(self, idade):
        self._idade = idade

    def setEmail(self, email):
        self._email = email
