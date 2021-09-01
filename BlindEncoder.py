class BlindEncoder:
  categories_ = {}
  
  def fit(self, df):
    if df is None or len(df) == 0:
      raise ValueError('empty dataframe')
    # Agrupa todos os elementos

    # Passa df para maiúsculas
    df = pd.concat([df[col].astype(str).str.upper() for col in df.columns], axis=1)

    elementos = []
    for coluna in df:
      for elemento in df[coluna]:
        elementos.append(elemento)
    # Remove duplicidades
    categ_list = np.unique(elementos, return_index=False, return_inverse=False, return_counts=False, axis=None)

    # Insere os valores para as categorias
    self.categories_ = {}
    pos = 0
    for categ in categ_list:
      self.categories_[categ] = pos
      pos = pos + 1
    # Garante que o encoder tenha referencia para 'DESCONHECIDO'
    if not 'DESCONHECIDO' in self.categories_:
        self.categories_['DESCONHECIDO'] = len(self.categories_) + 1

  def transform(self, df):
    if df is None or len(df) == 0:
      raise ValueError('empty dataframe')
    if len(self.categories_) == 0:
      raise ValueError('probably missing fit()')
    
    # Passa df para maiúsculas
    df = pd.concat([df[col].astype(str).str.upper() for col in df.columns], axis=1)

    # Garante que o encoder tenha referencia para 'DESCONHECIDO'
    if not 'DESCONHECIDO' in self.categories_:
        self.categories_['DESCONHECIDO'] = len(self.categories_) + 1

    # Agrupa todos os elementos do novo dataframe
    elementos = []
    for coluna in df:
      for elemento in df[coluna]:
        elementos.append(elemento)
    # Remove duplicidades
    categ_list = np.unique(elementos, return_index=False, return_inverse=False, return_counts=False, axis=None)

    # Troca as categorias conhecidas pelos números. As categorias desconhecidas ganham o número equivalene ao 'desconhecido'
    #Obs.: altera apenas string
    df = df.copy()
    for categ in categ_list:
      if isinstance(categ, str):
        if categ in self.categories_:
          df = pd.DataFrame(np.where(df == categ, self.categories_[categ], df))
        else:
          df = pd.DataFrame(np.where(df == categ, self.categories_['DESCONHECIDO'], df))

    return df

  def inverse_transform(self, df_rev):
    if df_rev is None or len(df_rev) == 0:
      raise ValueError('empty dataframe')
    if len(self.categories_) == 0:
      raise ValueError('probably missing fit()')
    
    res = {}
    dict_categ = self.categories_ 
    chaves = list(dict_categ.keys())
    valores = list(dict_categ.values())
 
    for lin in range(df_rev.shape[1]):
      for col in range(df_rev.shape[0]):
        if df_rev[lin][col] in valores:
          pos = valores.index( df_rev[lin][col] )
          res[pos] = chaves[pos]

    return res
    