# %%
import pandas as pd

# %%
df_filhos = pd.DataFrame(
    {
        'nome': ['Igor', 'Ingrid'],
        'idade': [30, 28],
    }
)
df_filhos
df_pais = pd.DataFrame(
    {
        'nome': ['Valdir', 'Verliani'],
        'idade': [60, 49],
    }
)
pd.concat([df_filhos, df_pais]).sort_values(['nome'])
# %%
