import random

tags = [
    'bestmeow10k', #175k
    'cat_features_daily', #86k
    'kittengram', #317k
    'kittenlife', #418k
    'kittenpaws', #42k
    'kittenselfie', #84k
    'cutekitties', #128k
    'cat_delight', #452k
    'catofday', #362k
    'catclub', #340k
    'catractive', #338k
    'purrpurrpurr', #226k
    'catpicoftheday', #153k
    'playfulkitty', #95k
    'catsarepawsome', #142k
    'sleepycatsofinstagram', #52k
    'sleepycats', #207k
    'floofycat', #93k
    'lazycats', #145k
    'caturdayvibes', #21k
    'purrfection', #262k
    'sleepycats', #207k
    'orangeandwhitecat', #54k
    'playfulcat', #129k
    'fluffycatsofinstagram', #128k
    'catgag', #109k
    'cutecats_oftheworld', #130k
    'catstoday', #145k
    'catexplorer', #73k
    'catcomics', #15k
    'catadventures', #79k
    'catbackpack', #18k
    'catsinquarantine', #12k
    'catsogram', #300k
    'catshaming', #56k
    'catsofquarantine', #15k
    'quarantinecats', #85k
    'orangecatsofinstagram', #410k
    'gingercatsrule', #276k
    'gingercatclub', #92k
    'longhairedcats', #56k
    'domesticshorthair', #371k
    'floofycat', #93k
    'twofacedcat', #15k
    'catsofnyc', #161k
    'catsofchicago', #61k
    'catsofcanada', #116k
    ]

count = 30

result = []

while len(result) < count:
    pick = tags[random.randint(0, len(tags)-1)]
    if pick not in result:
        result.append(pick)

output = '#' + ' #'.join(result) + ' @cutemeaws'

print(output)
