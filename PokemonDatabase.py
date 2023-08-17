import requests
from os import stat, system

website = "https://pokemondb.net/pokedex/"

def getAllWithText(site, text, secondText = ''):
    indices = [index for index in range(len(site)) if site.startswith(text, index)] + ([index for index in range(len(site)) if site.startswith(secondText, index)] if secondText != '' else [])
    uneffectivenesses = []
    for i in indices:
        startIndex = 0
        curIndex = i
        while 1:
            curIndex -= 1
            if site[curIndex] == "d" and site[curIndex-1] == "t" and site[curIndex-2] == "<":
                startIndex = curIndex-2
                break
        full = site[startIndex:]
        full = full[:full.index('>')+1]
        full = full.split('"')[1].split("&")[0].replace(" ", '')
        if not full in uneffectivenesses:
            uneffectivenesses.append(full)
    return uneffectivenesses
def CreateListText(list):
    EffectiveText = ""
    for i in list:
        if len(list) != 1 and list.index(i) != 0:
            EffectiveText += ", "
        if list.index(i) == len(list) - 1 and len(list) != 1:
            EffectiveText += "and "
        EffectiveText += i
        if list.index(i) == len(list):
            if len(list) == 1:
                EffectiveText += " is"
            else:
                EffectiveText += " and"
    return EffectiveText

while 1:
    system('cls')
    pokemon = input("Pokemon: ").lower()
    site = requests.get(website + pokemon)
    siteText = site.text
    linesSplitted = siteText.splitlines()

    try:
        # Get Text
        effectivenesses = getAllWithText(siteText, 'super-effective')
        uneffectivenesses = getAllWithText(siteText, 'not very effective')
        noneffectivenesses = getAllWithText(siteText, 'no effect')

        # List -> Text
        EffectiveText = CreateListText(effectivenesses)
        NotEffectiveText = CreateListText(uneffectivenesses)
        NonEffectiveText = CreateListText(noneffectivenesses)

        # Get Base Stats
        statsToGet = {"HP": (0), "Attack": (0), "Defense": (0), "Sp. Atk": (0), "Sp. Def": (0), "Speed": (0)}
        for i in statsToGet:
            statIndex = linesSplitted.index(f'<th>{i}</th>')
            stat = linesSplitted[statIndex + 1]
            stat = stat[stat.index(">") + 1:]
            stat = stat[:stat.index("<")]

            statMin = linesSplitted[statIndex + 5]
            statMin = statMin[statMin.index(">") + 1:]
            statMin = statMin[:statMin.index("<")]

            statMax = linesSplitted[statIndex + 6]
            statMax = statMax[statMax.index(">") + 1:]
            statMax = statMax[:statMax.index("<")]

            statsToGet[i] = (int(stat), int(statMin), int(statMax))
     
        if len(effectivenesses) != 0 and len(uneffectivenesses) != 0:
            system('cls')
            input(f"{pokemon[:1].upper() + pokemon[1:]} is very effective towards {EffectiveText} type(s),\nis not so effective towards {NotEffectiveText} type(s),\n{'has no effect to ' + NonEffectiveText + ' type(s)' if NonEffectiveText != '' else ''}\n")
            fullStats = "---Base Stats---\n"
            for i in statsToGet.keys():
                stat = statsToGet[i]
                fullStats += i  + ": " + str(stat[0])
                fullStats += "\n"
                fullStats += i + " Min: " + str(stat[1])
                fullStats += "\n"
                fullStats += i + " Max: " + str(stat[2])
                fullStats += "\n\n"
            fullStats += "Catch Rate: "
            stat = linesSplitted.index(f'<th>Catch rate</th>') + 2
            stat = linesSplitted[stat].replace('<small class="text-muted">', '').replace('</small>', '')
            fullStats += stat + "\n"
            system('cls')
            input(fullStats)
    except:
        input("Try again...")