
import pandas as pd

def process_solar_data(filename):
    # Load the data
    data = pd.read_csv(filename, encoding='CP932', skiprows=1, header=1)
    
    # Clean the data by removing the next two rows which contain additional header information
    data_cleaned = data.iloc[2:].reset_index(drop=True)
    data_cleaned.columns = data.iloc[0]
    
    # Create a new DataFrame for selected data
    data_selected = pd.DataFrame()
    data_selected['Date_Time'] = data_cleaned.iloc[:, 0]
    data_selected['Irradiance'] = pd.to_numeric(data_cleaned.iloc[:, 12], errors='coerce')
    
    # Constants
    PANEL_EFFICIENCY = 0.175  # 17.5%
    PANEL_SIZE_KW = 1  # 1KW
    
    # Calculate power output for each hour
    data_selected["Power_Output_Wh"] = data_selected["Irradiance"] * PANEL_EFFICIENCY * PANEL_SIZE_KW * 1000
    
    # Calculate the total power output for the month
    total_power_output_Wh = data_selected["Power_Output_Wh"].sum()
    
    return total_power_output_Wh

if __name__ == "__main__":
    filename = "data.csv"  # Adjust the filename/path as needed
    result = process_solar_data_refined(filename)
    print(f"Total power output for the month with a 1KW panel: {result} Wh or {result/1000:.2f} kWh")
