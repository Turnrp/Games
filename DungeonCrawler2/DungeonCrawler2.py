import copy
from genericpath import exists
from random import choices, choice, randint
from os import system
from json import dump, load
from os.path import dirname
from time import sleep
from tabulate import tabulate

class Item:
    def __init__(self, Price: int, MinPower: int, MaxPower: int, Speed: float, Name: str, Healing : bool = False) -> None:
        self.Price = Price
        self.MaxPower = MaxPower
        self.MinPower = MinPower
        self.Name = Name
        self.Speed = Speed
        self.Healing = Healing

class Character:
    def __init__(self, Name: str, MaxHealth: int = 100, Coins: int = 0, Inventory: list = [], Level : int = 1, XP : int = 0) -> None:
        self.Inventory = Inventory
        self.Coins = Coins
        self.Name = Name
        self.MaxHealth = MaxHealth
        self.Health = MaxHealth
        self.Level = Level
        self.XP = XP

class NPC:
    def __init__(self, Name: str, Weapon: Item, MaxHealth: int, GoldRewardMin : int, GoldRewardMax : int, Level : int = 1) -> None:
        self.Name = Name
        self.Weapon = Weapon
        self.MaxHealth = MaxHealth
        self.Health = MaxHealth
        self.Level = Level
        self.GoldRewardMin = GoldRewardMin
        self.GoldRewardMax = GoldRewardMax

class Items:
    def __init__(self):
        # Swords
        self.Basic_Sword = Item(0, 2, 10, 1, "Basic Sword")
        self.Sword = Item(5, 5, 15, 3, "Sword")
        self.Long_Sword = Item(25, 10, 25, 3.5, "Long Sword")
        self.Katana = Item(20, 10, 20, 1, "Katana")
        self.Great_Sword = Item(50, 30, 40, 10, "Great Sword")
        self.Thunder_Sword = Item(55, 25, 30, 8, "Thunder Sword")
        self.Holy_Sword = Item(65, 30, 35, 10, "Holy Sword")
        self.The_Excalibur = Item(1000, 100, 1000, 1, "The Excalibur")

        # Axe
        self.Axe = Item(30, 15, 20, 7, "Axe")

        # Lunge
        self.Spear = Item(25, 10, 15, 3, "Spear")

        # Quick
        self.Dagger = Item(10, 5, 10, 1, "Dagger")
        self.Poison_Dagger = Item(35, 10, 20, 3, "Poison Dagger")
        self.Blood_Dagger = Item(35, 15, 20, 8, "Blood Dagger")

        # Ranged
        self.Bow = Item(20, 10, 15, 5, "Bow")
        self.Ice_Bow = Item(45, 20, 30, 8, "Ice Bow")

        # Healing
        self.Bandage = Item(5, 5, 25, 1, "Bandage", True)
        self.Medkit = Item(30, 50, 100, 3, "Medkit", True)
        self.Health_Potion = Item(75, 75, 100, 2, "Health Potion", True)
        self.Healing_Staff = Item(100, 100, 100, 4, "Health Staff", True)

        # Special
        self.Magic_Wand = Item(50, 20, 25, 8, "Magic Wand")
        self.Fireball_Staff = Item(40, 15, 30, 7, "Fireball Staff")

        self.AllItems = {
            self.Basic_Sword.Name : self.Basic_Sword,
            self.Sword.Name : self.Sword,
            self.Long_Sword.Name : self.Long_Sword,
            self.Katana.Name : self.Katana,
            self.Great_Sword.Name : self.Great_Sword,
            self.Thunder_Sword.Name : self.Thunder_Sword,
            self.Holy_Sword.Name : self.Holy_Sword,
            self.The_Excalibur.Name : self.The_Excalibur,
            self.Axe.Name : self.Axe,
            self.Spear.Name : self.Spear,
            self.Spear.Name : self.Spear,
            self.Dagger.Name : self.Dagger,
            self.Poison_Dagger.Name : self.Poison_Dagger,
            self.Blood_Dagger.Name : self.Blood_Dagger,
            self.Bow.Name : self.Bow,
            self.Ice_Bow.Name : self.Ice_Bow,
            self.Bandage.Name : self.Bandage,
            self.Medkit.Name : self.Medkit,
            self.Health_Potion.Name : self.Health_Potion,
            self.Healing_Staff.Name : self.Healing_Staff,
            self.Magic_Wand.Name : self.Magic_Wand,
            self.Fireball_Staff.Name : self.Fireball_Staff,
        }

    def Find(self,  name):
        return self.AllItems[name]
C_Items = Items()

class NPCS:
    class Enemies:
        Skeleton = NPC("Skeleton", C_Items.Basic_Sword, 100, 5, 10)
        Zombie = NPC("Zombie", C_Items.Sword, 120, 10, 15)
        Orc = NPC("Orc", C_Items.Axe, 150, 15, 20)
        Wizard = NPC("Wizard", C_Items.Magic_Wand, 80, 15, 25)
        Giant_Spider = NPC("Giant Spider", C_Items.Spear, 90, 10, 15)
        Ghost = NPC("Ghost", C_Items.Dagger, 80, 5, 10)
        Fire_Elemental = NPC("Fire Elemental", C_Items.Fireball_Staff, 120, 20, 25)
        Assassin = NPC("Assassin", C_Items.Poison_Dagger, 100, 5, 15)
        Ice_Golem = NPC("Ice Golem", C_Items.Ice_Bow, 180, 20, 25)
        Thunder_Demon = NPC("Thunder Demon", C_Items.Thunder_Sword, 200, 30, 40)
        Angel = NPC("Angel", C_Items.Holy_Sword, 250, 10, 30)
        Vampire = NPC("Vampire", C_Items.Blood_Dagger, 160, 20, 25)
        King_Arthur = NPC("King Arthur", C_Items.The_Excalibur, 1000, 50, 500)


def AddItemToInventory(plr: Character, item: Item):
    if item.Name not in [item.Name for item in Player.Inventory]:
        plr.Inventory.append(copy.deepcopy(item))
    
def CheckDeath(target : NPC):
    if target.Health <= 0:
        return True
    else:
        return False

def QueueDeath(Enemy : NPC):
    if CheckDeath(Player):
        input("YOU DIED.\nStarting with half health..")
        Player.Health = Player.MaxHealth / 2
        return True
    
    if CheckDeath(Enemy):
        input("Enemy Defeated!")
        GoldReward = randint(Enemy.GoldRewardMin, Enemy.GoldRewardMax)
        Player.Coins += GoldReward
        Player.XP += GoldReward * 5
        print(f"Player Gained +{GoldReward} Coins!\nPlayer Gained +{GoldReward * 5} XP!")
        if Player.XP >= Player.Level * 125:
            Player.XP = 0
            Player.Level+=1
            print("Player Leveled UP!")
        input("Player Max Health!")
        Player.Health = Player.MaxHealth
        if Enemy.Name == NPCS.Enemies.King_Arthur.Name:
            input("YOU HAVE SLAYED ARTHUR, YOU NOW GAIN THE THE EXCALIBUR.")
            AddItemToInventory(Player, C_Items.The_Excalibur)
        return True
    
    return False

def Attack(target : NPC, weapon : Item):
    damage_amount = randint(weapon.MinPower, weapon.MaxPower)
    target.Health -= damage_amount
    print(f"{target.Name} takes -{damage_amount} HP!")

def Clamp(value, min, max):
    if value > max:
        return max
    elif value < min:
        return min
    else:
        return value

def Heal(target : NPC, item : Item):
    heal_amount = randint(item.MinPower, item.MaxPower)
    target.Health = Clamp(target.Health + heal_amount, 0, target.MaxHealth)
    print(f"{target.Name} gains +{heal_amount} HP!")

def Clear():
    system("cls")

def Save():
    print("Saving...")
    data = {
        "Inventory" : [item.Name for item in Player.Inventory],
        "Coins" : Player.Coins,
        "Level" : Player.Level,
        "XP" : Player.XP
    }
    SavePath = dirname(__file__) + "\\" + Player.Name + ".json"
    dump(data, open(SavePath, "w"))
    sleep(0.1)

def Load():
    PlayerName = input("Name: ")
    Player = Character(PlayerName)
    SavePath = dirname(__file__) + "\\" + PlayerName + ".json"
    if exists(SavePath):
        data = load(open(SavePath))
        for i in data["Inventory"]:
            Player.Inventory.append(C_Items.Find(i))
        Player.Coins = data["Coins"]
        Player.Level = data["Level"]
        Player.XP = data["XP"]
    else:
        Player.Inventory.append(C_Items.Basic_Sword)
        Player.Inventory.append(C_Items.Bandage)
    return Player

Clear()
Player = Load()

Shop = [
    C_Items.Sword, C_Items.Long_Sword, C_Items.Katana,
    C_Items.Holy_Sword, C_Items.Axe, C_Items.Spear, C_Items.Dagger, C_Items.Poison_Dagger,
    C_Items.Bow, C_Items.Medkit, C_Items.Health_Potion
]

Enemies= {
    **dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [NPCS.Enemies.Skeleton, NPCS.Enemies.Zombie, NPCS.Enemies.Orc]),
    **dict.fromkeys([11, 12 , 13, 14, 15], [NPCS.Enemies.Skeleton, NPCS.Enemies.Zombie, NPCS.Enemies.Orc, NPCS.Enemies.Wizard, NPCS.Enemies.Giant_Spider, NPCS.Enemies.Ghost]),
    **dict.fromkeys([16, 17, 18, 19, 20], [NPCS.Enemies.Skeleton, NPCS.Enemies.Zombie, NPCS.Enemies.Orc, NPCS.Enemies.Wizard, NPCS.Enemies.Giant_Spider, NPCS.Enemies.Ghost, NPCS.Enemies.Fire_Elemental, NPCS.Enemies.Assassin, NPCS.Enemies.Ice_Golem]),
    **dict.fromkeys([21], [NPCS.Enemies.Skeleton, NPCS.Enemies.Zombie, NPCS.Enemies.Orc, NPCS.Enemies.Wizard, NPCS.Enemies.Giant_Spider, NPCS.Enemies.Ghost, NPCS.Enemies.Fire_Elemental, NPCS.Enemies.Assassin, NPCS.Enemies.Ice_Golem, NPCS.Enemies.Thunder_Demon, NPCS.Enemies.Angel, NPCS.Enemies.Vampire, NPCS.Enemies.King_Arthur])
}

def StartShop(DisplayedShop : list):
    DisplayedShop = list(set(DisplayedShop))
    DisplayedShop = [item for item in DisplayedShop if item.Name not in [item.Name for item in Player.Inventory]]
    Saved = False

    while 1:
        ItemChoice = ''
        try:
            Clear()
            print(f"Welcome To The Shop {Player.Name}... \nLevel: {Player.Level} | Health: {Player.Health} / {Player.MaxHealth}\nCoins: {Player.Coins}")
            ShopTable = []
            ShopHead = ["Name", "Price", "Speed", "Min Power", "Max Power", "Selection"]
            for item in DisplayedShop:
                ShopTable.append([item.Name, item.Price, item.Speed, item.MinPower, item.MaxPower, DisplayedShop.index(item)])
            print(tabulate(ShopTable, headers=ShopHead, tablefmt="grid"))
            ItemChoice = input("Would you like to Exit, Save, Manage your items, or just type an item to purchase.\nChoice: ").lower()
            if ItemChoice == "exit":
                if not Saved:
                    if input("Leave without saving? Y/N\n") == "N":
                        if input("Save? Y/N\n") == "Y":
                            Save()
                break
            elif ItemChoice == "manage":
                ShopTable = []
                ShopHead = ["Name", "Speed", "Min Power", "Max Power", "Selection"]
                for item in Player.Inventory:
                    ShopTable.append([item.Name, item.Speed, item.MinPower, item.MaxPower, Player.Inventory.index(item)])
                print(tabulate(ShopTable, headers=ShopHead, tablefmt="grid"))
                ItemChoice = input("Item: ").lower()
                try:
                    if ItemChoice.isdigit():
                        ItemChoice = Player.Inventory[int(ItemChoice)]
                    else:
                        ItemChoice = Player.Inventory[[item.Name.lower() for item in Player.Inventory].index(ItemChoice)]
                    
                    Choice = input("Would you like to move it to the top, bottom, or just remove this item.\nChoice: ").lower()
                    if "top" in Choice:
                        Player.Inventory.insert(0, Player.Inventory.pop(Player.Inventory.index(ItemChoice)))
                    elif "bottom" in Choice:
                        Player.Inventory.insert(len(Player.Inventory)-1, Player.Inventory.pop(Player.Inventory.index(ItemChoice)))
                    elif "remove" in Choice:
                        if input(f"Do you really want to remove {ItemChoice.Name}? Y/N\n") == "Y":
                            Player.Inventory.remove(ItemChoice)
                except BaseException as e:
                    input(e)
            elif ItemChoice == "save":
                Save()
                Saved = True
            else:
                if ItemChoice.isdigit():
                    ItemChoice = DisplayedShop[int(ItemChoice)]
                else:
                    ItemChoice = DisplayedShop[[item.Name.lower() for item in DisplayedShop].index(ItemChoice)]
                if Player.Coins >= ItemChoice.Price:
                    DisplayedShop.remove(ItemChoice)
                    Player.Coins -= ItemChoice.Price

                    # print(" ".join(GetItemStats(ItemChoice)))

                    AddItemToInventory(Player, ItemChoice)
        except BaseException as e:
            input(e)
    Clear()


def Encounter(Fighter : NPC):
    Enemy = copy.deepcopy(Fighter)
    Enemy.Level = Player.Level + randint(-1, 1)
    Enemy.MaxHealth = Enemy.Level * 50 + 25
    Enemy.Health = Enemy.MaxHealth

    Player.MaxHealth = Player.Level * 50 + 50

    while 1:
        print(Enemy.Name, "| Level:", Enemy.Level, "|", Enemy.Weapon.Name, "|", Enemy.Health, "/", Enemy.MaxHealth)
        print(Player.Name, "| Level:", Player.Level, "|", Player.Health, "/", Player.MaxHealth, "\n")

        ShopTable = []
        ShopHead = ["Name", "Speed", "Min Power", "Max Power", "Selection"]
        for item in Player.Inventory:
            ShopTable.append([item.Name, item.Speed, item.MinPower, item.MaxPower, Player.Inventory.index(item)])
        print(tabulate(ShopTable, headers=ShopHead, tablefmt="grid"))
        while 1:
            ItemChoice = input("Item: ").lower()
            try:
                if ItemChoice.isdigit():
                    ItemChoice = Player.Inventory[int(ItemChoice)]
                else:
                    ItemChoice = Player.Inventory[[item.Name.lower() for item in Player.Inventory].index(ItemChoice)]
                break
            except BaseException as e:
                input(e)
        
        if ItemChoice.Speed <= Enemy.Weapon.Speed:
            if ItemChoice.Healing:
                Heal(Player, ItemChoice)
            else:
                Attack(Enemy, ItemChoice)
            if QueueDeath(Enemy):
                break
            Attack(Player, Enemy.Weapon)
        else:
            Attack(Player, Enemy.Weapon)
            if QueueDeath(Enemy):
                break
            if ItemChoice.Healing:
                Heal(Player, ItemChoice)
            else:
                Attack(Enemy, ItemChoice)
        input()
        Clear()

Player.MaxHealth = Player.Level * 50 + 50
Player.Health = Player.MaxHealth
if Player.Coins == 0 and Player.Level == 1 and Player.XP == 0:
    Encounter(NPCS.Enemies.Skeleton)
    StartShop(choices(Shop, k=2) + [C_Items.Sword])
    Encounter(NPCS.Enemies.Skeleton)
while 1:
    StartShop(choices(Shop, k=randint(3, 5)))
    Encounter(choice(Enemies[Clamp(Player.Level, 1, 21)]))
