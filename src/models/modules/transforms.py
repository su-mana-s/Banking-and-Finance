import pandas as pd

def date_to_qtr(date):
    yr = date[:4]
    q = date[5:7]
    if q == '12':
        qtr = 'Q4'
    if q == '09':
        qtr = 'Q3'
    if q == '06':
        qtr = 'Q2'
    if q == '03':
        qtr = 'Q1'    
    return (yr + " " + qtr)

def clean_vals(s):
    st = s[1:]
    st = st.replace(",","")
    i = int(st)
    return i

def get_merged_dataset(query, sc, df):
    # sc = pd.read_csv("../../data/raw/dfast/Historic_Domestic.csv", index_col=False)
    # df = pd.read_csv("../../data/raw/uslocs/banks_income_expense_final.csv", index_col=False)

    sc_n = pd.read_csv("../../data/processed/normalized_histdomestic.csv")
    # df_n =  pd.read_csv("../../data/processed/uslocs/normalized_usbanksincome.csv")

    # cd = dict(zip(df.columns, df_n.columns))
    # df = df.rename(columns=cd)
    # cd = dict(zip(sc.columns, sc_n.columns))
    # sc = sc.rename(columns=cd)


    #query 1 class Tag where query is string like : 'Total Assets:'
    r = df.query(f"Bank == {query}")
    r.drop('Bank', axis=1, inplace=True) # cos why? They are all the same
    #Clean values
    r = r.fillna("$0")
    r.isnull().sum()
    #Transform dates
    cols = [col for col in r.columns]
    columns = cols[1:]    
    for col in columns:
        # print(r[f'{col}'])
        r[f'{col}'] = r[f'{col}'].apply(lambda x : clean_vals(x))
    d2q = {col : date_to_qtr(col) for col in columns}
    n_df = r.rename(columns=d2q)

    

    #Transpose - to bank wise cols
    """Here, each bank col will become a dependent variable, so we will be predicting usng the 18 other 
    eco vars the tag(query) for each bank"""
    n_df = n_df.transpose()
    n_df.columns = n_df.iloc[0]
    ndf = n_df.iloc[1:, :] #setting column headers as bank names
    # this gives a data frame that has banks for columns and values for query with rows as quarters
    
    #map this to scenarios
    #I dont think the scenarios have the same number of years - they have more:')
    # inner join the 2 frames
    ndf['Date'] = ndf.index
    sc["Date"] = sc["Date"].astype(str)
    ndf["Date"] = ndf["Date"].astype(str)
    result = sc.merge(right=ndf, on="Date")
    
    return result #merged df
