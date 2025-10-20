#usuario digita o valor do r do raio de um circulo
#computador mostra o valor digitado
#computador calcula a area, area=pi.r**2
#computador mostra o resultado


#teste

import matplotlib.pyplot as plt
import numpy as np #trabalha com arrays e operações vetorizadas, calculos com listas de numeros
#import math , funções matematicas basicas

def entrada_positiva(mensagem, minimo, maximo, tentativa=3, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem))
            if minimo <= valor <= maximo:
                return minimo
            else:
                print("Valor fora do intervalo!")
                tentativa = tentativa - 1
            if tentativa < 0:
                raise ValueError ("Resposta invalida! Encerrando...")
        except KeyboardInterrupt:
            print("Atalho detectado. Tente novamente! ")
            tentativa = tentativa - 1
            if tentativa < 0:
                raise ValueError ("Resposta invalida! Encerrando...")
        except ValueError:
            print("Valor incorreto! Tente novamente somente com numeros.")
            tentativa = tentativa - 1
            if tentativa < 0:
                raise ValueError ("Resposta invalida! Encerrando...")

while True:
    raio_circulo = entrada_positiva("Digite o valor do R do raio de um circulo, no intervalo de 1 a 100: ", 1, 100)
    
    area = np.pi * raio_circulo**2 #precisa utilizar o np para puxar a biblioteca 
    
    print(f"Area: {area:.3f}")
    
    theta = np.linspace(0,2 * np.pi, 200)
    x = raio_circulo*np.cos(theta)
    y = raio_circulo*np.sin(theta)
    
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_aspect("equal")
    plt.title(f"Circulo de raio {raio_circulo}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
    
    while True:
        continuar = input("Gostaria de realizar outro calculo? (S/N):").strip().lower()
        if continuar == "s":
            break
        elif continuar == "n":
            print("Encerrando...")
            exit()
        else:
            print("Resposta invalida! Digite S para sim e N para não."),
             
             