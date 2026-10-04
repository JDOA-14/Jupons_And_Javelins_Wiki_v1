```statblock
layout: Basic 5e Layout
image: 
name: Shardbound Penitent
size: Medium
type: Humanoid
subtype: Paladin
alignment: Lawful Neutral
ac: 18
hp: 68
hit_dice: 8d8 + 32
speed: 30 ft.
stats:
  - 16
  - 10
  - 18
  - 10
  - 12
  - 14
saves:
  - Wis: +4
  - Cha: +5
skillsaves:
  - Athletics: +6
  - Intimidation: +5
  - Religion: +2
  - Perception: +4
senses: Passive Perception 14
languages: Common, Celestial
cr: 3
traits:
  - name: Desperate Faith
    desc: The penitent has advantage on saving throws against being frightened while it can see an allied Shardbound Penitent within 30 feet.
  - name: Guard the Relic
    desc: While the penitent is within 20 feet of the protected magic item, it has advantage on opportunity attacks and on saving throws against being charmed.
  - name: Shard Disruption
    desc: If the penitent takes 10 or more damage from a single source before it uses Shard Inhalation, or if it takes bludgeoning or lightning damage before then, it drops the shard it was preparing to use and can't use Shard Inhalation that turn.
actions:
  - name: Multiattack
    desc: The penitent makes two attacks with Greatsword or Javelin.
  - name: Greatsword
    desc: "Melee Attack Roll: +6, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage."
  - name: Javelin
    desc: "Melee or Ranged Attack Roll: +6, reach 5 ft. or range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage."
  - name: Smite Strike
    desc: "Melee Attack Roll: +6, reach 5 ft., one target. Hit: 19 (2d6 + 3 plus 2d8) slashing and radiant damage. The penitent can use this attack only if it used Shard Inhalation this turn or on its previous turn."
bonus_actions:
  - name: Shard Inhalation
    desc: The penitent crushes a faith shard and inhales its power. Until the end of its turn, the next time it hits with a melee weapon attack, the attack deals an extra 2d8 radiant damage. The penitent usually uses this every round while it still has shards. A penitent typically begins combat with 3 shards.
  - name: Vow of Endurance (1/Day)
    desc: The penitent gains 10 temporary hit points.
reactions:
  - name: Hold the Line
    desc: When a creature the penitent can see moves within 5 feet of the protected relic or tries to move away from the penitent, the penitent makes one Greatsword attack against that creature.
```

