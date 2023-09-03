import requests
import pandas as pd

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
    'ymdList': '["2023","2023","6","7","31","31"]',
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
    'PHPSESSID': '7p0cskrbtjd0uaovqgsh869h41'
}

response = requests.post(url, headers=headers, data=data)

# Save as CSV file
if response.status_code == 200:
    with open('data.csv', 'wb') as f:
        f.write(response.content)
else:
    print(f'Failed to download CSV. Status Code: {response.status_code}')

# Load the CSV file
csv_path = 'data.csv'  # Replace with your file path
df = pd.read_csv(csv_path, skiprows=3, encoding='cp932')

# Rename the columns for easier reference
df.columns = ['Timestamp', 'Sunlight Duration', 'Phenomenon Info', 'Quality Info', 'Homogeneous Number']

# Convert the 'Sunlight Duration' column to numeric values
df['Sunlight Duration'] = pd.to_numeric(df['Sunlight Duration'], errors='coerce')

# Drop rows where 'Sunlight Duration' is NaN
df = df.dropna(subset=['Sunlight Duration'])

# Given constants
installed_capacity = 100  # kWp
efficiency_coefficient = 0.7  # no unit

# Calculate the total power generation using the formula
total_power_generation = df['Sunlight Duration'].sum() * installed_capacity * efficiency_coefficient

# Display the total power generation in kWh
print(f'Total power generation: {total_power_generation} kWh')

# Calculate the total power generation using the formula
total_power_generation = df['Sunlight Duration'].sum() * installed_capacity * efficiency_coefficient

# Given constant for the trading price
trading_price = 16  # 16円/kWh

# Calculate the expected income using the formula: total_power_generation * trading_price
expected_income = total_power_generation * trading_price

# Display the expected income in 円 (Yen)
print(f'Expected income: {expected_income} 円')

# Calculate the initial investment cost: 1 kW costs 2,750,000 Yen and we have 100 kW installed
initial_investment = 2750000 * installed_capacity  # in Yen

# Calculate the Surface Profit
surface_profit = (expected_income*12 / initial_investment) * 100  # in percentage

# Display the Surface Profit in percentage
print(f'Surface Profit: {surface_profit} %')

