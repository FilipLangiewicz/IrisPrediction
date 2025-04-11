import os
import shutil


main_folder = "Database"
output_folder = "data2"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
for subfolder in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder)
    
    print(f"Processing subfolder: {subfolder}")
    
    if os.path.isdir(subfolder_path):
        
        for filename in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, filename)
            
            if filename.endswith(".JPG"):
                new_filename = f"eye_p{int(subfolder):02d}_{'left' if 'L' in filename else 'right'}{filename.split('_')[-1][0]}.jpg"
                new_file_path = os.path.join(output_folder, new_filename)
                
                shutil.copy2(file_path, new_file_path)
