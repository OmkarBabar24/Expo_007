import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# print('Modules are imported.')

# 1. Data Collection
# Load the dataset
df = pd.read_csv("C:\\omkar\\project\\archive\\E-commerce Data Analysis Project.csv")
print(df)

# 2. Data Cleaning
# Check for missing values and duplicates
nan_counts = df.isna().sum()
print('Missing values:\n', nan_counts)
print('Duplicate rows:', df.duplicated().sum())

# # Ensure dates are in 'datetime' format
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
#
# # 3. Exploratory Data Analysis (EDA)
# # Overview of Data Distribution
print(df.shape)
print(df.head())
print(df.describe())
#
# # Quantity Order Distribution
# quantity_counts = df['Quantity Ordered'].value_counts().reset_index()
# quantity_counts.columns = ['Quantity Ordered', 'Count']
# sns.barplot(x='Quantity Ordered', y='Count', data=quantity_counts)
# sns.despine()
# sns.set_context("talk")
# sns.set_style("whitegrid")
# plt.title('Quantity Ordered Distribution')
# plt.show()
#
# # Price Each Distribution
# sns.histplot(df['Price Each'], bins=50, kde=True)
# sns.despine()
# plt.title('Price Each Distribution')
# plt.show()
#
#
# # 4. Sales Trend Analysis
# # Monthly Sales Trend
# monthly_sales = df.groupby('Month')['Sales'].sum()
# monthly_sales = monthly_sales.reset_index()
# monthly_sales['Month'] = monthly_sales['Month'].astype(str)
# sns.barplot(x='Month', y='Sales', data=monthly_sales, color='#4682B4', label='Monthly Sales')
# sns.lineplot(x='Month', y='Sales', data=monthly_sales, color='red', marker='o', label='Trend Line')
# sns.set_context("talk")
# sns.set_style("whitegrid")
# plt.title('Monthly Sales Trend')
# plt.legend()
# plt.show()
#
# # Sales Trend by Hour
# hourly_sales = df.groupby('Hour')['Sales'].sum()
# hourly_sales = hourly_sales.reset_index()
# hourly_sales['Hour'] = hourly_sales['Hour'].astype(str)
# sns.barplot(x='Hour', y='Sales', data=hourly_sales, color='#4682B4', label='Hourly Sales')
# sns.lineplot(x='Hour', y='Sales', data=hourly_sales, color='red', marker='o', label='Trend Line')
# sns.set_context("talk")
# sns.set_style("whitegrid")
# plt.title('Hourly Sales Trend')
# plt.grid(True)
# plt.legend()
# plt.show()

# # Product Preference Analysis
# # Top-selling products
# product_sales = df.groupby(['Product Category', 'Product'])['Sales'].sum().reset_index()
# top_products = product_sales.sort_values(by='Sales', ascending=False).head(10)
# plt.figure(figsize=(12, 6))
# sns.barplot(x='Product', y='Sales', data=top_products)
# plt.title('Top 10 Products by Sales')
# plt.xlabel('Product')
# plt.ylabel('Total Sales')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()
# #
# # Product Category Preferences
# product_cat_sales = df.groupby('Product Category')['Sales'].sum().reset_index()
# plt.figure(figsize=(8, 6))
# wedges, texts, autotexts = plt.pie(
#     product_cat_sales['Sales'],
#     labels=product_cat_sales['Product Category'],
#     autopct='%1.0f%%',
#     startangle=140,
#     colors=sns.color_palette("Blues")
# )
# for text in autotexts:
#     text.set_fontsize(10)
# plt.title('Sales Distribution by Product Category')
# plt.axis('equal')
# plt.show()

# # City-wise Sales Analysis
# df['City'] = df['City'].str.strip()
# df['City'] = df['City'].str.title()
# city_sales = df.groupby('City')['Sales'].sum().reset_index()
# city_sales = city_sales.sort_values(by='Sales', ascending=False)
# plt.figure(figsize=(12, 6))
# sns.barplot(x='City', y='Sales', data=city_sales, color='#4682B4')
# plt.title('Sales by City')
# plt.xlabel('City')
# plt.ylabel('Total Sales')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()
#
# # Mapping total Sales
# df['City'] = df['City'].str.strip()
# df['City'] = df['City'].str.title()  # Capitalize first letter of each word
# city_sales = df.groupby('City')['Sales'].sum().to_dict()
# city_coords = {
#     'New York City': (-74.006, 40.7128),
#     'San Francisco': (-122.4194, 37.7749),
#     'Atlanta': (-84.3880, 33.7490),
#     'Portland': (-122.6765, 45.5234),
#     'Dallas': (-96.7970, 32.7767),
#     'Los Angeles': (-118.2437, 34.0522),
#     'Boston': (-71.0589, 42.3601),
#     'Austin': (-97.7431, 30.2672),
#     'Seattle': (-122.3321, 47.6062)
# }
#
# map_center = [sum(coord[1] for coord in city_coords.values()) / len(city_coords),
#               sum(coord[0] for coord in city_coords.values()) / len(city_coords)]
# m = folium.Map(location=map_center, zoom_start=5)
#
# for city, (lon, lat) in city_coords.items():
#     if city in city_sales:
#         sales = city_sales[city]
#         folium.Circle(
#             location=[lat, lon],
#             radius=sales * 0.02,
#             color='green',
#             fill=True,
#             fill_color='green',
#             fill_opacity=0.6,
#             popup=folium.Popup(f'{city}: ${sales:,.2f}', parse_html=True)
#         ).add_to(m)
#     else:
#         print(f"Warning: No data found for {city}")
#
# # Save the map to an HTML file
# m.save('sales_mapping.html')
# print('Sales Map is saved to the file sales_mapping.html')

# # 5. Customer Segmentation Analysis (Clustering)
#
# df['Unique Identifier'] = df['City'] + '-' + df['Product Category'] + '-' + df['Product']
# agg_data = df.groupby('Unique Identifier').agg({
#     'Order Date': 'max',
#     'Order ID': 'count',
#     'Sales': ['sum', 'mean']
# }).reset_index()
#
# agg_data.columns = ['Unique Identifier', 'Last Purchase Date', 'Frequency', 'Monetary Value', 'Average Purchase Value']
# current_date = pd.Timestamp.now()
# agg_data['Recency'] = (current_date - pd.to_datetime(agg_data['Last Purchase Date'],  dayfirst=True)).dt.days
# agg_data['Average Purchase Value'] = agg_data['Monetary Value'] / agg_data['Frequency']
# features = agg_data[['Recency', 'Frequency', 'Monetary Value']]
#
# scaler = StandardScaler()
# scaled_features = scaler.fit_transform(features)
# scaled_df = pd.DataFrame(scaled_features, columns=['Recency', 'Frequency', 'Monetary Value'])
# scaled_df[['Unique Identifier']] = agg_data[['Unique Identifier']]
#
# inertia = []
# K = range(1, 11)
# for k in K:
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(scaled_features)
#     inertia.append(kmeans.inertia_)
#
# plt.figure(figsize=(8, 5))
# plt.plot(K, inertia, 'bx-')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.title('Elbow Method For Optimal K')
# plt.show()
#
# kmeans = KMeans(n_clusters=4, random_state=42)
# agg_data['Cluster'] = kmeans.fit_predict(scaled_features)

# # Visualize clusters using PCA
# pca = PCA(n_components=2)
# pca_features = pca.fit_transform(scaled_features)
# agg_data['PCA1'] = pca_features[:, 0]
# agg_data['PCA2'] = pca_features[:, 1]
#
# plt.figure(figsize=(10, 7))
# sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=agg_data, palette='Set1', s=100)
# plt.title('Clusters in PCA-reduced Feature Space')
# plt.show()
#
# # Calculate the percentage of each cluster (segment)
# cluster_counts = agg_data['Cluster'].value_counts()
# cluster_percentages = cluster_counts / cluster_counts.sum() * 100
#
# # Round the percentages to integers
# cluster_percentages_rounded = cluster_percentages.round(0).astype(int)
#
# # Create labels for the pie chart
# labels = [f'Segment {i}' for i in cluster_counts.index]
#
# # Define the colors for each segment: 0 = red, 1 = blue, 2 = green, 3 = purple
# colors = ['red', 'purple', 'green', 'blue']
#
# # Plot the pie chart
# plt.figure(figsize=(8, 6))
# plt.pie(cluster_percentages, labels=labels, autopct='%1.0f%%', startangle=140, colors=colors)
#
# # Add a title
# plt.title('Customer Segments by Percentage')
#
# # Display the pie chart
# plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
# plt.show()
#
# # Select the necessary columns for saving
# segmentation_results = agg_data[['Unique Identifier', 'Cluster']]
#
# # Save the segmentation results to a CSV file
# segmentation_results.to_csv('customer_segmentation_results.csv', index=False)
#
# # 6. Evaluate the clustering using Silhouette Score
# silhouette_avg = silhouette_score(scaled_features, agg_data['Cluster'])
# print(f'Silhouette Score: {silhouette_avg:.2f}')
#
#
# print('Analysis and Visualization Completed')
