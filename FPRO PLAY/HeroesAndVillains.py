def fight(heroes,villain):
    for hero in heroes:
        if villain['category'] == hero['category']:
            if villain['health'] > hero['health']:
                villain['health'] -= hero['health']/2
            else:
                hero['score'] += 1
                return '{0} defeated the villain and now has a score of {1}'.format(hero['name'],hero['score'])
    return '{0} prevailed with {1}HP left'.format(villain['name'],villain['health'])