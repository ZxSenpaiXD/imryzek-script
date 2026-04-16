#!/usr/bin/env python3

import os
import random
import string
import time
import traceback

def display_banner():
    print(r"""
|||||||||||||||||||||||||||||||||||||||||||||
||                                         ||
||   IIIIII  M     M  RRRRR   Y   Y  ZZZZZ ||
||     II    MM   MM  R   R    Y Y      Z  ||
||     II    M M M M  RRRRR     Y      Z   ||
||     II    M  M  M  R  R      Y     Z    ||
||   IIIIII  M     M  R   R     Y    ZZZZZ ||
||                                         ||
||               * IMRYZEK *               ||
||                                         ||
|||||||||||||||||||||||||||||||||||||||||||||
""")

def generate_random_string(length=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def worker_loop():
    folder_name = "24"
    os.makedirs(folder_name, exist_ok=True)

    start_time = time.time()
    restart_after = 5 * 60  # 5 minutes

    while True:
        # Auto-restart timer
        if time.time() - start_time >= restart_after:
            print("🔁 5 minutes reached → restarting loop...")
            break

        file_name = os.path.join(folder_name, f"{generate_random_string(8)}.txt")

        # CREATE
        with open(file_name, "w") as file:
            for _ in range(random.randint(10, 100)):
                file.write(generate_random_string(100) + "\n")
        print(f"Created: {file_name}")

        time.sleep(2)

        # EDIT
        with open(file_name, "w") as file:
            for _ in range(random.randint(10, 100)):
                file.write(generate_random_string(100) + "\n")
        print(f"Edited: {file_name}")

        time.sleep(1)

        # DELETE
        try:
            os.remove(file_name)
            print(f"Deleted: {file_name}")
        except FileNotFoundError:
            pass

        time.sleep(1)

def main_supervisor():
    while True:
        try:
            worker_loop()
        except Exception as e:
            print("⚠️ Crash detected:", e)
            traceback.print_exc()
            print("🔄 Restarting in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    display_banner()
    main_supervisor()
