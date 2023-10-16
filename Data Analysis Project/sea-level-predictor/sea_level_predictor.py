import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('sea-level-predictor/epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    df.head()
    print(df.info())
    print(df.describe())
    print(df.shape)
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    first =linregress(x,y)
    print(first)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = first.slope * x_pred + first.intercept
    plt.plot(x_pred, y_pred, 'green')

    # Create second line of best fit
    df_new = df.loc[df['Year'] >= 2000]
    x_new = df_new['Year']
    y_new = df_new['CSIRO Adjusted Sea Level']
    second = linregress(x_new, y_new)
    x_prednew = pd.Series([i for i in range(1880, 2051)])
    y_prednew = second.slope * x_prednew + second.intercept
    plt.plot(x_prednew, y_prednew, 'purple')
    
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()