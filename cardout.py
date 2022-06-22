from ast import MatchOr
from random import shuffle
from sys import platlibdir
from tracemalloc import start
from card import Card, Deck
from termcolor import colored
from pyfiglet import figlet_format as ff
import re
import time

def start_color(input, color):
    color = colored(input, color)
    return color

def changL(input):
    if input[0] == "d":
        change = input.replace("d", "♦")
        return change
    elif input[0] == "s":
        change = input.replace("s", "♤")
        return change
    elif input[0] == "c":
        change = input.replace("c", "♧")
        return change
    elif input[0] == "h":
        change = input.replace("h", "🖤")
        return change
    
def changS(input):
    if input[0] == "♦":
        change = input.replace("♦", "d")
        return change
    elif input[0] == "♤":
        change = input.replace("♤", "s")
        return change
    elif input[0] == "♧":
        change = input.replace("♧", "c")
        return change
    elif input[0] == "🖤":
        change = input.replace("🖤", "h")
        return change

def remove_space(input):
    pattern = re.compile(r'\b(\w+)\b', re.I)
    match = pattern.search(input)
    if match: 
        return match.group() 
    else:
        return "nothing"

def end_game(card_taken, computer_card):
    plu=0
    for i in card_taken:
        plu= plu + int(i[1:])
    plu2=0
    for i in computer_card: 
        plu2=plu2+ int(i[1:])
    if plu<plu2:
        gm=start_color("You win based on count of cards", "green")
        gm= ff(gm)
        return gm
    elif plu>plu2:
        gm=start_color("Computer win based on count of cards","green)")
        gm = ff(gm)
    else:
        gm= start_color("It was a draw based on count of cards","green")
        gm= ff(gm)
        return gm

def main():
    """Pick four cards"""
    """shuffle the deck"""
 
    while True:
        shuf=input("Shuffle card deck: ")
        shuf=remove_space(shuf)
        d= Deck()
        d.shuffle()
        if shuf=="shuffle":
            shuffled_Deck = d.general_market
            time.sleep(1)
            print(f"\nThis is the shuffled General Market/Deck of cards: {d.general_market}")
            print(f"Deck of {d.count()} cards\n")
            
            while True:
                card_taken=input("Pick your cards(4 each): ")
                card_taken = remove_space(card_taken)
                if card_taken== "4":
                    time.sleep(1)
                    card_taken= d.deal(card_taken)
                    yourcards= start_color("Your cards:","blue")
                    print(f"{yourcards} {card_taken}")
                    computer_card= d.deal(4)
                    compcards= start_color("Computer cards:","blue")
                    print(f"{compcards} {computer_card}")
                    time.sleep(1)
                    gm=start_color("General Market:","green")
                    print(f"\n{gm} {d.general_market}")
                    print(f"Deck of {d.count()} cards\n")
                    start_card= d.deal(1)
                    start= start_color("Starting card:","red")
                    time.sleep(2)
                    print(f"{start} {start_card}\n")
                    #change_cards_letter(card_taken, computer_card)
                    whotoplay= input("do you want to play first(y/n): ")
                    whotoplay = remove_space(whotoplay)
                    if whotoplay == "y":
                        while True:
                            card_taken= player_plays(computer_card, card_taken, start_card, d)
                            if len(card_taken) == 1:
                                print("You have last card")
                            elif len(card_taken)==0:
                                print("You won")
                                break
                            computer_card= comp_plays(computer_card, card_taken, start_card, d)
                            if len(computer_card)==1:
                                print("Computer has last card")
                                
                            elif len(computer_card)==0:
                                print("Computer wins")
                                break
                            if d.count()<=0:
                                
                                g= ff("Game ends, no more GENRAL MARKET")
                                print(g)
                                print(end_game(card_taken, computer_card))
                                break
                            gm=start_color("Gneral Market:", "green")
                            print(f"{gm} {d.general_market}\n",f"Deck of {d.count()} cards\n")  
                            
                    else:
                        while True: 
                            computer_card = comp_plays(computer_card, card_taken, start_card, d)
                            if len(computer_card)==1:
                                print("Computer has last card")
                                
                            elif len(computer_card)==0:
                                print("Computer wins")
                                break
                            
                            card_taken= player_plays(computer_card, card_taken, start_card, d)
                            
                            if len(card_taken) == 1:
                                print("You have last card")
                            elif len(card_taken)==0:
                                print("You won")
                                break
                            if d.count()<=0:
                                e = ff("Game ends, no more GENeRAL MARKET")
                                print(e)
                                print(end_game(card_taken, computer_card))
                                break

                            gm=start_color("Gneral Market:", "green")
                            print(f"{gm} {d.general_market}\n",f"Deck of {d.count()} cards\n")

                    
                    break
                else:
                    print("You are only allowed to pick 4 cards\n")
            break
        else:
            print("Makes sure to check the documentation above to see how the game works or check your spelling")

def value_do_sth(computer_card, card_taken, start_card, d, sym_p_card, accepted_card ):
    #for player's card
    if sym_p_card[1:]=="2":
        print("computer pick 2")
        cc=d.deal(2)
        for i in cc:
            computer_card.append(i)
    elif sym_p_card[1:]=="5":
        print("computer pick 5")
        cc=d.deal(5)
        for i in cc:
            computer_card.append(i)
    elif sym_p_card[1:]=="1":
        print("computer hold on")
        player_plays(computer_card, card_taken, start_card, d)
    elif sym_p_card[1:]=="8":
        print("skip computer")
        player_plays(computer_card, card_taken, start_card, d)
    elif sym_p_card[1:]=="14":
        print("computer pick from market")
        cc=d.deal(1)
        for i in cc:
            computer_card.append(i)

    #for computer card
    elif accepted_card[1:]== "2":
        print("you, pick 2")
        ct=d.deal(2)
        for i in ct:
            card_taken.append(i)
    elif accepted_card[1:]=="5":
        print("you, pick 3")
        ct=d.deal(3)
        for i in ct:
            card_taken.append(i)
    elif accepted_card[1:]=="1":
        print("hold on")
        comp_plays(computer_card, card_taken, start_card, d)
    elif accepted_card[1:]=="8":
        print("skip you")
        comp_plays(computer_card, card_taken, start_card, d)
    elif accepted_card[1:]=="14":
        print(" pick from market")
        cc=d.deal(1)
        for i in cc:
            card_taken.append(i)

def  player_plays(computer_card, card_taken, start_card, d):
    cards=[]

    time.sleep(1)
    while True:
        player_card= input("Play your card/take from GM if you don't have the card: \n")
        player_card = remove_space(player_card)
        if player_card == "GM" or player_card== "gm":
            takenew_card= d.deal(1)[0]
            card_taken.append(takenew_card)
            time.sleep(1)
            print(f"You didn't play any card")
            time.sleep(1)
            cu=start_color("Your present card(s):","blue")
            print(f"{cu} {card_taken}") 
            break
        else:
            sym_p_card= changL(player_card)
            if sym_p_card in card_taken:
                
                        if sym_p_card[0] == start_card[-1][0] or sym_p_card[1:] == start_card[-1][1:]:
                            accepted_card=""
                            
                            card_taken.remove(sym_p_card)
                            start_card.append(sym_p_card)
                            
                            time.sleep(1)
                            print(f"You played: {sym_p_card}")
                            value_do_sth(computer_card, card_taken, start_card, d, sym_p_card, accepted_card )
                            time.sleep(1)
                            yu= start_color("Your present card(s):","blue")
                            print(f"{yu} {card_taken}\n")
                            time.sleep(1)
                            cu=start_color("Continuing card:","red")
                            print(f"{cu} {start_card[-1]}")
                            break
                        else:
                            print("Make sure your cards are identitical to the start card")
       
            else:
                print("Make sure that you have written your card well and it is within your card you have presently.")
    return card_taken

    
def comp_plays(computer_card, card_taken, start_card, d):
    elig_cards=[]
    accepted_card=""
    for i in computer_card:
        if i[0] == start_card[-1][0] or i[1:] == start_card[-1][1:]:
            elig_cards.append(i)
    if elig_cards==[]:
        takenew_card=d.deal(1)[0]
        computer_card.append(takenew_card)
        time.sleep(1)
        print("\nThe Computer picks from General market")
    else:
        for i in elig_cards:
            if i[1:]== "5":
                accepted_card= i
            elif i[1:] == "2":
                accepted_card= i
            elif i[1:] == "1":
                accepted_card= i
            elif i[1:] == "8":
                accepted_card=i
            elif i[1:] =="14":
                accepted_card=i
            else:
                accepted_card = i
    if accepted_card:
        sym_p_card=""
        computer_card.remove(accepted_card)
        time.sleep(1)
        print(f"\ncomputer plays: {accepted_card}\n ")
        start_card.append(accepted_card)
        value_do_sth(computer_card, card_taken, start_card, d, sym_p_card, accepted_card )
        yu= start_color("Your present card(s):","blue")
        print(f"{yu} {card_taken}")
        
    cu=start_color("Continuing card:", "red")
    
    print(f"{cu} {start_card[-1]}")
    time.sleep(1)
    su=start_color("Computer cards:", "blue")
    
    return computer_card

def change_cards_letter(card_taken, computer_card):
    """each player palays"""
    card_taken_letter= []
    computer_card_letter= []
    for i in card_taken:
        new = changS(i)
        card_taken_letter.append(new)
    for i in computer_card:
        new = changS(i)
        computer_card_letter.append(new)
    print(card_taken_letter)
    print(computer_card_letter)
    change_cards_symbols(card_taken_letter, computer_card_letter)

def change_cards_symbols(card_taken_letter, computer_card_letter):
    #change back to symbol
    card_taken=[]
    computer_card=[]
    for i in card_taken_letter:
        new = changL(i)
        card_taken.append(new)
    for i in computer_card_letter:
        new = changL(i)
        computer_card.append(new) 
    print(card_taken)
    print(computer_card)


def printCard():
    print(colored(ff("Card Game\n"), "red"))
    print("Symbols: ", "Diamonds- ♦️♦️♦️", "Spades- ♠️♠️♠️", "Clubs- ♣️♣️♣️", "Heart- ❤️❤️❤️\n")
    print("Quick thing to know: \n")
    
    start= "To start the game, type 'start'\n"
    quit= "To quit the game, type 'quit'\n"
    shuffle= "To shuffle the card, type 'shuffle'\n"
    pick= "To pick your cards write the number of card to pick\n"
    play= "To play a card type 's1-' for spade with a no 1 and 's2-' for spade with a no 2 and continue in that pattern\n 'd1-' for diamond with a no 1 and 'd2-' for diamond with a no 2 and continue in that pattern\n'h1-' for heart with a no 1 and 'h2-' for heart with a no 2 and continue in that pattern\n'c1-' for club with a no 1 and 'c2-' for club with a no 2 and continue in that pattern\n\n"
    havenot= "If you don't have the card, type 'GM' to take from general market"
    print("Note: All ways to call something to work must be written exactly how you have been told to write it above\n")
    
    time.sleep(0.3)
    print(start)
    time.sleep(0.3)
    print(quit)
    time.sleep(0.3)
    print(shuffle)
    time.sleep(0.3)
    print(pick)
    time.sleep(0.3)
    print(play)
    time.sleep(0.3)
    print(havenot)
    one="What the numbers mean: 1- hold on (meaning the player can play again as long as he plays a card with the number 1\n"
    two= "2- Pick two (this means that the player that is to play next when the card with the number 2 is played should pick two cards from the general market/Deck of cards and musn't play\n"
    three= "3- Pick three (this means that the player that is to play next when the card with the number 3 is played should pick three cards from the general market/Deck of cards and musn't play\n"
    five="5- Pick five (this means that the player that is to play next when the card with the number 5 is played should pick five cards from the general market/Deck of cards and musn't play\n"
    eight= "8- skip you (this means that the player that is to play next will be skip\n"
    fourteen= "14- Go to general market (this means that the player that is to play next when the card with the number 14 is played should pick a card from the general market/Deck of cards and musn't play\n"
    time.sleep(2)
    print(one)
    time.sleep(0.3)
    print(two)
    time.sleep(0.3)
    print(three)
    time.sleep(0.3)
    print(five)
    time.sleep(0.3)
    print(eight)
    time.sleep(0.3)
    print(fourteen)
    time.sleep(0.3)
    G= Deck()
    Gm=G.general_market
    print(f"General Market/Deck of cards: {Gm}\n")
    time.sleep(2)
    print(colored(ff("Start Game\n"), "red"))
    main()





printCard()

