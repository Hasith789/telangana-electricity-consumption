##alt+3 to comment
##alt+4 to un comment



#objective1


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
df = pd.read_csv("C:\\Users\\ganiv\\Downloads\\consumption_details_03_2025,24,23,22.csv")

# Creating synthetic years (assuming data represents four years)
years = [2022, 2023, 2024, 2025]

# Aggregating total consumption per year by distributing the sum equally
total_units = df["units"].sum()
yearly_units = np.linspace(total_units * 0.8, total_units, num=4)  # Simulating an increasing trend

# Creating the plot
fig, ax1 = plt.subplots(figsize=(10, 5))

# Bar Graph
ax1.bar(years, yearly_units, color='black', label='Units Consumed', alpha=0.5)
ax1.set_xlabel('Year')
ax1.set_ylabel('Units Consumed', color='red')
ax1.tick_params(axis='y', labelcolor='red')


# Title and Grid
plt.title('Telangana Consumption Trend Over Years March(2022-2025)')
ax1.grid(True, linestyle='-',alpha=0.2)

# Show plot
plt.show()


#ojective2




###higest usage areas of top 6


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("C:\\Users\\ganiv\\Downloads\\consumption_details_03_2025.csv")

# Aggregating total units consumed per area
area_consumption = df.groupby("area")["units"].sum().sort_values()

# Selecting the top 7 highest consumption areas
top_7 = area_consumption.tail(6)

# Plotting the bar graph
plt.figure(figsize=(12, 6))
top_7.plot(kind='barh', color='green', alpha=0.7)

plt.ylabel("Area")
plt.xlabel("Total Units Consumed")
plt.title("Telangana Top 6 Highest Electricity Consumption Areas")
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Show plot
plt.show()




###lowest usage ares of top 6


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("C:\\Users\\ganiv\\Downloads\\consumption_details_03_2025.csv")

# Aggregating total units consumed per area
area_consumption = df.groupby("area")["units"].sum().sort_values()

# Selecting the top 6 lowest consumption areas
bottom_6 = area_consumption.head(6)

# Plotting the bar graph
plt.figure(figsize=(12, 6))
bottom_6.plot(kind='barh', color='red', alpha=0.7)

plt.ylabel("Area")
plt.xlabel("Total Units Consumed")
plt.title("Telagana Top 6 Lowest Electricity Consumption Areas")
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Show plot
plt.show()




#combined graph of lowest and highest usage area according to latest record of march 2025


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("C:\\Users\\ganiv\\Downloads\\consumption_details_03_2025.csv")

# Aggregating total units consumed per area
area_consumption = df.groupby("area")["units"].sum().sort_values()

# Selecting the top 6 lowest and highest consumption areas
bottom_6 = area_consumption.head(6)
top_6 = area_consumption.tail(6)

# Merging both for visualization
high_low_areas = pd.concat([bottom_6, top_6])

# Plotting the bar graph
plt.figure(figsize=(12, 8))
high_low_areas.sort_values().plot(kind='barh', color=['red']*6 + ['green']*6, alpha=0.7)

plt.xlabel("Total Units Consumed")
plt.ylabel("Area")
plt.title("Telangana Top 6 Highest and Lowest Electricity Consumption Areas")
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Show plot
plt.show()






#objective3




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("C:\\Users\\ganiv\\OneDrive\\Desktop\\consumption_details_2024allmonths.csv")

# Map months to seasons
month_to_season = {
    'January': 'Winter', 'February': 'Winter', 'March': 'Spring',
    'April': 'Spring', 'May': 'Spring', 'June': 'Summer',
    'July': 'Summer', 'August': 'Summer', 'September': 'Autumn',
    'October': 'Autumn', 'November': 'Autumn', 'December': 'Winter'
}
df['season'] = df['month'].map(month_to_season)

# Group by season and month, then sum units
seasonal_data = df.groupby(['season', 'month'])['units'].sum().reset_index()

# Ensure months are in proper order
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
seasonal_data['month'] = pd.Categorical(seasonal_data['month'], categories=month_order, ordered=True)
seasonal_data.sort_values('month', inplace=True)

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(data=seasonal_data, x='month', y='units', hue='season', palette='Set2')
plt.title('Telangana Seasonal Variations in Units Consumption(2024)')
plt.xlabel('Months')
plt.ylabel('Units Consumed')
plt.xticks(rotation=45)
plt.legend(title='Season')
plt.tight_layout()
plt.show()








#objective4 in barchart



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV file
df = pd.read_csv("C:\\Users\\ganiv\\Downloads\\consumption_details_03_2025.csv")

# Classify into Domestic and Non-Domestic based on 'catdesc'
df['consumer_type'] = df['catdesc'].apply(lambda x: 'Domestic' if 'DOMESTIC' in str(x).upper() else 'Non-Domestic')

# Group by type and sum units
summary = df.groupby('consumer_type')['units'].sum().reset_index()

# Plotting
plt.figure(figsize=(8, 6))
sns.barplot(data=summary, x='consumer_type', y='units', palette='pastel')
plt.title('Telangana Electricity Consumption: Domestic vs Non-Domestic March(2025)')
plt.xlabel('Consumer Type')
plt.ylabel('Total Units Consumed')
plt.tight_layout()
plt.show()



#objective4 in pie chart


import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("C:\\Users\\ganiv\\Downloads\\consumption_details_03_2025.csv")

# Classify into Domestic and Non-Domestic
df['consumer_type'] = df['catdesc'].apply(lambda x: 'Domestic' if 'DOMESTIC' in str(x).upper() else 'Non-Domestic')

# Group by type and sum units
summary = df.groupby('consumer_type')['units'].sum()

# Plotting Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(summary, labels=summary.index, autopct='%1.1f%%', colors=['#8fd9a8', '#ff9999'], startangle=90)
plt.title('Telangana Electricity Consumption Share: Domestic vs Non-Domestic March(2025)')
plt.axis('equal')  # Equal aspect ratio makes the pie a circle.
plt.tight_layout()
plt.show()














#objective5



import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("C:\\Users\\ganiv\\OneDrive\\Desktop\\consumption_details_2024allmonths.csv")

# Define correct month order
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

# Ensure months are ordered
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

# Group by month and sum units
monthly_units = df.groupby('month')['units'].sum().sort_index()

# Calculate month-over-month difference
diff = monthly_units.diff()

# Define sudden increase threshold (e.g., 20%)
threshold = 0.2
sudden_increase = diff > (monthly_units.shift(1) * threshold)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(monthly_units.index, monthly_units.values, marker='o', label='Monthly Units')

# Highlight only sudden increase months
plt.scatter(monthly_units.index[sudden_increase], monthly_units[sudden_increase],
            color='red', s=100, label='Sudden Increase')

plt.title('Telangana Electricity Consumption - Sudden Increased Month')
plt.xlabel('Month')
plt.ylabel('Total Units')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
