
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SHIELD, SHIELD_TYPE, HEART, HEART_TYPE

class Shield(PowerUp):
 
    def __init__(self):
        self.image  = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)

class Hammer(PowerUp):
 
    def __init__(self):
        self.image  = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

class Heart(PowerUp):
 
    def __init__(self):
        self.image  = HEART
        self.type = HEART_TYPE
        super().__init__(self.image, self.type)