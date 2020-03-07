from random import shuffle


cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
shuffle(cards)

your_points = 0
dealler_points = 0 
move = 1
more = 'yes'

while more == 'yes':
    dealler_card = cards.pop()
    dealler_points += dealler_card
    
    
    your_cards = []
    if move == 1:
        for i in range(2):
            your_card = cards.pop()
            your_cards.append(your_card)
            your_points += your_card
    else:
        your_card = cards.pop()
        your_cards.append(your_card)
        your_points += your_card
  
  

    print(f'''
    ============
    POINTS:
    Nigga: {dealler_points}
    You: {your_points} 
    ============
    ''')

    if move == 1:
        print(f'You got cards with face value {your_cards[0]} and {your_cards[1]} ')
    else:
        print(f'You got cards with face value {your_cards[0]} ' )
    if your_points & dealler_points < 22:
        if your_points or dealler_points == 21:
            if your_points == 21:
                print('You win')
            if dealler_points == 21:
                print('You lose')
        elif your_points == dealler_points:
            print('draw')
            break
        elif your_points < dealler_points:
            print('You lose')
            break
        elif your_points > dealler_points:
            more = input('Else more? Yes or no\n' )
            if not more:
                if your_points > dealler_points:
                    print('You win')
                    break
    
    move += 1 
