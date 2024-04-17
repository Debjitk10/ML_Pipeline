import os

# Check if 'artifacts' directory exists
if os.path.exists('artifacts'):
    print("The 'artifacts' directory exists.")
else:
    print("The 'artifacts' directory does not exist.")



# List of files to check
file_names = ['train.csv', 'test.csv', 'raw.csv']

# Check if each file exists
for file_name in file_names:
    file_path = os.path.join('artifacts', file_name)
    if os.path.exists(file_path):
        print(f"The file '{file_name}' exists.")
    else:
        print(f"The file '{file_name}' does not exist.")
