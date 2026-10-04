---
statblock: inline
---

```statblock
layout: Basic 5e Layout
image: 
name: Undead Spirit
size: Medium
type: Undead
subtype: Summon
alignment: Neutral
ac: 11 + the spell's level
hp: 30 (Ghostly and Putrid only) or 20 (Skeletal only) + 10 for each spell level above 3
hit_dice: 
speed: 30 ft., fly 40 ft. (hover; Ghostly only)
stats:
  - 12
  - 16
  - 15
  - 4
  - 10
  - 9
saves:
  - Str: +1
  - Dex: +3
  - Con: +2
damage_immunities: Necrotic, Poison
condition_immunities: Exhaustion, Frightened, Paralyzed, Poisoned
senses: Darkvision 60 ft., Passive Perception 10
languages: understands the languages you know
cr: 0
traits:
  - name: Festering Aura (Putrid Only)
    desc: Any creature other than you that starts its turn within a 5-foot emanation originating from the spirit must make a Constitution saving throw against your spell save DC. On a failure, the creature has the Poisoned condition until the start of its next turn.
  - name: Incorporeal Passage (Ghostly Only)
    desc: The spirit can move through other creatures and objects as if they were difficult terrain. If it ends its turn inside an object, it is shunted to the nearest unoccupied space and takes 1d10 force damage for every 5 feet traveled.
actions:
  - name: Multiattack
    desc: The spirit makes a number of attacks equal to half the spell's level, rounded down.
  - name: Deathly Touch (Ghostly Only)
    desc: "Melee Attack Roll: bonus equals your spell attack modifier, reach 5 ft., one target. Hit: 1d8 + 3 + the spell's level necrotic damage, and the target has the Frightened condition until the end of its next turn."
  - name: Grave Bolt (Skeletal Only)
    desc: "Ranged Attack Roll: bonus equals your spell attack modifier, range 150 ft., one target. Hit: 2d4 + 3 + the spell's level necrotic damage."
  - name: Rotting Claw (Putrid Only)
    desc: "Melee Attack Roll: bonus equals your spell attack modifier, reach 5 ft., one target. Hit: 1d6 + 3 + the spell's level slashing damage. If the target has the Poisoned condition, it has the Paralyzed condition until the end of its next turn."
```
