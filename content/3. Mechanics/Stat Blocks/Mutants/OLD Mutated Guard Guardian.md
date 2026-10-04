
```statblock
layout: Basic 5e Layout
image: 
name: Mutated Guard Guardian
size: Large
type: Humanoid
subtype: Mutated, Guard
alignment: Lawful Evil
ac: 15
hp: 94
hit_dice: 9d10 + 45
speed: 30 ft.
stats:
  - 18
  - 13
  - 20
  - 8
  - 10
  - 9
saves:
  - Str: +4
  - Con: +5
  - Wis: +0
skillsaves:
  - Perception: +5
  - Religion: +2
senses: Darkvision 60 ft., Passive Perception 15
languages: Common, Celestial
cr: 5
traits:
  - name: Shard-Twisted Form (4/Day)
    desc: If the guardian ends any turn Bloodied and took 15 or more slashing damage during that turn, part of its body violently mutates or tears free. This fragment becomes a hostile Shard Fragment that acts immediately after the guardian's turn. The guardian has 1 level of Exhaustion for each fragment lost and regrows these parts the next time it regains hit points.
  - name: Corrupted Regeneration
    desc: The guardian regains 15 hit points at the start of each of its turns. If it takes radiant or fire damage, this trait doesn't function on its next turn. The guardian dies only if it starts its turn with 0 hit points and doesn't regenerate.
  - name: Broken Oath
    desc: The guardian has advantage on saving throws against being charmed or frightened. However, when reduced below half its hit points, it has disadvantage on Wisdom saving throws as its fractured mind begins to collapse.
actions:
  - name: Multiattack
    desc: The guardian makes three Rend attacks.
  - name: Rend
    desc: "Melee Attack Roll: +7, reach 10 ft., one target. Hit: 11 (2d6 + 4) slashing damage."
  - name: Shard Slam
    desc: "Melee Attack Roll: +7, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning and radiant damage."
bonus_actions:
  - name: Zealous Charge
    desc: The guardian moves up to half its speed straight toward an enemy it can see. If it ends this movement within 5 feet of a creature, it has advantage on its next Rend attack this turn.
```