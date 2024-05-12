
def recomendar_plano(consumo):
    if (consumo >= 0.5 and consumo<=10):
      return("Plano Essencial Fibra - 50Mbps")
    elif consumo <= 20 and consumo >10:
      return("Plano Prata Fibra - 100Mbps")
    else:
      return("Plano Premium Fibra - 300Mbps")

    


consumo = float(input())

print(recomendar_plano(consumo))