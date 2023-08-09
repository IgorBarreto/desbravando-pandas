# %%
import warnings
import pandas as pd

warnings.filterwarnings('ignore')


# %%
df = pd.read_csv('../data/pedido.csv')

# %%
df.head()

# %%
df[['idPedido', 'flKetchup']]

# %%
colunas = ['idPedido', 'descUF', 'flKetchup', 'txtRecado', 'dtPedido']
df = df[colunas]
df
# %%
df_sample = df.sample(100)
df_sample

# %%
df_sample.iloc[0]  # Retorna o registro na posição 0
# %%
df_sample.iloc[[0, 2, 5, 10]]

# %%
df_sample.iloc[0:10][['idPedido', 'dtPedido']]
# %%
