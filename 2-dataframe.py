# %%
import pandas as pd

# %%
data = {
    'nome': ['Igor', 'Maria', 'João', 'Carlos'],
    'idade': [30, 25, 50, 40],
    'renda': [3500, 40000, 5000, 1000],
    "cor": ['Vermelho', 'Azul', 'Preto', 'Amarelo'],
}
df = pd.DataFrame(data)
df

# %%
type(df['idade'])

# %%
df.mean()

# %%
df.describe()

# %%

# %%
