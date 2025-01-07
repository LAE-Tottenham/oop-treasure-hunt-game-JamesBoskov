class Move():
    def __init__(self, name, power, effect, attack):
        self.name = name
        self.power = power
        self.effect = effect
        self.attack = attack
        
booster_bounce = Move("booster bounce", 20, [None], True)
menacing_bark = Move("menacing bark", 0, ["attack", 0.67], True)
enticing_bark = Move("enticing bark", 0, ["defense", 0.5], True)
fake_out = Move("fake out", 35, [None], True)
mega_booster_bounce = Move("mega booster bounce", 60, [None], True)
spacewalk_scratch = Move("spacewalk scratch", 80, [None], True)
all_out_crash = Move("all out crash", 105, ["attack", 1.34], True)
steely_resolve = Move("steely resolve", 0, ["defense", 1.5], False)
stand_there = Move("float ominously", 0, [None], True)
laser_beam = Move("the laser beam", 25, [None], True)
cheese_strike = Move("cheese strike", 30, [None], True)

proggression_moves = {1 : enticing_bark,
                      3 : mega_booster_bounce,
                      5 : spacewalk_scratch,
                      7 : steely_resolve,
                      8 : all_out_crash}