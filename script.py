#!/usr/bin/env python3

import os
import random
import string
import time

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

def create_edit_delete_file():
    folder_name = "24"
    os.makedirs(folder_name, exist_ok=True)

    while True:  # 24/7 loop
        try:
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
            os.remove(file_name)
            print(f"Deleted: {file_name}")

            time.sleep(1)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    display_banner()
    create_edit_delete_file()