import numpy as np
import pandas as pd


# task2 a
data = np.random.randint(50, 501, size=(10, 30))
print(data)
print("#####################")

# task2 b
# Create a DataFrame from the data
companies = [f'company_{chr(97 + i)}' for i in range(10)]
df = pd.DataFrame(data, index=companies, columns=[f'day_{i+1}' for i in range(30)])
print(df)
print("#####################")

# task2 c
# Find the best-selling product (company with the highest total sales)
best_selling = df.sum(axis=1).idxmax()
# Find the worst-selling product (company with the lowest total sales)
worst_selling = df.sum(axis=1).idxmin()
print(f"Best-selling product: {best_selling} ")
print(f"Worst-selling product: {worst_selling} ")

print("#####################")

# task2 d
# Calculate the average daily sales for each company
average_sales = df.mean(axis=1)

# Find the product (company) with the highest average daily sales
highest_average_selling = average_sales.idxmax()

print(f"Product with highest average daily sales: {highest_average_selling} ")

print("#####################")

# task2 e
# Calculate the total sales for each day
total_sales_per_day = df.sum(axis=0)

# Find the most profitable day (day with the highest total sales)
most_profitable_day = total_sales_per_day.idxmax()
most_profitable_day_sales = total_sales_per_day.max()

# Find the least profitable day (day with the lowest total sales)
least_profitable_day = total_sales_per_day.idxmin()
least_profitable_day_sales = total_sales_per_day.min()

print(f"Most profitable day: {most_profitable_day} with total sales of {most_profitable_day_sales}")
print(f"Least profitable day: {least_profitable_day} with total sales of {least_profitable_day_sales}")

print("#####################")

# task2 f
# Calculate the average daily sales for each company
average_sales = df.mean(axis=1)

# Find the product (company) with the highest average daily sales
highest_average_selling = average_sales.idxmax()
highest_average_sales = average_sales.max()

print(f"Product with highest average daily sales: {highest_average_selling} with average sales of {highest_average_sales}")

print("#####################")

# task2 g
# Calculate the mean and standard deviation for each day
mean_sales_per_day = df.mean(axis=0)
std_sales_per_day = df.std(axis=0)

# Identify anomalies where sales values exceed 2 standard deviations from the mean
anomalies = (df - mean_sales_per_day).abs() > 2 * std_sales_per_day

# Get the indices of the anomalies
anomaly_indices = list(zip(*np.where(anomalies)))

# Convert the indices to the format (Product Index, Day Index)
anomaly_indices = [(df.index[product_idx], df.columns[day_idx]) for product_idx, day_idx in anomaly_indices]

print("Anomalies detected at the following indices (Product Index, Day Index):")
print(anomaly_indices)

print("#####################")
