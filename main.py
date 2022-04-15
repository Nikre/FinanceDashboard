from operator import length_hint
from numpy import append
import yfinance as yf
import pandas as pd
import pandas_ta as ta
import time
import json

def analysis(stock):
    print(stock)
    data = yf.download(tickers=stock, period='6mo', interval='1d')
    data['SMA20'] = data['Close'].rolling(20).mean()
    data['SMA200'] = data['Close'].rolling(200).mean()
    data['BBU20'] = data['SMA20'] + 2.5 * data['Close'].rolling(20).std()
    data['BBL20'] = data['SMA20'] - 2.5 * data['Close'].rolling(20).std()
    data.ta.rsi(close='Close', length=14, append=True)
    print(data.tail())
    check_entry_conditions(stock, data.tail(1))

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

if __name__ == '__main__':
    print('Ciao')
    for stock in stocks_list:
        analysis(stock=stock)
    
    with open('data.json', 'w') as fp:
        json.dump(possible_entry, fp)