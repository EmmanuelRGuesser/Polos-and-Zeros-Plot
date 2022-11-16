# Este código cria uma grafico de polos e zeros dado uma funcao de transferencia,
# sao gerados um grafico 2D onde mostra os polos e zeros, um em 3D que mostra a
# magnetude, e o outro mostrando o corte do anterior no eixo real igual a zero.

import control as ct
import matplotlib.pyplot as plt
import numpy as np

# Funcao de Tranferencia a ser computada
def f(s):
    return ((s + 1)*(s + 2))/((s**2 + 4*s + 5)*(s + 3))

# Plota o Grafico de polos e zeros
s = ct.TransferFunction.s
k = ct.pzmap(f(s), plot=True, title = 'Diagrama de Polos e Zeros')

# Determina o intervalo do eixo real e imag para o plotar a magnetude da funcao
x = np.linspace(min(min(k[0].real),min(k[1].real)) - abs(min(min(k[0].real),min(k[1].real)))*.5,
                max(max(k[0].real),max(k[1].real)) + abs(max(max(k[0].real),max(k[1].real)))*.5,
                100)
y = np.linspace(min(min(k[0].imag),min(k[1].imag)) - abs(min(min(k[0].imag),min(k[1].imag)))*.5,
                max(max(k[0].imag),max(k[1].imag)) + abs(max(max(k[0].imag),max(k[1].imag)))*.5,
                100)
X, Y = np.meshgrid(x, y)

# Calcula a magnetude
G = abs(f(X + Y*1j))

# Plot grafico 3D da magnitude
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_zlim([0,5])
ax.plot_surface(X, Y, G, cmap='coolwarm')
ax.set_title('Magnetude da Funcao de Tranferencia')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginario')
ax.set_zlabel('Magnetude')

# Plot do grafico 2D da magnitude em corte em real=0
plt.figure()
plt.plot(y, f(y*1j))
plt.xlabel('Imaginario')
plt.ylabel('Magnetude')
plt.grid(True)

# Exibe os graficos
plt.show()
