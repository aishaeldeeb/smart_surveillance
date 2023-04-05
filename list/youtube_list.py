import os
import random
import argparse

parser = argparse.ArgumentParser(description='RTFM')
parser.add_argument('--youtube_anomaly_dir', default='/scratch/aishaeld/I3D_Feature_Extraction_resnet/features/anomaly')
parser.add_argument('--youtube_non_anomaly_dir', default='/scratch/aishaeld/I3D_Feature_Extraction_resnet/features/non_anomaly')

parser.add_argument('--custom_anomaly_dir', default='/scratch/aishaeld/I3D_Feature_Extraction_resnet/custom_features/anomaly')
parser.add_argument('--custom_non_anomaly_dir', default='/scratch/aishaeld/I3D_Feature_Extraction_resnet/custom_features/non_anomaly')

parser.add_argument('--train_file', default='youtube_train_list.list')
parser.add_argument('--test_file', default='youtube_test_list.list')


args = parser.parse_args()

# Directories containing the files
youtube_anomaly_dir = args.youtube_anomaly_dir

youtube_non_anomaly_dir = args.youtube_non_anomaly_dir

custom_anomaly_dir = args.custom_anomaly_dir

custom_non_anomaly_dir = args.custom_non_anomaly_dir

# Percentage of files to use for training
train_percent = 0.6

# Output file names
train_file = args.train_file
test_file = args.test_file

# Get a list of files in the directories
youtube_anomaly_files = [os.path.join(youtube_anomaly_dir, f) for f in os.listdir(youtube_anomaly_dir)]
youtube_non_anomaly_files = [os.path.join(youtube_non_anomaly_dir, f) for f in os.listdir(youtube_non_anomaly_dir)]

random.shuffle(youtube_anomaly_files)
random.shuffle(youtube_non_anomaly_files)

youtube_files = youtube_anomaly_files + youtube_non_anomaly_files

custom_anomaly_files = [os.path.join(custom_anomaly_dir, f) for f in os.listdir(custom_anomaly_dir)]
custom_non_anomaly_files = [os.path.join(custom_non_anomaly_dir, f) for f in os.listdir(custom_non_anomaly_dir)]

random.shuffle(custom_anomaly_files)
random.shuffle(custom_non_anomaly_files)

custom_files = custom_anomaly_files + custom_non_anomaly_files



# Write the train files to the output files
with open(train_file, 'w') as f:
    for i in range(len(youtube_files)):
        print(youtube_files[i])
        f.write(youtube_files[i] + '\n')

# Write the test files to the output files
with open(test_file, 'w') as f:
    for i in range(len(custom_files)):
        print(custom_files[i])
        f.write(custom_files[i] + '\n')

print('Number of training anomaly files: ', len(youtube_anomaly_files), '\n')
print('Number of training non_anomaly files: ', len(youtube_non_anomaly_files), '\n')


with open('config.txt', 'w') as f:
    f.write(f'Number of training anomaly files: {len(youtube_anomaly_files)}\n')
    f.write(f'Number of trainng non-anomaly files: {len(youtube_non_anomaly_files)}\n')

