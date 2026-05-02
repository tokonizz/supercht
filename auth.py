from auth import register, login
from chat import chat

print("📱 CHAT PROTOTYPE (GITHUB VERSION)")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    pilih = input("Select: ")

    if pilih == "1":
        register()

    elif pilih == "2":
        user = login()
        if user:
            chat(user)

    elif pilih == "3":
        print("Bye 👋")
        break
