
#Código da questao 3, item C:
#Plote um gráfico da curva de deslocamento da viga AB com os valores de L, de 0 até #5m, usando incrementos de 1 m, utilizando o alumínio como material da viga 
import numpy as np
import matplotlib.pyplot as plt



# dados
P = 95000  # Peso = 45+50 = 95kN
E_al = 69e9  # Aço
I =  1.13e-4  # poderia ser 113e-6 tambem, que foi o valor utilizado nos meus calculos


L = np.array([0, 1, 2, 3, 4, 5])

# formula do deslocamento no ponto C: Xc = PL³/(48EI)
X_c_al = (P * L**3) / (48 * E_al * I)

print("Deslocamento no Ponto C - Alumínio (em METROS)")
print("-" * 50)
for i in range(len(L)):
    print(f"L = {L[i]} m: delta = {X_c_al[i]:.8f} m")


plt.figure(figsize=(10, 6))
plt.plot(L, X_c_al, 'bo-', linewidth=2, markersize=8, label='Alumínio')
plt.grid(True, alpha=0.3)
plt.xlabel('Comprimento L (m)', fontsize=12)
plt.ylabel('Deslocamento Xc (m)', fontsize=12)
plt.title('Curva de Deslocamento da Viga AB - Alumínio\nP = 95 kN, E = 69 GPa', 
          fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.xlim(-0.2, 5.2)
plt.ylim(bottom=0)

for i in range(len(L)):
    if L[i] > 0:
        plt.annotate(f'{X_c_al[i]:.8f} m', 
                     xy=(L[i], X_c_al[i]), 
                     xytext=(5, 5), 
                     textcoords='offset points',
                     fontsize=9)

plt.tight_layout()
plt.show()
