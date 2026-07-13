# Compiles data from ABC files and writes new one.

class Customer:
    first_name = ""
    last_name = ""
    address = ""
    city = ""
    state = ""
    zip_code = ""
    phone_number = ""

f1 = open("ABC_names.txt", "r")
f2 = open("ABC_addresses.txt", "r")
f3 = open("ABC_phone.txt", "r")

cust_list = []
for i in range(1000):
    cust = Customer()
    name = f1.readline().strip()
    names = name.split()
    address = f2.readline().strip()
    city = f2.readline().strip()
    state_zip = f2.readline().strip()
    state_zip = state_zip.split()
    phone_num = f3.readline().strip()
    cust.first_name = names[0]
    cust.last_name = names[1]
    cust.address = address
    cust.city = city
    cust.state = state_zip[0]
    cust.zip = state_zip[1]
    cust.phone_number = phone_num
    cust_list.append(cust)
    
f1.close()
f2.close()
f3.close()

f1 = open("ABC_Customer_Data.txt", "w")
for i in range(1000):
    cust = cust_list[i]
    f1.write(cust.last_name + ", " + cust.first_name + "\n")
    f1.write(cust.address + "\n")
    f1.write(cust.city + ", " + cust.state +" " + cust.zip_code + "\n")
    f1.write(cust.phone_number + "\n")
    f1.write("\n")

f1.close()
