def honoceni_graf(df):
    p = df.groupby('Rating')['Rating'].agg(['count'])
    movie_count = df.isnull().sum()[1]
    cust_count = df['Cust_Id'].nunique() - movie_count
    rating_count = df['Cust_Id'].count() - movie_count
    ax = p.plot(kind='barh', legend=False, figsize=(15, 10))
    plt.title('Total pool: {:,} Movies, {:,} customers, {:,} ratings given'.format(movie_count, cust_count, rating_count),fontsize=20)
    plt.axis('off')
    for i in range(1, 6):
        ax.text(p.iloc[i - 1][0] / 4, i - 1, 'Rating {}: {:.0f}%'.format(i, p.iloc[i - 1][0] * 100 / p.sum()[0]), color='white', weight='bold')
    plt.show()
def pridat_movie_ID(df):
    df_nan = pd.DataFrame(pd.isnull(df.Rating))
    df_nan = df_nan[df_nan['Rating'] == True]
    df_nan = df_nan.reset_index()
    movie_np = []
    movie_id = 1
    for i, j in zip(df_nan['index'][1:], df_nan['index'][:-1]):
        temp = np.full((1, i - j - 1), movie_id)
        movie_np = np.append(movie_np, temp)
        movie_id += 1
    last_record = np.full((1, len(df) - df_nan.iloc[-1, 0] - 1), movie_id)
    movie_np = np.append(movie_np, last_record)
    print('Movie numpy: {}'.format(movie_np))
    print('Length: {}'.format(len(movie_np)))
    df = df[pd.notnull(df['Rating'])]
    df['Movie_Id'] = movie_np.astype(int)
    df['Cust_Id'] = df['Cust_Id'].astype(int)
    print('-Dataset examples-')
    print(df.iloc[::5000000, :])
    return df