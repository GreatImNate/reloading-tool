from properties.case_properties import CaseProperties
from properties.powder_properties import PowderProperties
from properties.primer_properties import PrimerProperties
from properties.projectile_properties import ProjectileProperties


class CartridgeProperties:
    projectile: ProjectileProperties
    powder: PowderProperties
    case: CaseProperties
    primer: PrimerProperties
    powder_charge: float

    def __init__(self):
        pass