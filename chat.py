from data import chat_db

def chat(user):
    while True:
        print("\n💬 CHAT MENU")
        print("1. Send message")
        print("2. View chat")
        print("3. Exit")

        pilih = input("Choose: ")

        if pilih == "1":
            target = input("Send to: ")
            msg = input("Message: ")

            key = (user, target)

            if key not in chat_db:
                chat_db[key] = []

            chat_db[key].append(f"{user}: {msg}")
            print("📨 Sent")

        elif pilih == "2":
            target = input("View chat with: ")

            k1 = (user, target)
            k2 = (target, user)

            print("\n💬 CHAT HISTORY")

            if k1 in chat_db:
                for m in chat_db[k1]:
                    print(m)
            elif k2 in chat_db:
                for m in chat_db[k2]:
                    print(m)
            else:
                print("No chat yet")

        elif pilih == "3":
            break
