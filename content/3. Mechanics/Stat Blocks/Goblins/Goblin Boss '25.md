---
statblock: inline
---

```statblock
layout: Basic 5e Layout
image: 
name: Goblin Boss '25
size: Small
type: Fey
subtype: Goblinoid
alignment: Chaotic Neutral
ac: 17
hp: 21
hit_dice: 6d6
speed: 30 ft.
stats:
  - 10
  - 15
  - 10
  - 10
  - 8
  - 10
skillsaves:
  - Stealth: +6
senses: Darkvision 60 ft., Passive Perception 9
languages: Common, Goblin
cr: 1
actions:
  - name: Multiattack
    desc: The goblin makes two attacks using Scimitar or Shortbow in any combination.
  - name: Scimitar
    desc: "Melee Attack Roll: +4, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage, plus 2 (1d4) slashing damage if the attack roll had advantage."
  - name: Shortbow
    desc: "Ranged Attack Roll: +4, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage, plus 2 (1d4) piercing damage if the attack roll had advantage."
bonus_actions:
  - name: Nimble Escape
    desc: The goblin takes the Disengage or Hide action.
reactions:
  - name: Redirect Attack
    desc: "Trigger: A creature the goblin can see makes an attack roll against it. Response: The goblin chooses a Small or Medium ally within 5 feet of itself. The goblin and that ally swap places, and the ally becomes the target of the attack instead."
```
