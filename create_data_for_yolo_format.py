import os

def replace_class_name(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace "Wheelchair" with "0" in each line
    modified_lines = [line.replace('Wheelchair', '0') for line in lines]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            replace_class_name(file_path)

label_folder_path = "dataset/labels"
process_files_in_folder(label_folder_path)