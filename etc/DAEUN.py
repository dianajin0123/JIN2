import requests
import pandas as pd
import matplotlib.pyplot as plt
import chardet
from bs4 import BeautifulSoup

# Step 1: Visit the main page first to get PHPSESSID
initial_url = 'https://www.data.jma.go.jp/risk/obsdl/index.php'
session = requests.Session()  # Create a session object
session.get(initial_url)

# Step 2: Download the data
url = 'https://www.data.jma.go.jp/risk/obsdl/show/table'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8,ko;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'AWSALB=yAzov2iwdJzd+fSEkLHVe8uujqowey+7rAhiOKg7aLvdhNZqJYIk3rRAd8JsAdh3Uf6bCb4qSb0cb8PNB1MSmUVK1YcSGUlpa6VNua7Tftgak59EiXFfEcXCorir; AWSALBCORS=yAzov2iwdJzd+fSEkLHVe8uujqowey+7rAhiOKg7aLvdhNZqJYIk3rRAd8JsAdh3Uf6bCb4qSb0cb8PNB1MSmUVK1YcSGUlpa6VNua7Tftgak59EiXFfEcXCorir',
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
    'stationNumList': '["s47662"]',
    'aggrgPeriod': '9',
    'elementNumList': '[["401",""]]',
    'interAnnualFlag': '1',
    'ymdList': '["2023","2023","8","9","1","1"]',
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
    'PHPSESSID': 'pus54n113r381c80ab2trt5ia0'
}

response = session.post(url, headers=headers, data=data)

# Save as CSV file
if response.status_code == 200:
    with open('data.csv', 'wb') as f:
        f.write(response.content)
else:
    print(f'Failed to download CSV. Status Code: {response.status_code}')

# Load the CSV file
csv_path = 'data.csv'

# Detect the encoding
with open(csv_path, 'rb') as f:
    result = chardet.detect(f.read())
    
encoding_type = result['encoding']

df = pd.read_csv(csv_path, skiprows=3, encoding=encoding_type)

# Rename the columns for easier reference
df.columns = ['Timestamp', 'Sunlight Duration', 'Phenomenon Info', 'Quality Info', 'Homogeneous Number']

# Convert the 'Sunlight Duration' column to numeric values
df['Sunlight Duration'] = pd.to_numeric(df['Sunlight Duration'], errors='coerce')

# Drop rows where 'Sunlight Duration' is NaN
df = df.dropna(subset=['Sunlight Duration'])

# Given constants
installed_capacity = 100  # kWp
efficiency_coefficient = 0.7  # no unit
trading_price = 16  # 16円/kWh
operation_rate = 1

# Calculate the total power generation using the formula
total_power_generation = df['Sunlight Duration'].sum() * installed_capacity * efficiency_coefficient * operation_rate

# Calculate the expected income
expected_income = total_power_generation * trading_price

# Display the results
print(f'Total power generation: {total_power_generation} kWh')
print(f'Expected income: {expected_income} 円')

# Calculate the initial investment cost/ 1kW = 275,000 Yen
initial_investment = 2750000 * installed_capacity  # in Yen

# Calculate the Surface Profit
surface_profit = (expected_income/ initial_investment) * 100  # in percentage

# Display the Surface Profit in percentage
print(f'Surface Profit: {surface_profit} %')


# Step 1: Load and Preprocess the CSV File
data_df = pd.read_csv('data.csv', encoding='cp932', skiprows=[0, 2], header=1)
column_mapping = {
    'Unnamed: 0': 'Datetime',
    'Unnamed: 1': 'Sunshine_Duration',
    '現象なし情報': 'No_Phenomenon_Info',
    '品質情報': 'Quality_Info',
    '均質番号': 'Homogeneity_Number'
}
data_df = data_df.rename(columns=column_mapping)

# Step 2: Set Variables
installed_capacity = 100  # in kW
efficiency_coefficient = 0.7  # unitless
trading_price = 16  # in 円/kWh

# Step 3: Calculate Daily Power Generation and Expected Income
data_df['Daily_Power_Generation'] = data_df['Sunshine_Duration'] * installed_capacity * efficiency_coefficient
data_df['Daily_Expected_Income'] = data_df['Daily_Power_Generation'] * trading_price

# Extract date for grouping
data_df['Date'] = data_df['Datetime'].apply(lambda x: x.split()[0])

# Group data by date and sum up the daily values
grouped_data = data_df.groupby('Date').sum()

# Step 4: Create Graphs
plt.figure(figsize=(15, 8))

# Plot for Daily Power Generation
plt.subplot(2, 1, 1)
plt.plot(grouped_data.index, grouped_data['Daily_Power_Generation'], label='Daily Power Generation (kWh)', color='b')
plt.title('Daily Power Generation and Expected Income')
plt.xlabel('Date')
plt.ylabel('Power Generation (kWh)')
plt.legend()

# Plot for Daily Expected Income
plt.subplot(2, 1, 2)
plt.plot(grouped_data.index, grouped_data['Daily_Expected_Income'], label='Daily Expected Income (円)', color='r')
plt.xlabel('Date')
plt.ylabel('Expected Income (円)')
plt.legend()

plt.tight_layout()
plt.show()


