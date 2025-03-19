import numpy as np
import pandas as pd

# Parâmetros do sinal
fs = 200    # Frequência de amostragem (Hz)
dt = 1      # Duração de 1 segundo
t = np.arange(0, dt, 1/fs)  

# Frequências do sinal
f1 = 2  # Hz
f2 = 20 # Hz

# Gerar o sinal (união das duas frequências)
signal = np.sin(2 * np.pi * f1 * t) + 0,5*np.sin(2 * np.pi * f2 * t)

# Criar o DataFrame para salvar em CSV
df = pd.DataFrame({
    "Time (s)": t,
    "Signal": signal
})

# Salvar o DataFrame em um arquivo CSV
csv_path = '../Dados/sinal.csv'
df.to_csv(csv_path, index=False)
csv_path  
