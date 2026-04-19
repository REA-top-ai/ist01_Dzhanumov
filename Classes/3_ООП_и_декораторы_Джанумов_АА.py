# task 1

class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class

        if hero_class == "wizard":
            self.health = 60
            self.mana = 50
        else:
            self.health = 100
            self.mana = 10

        self.spells_names = {}
        self.items = {}

    def attack(self, damage):
        print(f'Герой нанес урон: {damage}')

    def heal(self, amount):
        self.health += amount

    def cast_spell(self, spell_name):
        spell = self.spells_names.get(spell_name)
        if spell and self.mana >= spell["mana_cost"]:
            self.mana -= spell["mana_cost"]
            print(f'Использовано заклинание: {spell_name}')

    def add_spell(self, spell_name, mana_cost, attack_damage, health_increase):
        self.spells_names[spell_name] = {
            "mana_cost": mana_cost,
            "attack_damage": attack_damage,
            "health_increase": health_increase
        }

    def add_item(self, item_name, stat, value):
        if len(self.items) < 6:
            self.items[item_name] = {stat: value}


# task 2

def is_alive(func):
    def wrapper(*args, **kwargs):
        hero = args[0]
        if hero.health <= 0:
            print(f'{hero.name} мертв и не может действовать!')
            return None
        return func(*args, **kwargs)
    return wrapper


# task 3

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f'[LOG] Начало действия: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'[LOG] Действие завершено')
        return result
    return wrapper


# task 4

class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class

        if hero_class == "wizard":
            self.health = 60
            self.mana = 50
        else:
            self.health = 100
            self.mana = 10

        self.spells_names = {}
        self.items = {}

    @is_alive
    def attack(self, damage):
        print(f'Герой нанес урон: {damage}')

    @log_action
    def heal(self, amount):
        self.health += amount

    @is_alive
    def cast_spell(self, spell_name):
        spell = self.spells_names.get(spell_name)
        if spell and self.mana >= spell["mana_cost"]:
            self.mana -= spell["mana_cost"]
            print(f'Использовано заклинание: {spell_name}')

    def add_spell(self, spell_name, mana_cost, attack_damage, health_increase):
        self.spells_names[spell_name] = {
            "mana_cost": mana_cost,
            "attack_damage": attack_damage,
            "health_increase": health_increase
        }

    def add_item(self, item_name, stat, value):
        if len(self.items) < 6:
            self.items[item_name] = {stat: value}


# task 5

def boost_health(func):
    def wrapper(*args, **kwargs):
        hero = args[0]
        original = hero.health
        hero.health *= 2
        result = func(*args, **kwargs)
        hero.health = original
        return result
    return wrapper


def boost_mana(func):
    def wrapper(*args, **kwargs):
        hero = args[0]
        original = hero.mana
        if hero.hero_class == "wizard":
            hero.mana = int(hero.mana * 1.5) + 5
        result = func(*args, **kwargs)
        hero.mana = original
        return result
    return wrapper


# дополнительный декоратор: уменьшает получаемый урон в 2 раза
def defense_buff(func):
    def wrapper(*args, **kwargs):
        if "damage" in kwargs:
            kwargs["damage"] //= 2
        elif len(args) > 1:
            args = list(args)
            args[1] //= 2
        return func(*args, **kwargs)
    return wrapper