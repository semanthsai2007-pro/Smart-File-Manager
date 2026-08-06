import os
import shutil

class FileManager:
    def search_file(self):
        folder = input("Enter Folder Path: ")
        filename = input("Enter File Name: ")

        print("\nFolder Path:", folder)
        print("\nSearching for:", filename)

        found = False

        for root, dirs, files in os.walk(folder):
            for file in files:
                if filename == file:
                    found = True
                    print(os.path.join(root, file))
                    break
            if found:
                    break

        if not found:
            print("File Not Found")

    def rename_file(self):
        folder = input("Enter Folder Path: ")
        filename = input("Enter Old File Name: ")
        new_filename = input("Enter New File Name: ")

        print("\nFolder Path:", folder)
        print("Searching for:", filename)

        found = False

        for root, dirs, files in os.walk(folder):
            for file in files:
                if filename == file:
                    found = True

                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_filename)

                    try:
                        os.rename(old_path, new_path)
                        print("\nFile Renamed Successfully!")
                        print(f"'{filename}' renamed to '{new_filename}'")

                    except Exception as e:
                        print("\nError:", e)

                    break

            if found:
                break

        if not found:
            print("\nFile Not Found")

    def move_file(self):
        folder = input("Enter Folder Path: ")
        filename = input("Enter File name: ")
        destination = input("Enter Destination Folder: ")

        print("\nFolder:", folder)
        print("File:", filename)
        print("Destination:", destination)

        found = False

        for root, dirs, files in os.walk(folder):
            for file in files:
                if filename == file:
                    found = True
                    old_path = os.path.join(root, file)
                    try:
                        shutil.move(old_path, destination)
                        print("File Moved Successfully!")

                    except Exception as e:
                        print("Error:", e)
                    break
            if found:
                break
        if not found:
            print("File not found")

    def delete_file(self):
        folder = input("Enter Folder Path: ")
        filename = input("Enter File Name: ")

        print("\nFolder:", folder)
        print("File:", filename)
        destination = "recycle_bin"
        found = False
        
        for root, dirs, files in os.walk(folder):
            for file in files:
                if filename == file:
                    found = True
                    old_path = os.path.join(root, file)
                    try:
                        shutil.move(old_path, destination)
                        print("File Deleted Successfully!")
        
                    except Exception as e:
                        print("Error:", e)
                    break
            if found:
                break
        if not found:
            print("File not found")

    def recover_file(self):
        filename = input("Enter File Name: ")
        destination = input("Enter Recovery Folder: ")

        folder = "recycle_bin"

        print("\nRecycle Bin:", folder)
        print("File:", filename)
        print("Recovery Folder:", destination)

        found = False

        for root, dirs, files in os.walk(folder):
            for file in files:
                if filename == file:
                    found = True

                    old_path = os.path.join(root, file)

                    try:
                        shutil.move(old_path, destination)
                        print("File Recovered Successfully!")

                    except Exception as e:
                        print("Error:", e)

                    break

            if found:
                break

        if not found:
            print("File Not Found")

    def compress_file(self):
        folder = input("Enter Folder Path: ")

        if not os.path.exists(folder):
            print("Folder Not Found")
            return

        zip_name = os.path.basename(folder)

        try:
            shutil.make_archive(zip_name, "zip", folder)
            print("Folder Compressed Successfully!")

        except Exception as e:
            print("Error:", e)

    def find_duplicates(self):
        folder = input("Enter Folder Path: ")

        if not os.path.exists(folder):
            print("Folder Not Found")
            return

        duplicates = {}

        for root, dirs, files in os.walk(folder):
            for file in files:

                file_path = os.path.join(root, file)

                with open(file_path, "rb") as f:
                    content = f.read()

                if content in duplicates:
                    print("\nDuplicate Found!")
                    print("Original :", duplicates[content])
                    print("Duplicate:", file_path)

                else:
                    duplicates[content] = file_path

    def exit(self):
        print("Exiting The File")