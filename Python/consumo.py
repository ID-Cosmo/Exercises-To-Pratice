def entrada_positiva(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Valor incorreto! Tente novamente.")
        except ValueError:
            print("Digite um valor valido!")
            
def calcular_consumo(distancia, combustivel):
        return distancia / combustivel

def adicionar_historico(historico, distancia, combustivel, consumo_medio):
    historico.append([distancia, combustivel, consumo_medio])
                      
def exibir_historico(historico):
    print("\nHistorico de calculos: ")
    for i, registro in enumerate(historico, 1):
        print(f"{i}: Distancia = {registro[0]} km | Combustivel = {registro[1]} L | Consumo = {registro[2]:.3f} km/L")

historico = []

while True:
    distancia = entrada_positiva("Distancia total percorrida: ")
    combustivel = entrada_positiva("Combustivel gasto: ")
    consumo_medio = calcular_consumo(distancia, combustivel)
    adicionar_historico(historico, distancia, combustivel, consumo_medio)
    
    continuar = input("Deseja realizar um novo calculo? (S/N):").strip().lower()
    if continuar != "s":
        break

exibir_historico(historico)
print("Programa encerrando...")