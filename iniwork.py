import configparser
import os

def write_data_to_ini(data, filename='data.ini'):
    config = configparser.ConfigParser()
    config.read(filename)
    
    # Convert data to configparser format
    for section, values in data.items():
        config[section] = values
    
    # Save data to the file
    with open(filename, 'w') as file:
        config.write(file)
