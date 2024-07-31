df_ad['new_column'] = df_ad['@'].where(df_ad['PostSpon'] == df_ad['PosterID'])
