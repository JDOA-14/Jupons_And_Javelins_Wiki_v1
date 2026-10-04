```statblock
layout: Basic 5e Layout
image: 
name: Mutated Guardian Juggernaut
size: Large
type: Humanoid
subtype: Mutated
alignment: Lawful Evil
ac: 16
hp: 105
hit_dice: 12d10 + 36
speed: 25 ft.
stats:
  - 19
  - 11
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
  - name: Regenerative Flesh
    desc: The juggernaut regains 15 hit points at the start of each of its turns. If it takes necrotic, poison, or acid damage, this trait doesn't function on its next turn. The juggernaut dies only if it starts its turn with 0 hit points and doesn't regenerate.
  - name: Weaponised Mutation (4/Day)
    desc: If the juggernaut ends any turn Bloodied and took 15 or more slashing damage during that turn, one of its limbs is violently torn or reshaped. The juggernaut gains 1 level of Exhaustion, but its melee attacks deal an additional 1d6 damage for the rest of the encounter (stacks per limb lost). Lost limbs regrow the next time it regains hit points.
  - name: Dense Mutation
    desc: The juggernaut has resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks.
  - name: Unstoppable Frame
    desc: The juggernaut can't be knocked prone or forcibly moved against its will.
actions:
  - name: Multiattack
    desc: The juggernaut makes two Slam attacks.
  - name: Slam
    desc: "Melee Attack Roll: +8, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage."
  - name: Crushing Grip
    desc: "Melee Attack Roll: +8, reach 5 ft., one target. Hit: 10 (1d10 + 4) bludgeoning damage, and the target is grappled (escape DC 14). While grappled, the target is restrained."
bonus_actions:
  - name: Ground Shock (Recharge 5–6)
    desc: Each creature within 10 feet must succeed on a DC 14 Strength saving throw or take 10 (2d6 + 3) bludgeoning damage and be knocked prone.
  - name: Tactical Advance
    desc: The juggernaut moves up to half its speed toward a creature it can see. If it ends this movement within 5 feet of a creature, it gains advantage on its next attack this turn.
reactions:
  - name: Brutal Retaliation
    desc: When a creature within 5 feet damages the juggernaut, it makes one Slam attack against that creature.
```
