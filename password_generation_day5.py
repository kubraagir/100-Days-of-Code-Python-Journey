import random
letters = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  # List of characters
numbers = ['0', '1', '2','3','4','5','6','7','8','9']  # List of numbers
symbols = ['!','#','$','%','&','(',')','*','+']
psw=[]
print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters would you like? \n"))
nr_numbers=int(input("How many numbers would you like? \n"))
nr_symbols=int(input("How many symbols would you like? \n"))

unique_items=[]
unique_items_random=[]
unique_items.extend(random.choices(letters, k=nr_letters))
unique_items.extend(random.choices(numbers, k=nr_numbers))
unique_items.extend(random.choices(symbols, k=nr_symbols))

random.shuffle(unique_items)
password="".join(unique_items)

#password2="".join(unique_items_random)
print("Your password is:", password)


