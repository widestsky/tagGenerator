import random

tags = [
    'ottawa',
    'myottawa',
    'ottawaliving',
    'ottcity',
    'ottawaontario',
    'ottawalife',
    'ottawablogger',
    'ottawastyle',
    'ottawabusiness',
    'ottawatourism',
    'ottawacanada',
    'downtownottawa',
    'ottawaquarantine',
    'ottawachinatown',
    'ottalovesyou',
    'ottawachiropractor',
    'ottawaevents',
    'ottawarestaurants',
    'quarantine',
    'stayhome',
    'lockdown',
    'quarantinelife',
    'selfquarantine',
    'backpain',
    'lowbackpain',
    'neckpain',
    'painmanagement',
    'standingdesk',
    'workspaces',
    'workstation',
    'deskdesign',
    'desksetup',
    'deskinspo'
    ]

count = 30

result = []

while len(result) < count:
    pick = tags[random.randint(0, len(tags)-1)]
    if pick not in result:
        result.append(pick)

output = '#' + ' #'.join(result)

print(output)
