# Japan Meteorological Agency Solar Power Analysis Project

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
        <li><a href="#installation">Installation</a></li>
        <li><a href="#Sample-Data-and-Web-Scraping-Caution">Sample Data and Web Scraping Caution</a></li>
        <li><a href="#Example-Output-Using-Sample-Data">Example Output Using Sample Data</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <ul>
        <li><a href="#Code-Overview">Code Overview</a></li>   
        <li><a href="#Variables-and-Assumptions">Variables and Assumptions</a></li>   
        <li><a href="#Papers-and-References">Papers and References</a></li>   
    </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#Data-Source-and-Acknowledgment">Data Source and Acknowledgment</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This Python script downloads, processes, and analyzes sunlight duration data from the Japan Meteorological Agency's website. Based on the sunlight data, it calculates the annual power generation, income, and surface profit that can be obtained by installing solar panels and visualizes various aspects of the data through graphs.


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


### Installation

>#### Prerequisites
  Python 3.11.4

  
  Library: Requests, Pandas, Matplotlib, Chardet, IO 

  ***


1. Open the terminal and run the following command to install the necessary libraries:
   ```bash
   pip install requests pandas matplotlib chardet
   ```

    This command installs the following libraries:
    - `requests`: A library for handling HTTP requests
    - `pandas`: A library for data analysis and manipulation
    - `matplotlib`: A library for data visualization
    - `chardet`: A library for character encoding detection

2. Download the Solar_Data_Analysis_Tool.py file to your local computer.
   
4. Open a terminal and navigate to the directory where the file is saved.
   
6. Run the following command to execute the script:
   ```bash
   python Solar_Data_Analysis_Tool.py
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Sample Data and Web Scraping Caution

Due to the potential legal and ethical issues of web scraping, a sample CSV file is provided for you to test and understand the functionality of the program. To use the sample data, follow these steps:

1. Download the `data_sample.csv` from [this location](data_sample.csv).
2. Place it in the same directory as the program.
3. Run the program as described in the [Installation](#Installation) section.

Please ensure you are in compliance with the terms of use of the website if you intend to use the web scraping feature.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Example Output Using Sample Data

#### Expected Outputs
Using the provided sample CSV file, the program will show the following outputs:

```bash
1 Year - Total power generation: 160118.0 kWh
1 Year - Expected income: 2561888.0 円
1 Year - Surface Profit: 9.316 %
```

1. Total solar power generation for one year
2. Expected income for one year
3. Surface profit rate for one year


#### Graphical Outputs

Along with text-based results, the program also generates graphs.

1. Daily Average Sunlight Duration: This graph shows the daily average duration of sunlight. It can be seen that the duration varies.
2. Monthly Total Sunlight Duration: This graph shows the total duration of sunlight for each month, allowing for easy understanding of sunlight duration in each month. 
3. Sunlight Duration Distribution: This histogram shows the distribution of sunlight durations. Most durations are close to 0, with very few outliers.
4. Monthly Average Sunlight Duration: This graph shows the average duration of sunlight per month, allowing for easy understanding of monthly variations.

> **Note**: You may see related warning messages while plotting the graphs. These are generally safe to ignore.

#### Sample Data Information
 
The sample data is based on Yokohama city's sunlight duration data from September 1, 2022, to September 1, 2023, provided by the Japan Meteorological Agency.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Usage

### Code Overview
This Python code aims to download and analyze solar power data from the Japan Meteorological Agency's website. The code consists of three main steps: data download, analysis, and visualization.

### Variables and Assumptions

#### Variables
- `installed_capacity`: Installed solar panel capacity in kWh
- `operating_rate `: The percentage of actual power output compared to the maximum possible output in percentage (%)
- `efficiency_coefficient`: Coefficient indicating the efficiency of the solar panel
- `trading_price`: Trading price of solar power in yen (円)
- `initial_investment`: Initial investment amount in yen (円)
- `df_1_year`: Dataframe containing data for one year
- `monthly_avg_sunlight`: Monthly average sunlight duration
- `daily_avg_sunlight`: Daily average sunlight duration
- `monthly_total_sunlight`: Monthly total sunlight duration
- `total_power_generation_1_year`: Total power generation in one year in kWh
- `expected_income_1_year`: Expected income in one year in yen (円)
- `surface_profit_1_year`: Surface profit rate in one year in percentage (%)

#### Assumptions

### Formula Descriptions

Total Power Generation Calculation

```bash
annual_power_generation = annual_sunlight_duration_sum × installed_capacity × operating_rate × efficiency_coefficient
```








### Papers and References
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

DAEUN JIN - dianajin0123@gmail.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

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






