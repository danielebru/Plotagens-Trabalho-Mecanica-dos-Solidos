
#Plotagem dos gráficos questao 1
#1A.
#Plote um gráfico da curva de deflexão máxima da viga com os valores de L variando de 0 até 8 m, usando incrementos de 1 m, utilizando o alumínio como material da viga
#1B.
#Plote um gráfico da curva de deflexão máxima da viga com os valores de L variando de 0 até 8 m, usando incrementos de 1 m, utilizando o aço como material da viga

import numpy as np
import matplotlib.pyplot as plt



P = 95000  #Peso = 45+50 = 95kN
I = 3.14e-4 
E_aluminio = 69e9  
E_aco = 200e9  


L_values = np.arange(0, 9, 1) 

def deflexao_maxima(P, L, E, I):
    """Calcula a deflexão máxima da viga"""
    return -3 * P * L**3 / (256 * E * I)

deflexao_aluminio = []
for L in L_values:
    y = deflexao_maxima(P, L, E_aluminio, I)
    deflexao_aluminio.append(y)  

deflexao_aco = []
for L in L_values:
    y = deflexao_maxima(P, L, E_aco, I)
    deflexao_aco.append(y)  


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Alumínio
ax1.plot(L_values, deflexao_aluminio, 'b-o', linewidth=2, markersize=8, label='Alumínio')
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('Comprimento L (m)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Deflexão Máxima (m)', fontsize=12, fontweight='bold')
ax1.set_title('Deflexão Máxima da Viga AB - ALUMÍNIO\nE = 69 GPa', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5)


for i, (l, d) in enumerate(zip(L_values, deflexao_aluminio)):
    ax1.annotate(f'{d:.8f}', xy=(l, d), xytext=(5, 5), 
                textcoords='offset points', fontsize=9)

# Gráfico 2: Aço
ax2.plot(L_values, deflexao_aco, 'r-s', linewidth=2, markersize=8, label='Aço')
ax2.grid(True, alpha=0.3)
ax2.set_xlabel('Comprimento L (m)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Deflexão Máxima (m)', fontsize=12, fontweight='bold')
ax2.set_title('Deflexão Máxima da Viga AB - AÇO\nE = 200 GPa', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11)
ax2.axhline(y=0, color='k', linestyle='--', linewidth=0.5)

for i, (l, d) in enumerate(zip(L_values, deflexao_aco)):
    ax2.annotate(f'{d:.8f}', xy=(l, d), xytext=(5, 5), 
                textcoords='offset points', fontsize=9)

plt.tight_layout()
plt.show()

print("="*70)
print("TABELA DE DEFLEXOES MAXIMAS")
print("="*70)
print(f"{'L (m)':<10} {'Aluminio (m)':<20} {'Aco (m)':<20}")
print("-"*70)
for i, L in enumerate(L_values):
    print(f"{L:<10.1f} {deflexao_aluminio[i]:<20.8f} {deflexao_aco[i]:<20.8f}")
print("="*70)
