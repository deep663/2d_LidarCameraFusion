import numpy as np
import matplotlib.pyplot as plt

def plot_specific_scan(scan_number, angle_range=None, data_file='data\scan2024-02-27_13-04-19.txt'):
    # Read data from the file
    with open(data_file, 'r') as file:
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

    # Filter points based on the specified angle range
    if angle_range:
        angle_min, angle_max = angle_range
        angle_mask = (np.array(angle) >= angle_min) & (np.array(angle) <= angle_max)
        x = x[angle_mask]
        y = y[angle_mask]
        scan_colors = scan_colors[angle_mask]

    # Filter points for the specified scan number
    scan_mask = np.array(scan_colors) == scan_number
    plt.scatter(x[scan_mask], y[scan_mask] * -1, c=scan_colors[scan_mask], cmap=cmap, marker='o', alpha=0.7)

    # Set labels and title
    plt.xlabel('X-axis (meters)')
    plt.ylabel('Y-axis (meters)')
    plt.title(f'Bird\'s Eye View of Lidar Data - Scan {scan_number}')

    # Set aspect ratio to be equal
    plt.axis('equal')

    # Show the plot
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

    # Return the total number of scans
    return int(np.max(scan_colors))

# Read data to get available scans
with open('data\scan2024-02-27_13-04-19.txt', 'r') as file:
    data = [line.strip().split('\t') for line in file]

# Convert data to separate lists for each column
true_values, _, _, _ = zip(*data)

# Convert the first column to boolean values
true_values = [val == 'True' for val in true_values]

# Group points by new scans
scan_colors = np.zeros(len(true_values))  # Initialize an array to store colors
current_color = 0
available_scans = set()
for i in range(len(true_values)):
    if true_values[i]:  # Check if it's a new scan
        current_color += 1
        available_scans.add(current_color)

print("Available scans: {}-{}".format(min(available_scans), max(available_scans)))

# Prompt user for scan number and angle range until 'q' key is pressed
while True:
    scan_number_input = input("Enter scan number to plot (or 'q' to exit): ")
    if scan_number_input.lower() == 'q':
        break

    try:
        scan_number = int(scan_number_input)
        if scan_number not in available_scans:
            print("Scan number not available.")
            continue

        angle_range_input = input("Enter angle range as 'min,max' (e.g., 0,180) or press Enter for full range: ")
        if angle_range_input:
            angle_range = tuple(map(float, angle_range_input.split(',')))
        else:
            angle_range = None

        plot_specific_scan(scan_number, angle_range)

    except ValueError:
        print("Invalid input. Please enter a valid scan number or 'q' to exit.")
