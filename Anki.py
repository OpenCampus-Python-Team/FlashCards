


def read_answer() -> str:
    """
    Reads input from the user and validates it, by calling itself recursively.

    :returns: either "A", "B", "C" or "" when the question is skipped.
    """

    user_input = input("Which answer is correct? A, B, C? or press Enter to skip \n")

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
        # NOTE: input should be in format: ['What is the output of the following code snippet?', '10', '5', '25', '10']
        self.question = args[0]  # pos of question
        for i in range(0, 3):
            self.answer_possiblities.append(args[1+i])  # append answers to empty list
        self.correct_answer = args[-1]  # correct answer at last position in list
        self.difficulty = 0  # default value

    def print_question(self) -> None:
        # prints question
        print(self.question)

    def is_correct(self, answer: str) -> bool:
        # translates the answer with ANSWER_KEY, then checks if choosen answer is correct
        # returns bool
        return self.answer_possiblities[self.ANWSER_KEY[answer]] == self.correct_answer


    def print_answer(self) -> None:
        # prints answer
        print(self.correct_answer)

    def update_difficult(self, new_difficulty: int) -> None:
        # updates difficulty
        self.difficulty = new_difficulty
        

def from_file(filename) :
    l = []
    file = open(filename,mode='r')
    lines = file.readlines()
    file.close()
    directed = lines[0] == 'directed\n'
    lines = lines[1:]
    for line in lines:
        cols = line.strip().split(";")
        l.append(cols)
    return l
l = from_file("questions_edu.csv")
# List of Class of each card
list_of_cards = []
for i in range(0,len(l)):
    list_of_cards.append(Card(l[i]))
#list_of_cards[X].is_correct("A") would work because its working on a Class


# card = Card(['What is the output of the following code snippet?', '10', '5', '25', '10'])
# card.print_answer()
# print(card.is_correct("A"))
# card.update_difficult(5)
# print(card.difficulty)
# card.print_question()
