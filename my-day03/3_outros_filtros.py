# %%
import pandas as pd

pd.set_option('display.max_rows', 100)
df = pd.read_csv('../data/produto.csv')

# %%
df['primeiroNome'] = df['descItem'].apply(
    lambda x: x.lower().split(' ')[0],
)
df
# %%
df = df.sort_values(
    by=['vlPreco', 'descItem'],
    ascending=[False, True],
)
# Remove all product with the same price and name
df.drop_duplicates(
    subset=[
        'primeiroNome',
        'vlPreco',
    ],
    keep='first',
)

# %%
df_pedido = pd.read_csv('../data/pedido.csv')

# %%
# REMOVE THE LINE THAT CONTAINS AT LEAST A FIELD WITH NaN VALUE
df_pedido.dorpna()


# %%
# REMOVE THE LINE THAT CONTAINS NaN IN THE FIELDS INSIDE OF SUBSET

# All subset
df_pedido.dropna(subset=['txtRecado'], how='all')

# %%
# At least a field inside subset
df_pedido.dropna(subset=['txtRecado'], how='any')
