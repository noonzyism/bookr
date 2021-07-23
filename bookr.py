import csv
from collections import Counter

def most_frequent(List):
    return max(set(List), key = List.count)

if __name__ == '__main__':
    
    alldates = []
    playerdates = {}
    gameplayers = {}

    gamedates = {}

    with open('signups.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
                print(f'\t{row[0]} sign-ups are: {", ".join(filter(None, row[1:]))}.')
                gameplayers[row[0]] = filter(None, row[1:])
                line_count += 1

    with open('scheds.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                alldates = row
                print(f'Dates are {", ".join(alldates)}')
                line_count += 1
            else:
                i = 0
                for cell in row[1:]:
                    i += 1
                    if (cell == "OK"):
                        row[i] = alldates[i]
                playerdates[row[0]] = [d for d in row[1:] if d]
                print(f'\t{row[0]} is free on {", ".join(playerdates[row[0]])}.')
                line_count += 1

    print(f'====')

    for game in gameplayers:
        dates = []
        for player in gameplayers[game]:
            if player in playerdates:
                dates += playerdates[player]
        
        c = Counter(date for date in dates)
        print("{}: {}".format(game, c.most_common(5)))
