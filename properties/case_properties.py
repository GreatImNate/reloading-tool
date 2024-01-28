from dataclasses import dataclass


class CaseProperties:
    manufacturer: str  # headstamp?
    caliber: str  # or id to SAAMI spec object?
    length: float
    capacity: float

    def __init__(self):
        self.case_id = None
