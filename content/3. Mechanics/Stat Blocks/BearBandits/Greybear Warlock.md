---
statblock: inline
---

```statblock
layout: Basic 5e Layout
image:
name: Greybear Warlock
size: Medium
type: Humanoid
subtype: Greybear
alignment: Chaotic Evil
ac: 13 (Hide Armor)
hp: 42
hit_dice: 5d8 + 20
speed: 30 ft.
stats:
  - 12
  - 14
  - 18
  - 10
  - 13
  - 16
saves:
  - Con: +6
  - Wis: +3
  - Cha: +5
skillsaves:
  - Arcana: +2
  - Intimidation: +5
  - Religion: +2
damage_resistances: Necrotic
senses: Darkvision 60 ft., Passive Perception 11
languages: Common, Greybear
cr: 3
traits:
  - name: Dark Bond to Gundrik
    desc: "If Gundrik Ashclaw is within 120 feet of the warlock, he gains the benefits of this warlock's Ritual of Empowerment. When the warlock dies, Gundrik permanently gains that benefit for the remainder of the encounter."
  - name: Ritual of Empowerment
    desc: "Choose one ritual for each warlock. (1) Haste: Gundrik is under the effects of the Haste spell. (2) Warding Bond: Gundrik gains the benefits of Warding Bond with the warlock. (3) Crushing Time: One creature of the warlock's choice within 60 feet of Gundrik is affected by Slow until the start of the warlock's next turn (DC 13 Wisdom save at end of turn). (4) Brutal Strikes: Gundrik deals maximum damage with weapon attacks. (5) Blood Surge: Once per turn when Gundrik deals damage, he regains 8 hit points. (6) Ashen Fury: Gundrik adds 1d8 force damage to his weapon attacks. (7) Unyielding Hide: Gundrik gains resistance to bludgeoning, piercing, and slashing damage."
actions:
  - name: Eldritch Bolt
    desc: "Ranged Spell Attack: +5 to hit, range 120 ft., one target. Hit: 10 (2d6 + 3) necrotic damage."
  - name: Hexing Curse (Recharge 5-6)
    desc: "One creature the warlock can see within 60 feet must succeed on a DC 13 Constitution saving throw or take 7 (2d6) necrotic damage and subtract 1d4 from the next attack roll or saving throw it makes before the end of its next turn."
bonus_actions:
  - name: Dark Channel
    desc: "Gundrik gains 10 temporary hit points."
reactions:
  - name: Dying Invocation
    desc: "When reduced to 0 hit points, the warlock may immediately cast one final Ritual of Empowerment on Gundrik, which becomes permanent for the remainder of the encounter."
```
