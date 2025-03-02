import pandas as pd

# task6 a
# Step 1: Read the CSV file into a DataFrame
housing_data = pd.read_csv('housing.csv')

# Step 2: Identify the row with the highest median house value
most_expensive_region = housing_data.loc[housing_data['median_house_value'].idxmax()]

# Step 3: Extract the location (longitude, latitude) of that row
longitude = most_expensive_region['longitude']
latitude = most_expensive_region['latitude']

print(f"The most expensive region is located at longitude: {longitude}, latitude: {latitude}")


print("#####################")

#task 6 b

# Step 1: Read the CSV file into a DataFrame
housing_data = pd.read_csv('housing.csv')

# Step 2: Calculate the population per household for each area
housing_data['population_per_household'] = housing_data['population'] / housing_data['households']

# Step 3: Identify the areas with the highest population per household
highest_population_density = housing_data.nlargest(10, 'population_per_household')

print("Areas with the highest population per household:")
print(highest_population_density[['longitude', 'latitude', 'population_per_household', 'median_house_value']])

# Step 4: Analyze the correlation between population per household and median house values
correlation = housing_data['population_per_household'].corr(housing_data['median_house_value'])

print(f"\nCorrelation between population per household and median house values: {correlation}")

print("#####################")

#task 6 c
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
housing_data = pd.read_csv('housing.csv')

# Step 2: Create a scatter plot to visualize the relationship
plt.figure(figsize=(10, 6))
plt.scatter(housing_data['median_income'], housing_data['median_house_value'], alpha=0.5)
plt.title('Median Income vs. Median House Value')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.show()

# Step 3: Calculate the correlation between median income and median house value
correlation = housing_data['median_income'].corr(housing_data['median_house_value'])
print(f"Correlation between median income and median house value: {correlation}")

# Step 4: Identify income brackets that afford expensive homes
# Define an expensive home as one with a value above a certain threshold (e.g., $500,000)
expensive_homes = housing_data[housing_data['median_house_value'] > 500000]
income_brackets = expensive_homes['median_income'].value_counts().sort_index()

print("Income brackets that afford expensive homes:")
print(income_brackets)

print("#####################")

#task 6 d

import pandas as pd

# Step 1: Read the CSV file into a DataFrame
housing_data = pd.read_csv('housing.csv')

# Step 2: Group the data by the 'ocean_proximity' column
grouped_data = housing_data.groupby('ocean_proximity')

# Step 3: Calculate the average median house value for each group
average_median_values = grouped_data['median_house_value'].mean()

# Step 4: Compare the average median house values
print("Average median house values by ocean proximity:")
print(average_median_values)