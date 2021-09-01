# BlindEncoder
Classe de apoio para transformar dados categóricos que estejam em formato tabular (dataframe Pandas)            Encoder para trocar qualquer valor categórico do dataframe sem levar em consideração a coluna em que ele aparece


Métodos: 
   fit()
   transform()
   inverse_transform()

Atributo: categories_ 

Exemplos:
dict = {}
dict[1] = ['abc','bcd','cde']
dict[2] = ['def','efg','fgh']
dict[3] = ['ghi','hij','ijk'] 
print(dict)
>>> {1: ['abc', 'bcd', 'cde'], 2: ['def', 'efg', 'fgh'], 3: ['ghi', 'hij', 'ijk']}
df = pd.DataFrame(dict)

benc. = BlindEncoder()
benc.fit(df)
novo_df = benc.transform(df)
print(novo_df)
>>> {0: {0: 0, 1: 1, 2: 2}, 1: {0: 3, 1: 4, 2: 5}, 2: {0: 6, 1: 7, 2: 8}}
print(benc.categories_)
>>> {'ABC': 0, 'BCD': 1, 'CDE': 2, 'DEF': 3, 'EFG': 4, 'FGH': 5, 'GHI': 6, 'HIJ': 7, 'IJK': 8, 'DESCONHECIDO': 10}

Tentativa de usar pandas.factorize() resulta em erro:
pd.factorize(df)
>>> ValueError: Buffer has wrong number of dimensions (expected 1, got 2)
