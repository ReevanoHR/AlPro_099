from exercise9Modul3 import Admin

admin = Admin(
    "Budi",
    "Santoso",
    30,
    "08123456789",
    "admin_budi@example.com"
)
print(Admin.describe_user(admin))
admin.show_privileges()