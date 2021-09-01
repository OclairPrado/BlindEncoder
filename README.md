# BlindEncoder
Classe de apoio para transformar dados categóricos que estejam em formato tabular (dataframe Pandas)            Encoder para trocar qualquer valor categórico do dataframe sem levar em consideração a coluna em que ele aparece


## Métodos: 
   <li>fit()
   <li>transform()
   <li>inverse_transform()

## Atributo:
   <li>categories_ 

## Exemplos:
<p>dict = {}
<p>dict[1] = ['abc','bcd','cde']
<p>dict[2] = ['def','efg','fgh']
<p>dict[3] = ['ghi','hij','ijk'] 
<p>print(dict)
<p>>>> {1: ['abc', 'bcd', 'cde'], 2: ['def', 'efg', 'fgh'], 3: ['ghi', 'hij', 'ijk']}
<p>df = pd.DataFrame(dict)

<p> benc. = BlindEncoder()
<p> benc.fit(df)
<p> novo_df = benc.transform(df)
<p> print(novo_df)
<p> >>> {0: {0: 0, 1: 1, 2: 2}, 1: {0: 3, 1: 4, 2: 5}, 2: {0: 6, 1: 7, 2: 8}}
<p> print(benc.categories_)
<p> >>> {'ABC': 0, 'BCD': 1, 'CDE': 2, 'DEF': 3, 'EFG': 4, 'FGH': 5, 'GHI': 6, 'HIJ': 7, 'IJK': 8, 'DESCONHECIDO': 10}

## Tentativa de usar pandas.factorize() resulta em erro:
<p> pd.factorize(df)
<p> >>> ValueError: Buffer has wrong number of dimensions (expected 1, got 2)
