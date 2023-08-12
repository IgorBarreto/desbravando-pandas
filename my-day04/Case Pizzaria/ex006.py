# %%
# Quais ingredientes podemos remover do cardápio para diminuir custo no estoque? # noqa
import pandas as pd

df_item_pedido = pd.read_csv('../../data/item_pedido.csv')
df_produto = pd.read_csv('../../data/produto.csv')

# %%
df_item_pedido
# %%
df_produto


# %%
df_group = (
    df_item_pedido[['descItem', 'idPedido']]
    .groupby(by=['descItem'])['idPedido']
    .count()
    .reset_index()
    .sort_values(['idPedido'], ascending=False)
)
df_group = df_group.rename({'idPedido': 'Quantidade'})
df_group


# %%
df_group = df_group.merge(df_produto[['descItem', 'vlPreco']], how='left')
df_group


# %%
df_group['vlCusto'] = df_group['vlPreco'] * df_group['idPedido']


# %%
df_group.sort_values(['vlCusto'])
df_group['idPedido'].sum()
# %%
