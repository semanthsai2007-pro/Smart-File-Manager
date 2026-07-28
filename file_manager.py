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
        print("Rename Module Opened")

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