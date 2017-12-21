import random

class HigherLower():
    def __init__(self):
        self._goal = 0
        self._count = 3
        self._range = 0
    
    def user_interface(self):
        while True:
            if self._welcome():
                num_range = self._number_range()
                if self._play_game():
                    continue
            else:
                break

    def _welcome(self) -> bool:
        print("Welcome to Higher or Lower!")
        while True:
            reply = input("Would you like to play? y/n \n").strip()
            if reply.lower() == "y":
                self._count = 3
                return True
            elif reply.lower() == "n":
                return False
            else:
                print("That is not a valid response.")
                continue

    def _number_range(self) -> int:
        while True:
            print("Enter the highest number you want to guess to.")
            try:
                num = input().strip()
                self._range = int(num) + 1
                break
            except:
                print("That is not a valid number.")
                continue
            
    def _play_game(self):
        self._goal = random.randint(1, self._range)
        print("You have 3 tries to guess the number.")
        while True:
            try:
                num = int(input("What is your guess? \n").strip())
                if num not in range(self._range):
                    print("That number is not between 1 and {}.".format(self._range))
                elif self._goal == num:
                    print("You win!")
                    return True
                else:
                    self._count -= 1
                    if self._count != 0 and self._count > 0:
                        print("Incorrect! \nTries Left: {}".format(self._count))
                        continue
                    else:
                        print("You have run out of tries!")
                        print("The secret number was: {} \n".format(self._goal))
                        return True
            except:
                print("That entry is invalid.")
                continue

if __name__ == '__main__':
    HigherLower().user_interface()
