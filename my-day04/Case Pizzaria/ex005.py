# %%
# A preferência do tipo de massa muda entre os estados?E os ingredientes prediletos?

import pandas as pd

df_item_pedido = pd.read_csv("../../data/item_pedido.csv")
df_pedido = pd.read_csv("../../data/pedido.csv")

# %%
df_item_pedido

# %%
df_pedido


# %%
df_massa = df_item_pedido[df_item_pedido['descTipoItem'] == 'massa']
df_massa = df_massa.merge(df_pedido[['descUF', 'idPedido']], how='left')
df_massa

# %%
(
    df_massa.groupby(by=['descUF', 'descItem'])['idPedido']
    .count()
    .reset_index()
    .sort_values(['descUF', 'descItem'], ascending=[True, False])
    .pivot_table(values='idPedido', columns='descItem', index='descUF')
    .reset_index()
    .fillna(0)
    .to_csv('./analise_borada.csv', sep=';', encoding='latin1', index=False)
)
# %%
