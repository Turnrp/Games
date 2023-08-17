import random
import time

Names = ['A_Goblin', 'A_Demogorgon', 'Karen', 'Zane', 'Joe', 'The_Booty_Tickler', 'The_Guy_From_Fortnite', 'Rory', 'Jay' ]
Aproaches = ['lurks', 'appears', 'bolts', 'jumps', 'leaps', 'pops', 'rushes']
Storys = ['You_were_walking_down_a_hall', 'You_were_getting_the_secret_formula', 'You_finally_found_who_asked', 'You found 20$_on_the_floor', 'You_were_playing_pokemon_go', 'You_were_eating_McDonald_']
BossNames = ['Big_Boy_Billy', 'Karl_The_Weeser', 'Arthur_Just_Arthur']

Attacks = ['Wooden_Sword', 'Bandage']
AttacksUpgrade = [1,1]
BuyableAttacks = ['Medkit', 'Iron_Sword', 'Katana']
BuyablePrices = [50, 200, 500]

AllAttacks = ['Wooden_Sword', 'Iron_Sword', 'Bandage', 'Medkit', 'The_Excalibur', 'Katana', 'Templar_Long_Sword']
AttackHitPoints = [5, 10, 5, 'max', 'max', 20, 40]
AttackHitPointsMax = [10, 15, 25, 'max', 'max', 25, 60]
AttackTypes = ['attack', 'attack', 'heal', 'heal', 'attack', 'attack', 'attack']
AttackRaritys = ['Common', 'Uncommon', 'Common', 'Rare', 'Unobtainable', 'Rare', 'Legendary']

BossDrops = ['Templar_Long_Sword']
LootChestDrops = ['Katana']

EnemyHP = 100
EnemyMaxHP = 100
EnemyLVL = 1

MaxHP = 100
HP = 100 
LVL = 1
EXP = 0
MaxEXP = 200
Coins = 0
medkitused = False
hasPlayed = False
justhealed = False

BossTimes = 5 * LVL

def CheckUpgrades():
    while not len(AttacksUpgrade) >= len(Attacks):
        AttacksUpgrade.append(1)
    if '0' in AttacksUpgrade or 0 in AttacksUpgrade:
        for i in AttacksUpgrade:
            if i == '0' or i == 0:
                index = AttacksUpgrade.index(i)
                AttacksUpgrade[index] = 1
CheckUpgrades()

for i in Attacks:
    if i in BuyableAttacks:
        index = BuyableAttacks.index(i)
        BuyableAttacks.remove(i)
        price = BuyablePrices[index]
        BuyablePrices.remove(price)

def BossFight():
    
    global HP
    global MaxHP
    global LVL
    global EXP
    global MaxEXP
    global Coins
    global justhealed
    global medkitused
    global EnemyHP
    global EnemyMaxHP
    global EnemyLVL
    global BossTimes

    global Data
    global hasPlayed

    NewName = random.choice(BossNames)
    print(random.choice(Storys), 'and', random.choice(NewName), random.choice(Aproaches), 'towards you....')
    medkitused = False
    EnemyLVL = LVL - random.randint(-15,15)
    if(EnemyLVL < 1):
        EnemyLVL = 1
    EnemyMaxHP = EnemyLVL * 100
    EnemyHP = EnemyMaxHP
    HP = LVL * 100
    MaxHP = HP
    BossNotDefeated = True
    print('Enemy HP:', EnemyHP, '| Enemy LVL:', EnemyLVL)
    print('')
    print('Your HP:', HP,'| Your LVL:', LVL, '| Your EXP:', EXP)
    print('Your Attacks: ')
    funnynumberthing = 1
    for i in Attacks:
        print(i.replace('_', ' '), ':', funnynumberthing)
        funnynumberthing += 1
    print('')

    while BossNotDefeated:
        #Player Attack
        while True:
            choice = input('What will you do: ')
            choiceReplace = choice.replace(' ', '_', 1)
            try:
                try:
                    index = AllAttacks.index(Attacks[int(choice) - 1])
                except :
                    if choiceReplace in Attacks:
                        index = AllAttacks.index(choiceReplace)
                    else:
                        somethingwronglolsoitgoestotheexceptoutsidethisexceptiguessthisisaneasteraegglol
    
                if AttackTypes[index] == 'attack':
                    if AttackHitPoints[index] == 'max':
                        EnemyHP = 0
                    else:
                        randAttack = random.randint(int(AttackHitPoints[index]), int(AttackHitPointsMax[index])) * (int(AttacksUpgrade[Attacks.index(AllAttacks[index])])) * (LVL / 1.5)
                        EnemyHP -= round(randAttack)
                        print(f'\nYou slash and you deal {round(randAttack)} hitpoints to the enemy...\n')
                elif AttackTypes[index] == 'heal':
                    if AttackHitPoints[index] == 'max':
                        HP = MaxHP
                        justhealed = True
                    else:
                        randAttack = random.randint(int(AttackHitPoints[index]), int(AttackHitPointsMax[index])) * (int(AttacksUpgrade[Attacks.index(AllAttacks[index])])) * (LVL / 1.5)
                        HP += round(randAttack)
                        justhealed = True
                        print(f'\nYou heal yourself and gain {round(randAttack)} hitpoints!\n')
                break
            except :
                print(f'\nAttack Not Found\n')
        # Boss Attack
        attackDamage = round(random.randint(5,10) * (EnemyLVL / 1.75))
        enemyDamage = random.randint(5,25) * (LVL / 1.25)
        roll = random.randint(0, 2)
        attackAmount = random.randint(2, 5)

        if roll == 0:
            print(f'\n{NewName} slashes at you and you take -{attackDamage} HP.\n')
            HP -= attackDamage
        elif roll == 1:
            print(f'\n{NewName} starts spinning his weapon around and hits you {attackAmount} times! -{attackDamage * attackAmount} HP.\n')
            HP -= attackDamage * attackAmount
        elif roll == 2:
            roll = random.randint(1,2)
            choice = input(f'\n{NewName} jumps into the sky beyond eyesight, you can either dodge left or right! (50/50)\n')
            if 'left' in choice.lower():
                if roll == 1:
                    print(f'BOOM! He slams right on top of you -{attackDamage * 2} HP!')
                    HP -= attackDamage * 2
                else:
                    print(f'Dodge! He misses you and takes -{enemyDamage} HP!')
                    EnemyHP -= enemyDamage
            elif 'right' in choice.lower():
                if roll == 2:
                    print(f'BOOM! He slams right on top of you -{attackDamage * 2} HP!')
                    HP -= attackDamage * 2
                else:
                    print(f'Dodge! He misses you and takes -{enemyDamage} HP!')
                    EnemyHP -= enemyDamage
            else:
                print(f'BOOM! He slams right on top of you in dissapointment you just stood there -{attackDamage * 2} HP!')
                HP -= attackDamage * 2
        if(HP > MaxHP):
            HP = MaxHP
        if(HP <= 0):
            hasPlayed = False
            print('You Died.... RESTARTING')
            print('')
            
            Play()
        if(EnemyHP <= 0):
            hasPlayed = False
            gainedXP = random.randint(1,4) * MaxEXP/2
            gainedCoins = random.randint(1,5) * 50 * EnemyLVL
            EXP += gainedXP
            Coins += gainedCoins
            BossDrop = random.choice(BossDrops)
            print(f'Enemy has Perished\n')

            print(f'You gained {gainedXP}')
            print(f'You gained {gainedCoins}')
            if not BossDrop in Attacks:
                print(f'You got a new item, {BossDrop}!\n')
                Attacks.append(BossDrop)
            if(EXP >= MaxEXP * LVL):
                EXP -= MaxEXP * LVL
                LVL += 1 
            time.sleep(1)
            
            Data = [LVL,EXP,Coins,Attacks,AttacksUpgrade,BossTimes]
            BossTimes = 5 * LVL
            Play()
        if(HP > 0):
            hasPlayed = True
            if(EXP >= MaxEXP * LVL):
                EXP -= MaxEXP * LVL
                LVL += 1  
            Data = [LVL,EXP,Coins,Attacks,AttacksUpgrade,BossTimes]
            BossFight()

def Play():
    
    global HP
    global MaxHP
    global LVL
    global EXP
    global MaxEXP
    global Coins
    global justhealed
    global medkitused
    global BossTimes

    global EnemyHP
    global EnemyMaxHP
    global EnemyLVL

    global Data
    global Attacks
    global AttacksUpgrade

    
    

    for i in Attacks:
        if i in BuyableAttacks:
            index = BuyableAttacks.index(i)
            BuyableAttacks.remove(i)
            price = BuyablePrices[index]
            BuyablePrices.remove(price)

    global hasPlayed
    if(Coins < 0):
        Coins = 0
    if(not hasPlayed):
        while True:
            CheckUpgrades()
            
            Data = [LVL,EXP,Coins,Attacks,AttacksUpgrade]
            print('Welcome to the shop!')
            print('Balance:', Coins)
            print('Here are the Attacks:')
            for i in BuyableAttacks:
                index = BuyableAttacks.index(i)
                price = BuyablePrices[index]
                print(i.replace('_', ' '), ':', price)
            print('')
            choice = input(f'Do you wanna either:\n Buy something from the Shop (Just type the item), \n Reset your progress,\n Upgrade your weapons, or exit?\n')
            if(not 'exit' in choice):
                newerchoice = choice.replace(' ', '_')
                if(newerchoice in BuyableAttacks):
                    index = BuyableAttacks.index(newerchoice)
                    if Coins >= BuyablePrices[index]:
                        newChoice = newerchoice.replace(' ', '')
                        Attacks.append(newChoice)
                        BuyableAttacks.remove(newerchoice)
                        price = BuyablePrices[index]
                        BuyablePrices.remove(price)
                        Coins -= price
                        if(Coins < 0):
                            Coins = 0
                        Data = [LVL,EXP,Coins,Attacks,AttacksUpgrade,BossTimes]
                elif 'reset' in choice.lower():
                    choice = input(f'Are you sure you wanna reset? y/n\n')
                    if(choice == 'y'):
                        CreateBackup()
                        LVL = 1
                        EXP = 0
                        Coins = 0
                        Attacks = ['Wooden_Sword', 'Bandage']
                        AttacksUpgrade = [1,1]
                        choice = input(f'Data Reset do you wish to save? y/n\n')
                        if(choice == 'y'):
                            Data = [LVL,EXP,Coins,Attacks,AttacksUpgrade,BossTimes]
                elif('codec' in choice):
                    if('var' in choice):
                        choice = input('What variable do you wanna edit? ')
                        if('LVL' in choice):
                            choice = input('To what number? ')
                            LVL = int(choice)
                    elif('Coins' in choice):
                            choice = input('To what number? ')
                            Coins = int(choice)
                    elif 'items' in choice.lower():
                        for i in AllAttacks:
                            print(i)
                        choice = input(f'What item would you like to add? (you can add multiple) \n')
                        for i in AllAttacks:
                            if choice == i:
                                Attacks.append(i)
                elif 'upgrade' in choice.lower():
                    coolnumber = 1
                    for i in Attacks:
                        print(i + ':', coolnumber)
                        coolnumber += 1
                    choice = input(f'\nPick which weapon you wanna upgrade..\n')
                
                    try:
                        index = int(choice) - 1
                    except :
                        index = Attacks.index(choice)
                    choice = input(f'\nHow many times will you upgrade?\n')
                    times = int(choice)
                    price = 100 * times
                    choice = input(f'\nThis will cost {price} are you sure? y/n\n')
                    if choice.lower() == 'y':
                        if Coins >= price:
                            Coins -= price
                            orginUpgrade = int(AttacksUpgrade[index])
                            AttacksUpgrade.remove(AttacksUpgrade[index])
                            AttacksUpgrade.insert(index, orginUpgrade + times)
                            print(f'\n{Attacks[index]} has been upgraded {times} time(s)\nCome Again!')
                            time.sleep(1)
                        else:
                            print(f'\nNot enought Coins...')
                            time.sleep(1)
            elif choice.lower() == 'exit':
                print('Come again!')
                time.sleep(1)
                break
        time.sleep(0.1)
        print(random.choice(Storys).replace('_', ' '), 'and', random.choice(Names).replace('_', ' '), random.choice(Aproaches).replace('_', ' '), 'towards you....')
        medkitused = False
        EnemyLVL = LVL - random.randint(-1,1)
        if(EnemyLVL < 1):
            EnemyLVL = 1
        EnemyMaxHP = EnemyLVL * 100
        EnemyHP = EnemyMaxHP
        HP = LVL * 100
        MaxHP = HP
    
    print('Enemy HP:', EnemyHP, '| Enemy LVL:', EnemyLVL)
    print('')
    print('Your HP:', HP,'| Your LVL:', LVL, '| Your EXP:', EXP)
    print('Your Attacks: ')
    funnynumberthing = 1
    for i in Attacks:
        print(i.replace('_', ' '), ':', funnynumberthing)
        funnynumberthing += 1
    print('')
    
    while True:
        choice = input('What will you do: ')
        #Player Attack
        choiceReplace = choice.replace(' ', '_', 1)
        try:
            try:
                index = AllAttacks.index(Attacks[int(choice) - 1])
            except :
                if choiceReplace in Attacks:
                    index = AllAttacks.index(choiceReplace)
                else:
                    somethingwronglolsoitgoestotheexceptoutsidethisexceptiguessthisisaneasteraegglol
    
            if AttackTypes[index] == 'attack':
                if AttackHitPoints[index] == 'max':
                    EnemyHP = 0
                else:
                    randAttack = random.randint(int(AttackHitPoints[index]), int(AttackHitPointsMax[index])) * (int(AttacksUpgrade[Attacks.index(AllAttacks[index])])) * (LVL / 1.5)
                    EnemyHP -= round(randAttack)
                    print(f'\nYou slash and you deal {round(randAttack)} hitpoints to the enemy...\n')
            elif AttackTypes[index] == 'heal':
                if AttackHitPoints[index] == 'max':
                    HP = MaxHP
                    justhealed = True
                else:
                    randAttack = random.randint(int(AttackHitPoints[index]), int(AttackHitPointsMax[index])) * (int(AttacksUpgrade[Attacks.index(AllAttacks[index])])) * (LVL / 1.5)
                    HP += round(randAttack)
                    justhealed = True
                    print(f'\nYou heal yourself and gain {round(randAttack)} hitpoints!\n')
            break
        except :
            print(f'\nAttack Not Found\n')
    Data = [LVL,EXP,Coins,Attacks,AttacksUpgrade,BossTimes]
    #Enemy Attack
    chance = random.randint(1,5)
    if(EnemyHP < EnemyMaxHP * 0.2 and chance == 1):
        print('Enemy will heal!')
        EnemyHP += round(random.randint(5,10) * (EnemyLVL / 1.75))
        print('')
        time.sleep(0.5)
    else:
        print('Enemy will attack!')
        if(justhealed == False):
            HP -= round(random.randint(5,15) * (LVL / 1.75))
        else:
            justhealed = False
        print('')
        time.sleep(0.5)
    if(HP > MaxHP):
        HP = MaxHP
    if(HP <= 0):
        hasPlayed = False
        print('You Died.... RESTARTING')
        print('')
        
        Play()
    if(EnemyHP <= 0):
        hasPlayed = False
        gainedXP = random.randint(1,4) * MaxEXP/2
        gainedCoins = random.randint(1,5) * 50 * EnemyLVL
        EXP += gainedXP
        Coins += gainedCoins
        print('Enemy has Perished')
        print('')
        print(f'You gained {gainedXP}')
        print(f'You gained {gainedCoins}')
        print('')
        if(EXP >= MaxEXP * LVL):
            EXP -= MaxEXP * LVL
            LVL += 1 
        time.sleep(1)
        
        Data = [LVL,EXP,Coins,Attacks,AttacksUpgrade,BossTimes]
        BossTimes -= 1
        if BossTimes <= 0:
            BossTimes = 5 * LVL
            BossFight()
        else:
            Play()
    if(HP >= 0):
        hasPlayed = True
        if(EXP >= MaxEXP * LVL):
            EXP -= MaxEXP * LVL
            LVL += 1  
        Data = [LVL,EXP,Coins,Attacks,AttacksUpgrade,BossTimes]
        Play()

Play()
# 590 lines of code 