# Individual Project
![EV Charging Station](https://i.insider.com/6042a8ac44d8e300117b9655?width=1200&format=jpeg)

# Current State of the Electric Vehicle (EV) Charging Network within the United States
By Jeff Akins

## Project Goal: 
The goal of this project is to examine the current state of the EV charging network within the United States and to project the growth of the EV charging network through 2025. 

## Executive Summary:
Based on the past rate of adding new EV charging stations within the US, and utilizing the Holt-Winters Exponential Smoothing Model, I forecasted that approximately 37,968 new EV chargers will be added to the network over the next two years.

### How to Reproduce:
- You will need a copy of the 'alternative fuel stations 2021 csv' file, which can be downloaded from data.gov [here](https://catalog.data.gov/dataset/alternative-fueling-station-locations-422f2/resource/341957d8-daf6-4a38-ab1d-8ec1bc21cfb9)
- Clone my github repo
- Run the 'individual_project' notebook


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
- Replaced 'Public w/descriptor' with just 'Public' in group_access_code column
- Replaced 'Private w/descriptor' with just 'Private' in group_access_code column
- Dropped stations (rows) that are labeled as 'planned' and 'not yet accessible' in the group_access_code column

Here is a summary of the data after I completed the cleaning process:

#### Data dictionary
|Index | Column Name | Description | Row Count | Dtype|
|---|---|---|---|---|
| 0  | fuel_code              | Type of Fuel i.e. 'Electric'                         | 47006 non-null | object     |
| 1  | station_name           | Name of station                                      | 47006 non-null | object     |
| 2  | address                | Address                                              | 47006 non-null | object     |
| 3  | city                   | City                                                 | 47006 non-null | object     |
| 4  | state                  | State                                                | 47006 non-null | object     |
| 5  | zip                    | Zip Code                                             | 47006 non-null | object     |
| 6  | group_access_code      | Whether public or private                            | 47006 non-null | object     |
| 7  | level1_evse_num        | Count of level 1 chargers                            | 47006 non-null | int64      |
| 8  | level2_evse_num        | Count of level 2 chargers                            | 47006 non-null | int64      |
| 9  | ev_dc_fast_count       | Count of DC fast chargers                            | 47006 non-null | int64      |
| 10 | ev_network             | Whether the charging stations is part of a network   | 47006 non-null | object     |
| 11 | lat                    | Latitude location                                    | 47006 non-null | float64    |
| 12 | long                   | Longitude location                                   | 47006 non-null | float64    |
| 13 | update_date            | Date stations information was updated                | 47006 non-null | datetime64 |
| 14 | open_date              | Date station was opened                              | 47006 non-null | datetime64 |
| 15 | connector_type         | Type of charging connector                           | 47006 non-null | object     |
| 16 | pricing                | Whether Free or Costs to charge                      | 47006 non-null | object     |
| 17 | year_opened            | Year the station opened                              | 47006 non-null | int64      |
| 18 | total_chargers         | Sum of all chargers per location                     | 47006 non-null | int64      |
| 19 | rolling_total_chargers | A rolling sum by open date of new chargers           | 47006 non-null | int64      |

### Explore:
Most of the EV charging stations within the US have been added since 2010 with a fluctuating but exponential increase over the last five years. My goal for this project was to predict the increase in charging stations 1-5 years into the future. Therefore, I reduced my data frame to only include the 'open_date' and 'total_chargers' for the exploration phase. I also only included the data from 2010 and beyond since most of the charger production has occurred since then. After splitting the data into train, validate, and test, I used statsmodels' seasonal decomposition function to explore the overall trends and seasonal components of the train dataset. The results showed that there are overall trend and seasonality components to the data. The trend component is clear based on the initial plots of the data in my notebook. The seasonality, it appears, can be attributed to fluctuations in the rate at which charging stations have been built in the US. Examining these results aided in choosing the best model for the project, which I will examine further in the next section.

### Model & Evaluate:
Due to the upward trend of the dataset over time I chose to use the Holt model and the Holt-Winters Exponential Smoothing Model. I began with fitting the model onto the train dataset and then creating a prediction for the same time period as the validate dataset. This allowed me to compare the prediction result to data that already exists. I then did the same using the Holt-Winters Exponential Smoothing model with the following results in root mean squared error (RMSE):
|Model| RMSE|
|---|---|
|Holt | 1010 |
|Holt-Winters Exponential Smoothing | 898 |
I achieved these results by adjusting the α and β smoothing parameters in order to optimally reduce the error. The data has a visually significant exponential trend to it, so there was no surprise that the Holt-Winters Exponential Smoothing model gave the best results. Therefore, I moved forward utilizing only the Holt-Winters Exponential Smoothing model for the Test dataset and then continued on to predict the EV Charging station growth two years into the future. The final prediction produced a result of 37,968 new EV chargers to be produced and installed over the next two years. This seems reasonable considering in 2019 there were 15,400 produced and in 2020 there were 26,395 produced. Only time will tell how accurate the prediction will be.

## Conclusion:
Predicting into the future can be tricky, and risky, business. Just because there was a trend in the past does not necessarily mean that a trend will continue into the future. In the case of Electric Vehicles, the technology behind these vehicles continues to change and progress on a regular basis. There are also environmental and political factors that heavily affect this business. Technology or legislation could be introduced at any time that would changes the rate of adding new charging stations to the US network. However, if the rate remains similar to the near past, then the Holt-Winters Exponential Smoothing Model proved to be a good predictor of future growth of EV chargers. The formula behind the model accounts for changes in rate of growth while not being overly sensitive to rapid changes in rate. It worked well for this situation, and I look forward to seeing how accurate the prediction becomes over time.

### Next Steps:
Going forward I would like to visually represent these findings on a dashboard using Tableau. I also plan to explore the other features of the dataset especially on pricing and public access to the charging stations.