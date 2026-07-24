print("=" * 40)
print("      SMART FILE MANAGER")
print("=" * 40)

print("1.Search File\n2.Rename File \n3.Move File\n4.Delete File\n5.Recover File\n6.Compress File\n7. Duplicate Finder\n8.Exit")

x=int(input("Enter Your Choice: "))
if (x==1):
	print("\nSearch File Selected")
elif(x==2):
	print("\nRename File")
elif(x==3):
	print("\nMove File")
elif(x==4):
	print("\nDelete File")
elif(x==5):
	print("\nRecover File")
elif(x==6):
	print("\nCompress File")
elif(x==7):
	print("\nFind Duplicate Files")
elif(x==8):
	print("\nThank you for using Smart File Manager!")
else:
    print("\nInvalid")

