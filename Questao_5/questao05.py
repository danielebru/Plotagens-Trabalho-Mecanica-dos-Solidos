
#Plotagem dos gráficos da questão 5
# Gráfico de deslocamento de viga utilizando o Teorema de Castigliano 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


P = 95e3      
L = 8.0        
I_mm4 = 125e6  
I = I_mm4 * 1e-12  

E_values = {
    "Aluminio (69 GPa)": 69e9,
    "Aco (200 GPa)": 200e9
}


a_vals = np.arange(0, 9, 1)  # 0, 1, 2, ..., 8 m
resultados = []

for a in a_vals:
    b = L - a
    for material, E in E_values.items():
        # cálculo do deslocamento usando o Teorema de Castigliano
        Xd_m= P * a**2 * b**2 / (3 * E * I * L) 
        resultados.append({
            "a (m)": a,
            "b (m)": b,
            "Material": material,
            "E (GPa)": E / 1e9,
            "Deflexao (m)": Xd_m,
        
        })

df = pd.DataFrame(resultados)
print("\n TABELA DE DESLOCAMENTOS \n")
print(df)


plt.figure(figsize=(8, 5))
for material in E_values.keys():
    subset = df[df["Material"] == material]
    plt.plot(subset["a (m)"], subset["Deflexao (m)"], marker='o', label=material)

plt.xlabel("a (m) — posição da carga a partir do apoio esquerdo")
plt.ylabel("Deslocamento no ponto da carga Xd (m)")
plt.title("Deslocamento da viga AB P = 95 kN (L = 8 m)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
