# Personal Diary Program
# This program creats a simple personal diary.

def add_entry():
    """
    Add a new diary entry.
    Input: Takes diary content from the user.
    Output: Appends the entry to a file with a timestamp.
    """

    entry = input("How was the day today? Write it down: ")

    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"📅 {current_time}\n")
        file.write(f"📑 {entry}\n")
        file.write(f"-" * 50 + "\n")

        print("✅ Entry saved successfully!")

def read_diary():
    """
    Read previous diary entries
    """
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                print("\n" + "="*60)
                print("📅 YOUR DIARY:")
                print("="*60)
                print(content)
            else:
                print("❌ Your diary is still empty!")
    except FileNotFoundError:
        print("❌ No entries yet. Add your first entry!")

def main():
    """
    Main function that runs the diary program.
    """
    while True:
        print("\n" + "⭐"*2)
        print("WELCOME TO PERSONAL DIARY")
        print("⭐"*2)
        print("1. Add a new entry")
        print("2. Read Previous entries")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            read_diary()
        elif choice == "3":
            print("Thank you! See you again!")
            break
        else:
            print("Invalid choice! Enter 1, 2 or 3")

if __name__ == "__main__":
    main()


