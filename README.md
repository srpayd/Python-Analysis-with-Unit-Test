# Bitly Coding Challenge 

This project aims to accomplish the Bitly Coding Challenge.


## Table of Contents

- [Introduction](#introduction)
- [Data](#introduction)
- [Problem](#introduction)
- [Usage](#usage)
- [Solution](#functionality)
- [Testing](#testing)
- [Contact](#contact)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Introduction

This project involves analyzing data files to solve the specific problem outlined in the challenge description.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Data

The challenge uses _'encodes.csv'_ and _'decodes.json',_ representative of data encountered in Bitly's daily operations:

- 'encodes.csv' contains shortened link information.
- 'decodes.json' includes raw bitlink clicks.

These datasets are utilized to address the problem statement.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Problem 

The goal is to calculate the number of clicks from 2021 for each record in the 'encodes.csv' dataset.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

### Pre-requisites

- Python 3 installed

### Steps to Run the Code

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/srpayd/bitly_challenge.git

2. **Navigate to the Project Directory:**
   ```bash
   cd bitly-coding-challenge

3. Install Dependencies (if any):
   Python's core libraries, such as dictionaries and lists, were utilized throughout the project. No external or third-party libraries were installed or employed.

4. Run the code
   Replace 'encodes.csv' and 'decodes.json' with your file paths.
   ```bash
   python solution.py 
   python test_solution.py 

1. Read _'encodes.csv'_ file: Create a dictionary using _'encodes.csv'_ where keys are long URLs, and values are corresponding shortened URLs.
2. Read _'decodes.json'_ file: Parse _'decodes.json'_ and filter records from 2021.
3. Match shortened URLs with records from 2021: Compare the bitlinks in the filtered records from 2021 with the dictionary created from _'encodes.csv'_ to identify corresponding long URLs. Finally, count clicks for each long URL: Tally the number of clicks from 2021 for each long URL.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Solution

### Overview

The provided code addresses the challenge by calculating the 2021 click counts for each record in 'encodes.csv' using data from 'decodes.json'.


### Key Features
1. **Reading CSV and JSON Files:**
   Reads 'encodes.csv' and 'decodes.json' to create dictionaries of shortened links and bitlink clicks.

2. **Data Processing:**
   Filters 2021 records in 'decodes.json' and matches bitlinks to corresponding long URLs in 'encodes.csv'.

3. **Click Count Calculation:**
   Counts 2021 clicks in descending order for each record in 'encodes.csv' by tallying matching records from 'decodes.json'.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Testing

### Unit Tests Overview

The project includes a test suite comprising three unit tests to validate specific functionalities within the codebase.

### Unit Test Descriptions

#### 1. `test_read_encode_csv`
- **Purpose:** This test validates the `read_encode_csv` function's behavior by checking if it correctly reads and parses the 'encodes.csv' file, creating a dictionary of encoded URLs.
- **Assertions:**
  - Ensures that the function returns a dictionary.
  - Verifies that the dictionary contains the expected number of entries (6 in this case).

#### 2. `test_read_decode_json`
- **Purpose:** Validates the `read_decode_json` function's behavior by verifying its ability to read and parse the 'decodes.json' file, creating a list of decoded click data.
- **Assertions:**
  - Confirms that the function returns a list.
  - Checks if the list contains the expected number of records (10,000 in this case).

#### 3. `test_filter_and_count_2021_clicks`
- **Purpose:** This test validates the `filter_and_count_2021_clicks` function's functionality by testing its ability to filter and count clicks from 2021 for each record in the 'encodes.csv' dataset.
- **Assertions:**
  - Ensures that the function returns a dictionary.
  - Verifies that the resulting dictionary contains the expected number of entries (6).
  - Tests if the click count for each record in the dictionary is greater than zero.

### Running the Unit Tests

To run the unit tests:
1. Navigate to the project directory in the terminal.
2. Execute the following command:
   ```bash
   python -m unittest test_solution.py

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Serap Aydogdu - [linkedin](https://www.linkedin.com/in/srpayd/) - 34serapaydogdu@gmail.com

Project Link: [https://github.com/srpayd/bitly_challenge](https://github.com/srpayd/bitly_challenge)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

