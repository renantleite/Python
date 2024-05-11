class PlanoTelefone:
    def __init__(self,nomeP,saldo):

        self.nomeP = nomeP
        self.saldo = saldo
    
    def verificar_saldo(self):
        return self.saldo
    def mensagem(self):
        if (self.saldo < 10):
            return f"Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif (self.saldo >= 50):
            return f"Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return f"Seu saldo está razoável. Aproveite o uso moderado do seu plano."
class usuarioTelefone:
    def __init__(self,nome,plano):
        self.nome = nome
        self.plano = plano
    
    def verificar_saldo(self):
        return self.plano.verificar_saldo(), self.plano.mensagem()

nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = usuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)
