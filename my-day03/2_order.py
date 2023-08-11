# %%
import pandas as pd

# %%
df = pd.read_csv('../data/produto.csv')
df
# %%
df.sort_values(by='vlPreco', ascending=False)

# %%
df.sort_values(by=['vlPreco', 'descItem'], ascending=[False, True])

# %%
