# This project was completed by me (Sofia Riojas) for CS50.
# guidance from ChatGPT (for structure and suggestions),
# but I wrote and understand all the code submitted.

import csv
from datetime import datetime

FILENAME = "journal.csv"

def add_entry():
    date = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    food = input("What did you eat? ").strip()
    mood = input("How did you feel afterward? ").strip()

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, food, mood])
    print("✅ Entry added!\n")

def view_entries():
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            print("\n📘 Mood + Food Journal Entries:")
            for row in reader:
                print(f"📅 {row[0]} | 🍽️ {row[1]} | 🙂 {row[2]}")
    except FileNotFoundError:
        print("No entries yet! Add one first.\n")

def main():
    print("Welcome to Mood + Food Journal 🥗🧠")
    while True:
        print("\nOptions:")
        print("1. Add a new entry")
        print("2. View all entries")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
