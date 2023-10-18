# 1.1 ternary operator
write_number_1TO = int(input("Write the number: "))
new_value_1TO = write_number_1TO/2 if write_number_1TO < 100 else -write_number_1TO
print(new_value_1TO)

# 1.2 ternary operator
write_number_1TO = int(input("Write the number: "))
new_value_1TO = write_number_1TO/2 if write_number_1TO < 100 else write_number_1TO*2
print(new_value_1TO)

# 2 ternary operator
write_number_2TO = int(input("Write the number: "))
new_value_2TO = 1 if write_number_2TO < 100 else 0
print(new_value_2TO)

# 3 ternary operator
write_number_3TO = int(input("Write the number: "))
new_value_3TO = 1 if write_number_3TO < 100 else 0
print(bool(new_value_3TO))

# 4 ternary operator
my_str_4TO = input("Write the text: ")
final_4TO = my_str_4TO*2 if len(my_str_4TO) < 5 else my_str_4TO
print(final_4TO)

# 5 ternary operator
my_str_5TO = input("Write the text: ")
final_5TO = my_str_5TO+my_str_5TO[::-1] if len(my_str_5TO) < 5 else my_str_5TO
print(final_5TO)
