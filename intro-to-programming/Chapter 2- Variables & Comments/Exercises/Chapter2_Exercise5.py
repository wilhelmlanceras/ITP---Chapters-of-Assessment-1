total_money = 50
usb_price = 6

usb_sticks = total_money // usb_price
money_left = total_money % usb_price

print("She can buy", usb_sticks, "USB sticks.")
print("She will have £" + str (money_left) + " left.")