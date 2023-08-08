# %%
import pandas as pd

# %%
df = pd.read_csv('data/pedido.csv')

# %%
df.head()
# %% Colunas
df.columns

# %% Shape
df.shape

# %%
print(df.index)
# %%
df.info(memory_usage='deep')

# %%
df.dtypes
# %%
df.head()

# %%
df.tail()
# %%
df.sample()
# %%
