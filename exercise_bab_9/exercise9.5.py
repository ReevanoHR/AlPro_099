class User:
    def __init__(self, first_name, last_name, age, contact, email, login_attempts =0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.contact = contact
        self.email = email
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'nama: {self.first_name} {self.last_name}')
        print(f'usia: {self.age}')
        print(f'contact: {self.contact}')
        print(f'email: {self.email}')
        
    def greet(self):
        print(f'Selamat Datang {self.first_name} {self.last_name}, Apa yang ingin kamu lakukan?')
        
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
user2 = User("Reevano", 'Rajendra', 18, '081280*******', 'reevano.rajendra@example.com')
user2.describe_user()
user2.greet()
print('=' * 50)
user1 = User('Rizky', 'Firmansyah', 19, '081280*******', 'rizky.firmansyah@example.com')
user1.describe_user()
user1.greet()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Jumlah percobaan login:")
print(user1.login_attempts)

user1.reset_login_attempts()

print("\nJumlah percobaan login setelah direset:")
print(user1.login_attempts)