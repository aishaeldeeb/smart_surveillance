import os

# The directory containing the files
directory1 = "/home/aishaeld/scratch//I3D_Feature_Extraction_resnet/features_v3/anomaly"
directory2 = "/home/aishaeld/scratch//I3D_Feature_Extraction_resnet/features_v3/non_anomaly"

# The list to store the filenames
filenames = []

# Loop through all the files in the directory
for filename in os.listdir(directory1):
    # Construct the full path to the file
    file_path = os.path.join(directory1, filename)
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Add the file to the list
        filenames.append(file_path)

# Loop through all the files in the directory
for filename in os.listdir(directory2):
    # Construct the full path to the file
    file_path = os.path.join(directory2, filename)
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Add the file to the list
        filenames.append(file_path)


# Write the list of filenames to the file
with open("train_list_aug.list", "w") as f:
    for filename in filenames:
        f.write(filename + "\n")