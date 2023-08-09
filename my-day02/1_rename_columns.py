# %%
import pandas as pd

df = pd.read_csv('../data/pedido.csv')
# %%
# maneira 1
df = df.rename(columns={'descUF': 'desEstado'})
# maneira 2
df.rename(columns={'descUF': 'desEstado'}, inplace=True)

# %%
