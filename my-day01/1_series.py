# %%
import pandas as pd

# %%
idades = [10, 5, 68, 15, 30, 29, 50]
print('Media{sum(idades)/len(idades)}')

# %%
s_idades = pd.Series(idades)
s_idades

# %%
# Média
media = s_idades.mean()
print('Média ', media)
# Variância
variância = s_idades.var()
print('Variância ', variância)
# %%
s_idades.describe

# %%
novas_idades = [x for x in idades if x > 30]
print(novas_idades)

# %%
filtro = s_idades >= 30
s_idades[filtro]
# Negativo do filtro
s_idades[~filtro]
# %%
