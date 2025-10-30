import pandas as pd 
import os 

# PATHS
ROOT_DIR = "mlops-dvc-1"
DATA_DIR = os.path.join(ROOT_DIR, "data")


# Create data frame.
data = {"name":["name1", "name2", "name3"],
    "age":[10,20,30]
}
df = pd.DataFrame(data)


# Check if data folder exists else create it.
os.makedirs(DATA_DIR, exist_ok=True)

# Add new column.
df['Address'] = ['a', 'b', 'c']

# Save the dataframe
df.to_csv(os.path.join(DATA_DIR, "info.csv"), index=False)
print(f"File is saved at --> {DATA_DIR}")