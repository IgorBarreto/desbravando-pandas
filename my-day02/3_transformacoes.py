# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('../data/produto.csv')

# %%
df
# %%
df.info()
# %% add new column
df['precoAjustado'] = (df['vlPreco'] * 1.09).round(2)
df
# %%
df['txAjuste(%)'] = (((df['precoAjustado'] / df['vlPreco']) - 1) * 100).round(
    2
)
df

# %% Remove a column
df = df.drop(columns=['txAjuste'])
# del df['txAjuste]
# %% apply log function on Series
df['txAjuste(Log)'] = np.log(df['txAjuste(%)'])
df['txAjuste(exp)'] = np.exp(df['txAjuste(%)'])
df


# %%
def fat(num: int):
    total = 1
    for i in range(2, int(num) + 1):
        total *= i
    return total


# %%
df['precoAjustado(fat)'] = df['precoAjustado'].apply(fat)
df

# %%
