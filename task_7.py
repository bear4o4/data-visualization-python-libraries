import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#task 7 a
housing_data = pd.read_csv('housing.csv')

# Step 2: Group the data by 'housing_median_age' and calculate the average median house value for each age
age_vs_value = housing_data.groupby('housing_median_age')['median_house_value'].mean().reset_index()

# Step 3: Plot the data using a line graph
plt.figure(figsize=(10, 6))
plt.plot(age_vs_value['housing_median_age'], age_vs_value['median_house_value'], marker='o')
plt.title('Relationship between Housing Median Age and Median House Value')
plt.xlabel('Housing Median Age')
plt.ylabel('Median House Value')
plt.grid(True)
plt.show()

print("#####################")

#task 7 b

# Step 2: Calculate the number of rooms per household for each area
housing_data['rooms_per_household'] = housing_data['total_rooms'] / housing_data['households']

# Step 3: Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(housing_data['rooms_per_household'], bins=30, edgecolor='black')
plt.title('Distribution of Rooms per Household')
plt.xlabel('Rooms per Household')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

print("#####################")

#task 7 c

# Step 2: Group the data by 'ocean_proximity' and calculate the total population for each group
total_population_by_proximity = housing_data.groupby('ocean_proximity')['population'].sum().reset_index()

# Step 3: Plot the data using a bar chart
plt.figure(figsize=(10, 6))
plt.bar(total_population_by_proximity['ocean_proximity'], total_population_by_proximity['population'], color='skyblue')
plt.title('Total Population by Ocean Proximity')
plt.xlabel('Ocean Proximity')
plt.ylabel('Total Population')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

print("#####################")

#task 7 d

# Step 2: Select only the numeric columns
numeric_data = housing_data.select_dtypes(include=[float, int])

# Step 3: Calculate the correlation matrix for the numerical features
correlation_matrix = numeric_data.corr()

# Step 4: Use a heatmap to visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Features in Housing Dataset')
plt.show()