import random
def read_answer() -> str:
    """
    Reads input from the user and validates it, by calling itself recursively.

    :returns: either "A", "B", "C" or "" when the question is skipped.
    """

    user_input = input("Which answer is correct? A, B, C? or press Enter to skip \n").upper()

    if user_input not in ["A", "B", "C", ""]:
        print("Please only enter A, B, C or press Enter to skip \n")
        return read_answer()

    return user_input


class Card:
    # class atributes
    question: str
    answer_possiblities: list[str] = []
    correct_answer: str
    difficulty: int
    ANWSER_KEY = {"A": 0, "B": 1, "C": 2}

    # constructor
    def __init__(self, args: list[str]):
        help_l = []
        # NOTE: input should be in format: ['What is the output of the following code snippet?', '10', '5', '25', '10']
        self.question = args[0]  # pos of question
        for i in range(0, 3):
            help_l.append(args[1+i])
        self.answer_possiblities.append(help_l)  # append answers to empty list
        self.correct_answer = args[-1]  # correct answer at last position in list
        # self.difficulty = 0  # default value
        self.difficulty = int(args[-2])

    def print_question(self,card) -> None:
        # prints question
        print(self.question)
        #print(len(self.answer_possiblities))
        print(f"A) {self.answer_possiblities[card][0]}  B) {self.answer_possiblities[card][1]}  C) {self.answer_possiblities[card][2]}")

    def is_correct(self, answer: str) -> bool:
        # translates the answer with ANSWER_KEY, then checks if choosen answer is correct
        # returns bool
        # return self.answer_possiblities[self.ANWSER_KEY[answer]] == self.correct_answer
        return answer == self.correct_answer


    def print_answer(self) -> None:
        # prints answer
        print(f"The right answer is: {self.correct_answer}")

    def update_difficult(self, new_difficulty: int) -> None:
        # updates difficulty
        self.difficulty = new_difficulty

class Deck:
    # class attributes
    cards: list[Card]
    total_points: int

    # constructor
    def __init__(self, filename):
        # NOTE: input should be in format: ['What is the output of the following code snippet?', '10', '5', '25', '5','10']
        self.load_cards_from_file(filename)
        self.total_points = 0
        for card in self.cards:
            self.total_points += card.difficulty

    def load_cards_from_file(self, filename):
        l = []
        file = open(filename ,mode='r')
        lines = file.readlines()
        file.close()
        directed = lines[0] == 'directed\n'
        lines = lines[1:]
        for line in lines:
            cols = line.strip().split(";")
            l.append(cols)

        # List of Class of each card
        self.cards = []
        for i in range(0 ,len(l)):
            self.cards.append(Card(l[i]))
        # list_of_cards[X].is_correct("A") would work because its working on a Class


def study():
    score = 0
    keep_going = True
    #cards_counter = 1# 0 because we start with the Card 1 which is in the Programm the 0 and
    current_card_number = 0
    deck = Deck("questions_edu.csv")
    while keep_going:
        current_card_number = random.randint(0,len(deck.cards)-1)
        current_card = deck.cards[current_card_number]
        print(f"CARD No.{current_card_number}")
        print(f"Card difficulty: {current_card.difficulty}")
        current_card.print_question(current_card_number)
        answer = read_answer()
        is_correct = current_card.is_correct(answer)
        result = "CORRECT" if is_correct else "INCORRECT"
        print(f'Your answer is {result}.')

        if is_correct:
            score += current_card.difficulty
        else:
            current_card.print_answer()
        print("\n")
        Continue = input("Want to continue ? press Enter for yes and Type n for no \n")
        if Continue == "n":
            keep_going = False
        
    grade = (score / deck.total_points) * 100
    score_out_of = f"{score} out of {deck.total_points}"
    if grade > 80:
        print(f"Congratulations! Your final score is: {score_out_of}.")
    elif grade > 70:
        print(f"You did a good job! Your final score is: {score_out_of}.")
    elif grade > 60:
        print(f"You passed! Your final score is: {score_out_of}.")
    else:
        print(f"You need to study more. Your final score is: {score_out_of}.")

study()

card = Card(['What is the output of the following code snippet?', '10', '5', '25', 2, 'A'])
card.update_difficult(5)
print(f"Card difficulty: {card.difficulty}")
card.print_question(0)
answer = read_answer()
is_correct = card.is_correct(answer)
result = "CORRECT" if is_correct else "INCORRECT"
print(f'Your answer is {result}.')