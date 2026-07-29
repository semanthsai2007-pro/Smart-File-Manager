import os

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
        print("Move Module Opened")

    def delete_file(self):
        print("Delete Module Opened")

    def recover_file(self):
        print("Recover Module Opened")

    def compress_file(self):
        print("Compress Module Opened")

    def find_duplicates(self):
        print("Duplicate Finder Module Opened")

    def exit(self):
        print("Exiting The File")