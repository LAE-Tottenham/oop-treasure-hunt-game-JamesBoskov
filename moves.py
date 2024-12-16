class Move():
    def __init__(self, name, power, effect, attack):
        self.name = name
        self.power = power
        self.effect = effect
        self.attack = attack
        
booster_bounce = Move("booster bounce", 20, [None], True)
menacing_bark = Move("menacing bark", 0, ["attack", 0.67], True)