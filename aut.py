import random
import time
from data import users

def send_otp():
    otp = str(random.randint(1000, 9999))
    print("\n📩 Sending OTP...")
    time.sleep(1)
    print("🔐 OTP (demo):", otp)
    return otp


def register():
    print("\n=== REGISTER ===")

    nomor = input("Phone number: ")

    if nomor in users:
        print("❌ Already registered")
        return

    otp = send_otp()
    masuk = input("Enter OTP: ")

    if masuk == otp:
        pw = input("Create password: ")
        users[nomor] = pw
        print("✅ Registered successfully")
    else:
        print("❌ Wrong OTP")


def login():
    print("\n=== LOGIN ===")

    nomor = input("Phone: ")
    pw = input("Password: ")

    if nomor in users and users[nomor] == pw:
        print("✅ Login success")
        return nomor
    else:
        print("❌ Login failed")
        return None
