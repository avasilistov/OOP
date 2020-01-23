from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            'HP': 128,  # health points
            'MP': 42,  # magic points
            'SP': 100,  # skill points
            'Strength': 15,
            'Perception': 4,
            'Endurance': 8,
            'Charisma': 2,
            'Intelligence': 3,
            'Agility': 8,
            'Luck': 1,
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffects(ABC, Hero):
    pass


class AbstractNegative(AbstractEffects):

    @abstractmethod
    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffects):

    @abstractmethod
    def get_positive_effects(self):
        pass


class Berserk(AbstractPositive):
    _base = None

    def __init__(self, _base: Hero):
        self._base = _base
        self.stats = _base.stats
        self.positive_effects = _base.positive_effects
        self.negative_effects = _base.negative_effects

    def get_positive_effects(self):
        self.positive_effects.append('Berserk')
        return self.positive_effects.copy()


    def get_stats(self):
        self.stats['HP'] += 50
        self.stats['Strength'] += 7
        self.stats['Endurance'] += 7
        self.stats['Agility'] += 7
        self.stats['Luck'] += 7
        self.stats['Perception'] -= 3
        self.stats['Charisma'] -= 3
        self.stats['Intelligence'] -= 3

        return self.stats.copy()


class Curse(AbstractNegative):
    _base = None

    def __init__(self, _base: Hero):
        self._base = _base
        self.stats = _base.stats.copy()
        self.positive_effects = _base.positive_effects.copy()
        self.negative_effects = _base.negative_effects.copy()

    def get_negative_effects(self):
        self.negative_effects.append('Curse')
        return self.negative_effects.copy()

    def get_stats(self):
        self.stats['Strength'] -= 2
        self.stats['Endurance'] -= 2
        self.stats['Agility'] -= 2
        self.stats['Luck'] -= 2
        self.stats['Perception'] -= 2
        self.stats['Charisma'] -= 2
        self.stats['Intelligence'] -= 2
        return self.stats.copy()


hero = Hero()
brs1 = Berserk(hero)
brs2 = Berserk(brs1)
crs1 = Curse(hero)
crs2 = Curse(brs2)

crs3 = Curse(crs2)
print(crs2.get_positive_effects())
print(crs2.get_negative_effects())
print(brs1.positive_effects)
print(brs2.positive_effects)
print(crs3.get_negative_effects())
print(crs3._base.get_negative_effects())
