# %%
# Podemos remover algum tipo de massa do cardápio? Qual o impacto dessa ação?
import pandas as pd

# %% DADOS
df_item_pedido = pd.read_csv('../../data/item_pedido.csv')
df_produto = pd.read_csv('../../data/produto.csv')

# %%
filtro_massa = df_item_pedido['descTipoItem'] == 'massa'

df_massa = df_item_pedido[filtro_massa].merge(df_produto, how='left')
df_massa

# %%
df_group = df_massa.groupby(by=['descItem'])
df_group = df_group.agg(
    {
        'idPedido': ['nunique'],
        'vlPreco': ['sum'],
    }
)
df_group

# %%%
df_group.columns = df_group.columns.get_level_values(0)
df_group.reset_index()
df_group

# %%
df_group['RepQtde(%)'] = (
    df_group['idPedido'] / df_group['idPedido'].sum()
).round(2)
df_group['RepReceita(%)'] = (
    df_group['vlPreco'] / df_group['vlPreco'].sum()
).round(2)
df_group
