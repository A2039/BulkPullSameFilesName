import os
import pandas as pd
from tqdm import tqdm
def validate_input_path(prompt):
    while True:
        folder_path = input(f"Enter the path for {prompt}: ")
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            return folder_path
        print(f"❌ Invalid folder path: {folder_path}. Please enter a valid path.")

def validate_excel_name():
    while True:
        excel_name = input("Enter the Excel filename (without extension): ")
        if excel_name.strip():
            return f"{excel_name.strip()}.xlsx"
        print("❌ Excel file name cannot be empty.")

def get_files(folder_path):
    files = set()
    for root, dirs, file_list in os.walk(folder_path):
        for file in file_list:
            files.add(os.path.splitext(file)[0])
    return files
def create_excel(data, excel_path):
    df = pd.DataFrame(list(data), columns=['CommonFileName'])
    df.to_excel(excel_path, index=False, engine='openpyxl')

def main():
    try:
        folder1 = validate_input_path("Folder 1")
        folder2 = validate_input_path("Folder 2")
        output_folder = validate_input_path("Folder to save Excel file")
        excel_name = validate_excel_name()

        excel_path = os.path.join(output_folder, excel_name)

        print("🚀 Processing file comparison...")
        files_folder1 = get_files(folder1)
        files_folder2 = get_files(folder2)

        common_files = files_folder1.intersection(files_folder2)

        with tqdm(total=len(common_files), desc="Comparing files", ncols=100, colour="green") as progress_bar:
            for _ in common_files:
                progress_bar.update(1)

        create_excel(common_files, excel_path)
        print(f"✅ Process complete. 🐍 Results saved at: {excel_path}")

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
