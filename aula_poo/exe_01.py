class Endereco: 
    def __init__(self,rua,numero,cep):
        self.rua = rua 
        self.numero = numero
        self.cep = cep 
class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco 

eder_01 = Endereco("av.bariloche",104,"06445040")
pessoa_01 = Pessoa("Isaque","19",eder_01)
print(pessoa_01.nome, pessoa_01.idade,pessoa_01.endereco.rua)