import pandas as pd
from dora import Dora
#from pydantic-settings import BaseSettings
#from pandas_profiling import ProfileReport

# Sample DataFrame with hardcoded data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve'],
    'Age': [25, 28, 22, 30],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Data profiling using pandas_profiling
#profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)

# Save the report to an HTML file
#profile.to_file("data_profiling_report.html")
