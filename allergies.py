class Allergies:

    def __init__(self, score: int):
        self.allergies = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }

        self.score = score
        pass

    def allergic_to(self, item: str):
        item_code = self.allergies[item]
        return self.score & item_code != 0

    @property
    def lst(self):
        return list(filter(lambda x: self.allergic_to(x), self.allergies))
