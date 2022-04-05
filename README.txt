README
Just A Fighting Game v1.0

Contents:
01. Introduction
02. Fighters
03. Fighter Stats
04. Basic Fighter Moves
05. Attack Rolls & Damage Rolls
06. Punch & Kick Moves: Damage Rolls
07. Block Move
08. Block Move: Defense Increases & Health Recovery
09. Opponent Difficulty
10. Player Fighter Upgrades
11. The Fight

01. Introduction
This is Just A Fighting Game, a text-based fighting game!
Available inputs at any time will be in caps & are case insensitive.
Input prompts will be indicated by the > symbol.
In this game you control a fighter fighting another fighter. Simple!

02. Fighters
There are 2 fighters in the fight: you and 1 opponent.
The opponent is controlled by the computer, and can be varying levels of difficulty.

03. Fighter Stats
All fighters have the following stats:
Health: the fighter's total health points. This decreases when an attack deals damage to the fighter.
Punch Defense: an opponent must roll at least this number to hit when making a punch attack.
Kick Defense: an opponent must roll at least this number to hit when making a kick attack.
Crit Roll: a fighter must roll at least this number to score a critical hit.
Punch Level: how strong the fighter's punch attack is.
Kick Level: how strong the fighter's kick attack is.
Block Level: how strong the fighter's block move is.
In addition, CPU fighters have a difficulty: easy, medium, hard or deadly.
View stats for each fighter using the Stats option in the Main Menu.

04. Basic Fighter Moves
All fighters have 3 moves: Punch, Kick & Block.
Punch: attack dealing more consistent damage.
Kick: attack dealing more varied damage, with higher maximum & lower minimum damage than the punch.
Block: attempt to recover health points by blocking the opponent's next attack.

05. Attack Rolls & Damage Rolls
Attacks are performed using dice rolls, specifically 6-sided, 8-sided & 10-sided dice.
'xdy' denotes a rolling a y-sided die x times. E.g. 3d6 would represent rolling 3 6-sided dice.
Punch & Kick attacks are broken into an Attack Role and a Damage Roll.
An Attack Role is 1d6.
If the attack role is at least the fighter's Crit Roll, the attack is a Critical Hit.
Else, if the attack role is less than the opponent's Punch/Kick Defense (depending on the type of attack), the attack is a Miss.
Else, the attack is a Hit.
Critical Hits do double damage.
Misses do zero damage.
The higher the fighter's Punch/Kick Level, the more damage dice are rolled for that attack.
The total damage is subtracted from the opponent fighter's health.

06. Punch & Kick Moves: Damage Rolls
After a successful Attack Roll, a different combination of damage dice are rolled depending on the attack and its level.
Punch Damage:
Lvl 1 (Punch): 2d6
Lvl 2 (Punch+): 4d6
Lvl 3 (Tiger's Bite): 8d6
Kick Damage:
Lvl 1 (Kick): 2d10
Lvl 2 (Kick+): 3d10
Lvl 3 (Dragon's Wrath): 1d6 + 5d10

07. Block Move
The Block move is different to the Punch & Kick Moves.
When a fighter blocks, their Punch & Kick Defense temporarily increases for 1 turn & no damage is dealt to the opponent.
On the opponent's next turn, the fighter recovers some health points.
The amount of health recovered depends on dice rolls.
The higher the fighter's Block Level, the more dice are rolled to determine this.
If the opponent's next attack is a Miss, the fighter regains the full amount of health points rolled.
If the opponent's next attack is a Hit, the fighter regains half the amount of health points rolled.
If the opponent's next attack is a Critical Hit, the fighter regains zero health points.
In addition, the higher the fighter's Block Level, the more their defense temporarily increases.
The fighter's Punch & Kick Defense returns to normal on their next turn.

08. Block Move: Defense Increases & Health Recovery
Defense Increases:
Lvl 1 (Block): +1 Punch & Kick Defense
Lvl 2 (Block+): +1 Punch & Kick Defense
Lvl 3 (Earthen Wall): +2 Punch & Kick Defense
Health Recovery:
Lvl 1 (Block): 2d6
Lvl 2 (Block+): 3d6 + 1d8
Lvl 3 (Earthen Wall): 3d6 + 2d8 + 2d10

09. Opponent Difficulty
Opponents have a difficulty (in increasing order) of Easy, Medium, Hard or Deadly.
You choose the difficulty of your opponent before the fight starts.
Choosing a higher difficulty means that you can upgrade your fighter's stats more before the fight.

10. Player Fighter Upgrades
Before the fight starts, you can upgrade your fighter a certain number of times, based on the opponent's difficulty.
The possible upgrades are:
Increase Health by 15, no maximum value.
Increase Punch Defense by 1, maximum value of 4.
Increase Kick Defense by 1, maximum value of 4.
Decrease Crit Roll by 1, minimum value of 5.
Increase Punch Level by 1, maximum value of 3.
Increase Kick Level by 1, maximum value of 3.
Increase Block Level by 1, maximum value of 3.

11. The Fight
Each fighter takes it in turn to choose a move, dealing damage and/or recovering health points.
The fight ends when one fighter has zero health points.
Against Easy, Medium & Hard opponents, the player takes their turn first.
Deadly opponents take their turn before the player.
Good luck!