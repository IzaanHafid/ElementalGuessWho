from random import sample, choice
from time import sleep as wait
from periodicTable import elements, makeBoard, formatBoard, findLocation, findElement, findSpecificElementInfo, \
    findElementInfo, fromIdxConverter

error = 0

print("Welcome to Elemental Guess Who")
# Choice 1: Game mode Selection
while True:
    print("1. 2 Player (Pass & Play)\n2. How to Play\n3. Exit")
    try:
        choice_input = int(input("> "))
        if not choice_input in range(1, 4):
            print("Invalid Choice; Choices: 1, 2, 3")
        else:
            # 2 Player

            if choice_input == 1:

                rE = sample(elements, 25)
                randomElements = []
                for dictionary in rE:
                    randomElements.append(dictionary["symbol"])

                sysBoard1 = makeBoard(randomElements)
                board1 = makeBoard(randomElements)
                formattedBoard1 = formatBoard(board1)
                card1 = choice(randomElements)

                sysBoard2 = makeBoard(randomElements)
                board2 = makeBoard(randomElements)
                formattedBoard2 = formatBoard(board2)
                card2 = choice(randomElements)

                win = False

                print("PASS THE DEVICE TO PLAYER 1")
                wait(3)
                print(f"This is your board, Your Card is {findSpecificElementInfo('symbol', card1, 'name')} ({card1}) located at {findLocation(sysBoard1, 'symbol', card1)}")
                wait(1)
                print(formattedBoard1)
                wait(2.5)
                print('\n' * 50)
                print("PASS THE DEVICE TO PLAYER 2")
                wait(3)
                print(f"This is your board, Your Card is {findSpecificElementInfo('symbol', card2, 'name')} ({card2}) located at {findLocation(sysBoard2, 'symbol', card2)}")
                wait(1)
                print(formattedBoard2)
                wait(2.5)
                print('\n' * 50)
                print("PASS THE DEVICE TO PLAYER 1")
                wait(3)

                while not win:
                    print(f"This is your board. Ask the other player about their element by typing your question here.")
                    print(formattedBoard1)
                    wait(1)
                    error = 3
                    while error == 3:
                        print("PLAYER 1")
                        q1 = input("Ask a Question: ")
                        wait(0.5)
                        print('\n' * 50)
                        print("PASS THE DEVICE TO PLAYER 2")
                        wait(3)
                        error = 1
                        while error == 1:
                            print(f"Player 1 Asked: {q1}\nChoices: 1. Yes 2. No 3. I Dont Understand\n")
                            print(f"Your Element is {findSpecificElementInfo('symbol', card2, 'name')} ({card2})")
                            print("(type 'info' if you want information about your element.)\n")
                            response = input("> ")
                            if response == '1':
                                r2 = "Yes."
                                error = 0
                            elif response == '2':
                                r2 = "No"
                                error = 0
                            elif response == '3':
                                r2 = "I Dont Understand"
                                wait(3)
                                print("PASS DEVICE TO PLAYER 1")
                                error = 3
                            elif response == 'info': print(f'{findElementInfo(card2)}\n\n')
                            else: print("Error; Respond Again.")
                    wait(0.5)
                    print('\n' * 50)
                    print("PASS THE DEVICE TO PLAYER 1")
                    wait(3)
                    print(f"You asked Player 2: {q1}")
                    wait(1)
                    print(f"Player 2 responded {r2}")
                    wait(1.5)
                    error = 1
                    print("\n\nYOU ARE NOW IN SELECT MODE. TO SELECT A CARD. TYPE ITS COORDINATE (A3, B2, E4).\nTO "
                          "PASS THE TURN, TYPE 'PASS'")
                    while error == 1:
                        print(formattedBoard1)
                        selectInput = input("> ").upper()
                        if selectInput == 'PASS':
                            error = 0
                            break
                        selectInput = list(selectInput)
                        if len(selectInput) != 2: print("Value must have 2 characters")
                        if selectInput[0] not in ['A', 'B', 'C', 'D', 'E']: print("Error; Invalid Column Identifier.")
                        else:
                            if selectInput[1] not in ['1', '2', '3', '4', '5']: print("Error; Invalid Row Identifier.")
                            else:
                                cardCol = fromIdxConverter('col', selectInput[0])
                                cardRow = fromIdxConverter('row', selectInput[1])
                                card = findElement(sysBoard1, cardCol, cardRow)
                                print(f"Card {''.join(selectInput)}: {findSpecificElementInfo('symbol', card, 'name')}")
                                print("What would you like to do?\n1. Flip Card\n2. Info\n3. Guess Card\n4. Cancel")
                                try:
                                    cardChoice = int(input("> "))
                                except ValueError:
                                    print("Invalid Choice; Choices: 1, 2, 3, 4")
                                    continue
                                if cardChoice not in [1, 2, 3, 4]:
                                    print("Invalid Choice; Choices: 1, 2, 3, 4")
                                    continue
                                if cardChoice == 1:
                                    if board1[cardRow][cardCol] != '-':
                                        board1[cardRow][cardCol] = '-'
                                        formattedBoard1 = formatBoard(board1)
                                        print("Card Flipped")
                                    else:
                                        board1[cardRow][cardCol] = sysBoard1[cardRow][cardCol]
                                        formattedBoard1 = formatBoard(board1)
                                        print("Card Unflipped")
                                elif cardChoice == 2:
                                    if board1[cardRow][cardCol] == '-': print("DISCLAIMER: THIS CARD IS FLIPPED")
                                    print(findElementInfo(sysBoard1[cardRow][cardCol]))
                                elif cardChoice == 3:
                                    print(f"Are you sure you want to guess {sysBoard1[cardRow][cardCol]}?")
                                    print("Yes/No")
                                    confirmation = input("> ").lower()
                                    if confirmation == 'yes':
                                        print(f"You have guessed card {''.join(selectInput)}: {findSpecificElementInfo('symbol', sysBoard1[cardRow][cardCol], 'name')}")
                                        wait(1)
                                        print("And you are...")
                                        wait(2)
                                        if sysBoard1[cardRow][cardCol] == card2:
                                            print("CORRECT!!")
                                            wait(1)
                                            print("PLAYER 1 WINS THE GAME.")
                                            error = 0
                                            win = True
                                            break
                                        else:
                                            print("Wrong...")
                                            wait(1.5)
                                            board1[cardRow][cardCol] = '-'
                                            print('\n' * 50)
                                            wait(3)
                                            error = 0
                    if win:
                        break
                    print('\n' * 50)
                    print("PASS THE DEVICE TO PLAYER 2")
                    wait(3)
                    print(f"This is your board. Ask the other player about their element by typing your question here")
                    print(formattedBoard2)
                    wait(1)
                    error = 3
                    while error == 3:
                        print("PLAYER 2")
                        q2 = input("Ask a Question: ")
                        print('\n' * 50)
                        print("PASS THE DEVICE TO PLAYER 1")
                        error = 1
                        while error == 1:
                            wait(3)
                            print(f"Player 2 Asked: {q2}\nChoices: 1. Yes 2. No 3. I Dont Understand\n")
                            print(f"Your Element is {findSpecificElementInfo('symbol', card1, 'name')} ({card1})")
                            print("(type 'info' if you want information about your element.)\n")
                            response = input("> ")
                            if response == '1':
                                r1 = "Yes."
                                error = 0
                            elif response == '2':
                                r1 = "No"
                                error = 0
                            elif response == '3':
                                r1 = "I Dont Understand"
                                print("PASS DEVICE TO PLAYER 2")
                                wait(3)
                                error = 3
                            elif response == 'info':
                                print(f'{findElementInfo(card1)}\n\n')
                            else:
                                print("Error; Respond Again.")
                    print('\n' * 50)
                    print("PASS THE DEVICE TO PLAYER 2")
                    wait(3)
                    print(f"You asked Player 1: {q2}")
                    wait(1)
                    print(f"Player 1 responded {r1}")
                    wait(1.5)
                    error = 1
                    print("\n\nYOU ARE NOW IN SELECT MODE. TO SELECT A CARD. TYPE ITS COORDINATE (A3, B2, E4).\nTO "
                          "PASS THE TURN, TYPE 'PASS'")
                    while error == 1:
                        print(formattedBoard2)
                        selectInput = input("> ").upper()
                        if selectInput == 'PASS':
                            error = 0
                            break
                        selectInput = list(selectInput)
                        if len(selectInput) != 2: print("Value must have 2 characters")
                        if selectInput[0] not in ['A', 'B', 'C', 'D', 'E']:
                            print("Error; Invalid Column Identifier.")
                        else:
                            if selectInput[1] not in ['1', '2', '3', '4', '5']:
                                print("Error; Invalid Row Identifier.")
                            else:
                                cardCol = fromIdxConverter('col', selectInput[0])
                                cardRow = fromIdxConverter('row', selectInput[1])
                                card = findElement(sysBoard2, cardCol, cardRow)
                                print(f"Card {''.join(selectInput)}: {findSpecificElementInfo('symbol', card, 'name')}")
                                print("What would you like to do?\n1. Flip Card\n2. Info\n3. Guess Card\n4. Cancel")
                                try:
                                    cardChoice = int(input("> "))
                                except ValueError:
                                    print("Invalid Choice; Choices: 1, 2, 3, 4")
                                    continue
                                if cardChoice not in [1, 2, 3, 4]:
                                    print("Invalid Choice; Choices: 1, 2, 3, 4")
                                    continue
                                if cardChoice == 1:
                                    if board2[cardRow][cardCol] != '-':
                                        board2[cardRow][cardCol] = '-'
                                        formattedBoard2 = formatBoard(board2)
                                        print("Card Flipped")
                                    else:
                                        board2[cardRow][cardCol] = sysBoard2[cardRow][cardCol]
                                        formattedBoard2 = formatBoard(board2)
                                        print("Card Unflipped")
                                elif cardChoice == 2:
                                    if board2[cardRow][cardCol] == '-': print("DISCLAIMER: THIS CARD IS FLIPPED")
                                    print(findElementInfo(sysBoard2[cardRow][cardCol]))
                                elif cardChoice == 3:
                                    print(f"Are you sure you want to guess {findSpecificElementInfo('symbol', sysBoard2[cardRow][cardCol], 'name')}?")
                                    print("Yes/No")
                                    confirmation = input("> ").lower()
                                    if confirmation == 'yes':
                                        print(
                                            f"You have guessed card {''.join(selectInput)}: {findSpecificElementInfo('symbol', sysBoard2[cardRow][cardCol], 'name')}")
                                        wait(1)
                                        print("And you are...")
                                        wait(2)
                                        if sysBoard2[cardRow][cardCol] == card1:
                                            print("CORRECT!!")
                                            wait(1)
                                            print("PLAYER 2 WINS THE GAME.")
                                            error = 0
                                            win = True
                                            break
                                        else:
                                            print("Wrong...")
                                            wait(1.5)
                                            board2[cardRow][cardCol] = '-'
                                            print('\n' * 50)
                                            print("PASS THE DEVICE TO PLAYER 1")
                                            wait(3)
                                            error = 0
                    if win:
                        break


            # How to Play

            elif choice_input == 2:
                print("""To play Elemental Guess Who, each player is given a 5x5 Board with Elements. Players take turns asking
Yes or No Questions relating to the Elements Physical/Chemical Properties. After every question, players eliminate all
elements which do not fit the criteria of the question. Once any player is confident with their answer, they may guess
An Element. If they are right, they win, otherwise, play continues.""")
                wait(1)
                print("""To select a card, use the coordinates located at the side of the board. (A-E columns; 1-5 rows) (A3, C4, D5)\n
After selecting a card, you may either flip the card to eliminate it, get information about the element, or guess the card.""")

            # Quit

            else:
                quit()

    except ValueError: print("Invalid Choice; Choices: 1, 2, 3")
