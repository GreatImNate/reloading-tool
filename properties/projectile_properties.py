from dataclasses import dataclass


class ProjectileProperties:
    diameter: float
    manufacturer: str
    profile: str  # bthp, round nose, flat point, swc, hollow point flat base
    material: str  #solid copper, copper jacket, copper plated, bimetal jacket, polymer tipped?
    overall_length: float
    base_to_ogive: float
    ballistic_coefficient_g1: float
    ballistic_coefficient_g7: float
    sectional_density: float

    def __init__(self):
        self.diameter = 0.0
