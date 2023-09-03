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
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
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





2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>










































<!-- MARKDOWN LINKS & IMAGES -->

[Python.js]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
[Visual Studio Code.js]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[Requests.js]: https://img.shields.io/badge/Requests-FFFF00?logoColor=white
[Pandas.js]: https://img.shields.io/badge/Pandas-000000?logoColor=white
[Matplotlib.js]: https://img.shields.io/badge/Matplotlib-00008B?logoColor=white
[Chardet.js]: https://img.shields.io/badge/Chardet-006400?logoColor=white
[IO.js]: https://img.shields.io/badge/IO-483D8B?logoColor=white






