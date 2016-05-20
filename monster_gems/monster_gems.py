import random

def slay_monsters():
  common = [i for i in range(1, 4)]
  uncommon = [i for i in range(4, 6)]
  rare = [6]
  gem_bag = []
  all_collected = False
  while(all_collected is False):
    gem = random.randint(1,6)
    if gem in common:
      gem_bag.append('common')

    if gem in uncommon:
      gem_bag.append('uncommon')

    if gem in rare:
      gem_bag.append('rare')

    if ('rare' in gem_bag and
        'uncommon' in gem_bag and
        'common' in gem_bag):
      all_collected = True

  return gem_bag.count('common')

counts = []

for i in range(1,100000):
  counts.append(slay_monsters())

print(sum(counts)/float(len(counts)))