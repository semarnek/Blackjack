import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list_card):

    if len(list_card) == 2 and sum(list_card) == 21:
        return 0
    if sum(list_card) > 21 and 11 in list_card:
        list_card.remove(11)
        list_card.append(1)

    return sum(list_card)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack :("
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

user_cards = []
computer_cards = []
is_game_over = False
user_score = 0
computer_score = 0

for i in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
       is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"    Your final hand: {user_cards}, final score: {user_score}")
print(f"    Computer's hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))