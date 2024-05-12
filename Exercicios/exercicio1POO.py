class usuario:
    def __init__(self,nome,plano,numero):
        self._nome = nome
        self._plano = plano
        self._numero = numero
    def __str__(self):
        return f"Usuário {self._nome} criado com sucesso."
    
nome = input()
numero = input()
plano = input()
user = usuario(nome,numero,plano)
print(user)