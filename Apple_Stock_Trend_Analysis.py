>>> import yfinance as yf
... import pandas as pd
... import matplotlib.pyplot as plt
... import seaborn as sns
...
... # Fetch 2 years of Apple stock data
... ticker = "AAPL"
... data = yf.download(ticker, period="2y", interval="1d", auto_adjust=True)
...
... # Show top rows
... print(data.head())
...
[*********************100%***********************]  1 of 1 completed
Price            Close        High         Low        Open     Volume
Ticker            AAPL        AAPL        AAPL        AAPL       AAPL
Date
2023-08-01  193.670898  194.779791  193.344168  194.294658   35175100
2023-08-02  190.670959  193.245177  189.948200  193.106565   50389300
2023-08-03  189.274902  190.463004  188.799665  189.670946   61235200
2023-08-04  180.185928  185.522496  180.116615  183.680934  115956800
2023-08-07  177.077072  181.314643  175.591942  180.324556   97576100
>>> # Daily Return (% change)
... data['Daily Return'] = data['Close'].pct_change()
...
... # 30-day Moving Average of Close Price
... data['MA30'] = data['Close'].rolling(window=30).mean()
...
... # 30-day Rolling Volatility (Standard Deviation of Daily Returns)
... data['Volatility'] = data['Daily Return'].rolling(window=30).std()
...
... # Drop missing values created by rolling functions
... data.dropna(inplace=True)
...
... # Preview the updated DataFrame
... print(data[['Close', 'Daily Return', 'MA30', 'Volatility']].head())
...
Price            Close Daily Return        MA30 Volatility
Ticker            AAPL
Date
2023-09-13  172.715988    -0.011855  178.961053   0.016743
2023-09-14  174.232864     0.008782  178.413117   0.016739
2023-09-15  173.509094    -0.004154  177.887590   0.016720
2023-09-18  176.443726     0.016913  177.762850   0.014745
2023-09-19  177.534302     0.006181  177.778091   0.014450
>>> plt.figure(figsize=(14, 6))
<Figure size 1400x600 with 0 Axes>
>>> plt.plot(data.index, data['Close'], label='Close Price', color='blue', linewidth=2)
[<matplotlib.lines.Line2D object at 0x0000023F0921F750>]
>>> plt.plot(data.index, data['MA30'], label='30-Day MA', color='orange', linewidth=2)
[<matplotlib.lines.Line2D object at 0x0000023F09CC7C50>]
>>> plt.title('Apple Stock Price vs 30-Day Moving Average', fontsize=16)
... plt.xlabel('Date')
... plt.ylabel('Price (USD)')
... plt.legend()
...
<matplotlib.legend.Legend object at 0x0000023F09CC9160>
>>> plt.grid(True)
... plt.tight_layout()
... plt.show()
...
>>> plt.figure(figsize=(10, 5))
<Figure size 1000x500 with 0 Axes>
>>> plt.figure(figsize=(10, 5))
<Figure size 1000x500 with 0 Axes>
>>> plt.hist(data['Daily Return'], bins=50, color='purple', edgecolor='black')
(array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  2.,  1.,  4.,  5.,  6.,
       11., 17., 12., 37., 63., 71., 85., 60., 38., 29., 17.,  2.,  3.,
        2.,  2.,  0.,  0.,  1.,  1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.]), array([-0.09245608, -0.08754119, -0.0826263 , -0.07771141, -0.07279651,
       -0.06788162, -0.06296673, -0.05805184, -0.05313695, -0.04822206,
       -0.04330717, -0.03839228, -0.03347739, -0.0285625 , -0.0236476 ,
       -0.01873271, -0.01381782, -0.00890293, -0.00398804,  0.00092685,
        0.00584174,  0.01075663,  0.01567152,  0.02058642,  0.02550131,
        0.0304162 ,  0.03533109,  0.04024598,  0.04516087,  0.05007576,
        0.05499065,  0.05990554,  0.06482043,  0.06973533,  0.07465022,
        0.07956511,  0.08448   ,  0.08939489,  0.09430978,  0.09922467,
        0.10413956,  0.10905445,  0.11396934,  0.11888424,  0.12379913,
        0.12871402,  0.13362891,  0.1385438 ,  0.14345869,  0.14837358,
        0.15328847]), <BarContainer object of 50 artists>)