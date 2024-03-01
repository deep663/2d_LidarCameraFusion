import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
with open('data\scan2024-02-26_14-28-31.txt', 'r') as file:
    data = [line.strip().split('\t') for line in file]

# Convert data to separate lists for each column
true_values, quality, angle, distance_mm = zip(*data)

# Convert the first column to boolean values
true_values = [val == 'True' for val in true_values]

# Convert the other columns to appropriate data types (e.g., float)
angle = [float(val) for val in angle]
distance_mm = [float(val) for val in distance_mm]

# Convert distances from mm to meters
distance_m = np.array(distance_mm) / 1000.0

# Convert polar coordinates to Cartesian coordinates
x = distance_m * np.cos(np.radians(angle))
y = distance_m * np.sin(np.radians(angle))

# Group points by new scans
scan_colors = np.zeros(len(true_values))  # Initialize an array to store colors
current_color = 0
for i in range(len(true_values)):
    if true_values[i]:  # Check if it's a new scan
        current_color += 1
    scan_colors[i] = current_color

# Create a color map for the scatter plot
cmap = plt.get_cmap('tab10')

# Create a scatter plot for bird's eye view
plt.figure(figsize=(8, 8))
plt.scatter(x, y*-1, c=scan_colors, cmap=cmap, marker='o', alpha=0.7)

# Set labels and title
plt.xlabel('X-axis (meters)')
plt.ylabel('Y-axis (meters)')
plt.title('Bird\'s Eye View of Lidar Data')


# Set aspect ratio to be equal
plt.axis('equal')

# Show the plot
plt.grid(True)  # Display grid
plt.axhline(0, color='black', linewidth=0.5)  # Horizontal axis line
plt.axvline(0, color='black', linewidth=0.5)  # Vertical axis line
plt.show()
