import requests
import pandas as pd
import matplotlib.pyplot as plt
import chardet

def download_data(ymdList, filename):
    # Initialize session and visit main page
    initial_url = 'https://www.data.jma.go.jp/risk/obsdl/index.php'
    session = requests.Session()
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
        'ymdList': '[]',
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
        'PHPSESSID': 'st2ejau4pmgdrrhd9i0phsmuc2'
    }

    data['ymdList'] = ymdList  # Update ymdList
    
    response = session.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print(f'Failed to download CSV. Status Code: {response.status_code}')
    
    with open(filename, 'rb') as f:
        result = chardet.detect(f.read())
    encoding_type = result['encoding']
    
    df = pd.read_csv(filename, skiprows=3, encoding=encoding_type)
    df.columns = ['Timestamp', 'Sunlight Duration', 'Phenomenon Info', 'Quality Info', 'Homogeneous Number']
    df['Sunlight Duration'] = pd.to_numeric(df['Sunlight Duration'], errors='coerce')
    df = df.dropna(subset=['Sunlight Duration'])
    return df

# Constants
installed_capacity = 100  # kWp
efficiency_coefficient = 0.7  # no unit
trading_price = 16  # 16円/kWh
initial_investment = 275000 * installed_capacity  # 1 kW = 275,000 Yen

# Download and analyze 1-month data
df_1_month = download_data('["2023","2023","8","9","1","1"]', 'data_1_month.csv')
total_power_generation_1_month = df_1_month['Sunlight Duration'].sum() * installed_capacity * efficiency_coefficient
expected_income_1_month = total_power_generation_1_month * trading_price


# Download and analyze 1-year data
df_1_year = download_data('["2022","2023","1","12","1","31"]', 'data_1_year.csv')
total_power_generation_1_year = df_1_year['Sunlight Duration'].sum() * installed_capacity * efficiency_coefficient
expected_income_1_year = total_power_generation_1_year * trading_price
surface_profit_1_year = (expected_income_1_year / initial_investment) * 100  # in percentage

# Display results
print(f'1 Month - Total power generation: {total_power_generation_1_month} kWh')
print(f'1 Month - Expected income: {expected_income_1_month} 円')

print(f'1 Year - Total power generation: {total_power_generation_1_year} kWh')
print(f'1 Year - Expected income: {expected_income_1_year} 円')
print(f'1 Year - Surface Profit: {surface_profit_1_year} %')

# Graphs
plt.figure(figsize=(20, 10))

# Graph for 1 Month
plt.subplot(2, 2, 1)
df_1_month['Sunlight Duration'].plot(kind='line', title='1 Month Sunlight Duration')
plt.xlabel('Time')
plt.ylabel('Sunlight Duration (hours)')

# Graph for 1 Year
plt.subplot(2, 2, 2)
df_1_year['Sunlight Duration'].plot(kind='line', title='1 Year Sunlight Duration')
plt.xlabel('Time')
plt.ylabel('Sunlight Duration (hours)')

plt.show()
