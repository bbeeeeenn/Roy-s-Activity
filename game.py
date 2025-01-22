from mod_char import *
from mod_party import Party
import random, os

os.system("cls")


def is_anyone_alive(party: Party):
    return any(member.is_alive() for member in party.members)


hero_party = Party()
heroes = [Swordsman("Alucard"), Archer("Miya"), Wizard("Cyclops"), Healer("Estes")]
for hero in heroes:
    print(hero_party.add_member(hero))
turn = 0

boss = BossMonster()

while True:
    print("\n")
    for hero in hero_party.members:
        if isinstance(hero, Healer):
            print(hero.heal(random.choice(hero_party.members)))
        else:
            print(hero.attack(boss))

        if not boss.is_alive():
            print("The boss has been defeated!")
            break
    if not boss.is_alive():
        break
    else:
        print(f"Boss HP remaining: {boss.health}")

    boss_target = random.choice(hero_party.members)
    print("\n" + boss.attack(boss_target))
    if not boss_target.is_alive():
        print(f"\n{boss_target.name} has died!\n")
        hero_party.remove_member(boss_target)
        if not is_anyone_alive(hero_party):
            print("All heroes have died!")
            break
    else:
        print(f"{boss_target.name}'s HP remaining: {boss_target.health}")
    input("Press Enter to continue...")
    os.system("cls")
