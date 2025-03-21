import pandas as pd
from google.colab import files

# Upload multiple files
uploaded = files.upload()

# Loop through all uploaded files
for filename in uploaded.keys():
    df = pd.read_csv(filename, sep=None, engine='python')
    
    # Extract candidate name from filename 
    candidate_name = filename.split('_')[2]
    df["candidate"] = candidate_name
    
    updated_filename = filename.replace('.csv', '_updated.csv')
    df.to_csv(updated_filename, index=False, sep="\t")
    
    files.download(updated_filename)