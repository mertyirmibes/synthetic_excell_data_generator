import os
import pandas as pd
import random

# Male and female name lists
male_names = ["Ahmet", "Mehmet", "Ali", "Mustafa", "Hüseyin", "Hasan", "İbrahim", "Osman", "Yusuf", "Kemal",
              "Ertuğrul", "Furkan", "Efe", "Oğuz", "Emre", "Kaan", "Murat", "Onur", "Burak", "Serkan",
              "Çağrı", "Emin", "Taylan", "Cem", "Tuna", "Fatih", "Alper", "Tolga", "Sinan", "Levent",
              "Selim", "Barış", "Enes", "Halil", "Volkan", "Recep", "Cihan", "Serdar", "Görkem", "Can",
              "Cenk", "Kerem", "Deniz", "Uğur", "Sefa", "Yunus", "Kadir", "Bekir", "Hakan", "Eren",
              "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles",
              "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua"]

female_names = ["Ayşe", "Fatma", "Hatice", "Emine", "Zeynep", "Elif", "Merve", "Gamze", "Sena", "Ece",
                "Şeyma", "İrem", "Burcu", "Buse", "Tuğba", "Ezgi", "Büşra", "Sevda", "Hülya", "Serap",
                "Nisa", "Yasemin", "Dilara", "Gizem", "Betül", "Derya", "Pınar", "Nazlı", "Melike", "Cansu",
                "Aslı", "Feride", "Canan", "Hande", "Dilek", "Ayça", "Ceren", "Zeliha", "Esra", "Gül",
                "Aylin", "Şule", "Naz", "Sevil", "Nil", "Ebru", "Berfin", "Sıla", "Leyla", "Damla",
                "Mary", "Patricia", "Linda", "Barbara", "Elizabeth", "Jennifer", "Maria", "Susan", "Margaret",
                "Dorothy"]

surnames = ["Yılmaz", "Kaya", "Demir", "Çelik", "Şahin", "Yıldız", "Yıldırım", "Aydın", "Öztürk", "Arslan",
            "Doğan", "Korkmaz", "Çetin", "Koç", "Kılıç", "Aslan", "Özdemir", "Kara", "Acar", "Polat"]

cities = ["Adana", "Ankara", "İstanbul", "İzmir", "Antalya", "Bursa", "Gaziantep", "Konya", "Kayseri", "Samsun"]

credit_limits = [100_000, 200_000, 300_000, 500_000, 1_000_000, 5_000_000, 10_000_000]

# Function to generate unique random 10-digit ID numbers
def generate_unique_ids(count):
    ids = set()
    while len(ids) < count:
        # Ensure IDs are exactly 10 digits and start with 1 or higher
        new_id = str(random.randint(10 ** 9, 10 ** 10 - 1))
        ids.add(new_id)
    return list(ids)


# Function to generate unique random 6-digit customer numbers
def generate_unique_customer_numbers(count):
    customer_numbers = set()
    while len(customer_numbers) < count:
        # Ensure customer numbers are exactly 6 digits and start with 1 or higher
        new_number = str(random.randint(10 ** 5, 10 ** 6 - 1))
        customer_numbers.add(new_number)
    return list(customer_numbers)


# Generate random customer data
def generate_random_customer_data():
   #You can change amount of customers
    num_customers = 50
    names = [f"{random.choice(male_names + female_names)} {random.choice(surnames)}" for _ in range(num_customers)]
    id_numbers = generate_unique_ids(num_customers)
    customer_numbers = generate_unique_customer_numbers(num_customers)
    cities_random = [random.choice(cities) for _ in range(num_customers)]
    credit_limits_random = [random.choice(credit_limits) for _ in range(num_customers)]

    return pd.DataFrame({
        "Full Name": names,
        "ID Number": id_numbers,
        "Customer Number": customer_numbers,
        "City": cities_random,
        "Credit Limit $": credit_limits_random
    })


# Generate and save data to Excel
customer_data = generate_random_customer_data()
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "Customer_Data.xlsx")
customer_data.to_excel(file_path, index=False)

print(f"Customer data successfully created and saved to {file_path}.")