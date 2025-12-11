import time
import pyttsx3
import math
import os
import platform

### HELPER CLASS FOR TTS
class ttsHelper:
    def __init__(self, speak_menu):
        try:
            self.engine = pyttsx3.init()
            self.speak_menu = speak_menu
        except:
            raise

    def toggleSpeakMenu(self):
        self.speak_menu = False if self.speak_menu else True

    
    def speak(self, text):
        if self.engine:
            self.engine.say(text)
            self.engine.runAndWait()

class DisplayHelper():
    def __init__(self):
        self.app_name = "Talking Calculator"
        self.app_version = "2.0"
        self.author = "Dr. Vedprakash Sharma"

    # Clear screen depending on OS
    def clear_screen(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def show_banner(self):
        self.clear_screen()
        print("=" * 60)
        print(f"{self.app_name}. Version {self.app_version}")
        print(f" Developed by {self.author}")
        print("=" * 60)
        print()

    def show_disclaimer(self):
        print("""Caution! This calculator uses a text-to-speech engine. Starting in 3 seconds...""")
        time.sleep(3)
        self.clear_screen()


class Calculator:
    def __init__(self, displayHelper, ttsHelper):
        self.display = displayHelper
        self.tts = ttsHelper

    def showOperations(self):
        self.display.clear_screen()
        self.display.show_banner()

        print("Select an option:")
        print("=" * 40)
        print(" 1. Addition")
        print(" 2. Subtraction")
        print(" 3. Multiplication")
        print(" 4. Division")
        print(" 5. Square Root")
        print(" 6. Prime Check")
        print(" 7. Toggle Menu Voice (Current: {})".format("ON" if self.tts.speak_menu else "OFF"))
        print(" 8. Exit")
        print("=" * 40)

        if self.tts.speak_menu:
            self.tts.speak("Menu. Choose an option from one to eight.")

    def printAndSpeakResult(self, result):
        print(f"Result = {result}")
        self.tts.speak(f"The result is {result}")
        input("\nPress Enter to continue...")

    # Check if input is prime
    def is_prime(self, n):
        if n <= 1 or n % 2 == 0 or n % 3 == 0:
            return False
        if n <= 3:
            return True
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Numbers only.")
                self.tts.speak("Invalid number. Try again.")


    def run(self):
        while True:
            self.showOperations()
            choice = input("Enter choice (1-8): ").strip()

            if choice == "1":
                n1 = self.get_number("Enter first number: ")
                n2 = self.get_number("Enter second number: ")
                result = n1 + n2
                self.printAndSpeakResult(result)

            elif choice == "2":
                n1 = self.get_number("Enter first number: ")
                n2 = self.get_number("Enter second number: ")
                result = n1 - n2
                self.printAndSpeakResult(result)

            elif choice == "3":
                n1 = self.get_number("Enter first number: ")
                n2 = self.get_number("Enter second number: ")
                result = n1 * n2
                self.printAndSpeakResult(result)

            elif choice == "4":
                n1 = self.get_number("Enter numerator: ")
                n2 = self.get_number("Enter denominator: ")
                if n2 == 0:
                    print("Cannot divide by zero.")
                    self.tts.speak("Division by zero is not allowed.")
                    input("\nPress Enter to continue...")
                else:
                    result = n1 / n2
                    self.printAndSpeakResult(result)

            elif choice == "5":
                num = self.get_number("Enter a number: ")
                if num < 0:
                    print("Negative numbers have no real square root.")
                    self.tts.speak("Square root of a negative number is not real.")
                    input("\nPress Enter to continue...")
                else:
                    result = math.sqrt(num)
                    self.printAndSpeakResult(result)

            elif choice == "6":
                num = self.get_number("Enter an integer: ")
                if not num.is_integer():
                    print("Please enter a whole number.")
                    self.tts.speak("Prime check works only for integers.")
                else:
                    n = int(num)
                    if self.is_prime(n):
                        print(f"{n} is a prime number.")
                        self.tts.speak(f"{n} is a prime number.")
                    else:
                        print(f"✘ {n} is not a prime number.")
                        self.tts.speak(f"{n} is not a prime number.")
                input("\nPress Enter to continue...")

            elif choice == "7":
                self.tts.toggleSpeakMenu()
                print(f"Menu voice turned {'ON' if self.tts.speak_menu else 'OFF'}.")
                self.tts.speak("Menu voice turned on." if tts.speak_menu else "Menu voice turned off.")
                time.sleep(1)

            elif choice == "8":
                self.tts.speak("Thank you for using talking calculator.")
                print("\nGoodbye!")
                time.sleep(2)
                break

            else:
                print("Invalid option.")
                self.tts.speak("Invalid option. Try again.")
                time.sleep(1)

if __name__ == "__main__":
    display = DisplayHelper() # Init display helper
    tts = ttsHelper(False) # Init TTS

    tts.speak("Welcome to the talking calculator.")

    display.show_banner()
    display.show_disclaimer()
    calculator = Calculator(displayHelper=display, ttsHelper=tts)
    calculator.run()