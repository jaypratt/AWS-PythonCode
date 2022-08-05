# imports
import json 
import requests
import time
import os

# to do

# analysis, which ran highest

# define function meanReversionStrategy
# run strategy and output buys/sells, final profit, and final percentage returns
def meanReversionStrategy(prices):
    i = 0
    avg_price = 0
    current_price = 0
    fbuy = 0
    buy = 0
    tprofit = 0
    percentReturn = 0
    sell = 0
    
    for i in range(len(prices)):
        if i >= 5:
            current_price = prices[i]
            avg_price = ((prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5)
            print(current_price, avg_price)
            if current_price < (avg_price*.98) and buy == 0: # buy
                buy = current_price
                if i == len(prices)-1:
                    print("buy today")
                if fbuy == 0:
                    fbuy += buy
                if buy != 0 and sell != 0:
                    tprofit += sell - buy
                else:
                    pass
            elif current_price > (avg_price*1.02) and buy != 0: # sell
                sell = current_price
                if i == len(prices)-1:
                    print("sell today")
                profit = (sell - buy)
                tprofit += profit
                buy = 0
            else:
                pass
        else:
            pass
    percentReturn = round(tprofit/fbuy*100,2)    # return profit and returns
    return round(tprofit,2), percentReturn


# define function simpleMovingAverageStrategy
# run strategy and output buys/sells, final profit, and final percentage returns
def simpleMovingAverageStrategy(prices):
    i = 0
    avg_price = 0
    current_price = 0
    fbuy = 0
    buy = 0
    tprofit = 0
    percentReturn = 0
    sell = 0
    
    for i in range(len(prices)):
        if i >= 5:
            current_price = prices[i]
            avg_price = ((prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5)
            if current_price > avg_price and buy == 0: # buy
                buy = current_price
                if fbuy == 0:
                    fbuy += buy
                if buy != 0 and sell != 0:
                    tprofit += sell - buy
                else:
                    pass
            elif current_price < avg_price and buy != 0: # sell
                sell = current_price
                profit = (sell - buy)
                tprofit += profit
                buy = 0
            else:
                pass
        else:
            pass
    percentReturn = round(tprofit/fbuy*100,2)    # return profit and returns
    return round(tprofit,2), percentReturn


# define function bollingerBandsStrategy
# run strategy and output buys/sells, final profit, and final percentage returns
def bollingerBandsStrategy(prices):
    i = 0
    avg_price = 0
    current_price = 0
    fbuy = 0
    buy = 0
    tprofit = 0
    percentReturn = 0
    sell = 0
    
    for i in range(len(prices)):
        if i >= 5:
            current_price = prices[i]
            avg_price = ((prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5)
            if current_price > (avg_price*1.05) and buy == 0: # buy
                buy = current_price
                if fbuy == 0:
                    fbuy += buy
                if buy != 0 and sell != 0:
                    tprofit += sell - buy
                else:
                    pass
            elif current_price < (avg_price*.95) and buy != 0: # sell
                sell = current_price
                
                profit = (sell - buy)
                tprofit += profit
                buy = 0
            else:
                pass
        else:
            pass
    percentReturn = round(tprofit/fbuy*100,2)    # return profit and returns
    return round(tprofit,2), percentReturn

# define function saveResults    
def saveResults(resultDict): 
    json.dump(results, open("results.json", "w"), indent = 4)
 
    return("Results Recorded")

#creates the csv files if they don't exist yet
def createData(ticker): 
    url = 'http://alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    print(url)
    request = requests.get(url)
    time.sleep(12)
    req_dict = json.loads(request.text)
    
    print(req_dict.keys())
    
    key1 = "Time Series (Daily)"
    key2 = '4. close'
    
    csv_file = open (ticker + ".csv", "w")
    write_lines = []
    for date in req_dict[key1]:
        print(date + "," + req_dict[key1][date][key2])
        write_lines.append(date+","+req_dict[key1][date][key2] + "\n") 
    write_lines = write_lines[::-1]
    csv_file.writelines(write_lines)
    csv_file.close()

#add's data to csv files if not up to date already
def appendData(ticker): 
    url = 'http://alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    print(url)
    req = requests.get(url)
    time.sleep(12)
    req_dict = json.loads(req.text)
    
    print(req_dict.keys())
    
    key1 = "Time Series (Daily)"
    key2 = '4. close'
    
    
    csv_file = open (ticker + ".csv", "r")
    lines = csv_file.readlines()
    last_date = lines[-1].split(",")[0]
    
    new_lines = []
    
    for date in req_dict[key1]:
        if date == last_date:
            break
        print(date + "," + req_dict[key1][date][key2])
        new_lines.append(date+","+req_dict[key1][date][key2] + "\n") 
    new_lines = new_lines[::-1]
    csv_file.writelines(new_lines)
    csv_file.close()


highestReturn = 0
highestTicker = " "
results = {} # create dictionary called results to store prices, profits and return percentages

# create list to store 10 tickers
tickers = ["AAPL", "ADBE"]#, "COST", "DIS", "GOOG", "MNST", "MSFT", "NTDOY", "NVDA", "SONY"]

results = {} 

for ticker in tickers: # loop through the list of tickers for updates/creation
    
    if not os.path.exists(ticker + ".csv"):
        print("File does not exist. Creating file")
        createData(ticker)
    else:
        print("File found. Updating...")
        appendData(ticker)
    

# loop through the list of tickers for Analysis
for ticker in tickers:
    file = open("/home/ec2-user/environment/" + ticker + ".csv", 'r')
    lines = file.readlines()

    prices = [ float(line.split(",")[-1]) for line in open(ticker+".csv").readlines()[1:]]
    
    
   # print(ticker + 'Stock Data') 
    tprofit, percentReturn = meanReversionStrategy(prices) #MR call and documenting, then store profit and returns in results dictionary
    if percentReturn > highestReturn:
        highestReturn = percentReturn
        highestTicker = ticker
        #highestStrategy = "meanReversionStrategy"
    else:
        pass
    results[ticker + " mr profit"] = tprofit
    results[ticker + " mr return"] = percentReturn    
    
    tprofit, percentReturn = simpleMovingAverageStrategy(prices) #SMA call and documenting, then store profit and returns in results dictionary
    
    results[ticker + " sma profit"] = tprofit
    results[ticker + " sma returns"] = percentReturn 
    
    tprofit, percentReturn = bollingerBandsStrategy(prices) #BB call and documenting, then store profit and returns in results dictionary
    
    results[ticker + " bb profit"] = tprofit
    results[ticker + " bb returns"] = percentReturn 
results[ticker + "Greatest Return"] = highestReturn
results[ticker + "Greatest Ticker"] = highestTicker
#print("Greatest Return: "+ highestReturn + ", " + highestTicker)
    
    


saveResults(results)  # call saveResults(results) and save the results dictionary to a file called results.json
