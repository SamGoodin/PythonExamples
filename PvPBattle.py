"""
edabit Coding Challenge PvP Battle: Alice vs Bob https://edabit.com/challenge/ifDM26p25bqS8EsFu
Having gotten rather sick of always being paired together in sciency literature, Alice and Bob have decided to finally
settle their differences with a magical duel. They'll each learn some skills and then battle it out.

Your Goal
Your job is to write the class Player which will handle all the combat mechanics.
"""

class Player:

    def __init__(self, name, health, energy, armor):
        self.__hp = health
        self.__maxHp = health
        self.__en = energy
        self.__maxEn = energy

        # Armor acts as a percentage reduction of damage ranging 0-100
        # ex. 100 dmg to player with 25 armor = 75% of 100 = 75 dmg
        if armor > 100:
            self.armor = 100
        elif armor < 0:
            self.armor = 0
        else:
            self.armor = armor

        self.name = name
        # Just tracks all player skills - arbitrary from the project
        self.skills = {}

    def learnSkill(self, skillName, stats):
        # "Fireball" "{ damage: 20, penetration: 1.2, heal: 10, cost: 15, desc: 'a fiery magical attack' }"

        def fn(self, victim):
            # skill use
            if self.__en < stats['cost']:
                return self.name + " attempted to use " + skillName + ", but didn't have enough energy!\n"
            else:
                effectiveVArmor = victim.armor - stats['penetration']
                effectiveDmg = stats['damage'] * ((100 - effectiveVArmor) / 100)

                # Attack
                victim.setHp(victim.getHp() - effectiveDmg)

                turnText = ""
                turnText += self.name + " used skill " + skillName + ", " + stats['desc'] + ", against " + \
                       victim.name + " doing " + str(effectiveDmg) + " damage!\n"

                # Heal
                if stats['heal'] != 0:
                    self.setHp(self.getHp() + stats['heal'])
                    turnText += self.name + " healed for " + str(stats['heal']) + " health.\n"

                # Check if victim dead
                if victim.getHp() <= 0:
                    turnText += victim.name + " died."
                else:
                    turnText += victim.name + " is at " + str(victim.getHpPerc()) + "% health.\n"

                return turnText

        self.skills[skillName] = stats

        # setattr(object, function name, function
        setattr(Player, skillName, fn)

    def getSkills(self):
        return self.skills

    def getHpPerc(self):
        return round(self.__hp / self.__maxHp, 2) * 100

    def getHp(self):
        return self.__hp

    def getEnergy(self):
        return self.__en

    def setHp(self, hp):
        if hp > self.__maxHp:
            self.__hp = self.__maxHp
        elif hp < 0:
            self.__hp = 0
        else:
            self.__hp = hp

    def setEn(self, energy):
        if energy > self.__maxEn:
            self.__en = self.__maxEn
        elif energy < 0:
            self.__en = 0
        else:
            self.__en = energy


bob = Player("Bob", 100, 50, 50)
bob.learnSkill("fireball", {
    'damage': 23,
    'penetration': 1.2,
    'heal': 5,
    'cost': 15,
    'desc': "a fiery magical attack"
})
hal = Player("Hal", 200, 25, 10)
hal.learnSkill("iceball", {
    'damage': 17,
    'penetration': .6,
    'heal': 3,
    'cost': 5,
    'desc': "an icy magical attack"
})

print(bob.getSkills())
print(hal.getSkills())

for x in range(10):
    if x % 2 == 0:
        print(bob.fireball(hal))
    else:
        print(hal.iceball(bob))