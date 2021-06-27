assets = ["John","Mason","Noah","Mike","Helen","Sadie","Imposter","Innocent"]
remainingPlayers = ["John","Mason","Noah","Mike","Helen","Sadie"]
impostorSee = ["John","Mason","Noah","Mike","Helen","Sadie"]

import random,time,keyboard,colorama
from colorama import Fore, Back, Style, init
colorama.init()

Loop = True

impWon = 0

dead = 5

devmode = 0 

thenumber = str(0)

player = (random.randrange(1,6))

charImpostor = (random.randrange(1,6))

char = assets[player] #Us ^

impostor = assets[charImpostor] #The Imposter ^

impostorSee.remove(impostor)

quit = 0

innocentWon = 0

if char in impostor:
  innocent = 0
  role = assets[6]
  print(Fore.YELLOW + "You are "+Fore.WHITE +char+ Fore.YELLOW+", and you are the"+Fore.RED + f" {role}"+Style.RESET_ALL)
else:
  innocent = 1
  role = assets[7]
  print(Fore.YELLOW + "You are "+Fore.WHITE +char+ Fore.YELLOW+", and you are"+Fore.GREEN + f" {role}"+Style.RESET_ALL)

wait = time.sleep

nightTime = 0

wait(1)

def randomLines(dead):
  if dead != 2:
    rp = (random.randrange(1,dead))
    randomPlayer = remainingPlayers[rp]
  if dead == 2:
    impWon = 1

  while True:
    if dead != 2:
      rp2 = (random.randrange(1,dead))
      randomPlayer2 = remainingPlayers[rp2]
    if dead == 2:
      impWon = 1
      break
    if rp != rp2:
      break

  if randomPlayer == char:
    randomPLayer = "You"
  if randomPlayer2 == char:
    randomPlayer2 = char + " (You)"

  Line = [f"{randomPlayer}: I am not suspicious!",f"{randomPlayer}: I think {randomPlayer2} is sus lol",f"{randomPlayer}: Im scared :'(",f"{randomPlayer}: Amogus",f"{randomPlayer}: Im voting {randomPlayer2}"]

  randomLine = (random.randrange(1,5))
  talkLine = Line[randomLine]
  color = (random.randrange(1,3))
  if color == 1:
    print(Fore.CYAN+talkLine)
  if color == 2:
    print(Fore.MAGENTA+talkLine)
  if color == 3:
    print(Fore.BLUE+talkLine)

def Discuss(dead):
  randomLines(dead)
  wait(Time)
  randomLines(dead)
  wait(Time)
  randomLines(dead)
  wait(Time)
  randomLines(dead)
  wait(1)

def most_frequent(List):
    counter = 0
    num = List[0]
      
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
  
    return num

def Vote(dead,remainingPlayers,quit,devmode):
  botVote = ""
  botVote2 = ""
  botVote3 = ""
  botVote4 = ""
  botVote5 = ""
  if dead > 0 or dead == 0:
    bVote = (random.randrange(1,dead))
    botVote = remainingPlayers[bVote]
  if dead > 1 or dead == 1:
    bVote1 = (random.randrange(1,dead))
    botVote1 = remainingPlayers[bVote1]
  if dead > 2 or dead == 2:
    bVote2 = (random.randrange(1,dead))
    botVote2 = remainingPlayers[bVote2]
  if dead > 3 or dead == 3:
    bVote3 = (random.randrange(1,dead))
    botVote3 = remainingPlayers[bVote3]
  if dead > 4 or dead == 4:
    bVote4 = (random.randrange(1,dead))
    botVote4 = remainingPlayers[bVote4]
  if dead > 5 or dead == 5:
    bVote5 = (random.randrange(1,dead))
    botVote5 = remainingPlayers[bVote5]
  votes = [botVote,botVote2,botVote3,botVote4,botVote5]
  num_of_voters=len(remainingPlayers)
  while True:
    num_of_voters=len(remainingPlayers)
    print(Fore.YELLOW+f"Who are you voting?", end=" ")
    vPerson = input()
    if vPerson not in remainingPlayers and "quit" not in vPerson and "devmode" not in vPerson:
      print(f"""Theres no one named "{vPerson}" """)
    if "quit" in vPerson:
      quit = 1
      break
    if "devmode" in vPerson:
      devmode = 1
      break
    else:
      if vPerson in remainingPlayers:
        break
  if quit != 1:
    votes = [botVote,botVote2,botVote3,botVote4,botVote5,vPerson]
    for _ in range(5):
      if "" in votes:
        votes.remove("")
    dPerson = most_frequent(votes)
    remainingPlayers.remove(dPerson)
    print(f"{Fore.YELLOW}{num_of_voters} people has voted, voted players: {Fore.WHITE}", ', '.join(map(str, votes))+ "."+ f"{Fore.RED} {dPerson} {Fore.YELLOW} is dead. ")
    if char in dPerson:
      print(f"{Fore.YELLOW}You got voted out by the public. {Fore.YELLOW} Remaining people:{Fore.WHITE}", ', '.join(map(str, remainingPlayers))+ f"{Fore.YELLOW}.")
      quit = 1



while Loop:
  if impostor not in remainingPlayers:
    innocentWon = 1
    Loop = False
  if devmode == 1:
    Loop = False
  if quit == 1:
    Loop = False
  if dead == 2:
    impWon = 1
  if impWon == 1:
    Loop = False
  #if keyboard.is_pressed("7"):
    #devmode = 1
    #break
  if nightTime == 0:
    late = (random.randrange(5,15))
    print(Fore.BLUE + "Its getting late.", end="\r")
    wait(late / 3)
    print(Fore.RED + "Its getting late..", end="\r")
    wait(late/ 3)
    print(Fore.MAGENTA + "Its getting late...", Style.RESET_ALL, end="\r")
    nightTime = 1
    wait(late / 6)
    if impostor not in remainingPlayers:
      innocentWon = 1
      Loop = False
    if devmode == 1:
      Loop = False
    if quit == 1:
      Loop = False
    if dead == 2:
      impWon = 1
    if impWon == 1:
      Loop = False

  if nightTime == 1:
    if innocent == 1:
      killRange = (random.randrange(1,dead))
      while True:
        if charImpostor == killRange:
          killRange = (random.randrange(1,dead))
        else:
          break

      deadPerson = remainingPlayers[killRange]

      if char in deadPerson:
        dead -= 1
        remainingPlayers.remove(deadPerson)
        if dead == 2:
          print(f"{Fore.YELLOW}You got murdered by {Fore.RED}{impostor}!{Fore.YELLOW} Remaining people:{Fore.WHITE}", ', '.join(map(str, remainingPlayers))+ f"{Fore.YELLOW}.")
          impWon = 1
          break
        else:
          if dead != 2:
            print(f"{Fore.YELLOW}You got murdered by {Fore.RED}{impostor}!{Fore.YELLOW} Remaining people:{Fore.WHITE}", ', '.join(map(str, remainingPlayers))+ ".", f"""{Fore.YELLOW}Press "Enter" to exit""", end="")
            input()
            nightTime = 0
            break

      if deadPerson != char:
        dead -= 1
        if dead == 2:
          impWon = 1
          break
        remainingPlayers.remove(deadPerson)
        Time = (random.randrange(2,3))
        print(f"{Fore.RED}{deadPerson} {Fore.YELLOW}is dead! Remaining people: {Fore.WHITE}", ', '.join(map(str, remainingPlayers))+ f"{Fore.YELLOW}. Chat is on for {Time * 4} seconds")
        wait(2)
        Discuss(dead)
        Vote(dead,remainingPlayers,quit,devmode)
        nightTime = 0

    else:
      if innocent == 0:
        WhoToKill = input(f"{Fore.YELLOW}Who do you wanna kill? Remaining ppl: {Fore.WHITE} "+', '.join(map(str, impostorSee))+" ")
        if WhoToKill in remainingPlayers and WhoToKill != char:
          dead -= 1
          if dead == 2:
            impWon = 1
            break
          Time = (random.randrange(2,3))
          remainingPlayers.remove(WhoToKill)
          impostorSee.remove(WhoToKill)
          print(f"{Fore.YELLOW}You successfully killed {Fore.RED}{WhoToKill}{Fore.WHITE}!")
          if dead == 2:
            impWon = 1
            break
          wait(1)
          print(f"{Fore.RED}{WhoToKill} {Fore.YELLOW}is dead! Remaining people: {Fore.WHITE}", ', '.join(map(str, remainingPlayers))+ f"{Fore.YELLOW}. Chat is on for {Time * 4} seconds")
          wait(2)
          Discuss(dead)
          Vote(dead,remainingPlayers,quit,devmode)
          nightTime = 0
        else:
          if WhoToKill == char:
            print("You can't kill urself!")
            wait(2)
          if WhoToKill not in remainingPlayers and "devmode" not in WhoToKill and "quit" not in WhoToKill:
            print(f"""There's no one named "{WhoToKill}"!""")
            wait(2)
          if "devmode" in WhoToKill:
            devmode = 1
            break
          if "quit" in WhoToKill:
            break 

if devmode == 1: #devmode doesn't work on v1.0.0
  print("What do you want? |1 Quit |2 Credits")
  while True:
    if keyboard.is_pressed("1"):
      break
    if keyboard.is_pressed("2"):
      print("The owner of this game is Zgn, and he is still working on it.")

if impWon == 1: #Impostor win works perfectly
  if char in impostor:
    print(Fore.YELLOW+f"The"+Fore.RED+ f" Imposter"+Fore.WHITE+f", {impostor}"+Fore.YELLOW+ f" has won the game by killing {WhoToKill}! ", end="")
    input()
  if char not in impostor:
    print(Fore.YELLOW+f"The"+Fore.RED+ f" Imposter"+Fore.WHITE+f", {impostor}"+Fore.YELLOW+ f" has won the game by killing {deadPerson}! ", end="")
    input()

if innocentWon == 1: # Innocent win works perfectly
  if char in impostor:
    print(Fore.YELLOW+f"The"+Fore.RED+ f" You, "+Fore.WHITE+f", are"+Fore.YELLOW+ f" dead! Innocents won! ", end="")
    input()
  if char not in impostor:
    print(Fore.YELLOW+f"The"+Fore.RED+ f" Imposter"+Fore.WHITE+f", {impostor}"+Fore.YELLOW+ f" has died! Innocents won! ", end="")
    input()