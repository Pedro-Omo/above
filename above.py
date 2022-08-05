#prime_numbers(2, 3, 5, 7, 11, 13, 17...)

number = int(input("Enter any number: ")) #allowing input from user.
if number>1:
    for i in range(2,number):
        if number ==0:  #if input nos/by nos within range=0,then its not prime
            print("No! This is not a PRIME number:",number)
            break
    else:
            print("Yes! This is a PRIME number:",number)
