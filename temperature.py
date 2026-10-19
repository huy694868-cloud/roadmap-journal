nhietdo = input("Nhập nhiệt độ : ")
nhietdo = float(nhietdo)
if nhietdo < -40 or nhietdo > 125:
    print("Invalid")
elif nhietdo < 20 :
    print("Cold")
elif nhietdo > 30:
    print("Hot")
else:
    print("Comfortable")