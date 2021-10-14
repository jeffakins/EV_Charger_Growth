# Individual Project
![EV Charging Station](https://i.insider.com/6042a8ac44d8e300117b9655?width=1200&format=jpeg)

# Current State of the Electric Vehicle (EV) Charging Network within the United States
By Jeff Akins

## Project Goal: 
The goal of this project is to examine the current state of the EV charging network within the United States and to project the growth of the EV charging network through 2025. 
### Additional Goals:

## Executive Summary:

## How to Reproduce:
- You will need a copy of the 'alternative fuel stations 2021 csv' file, which can be downloaded from data.gov [here](https://catalog.data.gov/dataset/alternative-fueling-station-locations-422f2/resource/341957d8-daf6-4a38-ab1d-8ec1bc21cfb9)
- Clone my github repo
- Run the 'individual_prject' notebook
- I hope that you find value in your exploration!


## Pipeline 

### Plan:
[Trello Board](https://trello.com/b/nCuPtuTu/individual-project-plan)

### Acquire:
You can find the original dataset file [here](https://catalog.data.gov/dataset/alternative-fueling-station-locations-422f2/resource/341957d8-daf6-4a38-ab1d-8ec1bc21cfb9) on data.gov
I downloaded the CSV version of the file with the name: 'alternative-fuel-stations-2021-csv-3.csv'

### Data Prep:
The following steps were taken to clean the data:

- Dropped all rows that were not "electric" charging stations
- Dropped all columns with over 1000 null values
- Dropped an additional 12 columns that would not be used for this project
- Changed the pricing column to only include 'free' or 'cost' in the rows
- Filled the EV connector types nulls with the most common connector type of 'J1772'
- Fill EV Network nulls with most common 'non network' label
- Added values for 2 missing longitude values based on city location
- Renamed columns for ease of referencing and use with pandas
- Converted date columns to pandas datetime type
- Added a column for year that the charging station was opened
- Converted all 'count' columns into 'int' type and filled nulls with 0

Here is a summary of the data after I completed the cleaning process:

#### Data dictionary
|Index | Column Name | Description | Row Count | Dtype|
|---|---|---|---|---|
| 0  | fuel_code         | Type of Fuel i.e. 'Electric'                         | 47006 non-null | object       |
| 1  | station_name      | Name of station                                      | 47006 non-null | object       |
| 2  | address           | Address                                              | 47006 non-null | object       |
| 3  | city              | City                                                 | 47006 non-null | object       |
| 4  | state             | State                                                | 47006 non-null | object       |
| 5  | zip               | Zip Code                                             | 47006 non-null | object       |
| 6  | group_access_code | Whether public or private                            | 47006 non-null | object       |
| 7  | level1_evse_num   | Count of level 1 chargers                            | 47006 non-null | int64        |
| 8  | level2_evse_num   | Count of level 2 chargers                            | 47006 non-null | int64        |
| 9  | ev_dc_fast_count  | Count of DC fast chargers                            | 47006 non-null | int64        |
| 10 | ev_network        | Whether the charging stations is part of a network   | 47006 non-null | object       |
| 11 | lat               | Latitude location                                    | 47006 non-null | float64      |
| 12 | long              | Longitude location                                   | 47006 non-null | float64      |
| 13 | update_date       | Date stations information was updated                | 47006 non-null | datetime64   |
| 14 | open_date         | Date station was opened                              | 47006 non-null | datetime64   |
| 15 | connector_type    | Type of charging connector                           | 47006 non-null | object       |
| 16 | pricing           | Whether Free or Costs to charge                      | 47006 non-null | object       |
| 17 | year_opened       | Year the station opened                              | 47006 non-null | int64        |


### Explore:

### Model & Evaluate:

## Conclusion: