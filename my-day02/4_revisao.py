# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('../data/produto.csv')

# %%
df = df.rename(columns={'vlPreco': 'vlPrecoReal'})

# %%
df
# %%
df[df['vlPrecoReal'] > 10]

# %%
queijos = ['queijo brie', 'queijo coalho', 'ricota']
df[df['descItem'].isin(queijos)]

# %%
df['vlPrecoInflacao'] = (df['vlPrecoReal'] * 1.09).round(2)
df

# %%
df['vlPrecoInflacaoLog'] = np.log(df['vlPrecoInflacao']).round(2)
df

# %%
