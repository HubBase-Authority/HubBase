from .Utils import player, GuardedCalculateDamage

class Creature:
    def __init__(self, name:str, health:int=30, damagetype:str|int="rand-10t20"):
        self.name = name
        self.health = health
        self.damagetype = str(damagetype)
        self.damage = 0
        self.dead = False

    def fight_player(self):
        self.damage = GuardedCalculateDamage(self.damagetype)
        player.damage = GuardedCalculateDamage(player.damagetype)
        player.take_damage(self.damage)
        self.take_damage(player.damage)
        self.dead = self.health == 0

    def take_damage(self, damage:int|float=0):
        self.health -= damage
        self.health = max(self.health, 0)
