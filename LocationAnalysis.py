import folium
from folium.plugins import HeatMap

# 1. Initialize Map centered on the average coordinates
base_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)

# 2. Create Heatmap Data
heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]

# 3. Add Heatmap Layer
HeatMap(heat_data).add_to(base_map)

# 4. Save visualization
base_map.save("output/restaurant_density_heatmap.html")
