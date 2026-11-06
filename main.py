import random
from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    @abstractmethod
    def hit(self, enemy):
        pass

    def alive(self):
        return self.hp > 0

    def info(self):
        print(f"  {self.name} — {max(self.hp, 0)} HP")


class Archer(Hero):
    def __init__(self, name):
        super().__init__(name, 85, 18)

    def hit(self, enemy):
        print(f"{self.name} пускает стрелу в {enemy.name}")
        enemy.hp -= self.power


class Berserker(Hero):
    def __init__(self, name):
        super().__init__(name, 130, 14)

    def hit(self, enemy):
        print(f"{self.name} крушит {enemy.name} дубиной")
        enemy.hp -= self.power


class Blacksmith(Hero):
    def __init__(self, name):
        super().__init__(name, 105, 16)

    def hit(self, enemy):
        print(f"{self.name} бьёт {enemy.name} молотом")
        enemy.hp -= self.power


class Knight(Hero):
    def __init__(self, name):
        super().__init__(name, 95, 17)

    def hit(self, enemy):
        print(f"{self.name} колет {enemy.name} копьём")
        enemy.hp -= self.power


class HeroFactory:
    types = {
        "archer": Archer,
        "berserker": Berserker,
        "blacksmith": Blacksmith,
        "knight": Knight,
    }

    @staticmethod
    def make(kind, name):
        cls = HeroFactory.types.get(kind.lower())
        if cls is None:
            raise ValueError(f"Нет такого героя: {kind}")
        return cls(name)


def battle(heroes):
    print(">>> БИТВА НАЧАЛАСЬ <<<\n")
    round_no = 1

    while sum(h.alive() for h in heroes) > 1:
        print(f"Раунд {round_no}")

        for attacker in heroes:
            if not attacker.alive():
                continue

            enemies = [h for h in heroes if h.alive() and h is not attacker]
            if not enemies:
                break

            victim = random.choice(enemies)
            attacker.hit(victim)

            if not victim.alive():
                print(f"  {victim.name} падает!")

        print()
        for h in heroes:
            h.info()
        print()

        round_no += 1

    for h in heroes:
        if h.alive():
            print(f">>> ПОБЕДИЛ: {h.name} <<<")
            return


def main():
    heroes = [
        HeroFactory.make("archer", "Эльф Володя"),
        HeroFactory.make("berserker", "Гном Кристина"),
        HeroFactory.make("blacksmith", "Огр Валерий"),
        HeroFactory.make("knight", "Фея Ольга"),
    ]
    battle(heroes)


if __name__ == "__main__":
    main()