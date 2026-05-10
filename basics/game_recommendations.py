def main():
    difficulty = input("Difficult or Casual ?").lower()
    if difficulty not in ["difficult", "casual"]:
        print("Enter a valid difficulty ")
        return
    
    players = input("Multiplayer or Singleplayer ?").lower()
    if players not in ["multiplayer", "singleplayer"]:
        print("Enter a valid amount of players")
        return
    
    if difficulty ==  "difficult" and players == "multiplayer":
        recommend("Poker")
    elif difficulty == "difficult" and players == "singleplayer":
        recommend("Klondike")
    elif difficulty == "casual" and players == "multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")
    
def recommend(game):
    print("You might like", game)
    
main()

#code for DM, DS, CM then CS(off case)
#DM-Difficult&Multiplayer Poker, DS-Difficult&Casual Klondike, CM -Casual&Multiplayer Hearts, CS(Casual&Singleelse )-Clock 