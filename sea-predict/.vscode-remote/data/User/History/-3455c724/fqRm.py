import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    plt.savefig('sea_level_plot.png')
    
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')
    
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred = intercept + slope * years_extended
    plt.plot(years_extended, sea_level_pred, color='green', label='Best Fit Line (1880-2050)')
    
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent_pred = intercept_recent + slope_recent * years_recent
    plt.plot(years_recent, sea_level_recent_pred, color='red', label='Best Fit Line (2000-2050)')
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    plt.savefig('/mnt/data/sea_level_plot.png')
    return plt.gca()

draw_plot()
