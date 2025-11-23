#Código da questao 3, item A:
#Plote um gráfico da curva de energia de deformação da viga AB com os valores de L, de 0 até 5 m, usando incrementos de 1 m, utilizando o alumínio como material da viga

import numpy as np
import matplotlib.pyplot as plt


# dados
P = 95000  # Peso = 45+50 = 95kN
E_al = 69e9 #Aluminio
I = 1.13e-4  # poderia ser 113e-6 tambem, que foi o valor utilizado nos meus calculos

L = np.array([0, 1, 2, 3, 4, 5])
# formula da energia de deformação U = P²L³/(96EI)
U_al = (P**2 * L**3) / (96 * E_al * I)

print("Energia de Deformacao - Aluminio")
print("-" * 50)
for i in range(len(L)):
    print(f"L = {L[i]} m: U = {U_al[i]:.4f} J")

plt.figure(figsize=(10, 6))
plt.plot(L, U_al, 'bo-', linewidth=2, markersize=8, label='Alumínio')
plt.grid(True, alpha=0.3)
plt.xlabel('Comprimento L (m)', fontsize=12)
plt.ylabel('Energia de Deformação U (J)', fontsize=12)
plt.title('Energia de Deformação vs Comprimento - Alumínio\nP = 95 kN, E = 69 GPa', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.xlim(-0.2, 5.2)
plt.ylim(bottom=0)


for i in range(len(L)):
    plt.annotate(f'{U_al[i]:.4f} J', 
                xy=(L[i], U_al[i]), 
                xytext=(5, 5), 
                textcoords='offset points',
                fontsize=9)

plt.tight_layout()

plt.show()
