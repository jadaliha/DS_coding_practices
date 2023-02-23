import pandas as pd

def get_attrition(grp, freq):
    prev_roll = grp.rolling(freq, on='yearmonth')['spent'].sum()
    next_roll = grp.rolling(freq, on='yearmonth')['spent'].sum().shift(-1)
    return 1*(next_roll < 0.25*prev_roll)

def main(input_location, output_location):
    data_org  = pd.read_csv(input_location, usecols = ['UserId', 'TransactionId', 'TransactionTime', 'ItemCode', 'NumberOfItemsPurchased', 'CostPerItem', 'ItemDescription'])
    data_org['spent'] = data_org['NumberOfItemsPurchased']*data_org['CostPerItem']
    data_org = data_org.loc[data_org['UserId']!=-1]
    data_org = data_org.drop_duplicates()
    data_org['yearmonth'] = [x[-4:]+x[4:7] for x in data_org['TransactionTime']]
    data_org['yearmonth'] =  pd.to_datetime(data_org['yearmonth'], format='%Y%b')
    data_org.set_index([pd.DatetimeIndex(data_org.yearmonth)], inplace=True)
    
    data_org_mod = data_org.groupby('UserId').resample('1M').sum()
    data_org_mod = data_org_mod.drop(columns=['UserId'])
    data_org_mod = data_org_mod.reset_index(level=['UserId', 'yearmonth'])

    data_org_mod['soft_attrition'] = data_org_mod.groupby('UserId', as_index=False, group_keys=False).apply(get_attrition, '90D')

    res = data_org_mod.loc[:,['UserId', 'yearmonth', 'soft_attrition']]
    res.to_csv(output_location, index=False)
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='data cleaning and computing soft attrition labels')
    parser.add_argument('--myinput', metavar='path', required=True,
                        help='the path to input')
    
    parser.add_argument('--myoutput', metavar='path', required=True,
                        help='the path to output')
    
    args = parser.parse_args()
    
    main(input_location=args.myinput, output_location=args.myoutput)