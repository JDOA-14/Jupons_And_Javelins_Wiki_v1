---
statblock: inline
---

```statblock
layout: Basic 5e Layout
image:
name: Aarakocra Monk Guard
size: Medium
type: Humanoid
subtype: Aarakocra
alignment: Lawful Neutral
ac: 15 (Unarmored Defense)
hp: 38
hit_dice: 7d8 + 7
speed: 30 ft., fly 50 ft.
stats:
  - 10
  - 16
  - 12
  - 10
  - 14
  - 11
saves:
  - Dex: +5
  - Wis: +4
skillsaves:
  - Acrobatics: +5
  - Insight: +4
  - Perception: +4
  - Athletics: +2
damage_resistances:
condition_immunities:
senses: Passive Perception 14
languages: Aarakocra, Common
cr: 2
proficiency_bonus: +2

traits:
  - name: Unarmored Movement
    desc: "The monk guard’s walking speed increases by 10 feet while not wearing armor or wielding a shield."

  - name: Windborne Step
    desc: "The guard does not provoke opportunity attacks when it flies out of an enemy’s reach."

  - name: Watchful Eyes
    desc: "The guard has advantage on Wisdom (Perception) checks that rely on sight or hearing."

actions:
  - name: Multiattack
    desc: "The guard makes two Unarmed Strike attacks."

  - name: Unarmed Strike
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage."

  - name: Wind Palm Technique
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage, and the target must succeed on a DC 13 Strength saving throw or be pushed 10 feet."

bonus_actions:
  - name: Step of the Wind (Reposition)
    desc: "The guard can Dash or Disengage."

reactions:
  - name: Deflect Strike
    desc: "When the guard is hit by a melee weapon attack, it reduces the damage by 1d10 + 3."
```
