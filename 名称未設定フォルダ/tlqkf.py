import requests

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
    'stationNumList': '["s47662"]',
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
    'PHPSESSID': 'djhp41vibu4tidqh6lnh7q7rn5'
}

response = requests.post('https://www.data.jma.go.jp/risk/obsdl/show/table', headers=headers, data=data)

# 파일을 저장하기 위한 코드 (예: "downloaded_file.csv"라는 이름으로 저장)
with open("downloaded_file.csv", "wb") as f:
    f.write(response.content)
