class Character:
    def __init__(self, name, health, attack_power):
        """
        Initialize the object with the given name, health, and attack power.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        """
        Decreases the health of the target by the attack power of the attacker and returns a message about the attack.
        """
        target.health -= self.attack_power
        return f"{self.name} attacks {target.name} for {self.attack_power} damage!"

    def is_alive(self):
        """
        Check if the entity is alive based on its health.
        """
        return self.health > 0


class Swordsman(Character):
    def __init__(self, name):
        """
        Initializes a new instance of the class.

        Parameters:
            name (str): The name of the instance.

        Returns:
            None
        """
        super().__init__(name, health=100, attack_power=15)

    def thrust(self, target):
        target.health -= 40
        return f"{self.name} thrusts {target.name} and deals 40 damage!"


class Wizard(Character):
    def __init__(self, name):
        """
        Initialize the object with the given name, health=80, and attack_power=25.
        """
        super().__init__(name, health=80, attack_power=25)

    def cast_spell(self, target):
        """
        This function casts a spell on the target, decreasing its health by 30. It returns a string describing the spell cast.
        """
        target.health -= 30
        return f"{self.name} casts fireball on {target.name} for 30 damage!"


class Healer(Character):
    def __init__(self, name):
        """
        Initializes the object with a given name, health of 70, and attack power of 5.
        """
        super().__init__(name, health=70, attack_power=5)

    def heal(self, target):
        """
        A function that heals the target by a specified amount and returns a message indicating the healing action.
        Parameters:
            target: The entity to be healed.
        Returns:
            A string indicating the healing action performed.
        """
        heal_amount = 20
        target.health += heal_amount
        return f"{self.name} heals {target.name} for {heal_amount} HP!"


class Archer(Character):
    def __init__(self, name):
        """
        Initialize the object with the given name, health, and attack power.
        """
        super().__init__(name, health=90, attack_power=20)

    def precision_shot(self, target):
        """
        A method to perform a precision shot on the target, causing 35 damage and returning a description of the action.
        """
        target.health -= 35
        return f"{self.name} makes a precision shot on {target.name} for 35 damage!"


class BossMonster(Character):
    def __init__(self):
        """
        Initializes the Boss Monster with a health of 500 and an attack power of 30.
        """
        super().__init__("Boss Monster", health=500, attack_power=30)

    def special_attack(self, target):
        """
        Perform a special attack on the target, decreasing its health by 50.
        Returns a message indicating the use of a special attack and the amount of damage dealt.
        """
        target.health -= 50
        return f"{self.name} uses a special attack on {target.name} for 50 damage!"


# class Character:
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def attack(self, target):
#         target.health -= self.attack_power
#         print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

#     def is_alive(self):
#         return self.health > 0

# class Swordsman(Character):
#     def __init__(self, name):
#         super().__init__(name, health=100, attack_power=15)

# class Wizard(Character):
#     def __init__(self, name):
#         super().__init__(name, health=80, attack_power=25)

# class Healer(Character):
#     def __init__(self, name):
#         super().__init__(name, health=70, attack_power=5)

#     def heal(self, target):
#         heal_amount = 20
#         target.health += heal_amount
#         print(f"{self.name} heals {target.name} for {heal_amount} health!")

# class Archer(Character):
#     def __init__(self, name):
#         super().__init__(name, health=90, attack_power=20)

# class Monster(Character):
#     def __init__(self, name, health, attack_power):
#         super().__init__(name, health, attack_power)

# # # Test creating characters
# # swordsman = Swordsman("Arthur")
# # wizard = Wizard("Merlin")
# # healer = Healer("Galahad")
# # archer = Archer("Robin")

# # # Test character interactions
# # print(f"Before healing: {swordsman.name}'s health = {swordsman.health}")
# # healer.heal(swordsman)
# # print(f"After healing: {swordsman.name}'s health = {swordsman.health}")

# # # Test attack
# # wizard.attack(swordsman)
# # print(f"After attack: {swordsman.name}'s health = {swordsman.health}")
