# random story generator


import random

when = [ 'A long time ago', 'Yesterday', 'Before you were born', 'In the future', 'Before Thanos arrived']
who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America']
where = ['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ']
why = ['to eat a lot of cakes', 'to fight fpr justice', 'to steal ice cream', 'to dance']


print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(where) + ' ' + random.choice(why))


