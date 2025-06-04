                             _   _                                       
 --- __ _ _   _  ___  ___ ___  | |_| |__   ___    __ _  __ _ _ __ ___   ___ 
 / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \  / _` |/ _` | '_ ` _ \ / _ \
| (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | (_| | (_| | | | | | |  __/
 \__, |\__,_|\___||___/___/  \__|_| |_|\___|  \__, |\__,_|_| |_| |_|\___|
 |___/                                        |___/                      ---

 def dog_to_human_age(dog_age):
    human_age = dog_age * 7
    return human_age
dog_age = int(input("Enter your dog's age : "))
print("Your dog's age in human years is:", dog_to_human_age(dog_age))