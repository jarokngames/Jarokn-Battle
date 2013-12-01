import cPickle as pickle
import os
import i18n
import random

random.seed()

_ = i18n.language.ugettext

playertech = 1
playerarmy = 1
playerlevel = 1
playermoney = 100

def RepresentsInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def clearScreen():
	""" Clears the screen """
	if os.name == "nt":
		os.system("cls")      # Works in w2k
	else:
		os.system("clear")   # Works in cygwin's Bash 

def calcArmyCost(playerlevel):
	armycost = playerlevel * 2
	return armycost

def calcTechCost(playertech):
	techcost = playertech * 20
	return techcost
	

def calcBattle(playereff, comeff):
	if playereff > comeff:
		return 1
	if playereff == comeff:
		return 2
	else:
		return 0

def giveMoney(comarmy, comlevel):
	comcost = calcArmyCost(comlevel) / 2
	moneygain = comarmy * comcost
	return moneygain

def loseSoldiers(playereff, comeff):
	soldierloss = comeff - playereff
	return soldierloss

def saveArmy():
	f = open("Jarokn-Battle.sav", "wb")
	f.write(playerlevel)
	f.write(playerarmy)
	f.write(playertech)
	f.write(playermoney)
	f.close()

choice = 0

while choice != "9":
	clearScreen()
	print _("1. Fight")
	print _("2. Buy Soldiers")
	print _("3. Buy Tech")
	print _("4. Check Army")
	print _("5. Check Cost")
	print _("6. Save Army")
	print _("7. Load Army")
	print _("9. Quit")
	choice = str(raw_input(_("Enter choice: ")))
	if choice == "1":
		clearScreen()
		comlevel = raw_input(_("What level army would you like to fight? "))
		if RepresentsInt(comlevel):
			if comlevel > 0:
				comlevel = int(comlevel)
				comarmy = random.randint((comlevel * 100) - 99, comlevel * 100)
				comtech = random.randint(1, comlevel)
				playereff = playerarmy * playertech
				comeff = comarmy * comtech
				print _("Player Efficiency: ") + str(playereff) + _(" vs. Computer Efficiency: ") + str(comeff)
				win = calcBattle(playereff, comeff)
				if win == 1:
					moneygain = giveMoney(comarmy, comlevel)
					playermoney = playermoney + moneygain
					print _("You win!")
					print _("Money Gain: $") + str(moneygain)
					print _("New Money Amount: $") + str(playermoney)
				if win == 2:
					print _("Dead heat, it's a tie!")
				if win == 0:
					soldierloss = loseSoldiers(playereff, comeff)
					playerarmy = playerarmy - soldierloss
					if playerarmy <= 0:
						playerarmy = 1
					print _("You lose!")
					print _("Soldier Loss: ") + str(soldierloss)
					print _("New Army Size: ") + str(playerarmy)
			else:
				print _("No such level.")
		else:
			print _("Please input a number.")
		raw_input(_("Press enter to continue."))
		continue
	elif choice == "2":
		clearScreen()
		armycost = calcArmyCost(playerlevel)
		print _("Money: $") + str(playermoney)
		print _("Soldier Cost: $") + str(armycost)
		armybuy = raw_input(_("How many soldiers would you like to buy? "))
		if RepresentsInt(armybuy):
			armybuy = int(armybuy)
			armybuycost = armybuy * armycost
			if armybuycost <= playermoney:
				playerarmy = armybuy + playerarmy
				playermoney = playermoney - armybuycost
				if playerarmy < 100:
					playerlevel = 1
					print _("New Level: ") + str(playerlevel)
					print _("New Army Size: ") + str(playerarmy)
				else:
					playerlevel = playerarmy / 100
					print _("New Level: ") + str(playerlevel)
					print _("New Army Size: ") + str(playerarmy)
			else:
				print _("Not enough money.")
		else:
			print _("Please input a number.")
		raw_input(_("Press enter to continue."))
		continue	
	elif choice == "3":
		clearScreen()
		techcost = calcTechCost(playertech)
		print _("Money: $") + str(playermoney)
		print _("Tech Cost: $") + str(techcost)
		techbuy = raw_input(_("How many techlevels would you like to buy? "))
		if RepresentsInt(techbuy):
			techbuy = int(techbuy)
			techbuycost = techbuy * techcost
			if techbuycost <= playermoney:
				playertech = techbuy + playertech
				playermoney = playermoney - techbuycost
				print _("New Tech Level: ") + str(playertech)
			else:
				print _("Not enough money.")
		else:
			print _("Please input a number")
		raw_input(_("Press enter to continue."))
		continue
	elif choice == "4":
		clearScreen()
		print _("Level: ") + str(playerlevel)
		print _("Army Size: ") + str(playerarmy)
		print _("Tech Level: ") + str(playertech)
		print _("Money: $") + str(playermoney)
		raw_input(_("Press enter to continue."))
		continue
	elif choice == "5":
		clearScreen()
		armycost = calcArmyCost(playerlevel)
		techcost = calcTechCost(playertech)
		print _("Soldier Cost: $") + str(armycost)
		print _("Tech Cost: $") + str(techcost)
		raw_input(_("Press enter to continue."))
		continue
	elif choice == "6":
		clearScreen()
		saveArmy()
		print _("Army saved.")
		raw_input(_("Press enter to continue."))
		continue
	elif choice == "7":
		clearScreen()
		try:
			with open('Jarokn-Battle.sav'):
				f = open('Jarokn-Battle.sav', 'rb')
				playerlevel = int(f.readline())
				playerarmy = int(f.readline())
				playertech = int(f.readlne())
				playermoney = int(f.readline())
				f.close()
				print _("Army loaded.")
		except IOError:
			print _("File not found.")
		raw_input(_("Press enter to continue."))
		continue
	elif choice == "9":
		clearScreen()
		print _("See you soon!")
		raw_input(_("Press enter to exit."))
		break
	else: # Incorrect Input
		clearScreen()
		print "Sorry, I couldn't understand you."
		raw_input(_("Press enter to continue."))
		continue
