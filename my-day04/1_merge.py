# %%
import pandas as pd

# %%
df_item_pedido = pd.read_csv('../data/item_pedido.csv')
df_item_pedido
# %%
df_produto = pd.read_csv('../data/produto.csv')
df_produto
# %%
df_pedido = pd.read_csv('../data/pedido.csv')
df_pedido
# %%

df = df_item_pedido.merge(
    df_produto,
    how='left',
    # on='descItem',
    left_on=['descItem'],
    right_on=['descItem'],
).merge(
    df_pedido[['idPedido', 'descUF']],
    how='left',
)

# df = pd.merge(
#     df_item_pedido,
#     df_produto,
#     on='descItem',
# )
df
# %%
