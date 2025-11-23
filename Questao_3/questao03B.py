
#Código da questao 3, item B:
#Plote um gráfico da curva de energia de deformação da viga AB com os valores de L, de 0 até 5 m, usando incrementos de 1 m, utilizando o aço como material da viga

import numpy as np
import matplotlib.pyplot as plt


# dados
P = 95000  # Peso = 45+50 = 95kN
E_aco = 200e9  #Aço
I =  1.13e-4  # poderia ser 113e-6 tambem, que foi o valor utilizado nos meus calculos

L = np.array([0, 1, 2, 3, 4, 5])
# formula da energia de deformação U = P²L³/(96EI)
U_aco = (P**2 * L**3) / (96 * E_aco * I)


print("Energia de Deformação - Aço")
print("-" * 50)
for i in range(len(L)):
    print(f"L = {L[i]} m: U = {U_aco[i]:.4f} J")

plt.figure(figsize=(10, 6))
plt.plot(L, U_aco, 'ro-', linewidth=2, markersize=8, label='Aço')
plt.grid(True, alpha=0.3)
plt.xlabel('Comprimento L (m)', fontsize=12)
plt.ylabel('Energia de Deformação U (J)', fontsize=12)
plt.title('Energia de Deformação vs Comprimento - Aço\nP = 95 kN, E = 200 GPa', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.xlim(-0.2, 5.2)
plt.ylim(bottom=0)


for i in range(len(L)):
    plt.annotate(f'{U_aco[i]:.4f} J', 
                xy=(L[i], U_aco[i]), 
                xytext=(5, 5), 
                textcoords='offset points',
                fontsize=9)

plt.tight_layout()
plt.show()