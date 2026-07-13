#Clean the phone numbers into one format

def format_phone_num(messy):
    clean = ""
    for i in range(0, len(messy)):
        ch = messy[i]
        if ch.isdigit():
            clean += ch
            if len(clean) == 3 or len(clean) == 7:
                clean += "-"
                
    return clean

phone_nums = []

f = open("phone_numbers_messy.txt", "r")
for line in f:
    phone_nums.append(line)
f.close()

clean_phone_nums = []
for i in range(0, len(phone_nums)):
    phone_nums[i] = format_phone_num(phone_nums[i])

f = open("phone_numbers_clean.txt", "w")
for i in range(0, len(phone_nums)):
    f.write(phone_nums[i] + "\n")
f.close()

