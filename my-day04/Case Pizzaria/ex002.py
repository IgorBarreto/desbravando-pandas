# %%
# Podemos deixar a de Catupiry como borda padrão?

import pandas as pd

df_item_pedido = pd.read_csv('../../data/item_pedido.csv')


# %%
df_borda = df_item_pedido[df_item_pedido['descTipoItem'] == 'borda']
df_borda

# %%
df_group = df_borda.groupby(by=['descItem']).sum().reset_index()
df_group['%'] = (
    df_group['idPedido'] / df_group['idPedido'].sum() * 100
).round(2)
df_group.sort_values(by=['%'])
