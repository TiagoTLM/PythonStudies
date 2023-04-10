# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. Fórmula: c²=a²+b²
import math 

catOp = float(input('Informe o comprimento do cateto oposto do triângulo retângulo: '))
catAd = float(input('Informe o comprimento do cateto adjacente do triângulo retângulo: '))
hipot = math.hypot(catOp, catAd)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipot))