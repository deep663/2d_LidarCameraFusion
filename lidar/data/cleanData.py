# Read the content of the file
with open('scan2024-02-26_14-24-50.txt', 'r') as file:
    lines = file.readlines()

# Filter out lines containing 'scan'
cleaned_lines = [line for line in lines if 'scan' not in line]

# Write the cleaned data back to the file
with open('scan2024-02-26_14-24-50.txt', 'w') as file:
    file.writelines(cleaned_lines)
