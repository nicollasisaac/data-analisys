import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')
    
    # Create first line of best fit using all data
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred = intercept + slope * years_extended
    plt.plot(years_extended, sea_level_pred, color='green', label='Best Fit Line (1880-2050)')
    
    # Create second line of best fit using data from 2000 onwards
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent_pred = intercept_recent + slope_recent * years_recent
    plt.plot(years_recent, sea_level_recent_pred, color='red', label='Best Fit Line (2000-2050)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
