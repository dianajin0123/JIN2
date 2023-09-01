import requests
import pandas as pd
import numpy as np

# Downloading CSV from website
def download_csv():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8,ko;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'AWSALB=B6yLNL9jC9yncydsM5q+373KsxiPKNDlpmuCuWqT7FEKVq96h0all0sBWhbUJC6Nsobxo6Q4b/jadOD+s1QVGVIXLyeJa8WS+gW96nBBwgxPvTKBuQLxgoKF9jIv; AWSALBCORS=B6yLNL9jC9yncydsM5q+373KsxiPKNDlpmuCuWqT7FEKVq96h0all0sBWhbUJC6Nsobxo6Q4b/jadOD+s1QVGVIXLyeJa8WS+gW96nBBwgxPvTKBuQLxgoKF9jIv',
        'Origin': 'https://www.data.jma.go.jp',
        'Referer': 'https://www.data.jma.go.jp/risk/obsdl/index.php',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }
    data = {
        'stationNumList': '["a0390"]',
        'aggrgPeriod': '9',
        'elementNumList': '[["201",""],["401",""],["610",""],["301",""]]',
        'interAnnualFlag': '1',
        'ymdList': '["2023","2023","7","8","29","29"]',
        'optionNumList': '[]',
        'downloadFlag': 'true',
        'rmkFlag': '1',
        'disconnectFlag': '1',
        'youbiFlag': '0',
        'fukenFlag': '0',
        'kijiFlag': '0',
        'huukouFlag': '0',
        'csvFlag': '1',
        'jikantaiFlag': '0',
        'jikantaiList': '[1,24]',
        'ymdLiteral': '1',
        'PHPSESSID': '4u5bbd0vahievgjmis04695vf4'
    }
    
    response = requests.post('https://www.data.jma.go.jp/risk/obsdl/show/table', headers=headers, data=data)
    csv_file_path = "downloaded_file.csv"
    with open(csv_file_path, "wb") as f:
        f.write(response.content)
    return csv_file_path

# Keep only selected columns and remove the rest
def keep_selected_columns(raw_data):
    columns_to_keep = ['Unnamed: 1', 'Unnamed: 4', 'Unnamed: 8', 'Unnamed: 11']
    cleaned_data = raw_data[columns_to_keep]
    cleaned_data = cleaned_data.dropna()
    return cleaned_data

# Function to calculate solar power
def calculate_solar_power_updated(cleaned_data, alpha=1.2, beta=0.8, gamma=0.5, delta=0.2):
    cleaned_data['SolarPowerOutput'] = (
        alpha * cleaned_data['Unnamed: 4'] +  # SolarRadiation
        beta * cleaned_data['Unnamed: 8'] +  # SunlightHours
        gamma * cleaned_data['Unnamed: 1'] -  # Temperature
        delta * cleaned_data['Unnamed: 11']   # WindSpeed
    )
    total_solar_power_output = np.sum(cleaned_data['SolarPowerOutput'])
    return cleaned_data, total_solar_power_output

# Main Program
if __name__ == "__main__":
    file_path = download_csv()
    
    # Read the raw data
    try:
        raw_data = pd.read_csv(file_path, skiprows=5, encoding='ISO-8859-1')
    except Exception as e:
        print(f"Unable to read the file. Error: {e}")
    
    # Clean the data by keeping only the selected columns
    cleaned_data = keep_selected_columns(raw_data)
    
    # Calculate solar power and get the total output using the updated formula
    calculated_data, total_output = calculate_solar_power_updated(cleaned_data)
    
    print(f"Total solar power output for the month: {total_output}")
