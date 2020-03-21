from random import shuffle, choise 


def get_deck():
    deck = []

    for suit in ('Diamonds' 'Hearts' 'Spades' 'Clubs'):
        for card in range(2,11):
            deck.append(f'{card} {suit}')
            for card in ('jack' , 'lady' , 'king', 'ace'):
            deck.append(f'{card} {suit}')
    shuffle(deck)
    return deck 

def get_card_points(card):
    card_name = card.split()
    card_points = {}

    for card_point in range (2,11)
        card_points[f'{card_point}'] = card_point
    for card_point in ('jack' , 'lady' , 'king')
        card_points[f'{card_point}'] = 10
    card_points['ace'] = choise([1,11])

    return card_points[card_name[0]]


        
your_points = 0
dealler_points = 0 
move = 1
more = 'yes'

while more == 'yes':
    if move == 1:
        dealler_card = cards.pop()
        dealler_points += dealler_card
    
    
        your_cards = []
    
        for i in range(2):
            your_card = cards.pop()
            your_cards.append(your_card)
            your_points += your_card
    else:
        your_card = cards.pop()
        your_points += your_card
  
  
  
    print(f'''
        ============
        POINTS:
        Nigga: {dealler_points}
        You: {your_points} 
        ============

        Nigga got cards with face value {dealler_card} 
        ''')
        

    if move == 1:
        print(f'You got cards with face value {your_cards[0]} and {your_cards[1]} ')
    else:
        print(f'You got cards with face value {your_cards} ' )

    if your_points & dealler_points < 22:
        if your_points == 21:
            more = 'no'
        else:
            more = input('more? yes or no\n')
    
        move += 1 
    else:
        print('over drow')
        break  
else:
    while dealler_points < 18:
        dealler_card = cards.pop()
        dealler_points += dealler_card
        
        print(f'''
    ============
    POINTS:
    Nigga: {dealler_points}
    You: {your_points} 
    ============

    Nigga got cards with face value {dealler_card} 
    ''')

    if your_points == dealler_points:
        print('draw')
    elif your_points > dealler_points:
        print('you win')
    elif your_points == 21:
        print('you win')
    elif dealler_points > 21:
        print('you win')
    else:
        print('you lose')