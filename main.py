from cmath import nan
import yfinance as yf
import pandas as pd
import numpy as np
import pandas_ta as ta
import json

def analysis(stock):
    data = yf.download(tickers=stock, period='6mo', interval='1d')
    data = add_indicators(data)
    check_entry_conditions(stock, data.tail(1))

def back_testing(stock):
    data = yf.download(tickers=stock, period='5y', interval='1d')
    data = add_indicators(data)
    open_trade = False
    exit_condition = False

    entry_price = None
    entry_date = None
    close_price = None
    close_date = None

    exspire_trade = 10

    for index, row in data.iterrows():
        if (not np.isnan(row['SMA200'])):
            if (not open_trade) and (row['Close'] < row['BBL20']):
                entry_price = row['Close'] * 0.97
            elif (entry_price) and (not open_trade) and (row['Low'] <= entry_price and entry_price <= row['High']):
                open_trade = True
                entry_date = index
            elif (open_trade) and (exspire_trade > 0):
                if (row['RSI_14'] >= 50):
                    exspire_trade = 10
                    exit_condition = True
                else:
                    exspire_trade = exspire_trade - 1
                
                if exspire_trade == 0: # ordine scaduto
                    exspire_trade = 10
                    
                    close_date = index
                    close_price = row['Open']
                    
                    back_testing_opearions['operations'].append({'titolo': stock,
                                                                'data_entrata': entry_date.strftime("%d/%m/%Y"),
                                                                'prezzo_entrata': entry_price,
                                                                'data_chiusura': close_date.strftime("%d/%m/%Y"),
                                                                'prezzo_chiusura': close_price,
                                                                'profitto': (close_price - entry_price)})

                    open_trade = False
                    exit_condition = False

                    entry_price = None
                    entry_date = None
                    close_price = None
                    close_date = None


            elif (exit_condition and open_trade):
                close_date = index
                close_price = row['Open']
                
                back_testing_opearions['operations'].append({'titolo': stock,
                                                            'data_entrata': entry_date.strftime("%d/%m/%Y"),
                                                            'prezzo_entrata': entry_price,
                                                            'data_chiusura': close_date.strftime("%d/%m/%Y"),
                                                            'prezzo_chiusura': close_price,
                                                            'profitto': (close_price - entry_price)})

                open_trade = False
                exit_condition = False

                entry_price = None
                entry_date = None
                close_price = None
                close_date = None
                

def add_indicators(data):
    data['SMA20'] = data['Close'].rolling(20).mean()
    data['SMA200'] = data['Close'].rolling(200).mean()
    data['BBU20'] = data['SMA20'] + 2.5 * data['Close'].rolling(20).std()
    data['BBL20'] = data['SMA20'] - 2.5 * data['Close'].rolling(20).std()
    data.ta.rsi(close='Close', length=14, append=True)
    return data

def check_entry_conditions(stock, data):
    if (data['Close'].values[0] <= data['BBL20'].values[0]):
        entry = {'Titolo': stock, 
                'Chiusura': data['Close'], 
                'BBL20': data['BBL20'], 
                'Prezzo entrata': data['Close'] * 0.97}
        possible_entry['operations'].append(entry)

stocks_list = ['A2A.MI', 'AMP.MI', 'ATL.MI', 'ATL.MI', 'BGN.MI',
    'BMED.MI', 'BAMI.MI', 'BPE.MI', 'CPR.MI', 'CNHI.MI', 
    'DIA.MI', 'ENEL.MI', 'ENI.MI', 'EXO.MI', 'RACE.MI', 
    'FBK.MI', 'G.MI', 'HER.MI', 'IP.MI', 'ISP.MI', 
    'INW.MI', 'IG.MI', 'IVG.MI', 'LDO.MI', 'MB.MI', 
    'MONC.MI', 'NEXI.MI', 'PIRC.MI', 'PST.MI', 'PRY.MI', 
    'REC.MI', 'SPM.MI', 'SRG.MI', 'STLA.MI', 'STM.MI', 
    'TIT.MI', 'TEN.MI', 'TRN.MI', 'UCG.MI', 'UNI.MI']

possible_entry = {'operations': []}
back_testing_opearions = {'operations': []}

if __name__ == '__main__':
    for stock in stocks_list:
        print(stock)
        # analysis(stock=stock)
        back_testing(stock=stock)
        
    with open('possible_entry.json', 'w') as fp:
        json.dump(possible_entry, fp)
    
    with open('back_testing_opearions.json', 'w') as fp:
        json.dump(back_testing_opearions, fp)