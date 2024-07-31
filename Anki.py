import tkinter as tk
import random

class Card:
    question: str
    answer_possibilities: list[str] = []
    correct_answer: str
    difficulty: int
    ANSWER_KEY = {"A": 0, "B": 1, "C": 2}

    def __init__(self, args: list[str]):
        self.question = args[0]
        self.answer_possibilities = args[1:4]
        self.correct_answer = args[-1]
        self.difficulty = int(args[-2])

    def print_question(self) -> None:
        print(self.question)
        print(f"A) {self.answer_possibilities[0]}  B) {self.answer_possibilities[1]}  C) {self.answer_possibilities[2]}")

    def is_correct(self, answer: str) -> bool:
        return answer == self.correct_answer

    def print_answer(self) -> str:
        return f"The right answer is: {self.correct_answer}"

    def update_difficult(self, new_difficulty: int) -> None:
        self.difficulty = new_difficulty

class Deck:
    cards: list[Card]
    total_points: int

    def __init__(self, filename):
        self.load_cards_from_file(filename)
        self.set_total_points()

    def load_cards_from_file(self, filename):
        l = []
        with open(filename, mode='r') as file:
            lines = file.readlines()
        lines = lines[1:]
        for line in lines:
            cols = line.strip().split(";")
            l.append(cols)

        self.cards = [Card(card_info) for card_info in l]

    def set_total_points(self):
        self.total_points = sum(card.difficulty for card in self.cards)
# Updates the Label text which is showing the Questions
def update_text(new_text):
    label.config(text=new_text)
    
# Checks if the Button which is pressed represents the right answer or not
def button_click(answer):
    result = "CORRECT" if current_card.is_correct(answer) else "INCORRECT"
    if result == "INCORRECT":
        result = result + " " + current_card.print_answer()
    update_text(result)
    # Wait for 2 seconds before showing the next question
    window.after(2000, next_question)  
# Select the next_question which will be ask
def next_question():
    global current_card, current_card_number
    current_card_number = get_unseen_card_number(len(deck.cards), viewed_cards)
    if current_card == -1:
        update_text("Thanks for playing")
    else:
        viewed_cards.append(current_card_number)
        current_card = deck.cards[current_card_number]
        update_question()
#Returns a Card which havent been asked
def get_unseen_card_number(total_cards, viewed_cards):
    if len(viewed_cards) == total_cards:
        return -1
    card_number = -1
    while card_number == -1 or card_number in viewed_cards:
        card_number = random.randint(0, total_cards - 1)
    return card_number
# Updates the whole GUI to represent the current Question with the possible Answers
def update_question():
    new_question=current_card.question
    label.config(text=new_question)
    A_button.config(text=current_card.answer_possibilities[0])
    B_button.config(text=current_card.answer_possibilities[1])
    C_button.config(text=current_card.answer_possibilities[2])

window = tk.Tk()
window.title("Anki")

deck = Deck("python.csv")
viewed_cards = []
current_card_number = get_unseen_card_number(len(deck.cards), viewed_cards)
viewed_cards.append(current_card_number)
current_card = deck.cards[current_card_number]

main_frame = tk.Frame(window)
main_frame.pack(expand=True)

label = tk.Label(main_frame, text=current_card.question, font=("Helvetica", 16))
label.pack(pady=20)

button_frame = tk.Frame(main_frame)
button_frame.pack()

A_button = tk.Button(button_frame, text=current_card.answer_possibilities[0], command=lambda: button_click("A"))
A_button.pack(side=tk.LEFT, padx=5)

B_button = tk.Button(button_frame, text=current_card.answer_possibilities[1], command=lambda: button_click("B"))
B_button.pack(side=tk.LEFT, padx=5)

C_button = tk.Button(button_frame, text=current_card.answer_possibilities[2], command=lambda: button_click("C"))
C_button.pack(side=tk.LEFT, padx=5)

main_frame.pack(expand=True, anchor='center')

tk.mainloop()
