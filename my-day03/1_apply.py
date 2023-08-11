# %%
import pandas as pd

# %%
df = pd.read_csv('../data/produto.csv')

# %%
df['descItem'].unique


# %%
def is_massa(x: str):
    return x.lower().startswith('massa')


# %%
is_massa('MASSa vegana')

# %%
(df['descItem'].apply(lambda x: x.lower().startswith('massa')))
# %%
filtro = df['descItem'].str.lower().str.startswith('massa')
df[filtro]

# %%
