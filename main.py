#Goal: convert 4000 individual dice rolls into 2000 pairs of dice rolls summed together. Then use those dice pairs to simulate 200 games of craps
inFile = open("rawRandomNums.txt")
outFile = open("crapsGames.txt","w")

gameCount = 0
for line in inFile:
  #Remove all whitespace from line
  line = "".join(line.split())
  
  #Iterate through every other die roll in the line
  for i in range(1,len(line),2):
    #Sum the current dice result with the previous roll in the line and write the sum to a file
    rollSum = int(line[i]) + int(line[i-1])
    outFile.write(str(rollSum)+" ")

    #If the player has either won or lost, make a newline to start new game
    if rollSum in [2,3,7,11,12]:
      outFile.write("\n")
      gameCount += 1
    
    #End loop if 200 games have already been simulated
    if gameCount >= 200:
      break
  if gameCount >= 200:
    break

outFile.close()
inFile.close()
