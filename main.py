import yfinance as yf
import pandas as pd
import time

def analysis(stock):
    print(stock)
    data = yf.download(tickers=stock, period='6mo', interval='1d')
    print(data.tail(3))

stocks_list = ['A2A.MI', 'AMP.MI', 'ATL.MI', 'ATL.MI', 'BGN.MI',
    'BMED.MI', 'BAMI.MI', 'BPE.MI', 'CPR.MI', 'CNHI.MI', 
    'DIA.MI', 'ENEL.MI', 'ENI.MI', 'EXO.MI', 'RACE.MI', 
    'FBK.MI', 'G.MI', 'HER.MI', 'IP.MI', 'ISP.MI', 
    'INW.MI', 'IG.MI', 'IVG.MI', 'LDO.MI', 'MB.MI', 
    'MONC.MI', 'NEXI.MI', 'PIRC.MI', 'PST.MI', 'PRY.MI', 
    'REC.MI', 'SPM.MI', 'SRG.MI', 'STLA.MI', 'STM.MI', 
    'TIT.MI', 'TEN.MI', 'TRN.MI', 'UCG.MI', 'UNI.MI']

thread_list = []

if __name__ == '__main__':
    print('Ciao')
    for stock in stocks_list:
        analysis(stock=stock)
       