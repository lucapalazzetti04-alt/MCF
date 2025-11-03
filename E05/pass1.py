import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fM0 = 'hit_times_M0.csv'


df = pd.read_csv(fM0)

plt.hist(df['hit_time'], bins=50)
plt.xlabel('Tempo [ns]')
plt.ylabel('Numero di Hit')
plt.show()


dt_cons = np.diff(df['hit_time'])

plt.hist(dt_cons, bins=50)
plt.xlabel('Δt [ns]')
plt.ylabel('Conteggio')
plt.show()
