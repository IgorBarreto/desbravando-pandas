# %%
# Vários queijos estão estragando pela validade.
# Quais queijos juntos atendem 90% dos pedidos?
import pandas as pd

df_item_pedido = pd.read_csv('../../data/item_pedido.csv')
df_produto = pd.read_csv('../../data/produto.csv')
# %%
filtro_queijo = df_item_pedido['descTipoItem'].isin(['queijo 1', 'queijo 2'])
df_queijo = df_item_pedido[filtro_queijo]
df_queijo

# %%
df_group = (
    df_queijo.groupby(by=['descItem'])['idPedido']
    .nunique()
    .reset_index()
    .sort_values(['idPedido'], ascending=False)
)
df_group
# %%
df_group['pct'] = (
    df_group['idPedido'] / df_group['idPedido'].sum() * 100
).round(2)
df_group['pctAcum'] = df_group['pct'].cumsum()
df_group
# %%
