```statblock
layout: Basic 5e Layout
image: 
name: Priest '25
size: Medium
type: Humanoid
subtype: Cleric
alignment: Neutral
ac: 13
hp: 38
hit_dice: 7d8 + 7
speed: 30 ft.
stats:
  - 16
  - 10
  - 12
  - 13
  - 16
  - 13
skillsaves:
  - Medicine: +7
  - Perception: +5
  - Religion: +5
senses: Passive Perception 15
languages: Common, one other
cr: 2
spells:
  - The priest casts spells using Wisdom.
  - At will: light, thaumaturgy
  - 1/day: spirit guardians
actions:
  - name: Multiattack
    desc: The priest makes two attacks, using Mace or Radiant Flame in any combination.
  - name: Mace
    desc: "Melee Attack Roll: +5, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage plus 5 (2d4) radiant damage."
  - name: Radiant Flame
    desc: "Ranged Attack Roll: +5, range 60 ft., one target. Hit: 11 (2d10) radiant damage."
  - name: Spellcasting
    desc: The priest casts one of its prepared spells.
bonus_actions:
  - name: Divine Aid (3/Day)
    desc: The priest casts Bless, Dispel Magic, Healing Word, or Lesser Restoration using the same spellcasting ability as Spellcasting.
```
