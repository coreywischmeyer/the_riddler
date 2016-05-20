'''
A video game requires you to slay monsters to collect gems.
Every time you slay a monster, it drops one of three types of gems:
a common gem, an uncommon gem or a rare gem. The probabilities of
these gems being dropped are in the ratio of 3:2:1 — three common
gems for every two uncommon gems for every one rare gem, on average.
If you slay monsters until you have at least one of each of the three
types of gems, how many of the most common gems will you end up with, on average?
'''
import random

common = [i for i in range(1, 4)]
uncommon = [i for i in range(4, 6)]
rare = [6]

def slay_monsters():
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