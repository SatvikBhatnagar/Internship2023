#!pip install plotly==5.4.0
#import dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import math
import time
import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.express as px
import os
import yfinance as yf
    

#load data from y finance
#tickers = ['TSLA']
#tickers = ['TSLA', 'BAJFINANCE.NS', 'OIL.BO']
#print(ticker)



tickers = ['ICICIBANK.NS', 'NESTLEIND.NS', 'APOLLOHOSP.NS', 'WIPRO.NS', 'CIPLA.NS',
           'TECHM.NS', 'BHARTIARTL.NS', 'HDFCLIFE.NS', 'TCS.NS', 'BAJFINANCE.NS',
           'LT.NS', 'BAJAJ-AUTO.NS', 'ADANIENT.NS', 'TATACONSUM.NS', 'BRITANNIA.NS',
           'BAJAJFINSV.NS', 'MARUTI.NS', 'RELIANCE.NS', 'KOTAKBANK.NS', 'TITAN.NS',
           'NTPC.NS', 'ULTRACEMCO.NS', 'HEROMOTOCO.NS', 'ITC.NS', 'INDUSINDBK.NS',
           'TATASTEEL.NS', 'HINDALCO.NS', 'ONGC.NS', 'COALINDIA.NS', 'M&M.NS', ]

ticker_df=[]
max_price_df=[]
min_price_df=[]
difference_df=[]
first_level_df=[]
second_level_df=[]
third_level_df=[]
fourth_level_df=[]
fifth_level_df=[]



for ticker in tickers:
    
    financialCurrency = yf.Ticker(ticker).info['financialCurrency']

    current_time = datetime.datetime.now() 
    year = current_time.year
    month = current_time.month
    
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    
    
    start_year = 2018
    start_month = 1
    start_day = 1
    
    #datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    #period1 = int(time.mktime(datetime.datetime(2020, 6, 22, 23, 59).timetuple())) #'1516406400'
    period1 = int(time.mktime(datetime.datetime(start_year, start_month, start_day, hour, minute).timetuple())) #'1516406400'
    #time.mktime converts our ouptput into second values
    period2 = int(time.mktime(datetime.datetime(year, month, day, hour, minute).timetuple())) #'1624147200'
    interval = '1d' #'1wk' '1m'
    
    #date ranges are provided in seconds, so when we provide date ranges we must convert them to seconds
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    #https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1516406400&period2=1624147200&interval=1d&events=history&includeAdjustedClose=true
    
    
    #Convert Date to indexred
    df = pd.read_csv(query_string)
    
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))


    #plot close price on chart
    plt.figure(figsize=(9, 5.5))
    plt.plot(df.Close, color='blue')
    plt.title(f'{ticker} Close Price')
    plt.xlabel('Date ({}/{}/{} - {}/{}/{})'.format(start_day, start_month, start_year, day, month, year))
    plt.ylabel('Price {}'.format(financialCurrency))
    plt.legend(['Price line'])
    plt.gcf() #get current figure 
    plt.savefig("output_img/{}_closePrice.jpg".format(ticker), dpi = 500, bbox_inches = 'tight')
    plt.show()


    #Calculate Fib Retracement Level prices with a non-fib level/ratio of .5 or 50%
    #Fib Ratios:
      #0.236, 0.382, 0.618
    #.618 = Ni/Ni+1
    #.382 = Ni/Ni+2
    #.236 = Ni/Ni+3
    
    #Get max and min for close price of time period
    max_price = df['Close'].max()
    min_price = df['Close'].min()
    
    #Calc diff between min and max
    difference = max_price - min_price
    first_level = max_price - difference * .236
    second_level = max_price - difference * .382
    third_level = max_price - difference * .5
    fourth_level = max_price - difference * .618
    fifth_level = max_price - difference * .786
    
    ticker_df.append(ticker)
    max_price_df.append(max_price)
    min_price_df.append(min_price)
    difference_df.append(difference)
    first_level_df.append(first_level)
    second_level_df.append(second_level)
    third_level_df.append(third_level)
    fourth_level_df.append(fourth_level)
    fifth_level_df.append(fifth_level)
    #data_to_csv = pd.DataFrame(data, columns=['Stocks', 'max_price', 'min_price', 'difference',
                                                      #'23.6%','38.2%', '50%', '61.8%', '78,6%'])
    
    #with open('')
    
    
    #Print the price at each level
    '''print ('Level Percentage Price($)' )
    print('00.0%\t\t', max_price)
    print('23.6%\t\t', first_level)
    print('38.2%\t\t', second_level)
    print('50%\t\t', third_level)
    print('61.8%\t\t', fourth_level)
    print('78.6%\t\t', fifth_level)
    print('100%\t\t', min_price)'''
    
    #entries = os.listdir('final_internship/')
    #print(entries)
    
    
    #print(pwd)
    #entries = os.listdir('/home/stoner69/codes/final_internship/') -- code not working
    
    '''fig = px.line(df, x='Date', y='Close', title=f'{ticker} Line Chart')
    fig.add_hline(y=max_price, annotation_text=f"Maximum Price: {max_price}", annotation_font_color="blue")
    fig.add_hline(y=first_level, annotation_text=f"23.6% {first_level}", annotation_font_color="green")
    fig.add_hline(y=second_level, annotation_text=f"38.2% {second_level}", annotation_font_color="yellow")
    fig.add_hline(y=third_level, annotation_text=f"50% {third_level}", annotation_font_color="orange")
    fig.add_hline(y=fourth_level, annotation_text=f"61.8% {fourth_level}", annotation_font_color="purple")
    fig.add_hline(y=fifth_level, annotation_text=f"78.6% {fifth_level}", annotation_font_color="red")
    fig.add_hline(y=min_price, annotation_text=f"MInimum Price: {min_price}", annotation_font_color="black")
    fig.show()'''
    
    
    
    
    
    #Time delta for how long to plot line
    time_delta = datetime.timedelta(days=30)
    
    #plot fib level prices with close price. 
    fib_df = df
    plt.figure(figsize=(12.33, 4.5))
    plt.title(f'Fibonnaci Retracement & Support/Resistance {ticker}')
    plt.plot(fib_df.index, fib_df['Close'])
    plt.axhline(max_price, linestyle='--', alpha = .5, color = 'red')
    plt.axhline(first_level, linestyle='--', alpha = .5, color = 'orange')
    plt.axhline(second_level, linestyle='--', alpha = .5, color = 'yellow')
    plt.axhline(third_level, linestyle='--', alpha = .5, color = 'blue')
    plt.axhline(fourth_level, linestyle='--', alpha = .5, color = 'purple')
    plt.axhline(fifth_level, linestyle='--', alpha = .6, color = "pink")
    plt.axhline(min_price, linestyle='--', alpha = .5, color = 'green')
    plt.xlabel('Date ({}/{}/{} - {}/{}/{})'.format(start_day, start_month, start_year, day, month, year))
    plt.ylabel('Price {}'.format(financialCurrency))
    
    pivots = [] #store pivot values
    pivot_date = [] #store date corresponding to pivot value
    counter = 0 #keeps track of if certain value is a pivot
    lastpivot = 0 #store last pivot value
    
    Range = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #array to iterate through stock prices
    date_range = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #array to iterate through corresponding dates
    for i in df.index: #iterates through price history 
      currentmax = max(Range, default=0) #Determines max value of 10 item array 'range'
      value = round(df['High'][i],2) #receives next high value from df
    
      Range = Range[1:9] #cuts range array to only show most recent 9 values
      Range.append(value) #adds newest high value from df 
      date_range = date_range[1:9] #cuts date array to only most 9 recent values same as above 
      date_range.append(i) #adds newest date to 'date_range' array
    
      if currentmax == max(Range, default=0): #checks if max stay
        counter+=1
      else:
        counter=0
      if counter == 5:
        lastpivot = currentmax
        dateloc= Range.index(lastpivot)
        lastdate = date_range[dateloc]
        
        pivots.append(lastpivot)
        pivot_date.append(lastdate)
    
    for index in range(len(pivots)):
      #print(str(pivots[index])+': '+str(pivot_date[index]))
    
      plt.plot_date([pivot_date[index],pivot_date[index]+time_delta], [pivots[index],pivots[index]], linestyle='-', linewidth=2, marker=',')
    
    
    #df['High'].plot(label='high', figsize=(20, 12))
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(["price line", "red -- 0%", "orange -- 23.6%", "yellow -- 38.2%", "blue -- 50%", "purple -- 61.8%", "pink -- 78.6%", "green -- 100%"], bbox_to_anchor = (1.25, 0.6), loc='center right')
    
    plt.gcf() #get current figure 
    plt.savefig("output_img/{}_fib_level_prices.jpg".format(ticker), dpi = 500, bbox_inches = 'tight')
    plt.show()
    
    
    #Create plot now with levels filled.
    fig = plt.figure(figsize=(12.33, 4.5))
    ax = fig.add_subplot(1,1,1)
    
    plt.title(f'Fibonnaci Retracement {ticker}')
    plt.plot(fib_df.index, fib_df['Close'], color = 'black')
    
    plt.axhline(max_price, linestyle='--', alpha = .5, color = 'red')
    ax.fill_between(fib_df.index, max_price, first_level, color = 'red')
    
    plt.axhline(first_level, linestyle='--', alpha = .5, color = 'orange')
    ax.fill_between(fib_df.index, first_level, second_level, color = 'orange')
    
    plt.axhline(second_level, linestyle='--', alpha = .5, color = 'yellow')
    ax.fill_between(fib_df.index, second_level, third_level, color = 'yellow')
    
    plt.axhline(third_level, linestyle='--', alpha = .5, color = 'blue')
    ax.fill_between(fib_df.index, third_level, fourth_level, color = 'blue')
    
    plt.axhline(fourth_level, linestyle='--', alpha = .5, color = 'purple')
    ax.fill_between(fib_df.index, fourth_level, fifth_level, color = 'purple')
    
    plt.axhline(fifth_level, linestyle='--', alpha = .5, color = 'pink')
    ax.fill_between(fib_df.index, fifth_level, min_price, color = 'pink')
    
    plt.axhline(min_price, linestyle='--', alpha = .5, color = 'green')
    
    plt.xlabel('Date ({}/{}/{} - {}/{}/{})'.format(start_day, start_month, start_year, day, month, year))
    plt.ylabel('Price {}'.format(financialCurrency))
    plt.legend(["price line", "red -- 0%", "orange -- 23.6%", "yellow -- 38.2%", "blue -- 50%", "purple -- 61.8%", "pink -- 78.6%", "green -- 100%"], bbox_to_anchor = (1.25, 0.6), loc='center right')
    plt.legend(["price line",
                "red -- 0%", "red zone -- 0% to 23.6%",
                "orange --23.6%", "orange zone -- 23.6% to 38.2%",
                "yellow 38.2%%", "yellow zone -- 38.2% to 50%",
                "blue -- 50%", "blue zone -- 50% to 61.8%",
                "purple -- 61.8%", "purple zone -- 61.8% to 78.6%",
                "pink -- 78.6%", "pink zone -- 78.6% to 100%",
                "green -- 100%"], bbox_to_anchor = (1.45, 0.5), loc='center right')
    plt.gcf() #get current figure 
    plt.savefig("output_img/{}_fib_level_filled.jpg".format(ticker), dpi = 1000, bbox_inches = 'tight')
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
data_for_csv = {'ticker' : ticker_df , 'max_price' : max_price_df , 'min_price' : min_price_df,
                'difference' : difference_df, 'first_level' : first_level_df,
                'second_level' : second_level_df,'third_level' : third_level_df,
                'fourth_level' : fourth_level_df, 'fifth_level' : fifth_level_df}
data_to_csv = pd.DataFrame(data_for_csv)
data_to_csv.to_csv(r'/home/stoner69/codes/final_internship/fib_data.csv')