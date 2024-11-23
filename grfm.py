import matplotlib.pyplot as plt
import numpy as np

title = input("Digite o titulo do seu gráfico: ")

tipe = input("Selecione o tipo de Gráfico: \n 1 - vertical \n 2 - horizontal \n 3 - Pizza \n 4 - Linha \n > ")
tipe2 = input("Qual será o número de Items? \n 3 \n 4 \n 5 \n >  ")

if tipe2 == "3":
    dado1 = input("Dado 1: ")
    dado2 = input("Dado 2: ")
    dado3 = input("Dado 3: ")

if tipe2 == "4":
    dado1 = input("Dado 1: ")
    dado2 = input("Dado 2: ")
    dado3 = input("Dado 3: ")
    dado4 = input("Dado 4: ")

if tipe2 == "5":
    dado1 = input("Dado 1: ")
    dado2 = input("Dado 2: ")
    dado3 = input("Dado 3: ")
    dado4 = input("Dado 4: ")
    dado5 = input("Dado 5: ")
   

if tipe2 == "3":
    val1 = input("Valor do 1º Dado: ")
    val2 = input("Valor do 2º Dado: ")
    val3 = input("Valor do 3º Dado: ")
    

if tipe2 == "4":
    val1 = input("Valor do 1º Dado: ")
    val2 = input("Valor do 2º Dado: ")
    val3 = input("Valor do 3º Dado: ")
    val4 = input("Valor do 4º Dado: ")

if tipe2 == "5":
    val1 = input("Valor do 1º Dado: ")
    val2 = input("Valor do 2º Dado: ")
    val3 = input("Valor do 3º Dado: ")
    val4 = input("Valor do 4º Dado: ")
    val5 = input("Valor do 5º Dado: ")


if tipe2 == "4":
    x = np.array([dado1,dado2,dado3,dado4])
    y = np.array([float(val1),float(val2),float(val3),float(val4)])

if tipe2 == "3":
    x = np.array([dado1,dado2,dado3])
    y = np.array([float(val1),float(val2),float(val3)])

if tipe2 == "5":
    x = np.array([dado1,dado2,dado3,dado4,dado5])
    y = np.array([float(val1),float(val2),float(val3),float(val4),float(val5)])



if tipe == "1":
    plt.bar(x,y)
    plt.title(title)
    plt.grid
    plt.show()

if tipe == "2":
    plt.barh(x,y)
    plt.title(title)
    plt.grid
    plt.show()

if tipe == "3":
    plt.pie(y,labels=x)
    plt.legend()
    plt.show()

if tipe == "4":
    ex = input("Oque será escrito na linha Horizontal? > ")
    ey = input("Oque será escrito na linha Vertical? >")

    plt.plot(x,y)
    plt.title(title)
    plt.xlabel(ex)
    plt.ylabel(ey)
    plt.grid()
    plt.show()


