import requests
import pandas as pd
import chardet
from solar_data_processing import process_solar_data
url = "https://www.data.jma.go.jp/risk/obsdl/show/table"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "AWSALB=ch2dl6t4vlsekinkjK4z/xBwgRJnoWSPnGwwbWnxMOO535OpYKLre+fUeQdXj+5rLqfaXi9T6E78Ovw0BYIwUznfyYnOLOq6lmZ8s97J8OL8UIzPok8PD66qk6nS; AWSALBCORS=ch2dl6t4vlsekinkjK4z/xBwgRJnoWSPnGwwbWnxMOO535OpYKLre+fUeQdXj+5rLqfaXi9T6E78Ovw0BYIwUznfyYnOLOq6lmZ8s97J8OL8UIzPok8PD66qk6nS",
    "DNT": "1",
    "Origin": "https://www.data.jma.go.jp",
    "Referer": "https://www.data.jma.go.jp/risk/obsdl/index.php",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

data = {
    "stationNumList": '["s47662"]',
    "aggrgPeriod": "9",
    "elementNumList": '[["201",""],["401",""],["301",""],["610",""]]',
    "interAnnualFlag": "1",
    "ymdList": '["2023","2023","7","8","29","29"]',
    "optionNumList": "[]",
    "downloadFlag": "true",
    "rmkFlag": "1",
    "disconnectFlag": "1",
    "youbiFlag": "0",
    "fukenFlag": "0",
    "kijiFlag": "0",
    "huukouFlag": "0",
    "csvFlag": "1",
    "jikantaiFlag": "0",
    "jikantaiList": "[1,24]",
    "ymdLiteral": "1",
    "PHPSESSID": "hu48c3ciggqcndhii5qoek3im0"
}

response = requests.post(url, headers=headers, data=data)

def detect_encoding(filename):
    bytes_to_check = 10000  # Number of bytes to use for encoding detection
    
    with open(filename, 'rb') as f:
        # Read the first part of the file
        first_part = f.read(bytes_to_check)
        
        # Move to the middle of the file and read
        f.seek(len(f.read()) // 2)
        mid_part = f.read(bytes_to_check)
        
        # Detect encoding for both parts
        first_part_detection = chardet.detect(first_part)
        mid_part_detection = chardet.detect(mid_part)
        
        # If the mid_part detection has a higher confidence, return that. Otherwise, return the first part's detection
        if mid_part_detection['confidence'] > first_part_detection['confidence']:
            return mid_part_detection['encoding']
        else:
            return first_part_detection['encoding']

# def convert_csv_to_xlsx():
#     # Detect the encoding of the CSV file
#     encoding = detect_encoding('data.csv')
    
#     # Load the CSV with detected encoding
#     data = pd.read_csv('data.csv', encoding=encoding)
    
#     # Save the data to an Excel file
#     data.to_excel('data.xlsx', index=False)
    
# 응답 내용을 CSV 파일로 저장
with open('data.csv', 'wb') as file:
    file.write(response.content)
    
# convert_csv_to_xlsx()

if __name__ == "__main__":
    filename = "data.csv"
    result = process_solar_data(filename)
    print(f"Total power output for the month with a 1KW panel: {result} Wh or {result/1000:.2f} kWh")