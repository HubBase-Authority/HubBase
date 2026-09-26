from .Utils import player


class Item:
    def __init__(self, name: str = "Default Item", description: str = "", onuse: dict | None = None):
        self.name = name
        self.description = description
        self.taken = False
        self.special_conditions = {"unlock": self.unlocker}
        self.default_changes = {
            "HealAmount": 0,
            "special_use_conditions": None,
            "Target": None,
            "Passive": False
        }
        self.infinite = False
        self.used = False
        self.onuse = self.onuse_backend(onuse)
        if isinstance(self.onuse["special_use_conditions"], list):
            for condition in self.onuse["special_use_conditions"]:
                if condition == "infinite":
                    self.infinite = True

    def onuse_backend(self, changes: dict | None) -> dict:
        if not changes:
            return self.default_changes
        elif len(changes.keys()) <= 0:
            return self.default_changes
        else:
            return self.insert_changes(changes)

    def insert_changes(self, changes: dict) -> dict:
        onuse = self.default_changes
        for key in changes.keys():
            if key in onuse.keys():
                onuse[key] = changes[key]
        return onuse

    def use(self, current_room):
        if not self.onuse["Passive"]:
            if self.onuse["special_use_conditions"]:
                if isinstance(self.onuse["special_use_conditions"], list):
                    for condition in self.onuse["special_use_conditions"]:
                        if condition in self.special_conditions.keys():
                            self.used = self.special_conditions[condition](current_room=current_room)
            else:
                if self.onuse["Target"]:
                    if self.onuse["Target"] == "Player":
                        player.health += self.onuse["HealAmount"]
                        self.used = True
                    elif self.onuse["Target"] == "Creature":
                        try:
                            current_room.creature.take_damage(-self.onuse["HealAmount"])
                            self.used = True
                        except AttributeError:
                            print("There is no use for this item here.")
            if not self.infinite and self.used:
                player.inventory.remove(self)
        else:
            pass

    def take(self, current_room):
        try:
            current_room.items.remove(self)
        except (AttributeError, ValueError):
            print("This item is not in this room.")
            return
        self.taken = True
        player.inventory.append(self)

    def info(self) -> str:
        text = f"{self.name} - {self.description} "
        if self.onuse.values() != self.default_changes.values():
            text += "\nOn use: \n"
            if self.onuse["HealAmount"] != 0:
                text += f"{self.onuse["HealAmount"]}" if self.onuse["HealAmount"] < 0 else f"+{self.onuse["HealAmount"]}"
                text += "hp \n"
            if self.onuse["Target"]:
                text += f"This item targets the {self.onuse["Target"]}. \n"
            if self.onuse["special_use_conditions"]:
                if isinstance(self.onuse["special_use_conditions"], list):
                    for condition in self.onuse["special_use_conditions"]:
                        if condition in self.special_conditions.keys():
                            text += f"{condition.title()}s doors \n"
            if self.onuse["Passive"]:
                text += "This item is passive, meaning it is automatically used, and never spent \n"
            elif self.infinite:
                text += "This item is infinite, meaning it is never spent \n"
        return text

    def print_info(self):
        print(self.info())

    @staticmethod
    def unlocker(current_room):
        return current_room.handle_unlock()
