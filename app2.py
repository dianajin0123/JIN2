import requests
import pandas as pd
import numpy as np
import chardet
import matplotlib.pyplot as plt
        
# Downloading CSV from website
def download_csv():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8,ko;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'AWSALB=DAoAf7QYHn4LeaVijqdRn0xcToO/cBRTyK6AxMJc0/869cace6ZNHaEfRydo9aJ+I2j7qu4pkc7THDgC3y7HeMQ6tsXVPpWDbKGXxv3PgrW1taS/IxrxanOmAt4R; AWSALBCORS=DAoAf7QYHn4LeaVijqdRn0xcToO/cBRTyK6AxMJc0/869cace6ZNHaEfRydo9aJ+I2j7qu4pkc7THDgC3y7HeMQ6tsXVPpWDbKGXxv3PgrW1taS/IxrxanOmAt4R',
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
        'stationNumList': '["s47670"]',
        'aggrgPeriod': '9',
        'elementNumList': '[["401",""]]',
        'interAnnualFlag': '1',
        'ymdList': '["2023","2023","7","8","31","31"]',
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
        'PHPSESSID': 'jusad0u49007r9dl74e116m9f1'
    }
    
    response = requests.post('https://www.data.jma.go.jp/risk/obsdl/show/table', headers=headers, data=data)
    return response.content


# Function to calculate solar power
def calculate_solar_power(file_path, alpha=1.2, beta=0.8, gamma=0.5, delta=0.2):
    # Load CSV data
    try:
        raw_data = pd.read_csv(file_path, encoding='cp932', header=[2, 3])
    except Exception as e:
        return f"Unable to read the file. Error: {e}"
    
    # Directly use the multi-level column names for selection
    cleaned_data = raw_data[
        [('年月日時', 'Unnamed: 0_level_1'), 
         ('気温(℃)', 'Unnamed: 1_level_1'), 
         ('日照時間(時間)', 'Unnamed: 4_level_1'), 
         ('風速(m/s)', 'Unnamed: 11_level_1'), 
         ('日射量(MJ/㎡)', 'Unnamed: 8_level_1')]
    ].dropna()
    
    # Calculate SolarPowerOutput
    cleaned_data['SolarPowerOutput'] = (
        alpha * cleaned_data[('日射量(MJ/㎡)', 'Unnamed: 8_level_1')] +
        beta * cleaned_data[('日照時間(時間)', 'Unnamed: 4_level_1')] +
        gamma * cleaned_data[('気温(℃)', 'Unnamed: 1_level_1')] -
        delta * cleaned_data[('風速(m/s)', 'Unnamed: 11_level_1')]
    )
    
    # Calculate the total solar power output
    total_solar_power_output = np.sum(cleaned_data['SolarPowerOutput'])
    return cleaned_data, total_solar_power_output


def visualize_data():
    # Read the CSV data using the previously identified encoding and multi-level header
    data = pd.read_csv('downloaded_file.csv', encoding='cp932', header=[2, 3])

    # Calculate the SolarPowerOutput using the formula from app2.py
    data['SolarPowerOutput'] = (
        1.2 * data[('日射量(MJ/㎡)', 'Unnamed: 8_level_1')] +
        0.8 * data[('日照時間(時間)', 'Unnamed: 4_level_1')] +
        0.5 * data[('気温(℃)', 'Unnamed: 1_level_1')] -
        0.2 * data[('風速(m/s)', 'Unnamed: 11_level_1')]
    )

    # Plotting the relationships
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Relationships between Variables and SolarPowerOutput', fontsize=16)

    # SolarRadiation vs SolarPowerOutput
    axes[0, 0].scatter(data[('日射量(MJ/㎡)', 'Unnamed: 8_level_1')], data['SolarPowerOutput'], alpha=0.5)
    axes[0, 0].set_title('SolarRadiation vs SolarPowerOutput')
    axes[0, 0].set_xlabel('SolarRadiation (MJ/㎡)')
    axes[0, 0].set_ylabel('SolarPowerOutput')

    # SunlightHours vs SolarPowerOutput
    axes[0, 1].scatter(data[('日照時間(時間)', 'Unnamed: 4_level_1')], data['SolarPowerOutput'], alpha=0.5, color='orange')
    axes[0, 1].set_title('SunlightHours vs SolarPowerOutput')
    axes[0, 1].set_xlabel('SunlightHours (hours)')
    axes[0, 1].set_ylabel('SolarPowerOutput')

    # Temperature vs SolarPowerOutput
    axes[1, 0].scatter(data[('気温(℃)', 'Unnamed: 1_level_1')], data['SolarPowerOutput'], alpha=0.5, color='green')
    axes[1, 0].set_title('Temperature vs SolarPowerOutput')
    axes[1, 0].set_xlabel('Temperature (℃)')
    axes[1, 0].set_ylabel('SolarPowerOutput')

    # WindSpeed vs SolarPowerOutput
    axes[1, 1].scatter(data[('風速(m/s)', 'Unnamed: 11_level_1')], data['SolarPowerOutput'], alpha=0.5, color='red')
    axes[1, 1].set_title('WindSpeed vs SolarPowerOutput')
    axes[1, 1].set_xlabel('WindSpeed (m/s)')
    axes[1, 1].set_ylabel('SolarPowerOutput')

    plt.tight_layout()
    plt.subplots_adjust(top=0.90)
    plt.show()
# Main Program
if __name__ == "__main__":
    file_path = download_csv()
    # calculated_data, total_output = calculate_solar_power(file_path)
    visualize_data()
    # print(f"Total solar power output for the month: {total_output}")
    
    
