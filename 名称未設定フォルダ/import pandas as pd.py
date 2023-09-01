import pandas as pd
import numpy as np

def calculate_solar_power(file_path, alpha=1.2, beta=0.8, gamma=0.5, delta=0.2):
    # Load the Excel data
    raw_data = pd.read_excel(file_path, skiprows=4)
    
    
    # Select and clean relevant columns
    column_mapping = {
        '年月日時': 'DateTime',
        '気温(℃)': 'Temperature',
        '日照時間(時間)': 'SunlightHours',
        '風速(m/s)': 'WindSpeed',
        '日射量(MJ/㎡)': 'SolarRadiation'
    }
    
    # Rename the columns and drop NaN values
    raw_data.rename(columns=column_mapping, inplace=True)
    cleaned_data = raw_data[['DateTime', 'Temperature', 'SunlightHours', 'WindSpeed', 'SolarRadiation']].dropna()
    
    # Calculate Solar Power Output using the linear model
    cleaned_data['SolarPowerOutput'] = (
        alpha * cleaned_data['SolarRadiation'] +
        beta * cleaned_data['SunlightHours'] +
        gamma * cleaned_data['Temperature'] -
        delta * cleaned_data['WindSpeed']
    )
    
    # Calculate the total solar power output for the whole month
    total_solar_power_output = np.sum(cleaned_data['SolarPowerOutput'])
    
    return cleaned_data, total_solar_power_output

# Example usage
file_path = '/Users/jindaeun/Desktop/downloaded_filees.xlsx'  # Replace with the actual path to your Excel file
calculated_data, total_output = calculate_solar_power(file_path)
print(f"Total solar power output for the month: {total_output}")
