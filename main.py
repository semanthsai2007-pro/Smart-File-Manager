from file_manager import FileManager

fm = FileManager()

print("=" * 40)
print("      SMART FILE MANAGER")
print("=" * 40)

print("1.Search File\n2.Rename File \n3.Move File\n4.Delete File\n5.Recover File\n6.Compress File\n7. Duplicate Finder\n8.Exit")

x=int(input("Enter Your Choice: "))
if (x==1):
	fm.search_file()
elif(x==2):
	fm.rename_file()
elif(x==3):
	fm.move_file()
elif(x==4):
	fm.delete_file()
elif(x==5):
	fm.recover_file()
elif(x==6):
	fm.compress_file()
elif(x==7):
	fm.find_duplicates()
elif(x==8):
	fm.exit()
else:
    print("\nInvalid")

