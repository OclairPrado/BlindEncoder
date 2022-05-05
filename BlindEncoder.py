# NOVA VERSÃO DANIEL
class BlindEncoder:
  categories_ = {}
    
    
  def fit(self, df):
    if df is None or len(df) == 0:
      raise ValueError('Empty DataFrame.')

    df = pd.concat([df[col].map(lambda x: x.upper() if isinstance(x, str) else x) for col in df.columns], axis=1)

    cat_list = []
    for col in df.columns:
      cat_list.extend(df[col].unique())
    cat_list = set(cat_list)

    num_set = set()
    for cat in cat_list:
      if isinstance(cat, (int, float, np.int64, np.float64)):
        num_set.add(cat)

    self.categories_ = {}
    num_cats     = len(cat_list)
    code         = 0
    for cat in cat_list:
      if isinstance(cat, (int, float, np.int64, np.float64)):
        self.categories_[cat] = cat
      else:
        code = min( set(range(code, num_cats)) - num_set )
        self.categories_[cat] = code
        code += 1
        
    self.categories_['DESCONHECIDO'] = self.categories_.get('DESCONHECIDO', num_cats+1)
    


  def transform(self, df):
    if df is None or len(df) == 0:
      raise ValueError('Empty DataFrame.')

    if len(self.categories_.keys()) == 0:
      raise ValueError('Probably missing .fit().')

    df = pd.concat([df[col].map(lambda x: x.upper() if isinstance(x, str) else x) for col in df.columns], axis=1)

    cat_list = []
    for col in df.columns:
      cat_list.extend(df[col].unique())
    cat_list = set(cat_list)

    for cat in cat_list:
      self.categories_[cat] = self.categories_.get(cat, self.categories_['DESCONHECIDO'])
  
    df_enc = df.apply(lambda col: col.map(self.categories_))

    return df_enc



  def inverse_transform(self, df_enc):
    if df_enc is None or len(df_enc) == 0:
      raise ValueError('Empty DataFrame.')

    if len(self.categories_) == 0:
      raise ValueError('Probably missing .fit().')

    categories_inv = {v:k for k,v in self.categories_.items()}
    categories_inv[self.categories_['DESCONHECIDO']] = 'DESCONHECIDO'
    df = df_enc.apply(lambda col: col.map(categories_inv))

    return df
  
