import pandas as pd

listed_companies = pd.read_csv('data/Listed_Companies.csv')

columns = listed_companies.columns

listed_companies[listed_companies['Ticker'] == '*']

def getCompanyData(countries,exchnage):

    if len(countries) != 0 and len(exchnage) != 0:
        return listed_companies.loc[(listed_companies['Country'].isin(countries))
                                    & (listed_companies['Exchange'].isin(exchnage))]
    elif len(countries) == 0 and len(exchnage) != 0:
        return listed_companies.loc[listed_companies['Exchange'].isin(exchnage)]
    elif len(countries) != 0 and len(exchnage) == 0:
        return listed_companies.loc[listed_companies['Country'].isin(countries)]
    else:
        return listed_companies

print(getCompanyData(['India'],['BSE']))