import os
import shutil


main_folder = "MMU-Iris-Database"
output_folder = "data"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
for subfolder in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder)
    
    print(f"Processing subfolder: {subfolder}")
    
    for subsubfolder in os.listdir(subfolder_path):
        subsubfolder_path = os.path.join(subfolder_path, subsubfolder)
        
        if os.path.isdir(subsubfolder_path):
            
            for filename in os.listdir(subsubfolder_path):
                file_path = os.path.join(subsubfolder_path, filename)
                
                if filename.endswith(".bmp"):
                    new_filename = f"eye_p{int(subfolder):02d}_{subsubfolder}{filename.split('.')[0][-1]}.bmp"
                    new_file_path = os.path.join(output_folder, new_filename)
                    
                    shutil.copy2(file_path, new_file_path)
