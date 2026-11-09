class User:
    def __init__(self, first_name, last_name, age, contact, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.contact = contact
        self.email = email
        
    def describe_user(self):
        print(f'nama: {self.first_name} {self.last_name}')
        print(f'usia: {self.age}')
        print(f'contact: {self.contact}')
        print(f'email: {self.email}')
        
    def greet(self):
        print(f'Selamat Datang {self.first_name} {self.last_name}, Apa yang ingin kamu lakukan?')
        
class Admin(User):
    def __init__(
        self,
        first_name,
        last_name,
        age,
        contact,
        email
    ):
        super().__init__(
            first_name,
            last_name,
            age,
            contact,
            email
        )

        self.privileges = [
            "dapat menambah postingan",
            "dapat menghapus postingan",
            "dapat memblokir pengguna"
        ]

    def show_privileges(self):
        print("Hak akses administrator:")

        for hak_akses in self.privileges:
            print(f"- {hak_akses}")


admin = Admin(
    "Budi",
    "Santoso",
    30,
    "08123456789",
    "admin_budi@example.com"
)

print(Admin.describe_user(admin))
admin.show_privileges()