class Item():
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

blowtorch = Item("blowtorch", ["health", 20])
window_sealant = Item("window sealant", ["health", 25])
low_quality_kibble = Item("low quality kibble", ["health", 10])
standard_issue_kibble = Item("standard issue kibble", ["health", 17])
luxury_quality_kibble = Item("luxury quality kibble", ["health", 30])
dog_treats = Item("dog treats", ["health", 27])
glizzy = Item("glizzy", ["health", 25])
wd40 = Item("WD40", ["health", 20])
new_batteries = Item("new batteries for the ship", ["speed", 1.5])
booster_rocket = Item("booster rocket", ["speed", 1.7])
adrenaline = Item("adrenaline", ["speed", 1.5])
nitros = Item("nos", ["speed", 1.3])
jet_fuel = Item("jet fuel", ["speed", 1.15])
hyperactive_cheese = Item("hyperative cheese", ["speed", 2])
sandpaper = Item("sandpaper", ["attack", 1.15])
jagged_fins = Item("jagged fins", ["attack", 1.35])
corrosive_acid = Item("corrosive acid", ["attack", 1.75])
rebar = Item("rebar", ["defense", 1.2])
reinforced_steel = Item("reinforced steel", ["defense", 1.7])
nose_armour = Item("nose armour", ["defense", 1.35])
chainmail = Item("chainmail", ["defense", 1.45])
wenslydale = Item("Wenslydale", ["defense", 1.25])