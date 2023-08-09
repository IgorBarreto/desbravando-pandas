# %%
import pandas as pd

# %%
idades = pd.Series([10, 20, 30, 45, 8, 91])

# %%
idades.describe()

# %%
df = pd.DataFrame(
    {
        'Nome': ['Igor', 'Maria', 'João'],
        'Idade': [30, 20, 50],
    }
)
df

# %%
df_pedidos = pd.read_csv('../data/pedido.csv')
df_pedidos

# %%
df_pedidos.head()  # primeiras 5 linhas

# %%
df_pedidos.tail()  # yltimas 5 linhas
# %%
df_pedidos.sample(10)  # aleatórios

# %%
df_pedidos.info(memory_usage='deep')

# %%
df_pedidos.dtypes
# %%
df_pedidos[['descUF', 'flKetchup']]
# %%
df_pedidos.iloc[10] # retorna o item na posição do df

# %%
df_pedidos.loc[10] # retorna o item no índice do df
# %%
