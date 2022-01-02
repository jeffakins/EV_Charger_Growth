# This is a file that I will store all of my steps for cleaning the EV Charging Station dataset

# ----- Imports -----
import pandas as pd
import numpy as np
from datetime import datetime

# ----- Function to Clean the EV 2021 Charging Station Data -----
def clean_ev(csv_file_name):
    '''Function to Clean the EV 2021 Charging Station Data'''

    ev_21 = pd.read_csv(csv_file_name)     # Import csv file 
        
    ev_21 = ev_21[ev_21['Fuel Type Code'] == 'ELEC']    # To keep only EV stations

    # Drop columns that mostly have nulls
    # Thresh of 1000 was chosen because I wanted to keep the 'EV Level1 EVSE Num' column
    ev_21 = ev_21.dropna(axis=1, thresh=1000)   

    # Additional columns to drop:
    columns_to_drop = ['Intersection Directions', 'Station Phone', 'Status Code', 'Access Days Time', 
                   'EV Network Web', 'Date Last Confirmed', 'Geocode Status', 'Groups With Access Code (French)',
                   'Owner Type Code', 'Access Code', 'Access Detail Code', 'Facility Type', 'ID', 'Country']
    ev_21 = ev_21.drop(columns=columns_to_drop)

    # Update cost of charging to free or cost:
    ev_21['EV Pricing'] = ev_21['EV Pricing'].apply(lambda x: 'Free' if (x == 'FREE') | (x == 'Free') else 'Cost')

    # Fill EV connector types nulls with the most common connector type:
    ev_21['EV Connector Types'] = ev_21['EV Connector Types'].fillna(value='J1772')

    # Fill 'EV Network' nulls with "non network"
    ev_21['EV Network'] = ev_21['EV Network'].fillna(value='Non-Networked')

    # Add values for 2 missing longitude values based on city:
    ev_21.loc[54857, 'Longitude'] = -73.818871
    ev_21.loc[54865, 'Longitude'] = -79.299801

    # Renaming columns for ease of referencing:
    rename_list = {'Fuel Type Code': 'fuel_code',
              'Station Name': 'station_name',
              'Street Address': 'address',
              'City': 'city',
              'State': 'state',
              'ZIP': 'zip',
              'Groups With Access Code': 'group_access_code',
              'EV Level1 EVSE Num': 'level1_evse_num',
              'EV Level2 EVSE Num': 'level2_evse_num',
              'EV DC Fast Count': 'ev_dc_fast_count',
              'EV Network': 'ev_network',
              'Latitude': 'lat',
              'Longitude': 'long',
              'Updated At': 'update_date',
              'Open Date': 'open_date',
              'EV Connector Types': 'connector_type',
              'EV Pricing': 'pricing'}

    ev_21 = ev_21.rename(columns=rename_list)

    # convert our date columns to pandas datetime type:
    ev_21.update_date = pd.to_datetime(ev_21.update_date)
    ev_21.open_date = pd.to_datetime(ev_21.open_date)

    # Filling open_date null values with the update_date:
    ev_21.open_date = ev_21.open_date.fillna(value=ev_21.update_date)

    # Filling open_date null values with the update_date:
    ev_21.open_date = ev_21.open_date.fillna(value=ev_21.update_date)
    # Ensuring our dates have converted to datetime type:
    ev_21.update_date = pd.to_datetime(ev_21.update_date, utc=True)
    ev_21.open_date = pd.to_datetime(ev_21.open_date, utc=True)

    # Adding a column for year that the charging station was opened:
    ev_21['year_opened'] = ev_21.open_date.dt.year
   
   # Stripping off the timestamp of rows with dates:
    ev_21.update_date = ev_21.update_date.dt.date
    ev_21.open_date = ev_21.open_date.dt.date

    # Converting count columns into int type and filling nulls with 0:
    ev_21['level1_evse_num'] = ev_21['level1_evse_num'].fillna(0)
    ev_21['level2_evse_num'] = ev_21['level2_evse_num'].fillna(0)
    ev_21['ev_dc_fast_count'] = ev_21['ev_dc_fast_count'].fillna(0)

    ev_21['level1_evse_num'] = ev_21['level1_evse_num'].astype('int64')
    ev_21['level2_evse_num'] = ev_21['level2_evse_num'].astype('int64')
    ev_21['ev_dc_fast_count'] = ev_21['ev_dc_fast_count'].astype('int64')

    # Once again converting dates to datetime format:
    ev_21.update_date = pd.to_datetime(ev_21.update_date)
    ev_21.open_date = pd.to_datetime(ev_21.open_date)

    # Replacing 'Public w/descriptor' with just 'Public' (will add a loop later to clean it up)
    ev_21.group_access_code = ev_21.group_access_code.replace('Public - Call ahead', 'Public') 
    ev_21.group_access_code = ev_21.group_access_code.replace('Public - Credit card at all times', 'Public')
    ev_21.group_access_code = ev_21.group_access_code.replace('Public - Card key at all times', 'Public')
    ev_21.group_access_code = ev_21.group_access_code.replace('TEMPORARILY UNAVAILABLE (Public)', 'Public')
    ev_21.group_access_code = ev_21.group_access_code.replace('TEMPORARILY UNAVAILABLE (Public - Call ahead)', 'Public')
    ev_21.group_access_code = ev_21.group_access_code.replace('TEMPORARILY UNAVAILABLE (Public - Credit card at all times)', 'Public')

    # Replacing 'Private w/descriptor' with just 'Private'
    ev_21.group_access_code = ev_21.group_access_code.replace('Private - Government only', 'Private')
    ev_21.group_access_code = ev_21.group_access_code.replace('Private - Credit card at all times', 'Private')
    ev_21.group_access_code = ev_21.group_access_code.replace('Private - Fleet customers only', 'Private')
    ev_21.group_access_code = ev_21.group_access_code.replace('Private - Call ahead', 'Private')
    ev_21.group_access_code = ev_21.group_access_code.replace('Private - Credit card after hours', 'Private')
    ev_21.group_access_code = ev_21.group_access_code.replace('TEMPORARILY UNAVAILABLE (Private - Government only)', 'Private')
    ev_21.group_access_code = ev_21.group_access_code.replace('TEMPORARILY UNAVAILABLE (Private)', 'Private')

    # Dropping stations that are 'planned' and not yet accessible:
    ev_21 = ev_21[ev_21.group_access_code != 'PLANNED - not yet accessible (Public)']
    ev_21 = ev_21[ev_21.group_access_code != 'PLANNED - not yet accessible (Public - Credit card at all times)']
    ev_21 = ev_21[ev_21.group_access_code != 'PLANNED - not yet accessible (Public - Call ahead)']
    ev_21 = ev_21[ev_21.group_access_code != 'PLANNED - not yet accessible (Private)']

    # Create a total number chargers column:
    ev_21['total_chargers'] = ev_21.level1_evse_num + ev_21.level2_evse_num + ev_21.ev_dc_fast_count    

    # Sort values by open date
    ev_21 = ev_21.sort_values('open_date')
    # Reset Index
    ev_21 = ev_21.reset_index(drop=True)

    # Now we can create a column that sums the previous rows using cumsum:
    ev_21['rolling_total_chargers'] = ev_21.total_chargers.cumsum()

    return ev_21