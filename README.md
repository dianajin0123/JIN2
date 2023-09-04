# 일본 기상청 태양광 분석 프로젝트

![Contributors](https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge)
![MIT License](https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/daeunjin/)


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <ul>
        <li><a href="#Python-Library">Python Library</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#Sample-Data-and-Web-Scraping-Caution">Sample Data and Web Scraping Caution</a></li>
        <ul>
        <li><a href="#Example-Output-Using-Sample-Data">Example Output Using Sample Data</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <ul>
        <li><a href="#Variables and Assumptions">Variables and Assumptions</a></li>   
        <li><a href="#Papers and References">Papers and References</a></li>   
    </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#Data Source and Acknowledgment">Data Source and Acknowledgment</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


이 파이썬 스크립트는 일본 기상청의 웹사이트에서 일조 시간 데이터를 다운로드, 처리, 분석하며, 일조 데이터를 기반으로 태양광 패널 설치로 얻을 수 있는 연간 발전량,수익,표면이익을 계산하고 다양한 측면의 데이터를 그래프로 시각화합니다.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

[![Python][Python.js]][Python-url]
![Visual Studio Code][Visual Studio Code.js]

#### Python Library

![Requests][Requests.js]
![Pandas][Pandas.js]
![Matplotlib][Matplotlib.js]
![Chardet][Chardet.js]
![IO][IO.js]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

Python 3.11.4

Library: Requests, Pandas, Matplotlib, Chardet, IO 


### Installation

1. 터미널을 열고 다음 명령어를 실행하여 필요한 라이브러리를 설치합니다.
   ```bash
   pip install requests pandas matplotlib chardet
   ```

    이 명령어는 다음 라이브러리를 설치합니다:
    - `requests`: HTTP 요청을 처리하기 위한 라이브러리
    - `pandas`: 데이터 분석 및 조작을 위한 라이브러리
    - `matplotlib`: 데이터 시각화를 위한 라이브러리
    - `chardet`: 문자 인코딩 탐지를 위한 라이브러리

2. `Solar_Data_Analysis_Tool.py` 파일을 로컬 컴퓨터에 다운로드합니다.
   
4. 터미널을 열고 파일이 저장된 디렉토리로 이동합니다.
   
6. 다음 명령어를 실행하여 스크립트를 실행합니다.
   ```bash
   python Solar_Data_Analysis_Tool.py
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Sample Data and Web Scraping Caution

웹 스크래핑의 잠재적인 법적 및 윤리적 문제로 인해, 이 프로그램의 기능을 테스트하고 이해하기 위한 샘플 CSV 파일을 제공합니다. 샘플 데이터를 사용하려면 다음 단계를 따르십시오.

1. [이 위치](샘플 파일 위치)에서 `sample.csv`를 다운로드합니다.
2. 이 파일을 프로그램과 동일한 디렉토리에 배치합니다.
3. [사용법](#사용법) 섹션에 설명된대로 프로그램을 실행합니다.

이 프로그램은 원래 웹에서 데이터를 스크래핑하기 위해 설계되었습니다. 이 기능을 사용하려면 해당 웹사이트의 이용 약관을 준수하고 있는지 확인하십시오.












































<!-- MARKDOWN LINKS & IMAGES -->

[Python.js]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
[Visual Studio Code.js]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[Requests.js]: https://img.shields.io/badge/Requests-FFFF00?logoColor=white
[Pandas.js]: https://img.shields.io/badge/Pandas-000000?logoColor=white
[Matplotlib.js]: https://img.shields.io/badge/Matplotlib-00008B?logoColor=white
[Chardet.js]: https://img.shields.io/badge/Chardet-006400?logoColor=white
[IO.js]: https://img.shields.io/badge/IO-483D8B?logoColor=white






