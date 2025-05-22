import pandas as pd
import os


data = { 
    "student":['Vivek','Rohit','Sandeep'],
    "branch":['metallurgy','mathematics','physics']
}

df = pd.DataFrame(data)


data_directory='data'
os.makedirs(data_directory,exist_ok=True)
file_path = os.path.join(data_directory,'sample_data.csv')
df.to_csv(file_path,index=False)

print(f'csv file saved to : {file_path}')