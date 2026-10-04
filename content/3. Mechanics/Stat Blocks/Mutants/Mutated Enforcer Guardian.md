```statblock
layout: Basic 5e Layout
image: 
name: Mutated Enforcer Guardian
size: Large
type: Humanoid
subtype: Mutated
alignment: Lawful Evil
ac: 16
hp: 94
hit_dice: 9d10 + 45
speed: 30 ft.
stats:
  - 18
  - 13
  - 20
  - 9
  - 11
  - 10
saves:
  - Str: +4
  - Con: +5
  - Wis: +0
skillsaves:
  - Perception: +5
  - Intimidation: +3
senses: Darkvision 60 ft., Passive Perception 15
languages: Common
cr: 5
traits:
  - name: Controlled Mutation (4/Day)
    desc: If the enforcer ends any turn Bloodied and took 15 or more slashing damage during that turn, part of its mutated body tears away or hardens under stress. The enforcer gains 1 level of Exhaustion, but its attacks deal an additional 1d6 damage until the end of its next turn. Lost tissue rapidly reforms the next time it regains hit points.
  - name: Regenerative Flesh
    desc: The enforcer regains 15 hit points at the start of each of its turns. If it takes necrotic or fire damage, this trait doesn't function on its next turn. The enforcer dies only if it starts its turn with 0 hit points and doesn't regenerate.
  - name: Engineered Brutality
    desc: The enforcer's body is designed for combat efficiency. Its melee attacks score a critical hit on a roll of 19–20.
actions:
  - name: Multiattack
    desc: The enforcer makes three Rend attacks.
  - name: Rend
    desc: "Melee Attack Roll: +7, reach 10 ft., one target. Hit: 11 (2d6 + 4) slashing damage."
  - name: Crushing Blow
    desc: "Melee Attack Roll: +7, reach 5 ft., one target. Hit: 15 (2d10 + 4) bludgeoning damage. If the target is Medium or smaller, it must succeed on a DC 14 Strength saving throw or be knocked prone."
bonus_actions:
  - name: Tactical Advance
    desc: The enforcer moves up to half its speed toward a creature it can see. If it ends this movement within 5 feet of a creature, it gains advantage on its next attack this turn.
```
