humid =  input("Nhập độ ẩm từ 0 đến 100% : ")
humid = float(humid)
if humid < 0 or humid > 100:
    print("Invalid")
elif humid < 30:
    print("Dry")
elif humid > 70:
    print("Humid")
else:
    print("Normal")