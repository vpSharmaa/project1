import time
import pyttsx3
import math
import os
import platform

APP_NAME = "Talking Calculator"
APP_VERSION = "2.0"
APP_AUTHOR = "Dr. Vedprakash Sharma"

# Clear screen depending on OS
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def show_banner():
    clear_screen()
    print("=" * 60)
    print(f" 🔊  {APP_NAME}  — Version {APP_VERSION}")
    print(f" 👤  Developed by {APP_AUTHOR}")
    print("=" * 60)
    print()

def show_disclaimer():
    print("""
⚠️  Caution!
This calculator uses a text-to-speech engine.

If voice does not work, install pyttsx3:

    pip install pyttsx3

Starting in 3 seconds...
""")
    time.sleep(3)
    clear_screen()

# Initialize TTS safely
try:
    engine = pyttsx3.init()
except:
    engine = None

# Global toggle for menu speech
SPEAK_MENU = False

def speak(text):
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            pass

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Numbers only.")
            speak("Invalid number. Try again.")

def menu():
    clear_screen()
    show_banner()

    print("Select an option:")
    print("=" * 40)
    print(" 1. ➕ Addition")
    print(" 2. ➖ Subtraction")
    print(" 3. ✖ Multiplication")
    print(" 4. ➗ Division")
    print(" 5. √  Square Root")
    print(" 6. 🔍 Prime Check")
    print(" 7. 🔊 Toggle Menu Voice (Current: {})".format(
        "ON" if SPEAK_MENU else "OFF"
    ))
    print(" 8. 🚪 Exit")
    print("=" * 40)

    if SPEAK_MENU:
        speak("Menu. Choose an option from one to eight.")

def calculator():
    global SPEAK_MENU

    speak("Welcome to the talking calculator.")

    while True:
        menu()
        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            n1 = get_number("Enter first number: ")
            n2 = get_number("Enter second number: ")
            result = n1 + n2
            print(f"Result = {result}")
            speak(f"The result is {result}")
            input("\nPress Enter to continue...")

        elif choice == "2":
            n1 = get_number("Enter first number: ")
            n2 = get_number("Enter second number: ")
            result = n1 - n2
            print(f"Result = {result}")
            speak(f"The result is {result}")
            input("\nPress Enter to continue...")

        elif choice == "3":
            n1 = get_number("Enter first number: ")
            n2 = get_number("Enter second number: ")
            result = n1 * n2
            print(f"Result = {result}")
            speak(f"The result is {result}")
            input("\nPress Enter to continue...")

        elif choice == "4":
            n1 = get_number("Enter numerator: ")
            n2 = get_number("Enter denominator: ")
            if n2 == 0:
                print("❌ Cannot divide by zero.")
                speak("Division by zero is not allowed.")
            else:
                result = n1 / n2
                print(f"Result = {result}")
                speak(f"The result is {result}")
            input("\nPress Enter to continue...")

        elif choice == "5":
            num = get_number("Enter a number: ")
            if num < 0:
                print("❌ Negative numbers have no real square root.")
                speak("Square root of a negative number is not real.")
            else:
                result = math.sqrt(num)
                print(f"Square root = {result}")
                speak(f"The square root is {result}")
            input("\nPress Enter to continue...")

        elif choice == "6":
            num = get_number("Enter an integer: ")
            if not num.is_integer():
                print("❌ Please enter a whole number.")
                speak("Prime check works only for integers.")
            else:
                n = int(num)
                if is_prime(n):
                    print(f"✔ {n} is a prime number.")
                    speak(f"{n} is a prime number.")
                else:
                    print(f"✘ {n} is not a prime number.")
                    speak(f"{n} is not a prime number.")
            input("\nPress Enter to continue...")

        elif choice == "7":
            SPEAK_MENU = not SPEAK_MENU
            print(f"🔊 Menu voice turned {'ON' if SPEAK_MENU else 'OFF'}.")
            speak("Menu voice turned on." if SPEAK_MENU else "Menu voice turned off.")
            time.sleep(1)

        elif choice == "8":
            speak("Thank you for using the Talking Calculator.")
            print("\nGoodbye!")
            time.sleep(2)
            break

        else:
            print("❌ Invalid option.")
            speak("Invalid option. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    show_banner()
    show_disclaimer()
    calculator()
