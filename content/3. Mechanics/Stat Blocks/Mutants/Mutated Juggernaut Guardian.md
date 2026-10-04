---
statblock: inline
---

```statblock
layout: Basic 5e Layout
image: 
name: Mutated Juggernaut Guardian
size: Large
type: Humanoid
subtype: Mutated
alignment: Lawful Evil
ac: 17
hp: 102
hit_dice: 12d10 + 36
speed: 25 ft.
stats:
  - 19
  - 10
  - 18
  - 8
  - 12
  - 9
saves:
  - Str: +6
  - Con: +6
  - Wis: +3
skillsaves:
  - Athletics: +8
  - Intimidation: +3
senses: Darkvision 60 ft., Passive Perception 13
languages: Common
cr: 6
traits:
  - name: Dense Mutation
    desc: The juggernaut has resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks.
  - name: Unstoppable Frame
    desc: The juggernaut cannot be knocked prone or forcibly moved against its will.
  - name: Pressure Build
    desc: Each time the juggernaut takes damage from a creature within 5 feet, it gains a charge (maximum 3). At 3 charges, its next Slam deals an additional 2d10 damage and expends all charges.
actions:
  - name: Multiattack
    desc: The juggernaut makes two Slam attacks.
  - name: Slam
    desc: "Melee Attack Roll: +8, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage."
  - name: Crushing Grip
    desc: "Melee Attack Roll: +8, reach 5 ft., one target. Hit: 10 (1d10 + 4) bludgeoning damage, and the target is grappled (escape DC 14). While grappled, the target is restrained."
bonus_actions:
  - name: Ground Shock (Recharge 5–6)
    desc: The juggernaut slams the ground. Each creature within 10 feet must succeed on a DC 14 Strength saving throw or take 10 (2d6 + 3) bludgeoning damage and be knocked prone.
reactions:
  - name: Brutal Retaliation
    desc: When a creature within 5 feet damages the juggernaut, it makes one Slam attack against that creature.
```
