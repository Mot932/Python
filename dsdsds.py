class videocard:
    def __init__(self, name="RTX 3090", memory=24, pin=8):
        self.name = name
        self.amount_of_memory = memory
        self.additional_power = pin

p1 = videocard()
print(p1.name)
print(p1.amount_of_memory)
print(p1.additional_power)