from quiz_creator import QuizCreator
from colorama import init, Fore
import pyfiglet

def print_banner():
    init(autoreset=True)
    banner = pyfiglet.figlet_format("QUIZ CREATOR")
    print(Fore.YELLOW + banner)

def main():
    print_banner()
    quiz_creator = QuizCreator()
    quiz_creator.run()

if __name__ == "__main__":
    main()
