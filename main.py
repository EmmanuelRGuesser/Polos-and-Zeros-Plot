# Este código cria uma gráfico de polos e zeros dado uma função de transferência,
# sao gerados um gráfico 2D onde mostra os polos e zeros, um em 3D que mostra a
# magnitude, e o outro mostrando o corte do anterior no eixo real igual a zero.

import control as ct
import matplotlib.pyplot as plt
import numpy as np

# Funcao de Tranferencia a ser computada
def f(s):
    return ((s + 1)*(s + 2))/((s**2 + 2*s + 3)*(s + 3))

# Plota o Grafico de polos e zeros
s = ct.TransferFunction.s
k = ct.pzmap(f(s), plot=True, title = 'Diagrama de Polos e Zeros')

# Determina o intervalo do eixo real e imag para o plotar a magnetude da funcao
x = np.linspace(min(min(k[0].real),min(k[1].real),min(k[0].imag),min(k[1].imag)) -
                abs(min(min(k[0].real),min(k[1].real), min(k[0].imag),min(k[1].imag))),
                
                max(max(k[0].real),max(k[1].real),max(k[0].imag),max(k[1].imag)) + 
                abs(max(max(k[0].real),max(k[1].real), max(k[0].imag),max(k[1].imag))),
                
                100)

X, Y = np.meshgrid(x, x)

# Calcula a magnetude
G = abs(f(X + Y*1j))

# Configuracao do grafico da magnitude
plt.figure()
ax = plt.axes(projection='3d')
ax.set_zlim([0,5])
ax.plot_surface(X, Y, G, cmap='coolwarm')
ax.set_title('Magnitude da Funcao de Tranferencia')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginario')
ax.set_zlabel('Magnitude')

# Plot do eixo imag
plt.figure()
plt.plot(x, f(x*1j))
plt.xlabel('Imaginario')
plt.ylabel('Magnitude')
plt.grid(True)

plt.show()
