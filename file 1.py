from db import connect

def Register_User():
    conn = connect()
    cursor = conn.cursor()
    
    print("Enter the following details:\n")
    user_id = input("User ID: ")
    name = input("Name: ")
    contact = input("Contact: ")
    email = input("Email: ")
    skill1 = input("Skill 1: ")
    skill2 = input("Skill 2: ")
    skill3 = input("Skill 3: ")
    skill4 = input("Skill 4: ")
    skill5 = input("Skill 5: ")
    years_of_experience = int(input("Years of Experience: "))
    
    print("\nAvailability Menu:")
    print("1. Morning\n2. Afternoon\n3. Evening\n4. Part Time\n5. Full Time")
    ch = int(input("Enter your choice (1-5): "))
    
    availability_options = ["Morning", "Afternoon", "Evening", "Part Time", "Full Time"]
    availability = availability_options[ch - 1] if 1 <= ch <= 5 else "Not specified"
    
    username = input("Create Username: ")
    password = input("Create Password: ")
    
    query = """INSERT INTO Register_User(user_id, name, contact, email, skill1, skill2, skill3, skill4, skill5, 
              years_of_experience, availability, username, password) 
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    values = (user_id, name, contact, email, skill1, skill2, skill3, skill4, skill5, years_of_experience, availability, username, password)
    
    cursor.execute(query, values)
    conn.commit()
    print("*User details collected successfully!")
    
    cursor.close()
    conn.close()

def login_user():
    conn = connect()
    cursor = conn.cursor()
    
    username = input("Username: ")
    password = input("Password: ")
    
    cursor.execute("SELECT * FROM Register_User WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Login successful. Welcome", user[1])
        find_partner()
    else:
        print("Invalid credentials.")
    
    cursor.close()
    conn.close()

def find_partner():
    conn = connect()
    cursor = conn.cursor()
    
    required_skill = input("Enter required skill: ")
    group_size = int(input("How many partners do you want (1 to 10)? "))
    required_availability = input("Enter preferred availability (Morning/Afternoon/Evening/Part Time/Full Time): ")
    
    query = """SELECT name, email, skill1, skill2, skill3, availability, years_of_experience, contact 
               FROM Register_User 
               WHERE (skill1=%s OR skill2=%s OR skill3=%s OR skill4=%s OR skill5=%s) 
               AND availability=%s"""
    
    cursor.execute(query, (required_skill, required_skill, required_skill, required_skill, required_skill, required_availability))
    results = cursor.fetchall()
    
    if results:
        print(f"You requested {group_size} partners. Best matches:\n")
        for row in results[:group_size]:  # Display only requested number of partners
            print(f"Name: {row[0]}")
            print(f"Email: {row[1]}")
            print(f"Skill 1: {row[2]}")
            print(f"Skill 2: {row[3]}")
            print(f"Skill 3: {row[4]}")
            print(f"Availability: {row[5]}")
            print(f"Years of experience: {row[6]}")
            print(f"Contact: {row[7]}")
            print("-" * 40)
    else:
        print("No matching partners found.")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    Register_User()
