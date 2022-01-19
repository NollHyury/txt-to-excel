# Import Module
import os
from pandas import ExcelWriter
from jobSap import get_data_frame_from_text_job_file
import pandas as pd
  
# Folder Path
path = "C:/Projects/LEARN/test fastapi file/files"
  
# Change the directory
os.chdir(path)
  
# Read text File
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
  
  

concat_df = pd.DataFrame()
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        df = get_data_frame_from_text_job_file(file_path)
        concat_df = pd.concat([concat_df, df])


with ExcelWriter('C:/Projects/LEARN/test fastapi file/temp/bonomini.xlsx') as writer:
    concat_df.to_excel(writer, index=False)