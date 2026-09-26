class Player:
    def __init__(self):
        self.health = 100
        self.fullinventory = []
        self.inventory = []
        self.damagetype = "rand-5t15"
        self.damage = 0
        self.dead = False

    def take_damage(self, damage: int | float = 0):
        self.health -= damage
        self.health = max(self.health, 0)
        self.dead = self.health == 0

    def reset(self):
        self.health = 100
        self.fullinventory = []
        self.inventory = []
        self.damagetype = "rand-5t15"
        self.damage = 0
        self.dead = False
