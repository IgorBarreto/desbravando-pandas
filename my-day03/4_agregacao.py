# %%
import pandas as pd
import numpy as np

df_product = pd.read_csv('../data/produto.csv')

# %%
df_product['vlPreco'].describe()
# %%
df_product['vlPriceInflation'] = (df_product['vlPreco'] * 1.09).round(2)
df_product.describe()
# %%
# Frequency table => Can be used in quantitative and qualitative values
pd.value_counts(df_product['vlPriceInflation'])

# %%
df_product['firstName'] = df_product['descItem'].apply(
    lambda x: x.lower().split(' ')[0]
)

df_product.groupby(by=['firstName'])['vlPreco'].mean()
(
    df_product.groupby(by=['firstName'])[['vlPreco', 'vlPriceInflation']].agg(
        ['mean', 'min', 'max', 'median']
    )
)


# %%
