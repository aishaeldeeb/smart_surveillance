import os
import shutil

# Define the paths to the list files
train_list_path = 'train_list_v2.list'
test_list_path = 'test_list_v2.list'

# Define the destination directories
train_dest_path = '/data_v3/train'
test_dest_path = '/data_v3/test'

# Loop through the train list file
with open(train_list_path, 'r') as train_file:
    for line in train_file:
        # Remove the newline character from the end of the line
        line = line.rstrip('\n')
        
        # Get the directory of the .mp4 file
        directory = os.path.dirname(line)
        
        # Remove the '.npy' extension and replace 'features_v2' with 'data_v2'
        directory = directory.replace('features_v2', 'data_v2')
        directory = directory.replace('.npy', '.mp4')
        
        # Get the label of the video (anomaly or non_anomaly)
        label = os.path.basename(os.path.dirname(directory))
        
        # Create the destination directory if it doesn't exist
        dest_directory = os.path.join(train_dest_path, label)
        os.makedirs(dest_directory, exist_ok=True)
        
        # Get the subfolder name from the directory
        subfolder = os.path.basename(os.path.dirname(os.path.dirname(directory)))
        
        # Create the subdirectory if it doesn't exist
        dest_directory = os.path.join(dest_directory, subfolder)
        os.makedirs(dest_directory, exist_ok=True)
        
        # Copy the directory to the destination directory
        shutil.copytree(directory, os.path.join(dest_directory, os.path.basename(directory)))

# Loop through the test list file
with open(test_list_path, 'r') as test_file:
    for line in test_file:
        # Remove the newline character from the end of the line
        line = line.rstrip('\n')
        
        # Get the directory of the .mp4 file
        directory = os.path.dirname(line)
        
        # Remove the '.npy' extension and replace 'features_v2' with 'data_v2'
        directory = directory.replace('features_v2', 'data_v2')
        directory = directory.replace('.npy', '.mp4')
        
        # Get the label of the video (anomaly or non_anomaly)
        label = os.path.basename(os.path.dirname(directory))
        
        # Create the destination directory if it doesn't exist
        dest_directory = os.path.join(test_dest_path, label)
        os.makedirs(dest_directory, exist_ok=True)
        
        # Get the subfolder name from the directory
        subfolder = os.path.basename(os.path.dirname(os.path.dirname(directory)))
        
        # Create the subdirectory if it doesn't exist
        dest_directory = os.path.join(dest_directory, subfolder)
        os.makedirs(dest_directory, exist_ok=True)
        
        # Copy the directory to the destination directory
        shutil.copytree
