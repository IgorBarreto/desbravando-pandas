# %%
import pandas as pd

df_product = pd.read_csv('../data/produto.csv')
df_product
# %%
df_product['descItemFirstName'] = df_product[['descItem']].apply(
    lambda x: x.lower().split(' ')[0]
)
df_product
df_product.sort_values(
    by=['vlPreco', 'descItem'],
    ascending=[False, True],
)
# %%
df_product.drop_duplicates(
    subset=['descItemFirstName'],
    keep='first',
)

# %%
df_product.groupby(['descItemFirstName']).agg(
    {'vlPreco': ['mean', 'count', 'median']}
)
