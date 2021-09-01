# BlindEncoder
Classe de apoio para transformar dados categóricos que estejam em formato tabular (dataframe Pandas)            Encoder para trocar qualquer valor categórico do dataframe sem levar em consideração a coluna em que ele aparece


## Métodos: 
   <li>fit()
   <li>transform()
   <li>inverse_transform()

## Atributo:
   <li>categories_ 

## Exemplos:
<l>dict = {}
<l>dict[1] = ['abc','bcd','cde']
<l>dict[2] = ['def','efg','fgh']
<l>dict[3] = ['ghi','hij','ijk'] 
<l>print(dict)
<l>>>> {1: ['abc', 'bcd', 'cde'], 2: ['def', 'efg', 'fgh'], 3: ['ghi', 'hij', 'ijk']}
<l>df = pd.DataFrame(dict)

<l> benc. = BlindEncoder()
<l> benc.fit(df)
<l> novo_df = benc.transform(df)
<l> print(novo_df)
<l> >>> {0: {0: 0, 1: 1, 2: 2}, 1: {0: 3, 1: 4, 2: 5}, 2: {0: 6, 1: 7, 2: 8}}
<l> print(benc.categories_)
<l> >>> {'ABC': 0, 'BCD': 1, 'CDE': 2, 'DEF': 3, 'EFG': 4, 'FGH': 5, 'GHI': 6, 'HIJ': 7, 'IJK': 8, 'DESCONHECIDO': 10}

## Tentativa de usar pandas.factorize() resulta em erro:
<l> pd.factorize(df)
<l> >>> ValueError: Buffer has wrong number of dimensions (expected 1, got 2)
