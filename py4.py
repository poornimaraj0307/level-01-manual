print("Poornima SuperMarket")
print("No.24,Sri sapthagiri Garden,Cuddalore")
print("-------------------------------------")
print("Bill Receipt")
print("-------------------------------------")
serialno=int(input("Enter the serial no:"))
particular=input("Enter the particular:")
rate=int(input("Enter the rate:"))
quantity=int(input("Enter the quantity:"))
total=rate*quantity
print("Total amount:",total)
GST=total*10/100
print("GST(10%)is:",GST)
paid=total+GST
print("Amount to be paid Rs:",paid)
