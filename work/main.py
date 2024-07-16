import cipher as ci
import art as di
import random
#creating a country class
class Country():
    def __init__(self,name,currency,area):
        self.name=name
        self.currency=currency
        self.area=area
countries = [
    Country("Sweden", "Krona", 450295),
    Country("France", "Euro", 551695),
    Country("Germany", "Euro", 357022),
    Country("Italy", "Euro", 301340),
    Country("Spain", "Euro", 505990)
]
#Defining global varibles
attempt=1
max_attempts=4 #its actually 3 but i used < when running while and not <=
high_area= 500000  #dividing countries on basis of their area to elevate difficulty for them
low_area= 300000
#shit starts i didnt make a loop cuz i wanted someone to see this 
print(f"Please choose your nation:")
for _ in countries:
    print(_.name)
Selected_Country=input("Please type the name of the country as it is given :\n")
for _ in countries:
    if _.name ==Selected_Country:
        Selected_area= int(_.area)
    
        if Selected_area > high_area:
            set_lenght=5
            key=ci.generate_key(set_lenght)
            print("Key :" ,key)
            text=ci.get_word(set_lenght)
            cipher_1=ci.encrypt_1(text, key)
            print("Encypted mystery code from god :", cipher_1, "\n")
            print("Its whats called one-time pad encryption it was during WW2, you can look it up \n")
            decipher_1=ci.decrypt_1(cipher_1, key)
            while attempt < max_attempts:
                current_attempt=int(max_attempts - attempt) 
                reply=input("Now take a nice guess, you have "+str(current_attempt)+" attempts :\n")
                if reply==decipher_1:
                    print("LET ME SUCK YOU, NO WAY YOU DID IT ON YOUR OWN!")
                    print(di.pp)
                    break
                attempt +=1
            if attempt==max_attempts:
                print("Try again loser!, all you had to was decipher the damn code, now re run")
        else:       #yeah its the same shit copied below could have done better
            set_lenght=4 #set_length didnt worrk somehow
            key=ci.generate_key(set_lenght)
            print("Key :" ,key)
            text=ci.get_word(set_lenght)
            cipher_1=ci.encrypt_1(text, key)
            print("Encypted mystery code from god :", cipher_1, "\n")
            print("Its whats called one-time pad encryption it was during WW2, you can look it up \n")
            decipher_1=ci.decrypt_1(cipher_1, key)
            while attempt < max_attempts:
                current_attempt=int(max_attempts - attempt) 
                reply=input("Now take a nice guess, you have "+str(current_attempt)+" attempts :\n")
                if reply==decipher_1:
                    print("LET ME SUCK YOU, NO WAY YOU DID IT ON YOUR OWN!")
                    print(di.pp)
                    break
                attempt +=1
            if attempt==max_attempts:
                print("Try again loser!, all you had to was decipher the damn code, now re run")
else:
     print("Type it EXACTLY AS IT IS DISPLAYED, now re run!")   #this falls in for _ loop so it would print many times without that if
        