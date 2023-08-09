# %%
import pandas as pd

# %%
df = pd.read_csv('../data/pedido.csv')
df

# %% Somente pedidos do estado de São Paulo
df[(df['descUF'] == 'São Paulo')]

# %% Somente pedidos do estado de São Paulo e ketchup
filtro_sp_ketchup = (df['descUF'] == 'São Paulo') & df['flKetchup']
df[filtro_sp_ketchup]

# %% Somente pedidos dos estados de São Paulo,Paraná,Rio de Janeiro e ketchup
# JEITO RUIM
filtro_ufs_ketchup = (
    (df['descUF'] == 'São Paulo')
    | (df['descUF'] == 'Paraná')  # noqa
    | (df['descUF'] == 'Rio de Janeiro')  # noqa
) & df['flKetchup']
df[filtro_ufs_ketchup]

# %% Somente pedidos dos estados de São Paulo,Paraná,Rio de Janeiro e ketchup
# JEITO CERTO
filtro_ufs_ketchup = (
    df['descUF'].isin(['São Paulo', 'Paraná', 'Rio de Janeiro'])
    & df['flKetchup']  # noqa
)
df[filtro_ufs_ketchup]
# %% Pedidos sem recado => campo = NaN
df[df['txtRecado'].isna()]

# %%
