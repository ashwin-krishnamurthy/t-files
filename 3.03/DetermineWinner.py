#Kawika tuple
#Intro to CS 
#4 March 2019

player1_name = input("what is player 1's name?")
P1_score = 0
player2_name = input("what is player 2's name?")
P2_score = 0
Win = False

# name: shuffle
# purpose: will return a shuffled deck to the user
# input:
# returns: a list representing a shuffled deck
import random
def shuffle():
  basic_deck = []
  basic_deck = list(range(2, 15)) * 4
  random.shuffle(basic_deck)
  return list(basic_deck)
shuffled_deck = shuffle()


# name: player_turn
# purpose: takes in a player name and draws/removes a card from the deck, prints "user drew card x", and returns the value
# input: player_name as string, deck as list
# returns: integers
def player_turn(name1,deck):
  print(name1 + " drew card " + str(deck[0]))
  print (deck)
  a = deck.pop(0)
  return a

# name: compare_values
# purpose: will compare the two cards drawn by the players
# input:p1 and p2's cards
# returns: the winner
def compare_values(a,b):
  global player1_name
  global player2_name
  if a == b:
    print("Both of you drew the same card, we have WAR!")
    return ("WAR")
  elif a > b:
    return (player1_name)
  else:
    return (player2_name)
  

while len(shuffled_deck) != 0:

  if compare_values(shuffled_deck[0],shuffled_deck[1]) == "WAR":
    shuffled_deck.pop(shuffled_deck[0])
    shuffled_deck.pop(shuffled_deck[0])
    compare_values(shuffled_deck[0],shuffled_deck[1])
    compare_values(shuffled_deck.pop(shuffled_deck[0]),shuffled_deck.pop(shuffled_deck[1]))
  else:
    k = player_turn(player1_name,shuffled_deck)
    l = player_turn(player2_name,shuffled_deck)
    if compare_values(k,l) == player1_name:
      print(player1_name + " has the higher card")
      P1_score = P1_score + 2
    elif compare_values(k,l) == player2_name:
      print(player2_name + " has the higher card")
      P2_score = P2_score + 2
    print(player1_name + ": " + str(P1_score))
    print(player2_name + ": " + str(P2_score))
    shuffled_deck.pop(0)
    shuffled_deck.pop(0)
  yolo = input("")
    
  if len(shuffled_deck) == 0:
    if P1_score > P2_score:
      print("Congrats to our winner " + player1_name)
      print("You won with a score of " + str(P1_score) + " compared to " + player2_name + "'s " + str(P2_score) + " points")

