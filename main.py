from quiz_creator import QuizCreator
from quiz_answers import QuizTaker
from colorama import init, Fore
import pyfiglet

def print_banner():
    init(autoreset=True)
    banner = pyfiglet.figlet_format("QUIZ SYSTEM")
    print(Fore.CYAN + banner)

def show_menu():
    print(Fore.YELLOW + "\n=== QUIZ MENU ===")
    print("1. Create a Quiz")
    print("2. Take the Quiz")
    print("3. Exit")

def main():
    print_banner()

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            creator = QuizCreator()
            creator.run()

        elif choice == "2":
            taker = QuizTaker("questions_for_quiz.txt")
            taker.load_questions_from_file()
            taker.ask_questions()
            taker.show_results()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
