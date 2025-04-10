"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_fish: list[Fish] = (
            []
        )
        new_bears: list[Bear] = (
            []
        )
        for fish in self.fish:
            if fish.age <=3: 
                new_fish.append(
                    fish
                )
        for bears in self.bears
            if bears.age <= 5:
                new_bears.append(bears)
        self.fish = new_fish
        self.bears = new_bears
        return None

    def bears_eating(self):
        for bear in self.bears: 
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        hungry_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                hungry_bears.append(
                    bear
                )
        self.bears = hungry_bears
        return None

    def repopulate_fish(self):
        new_fish: list[Fish] = []
        for n in self.fish:
            if n == 2:
                new_fish.append((n // 2) * 4)
        self.fish = new_fish
        return None

    def repopulate_bears(self):
        new_bears: list[Bear] = []
        for n in self.bears:
            if n == 2:
                new_bears.append(n // 2)
        self.bears = new_bears
        return None

    def view_river(self):
        day = self.day
        fish_len = len(self.fish)
        bears_len = len(self.bears)
        print(f"~~~ Day {day}: ~~~")
        print(f"Fish population: {fish_len}")
        print(f"Bear population: {bears_len}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        index: int = 0
        while index < 8:
            self.one_river_day()

    def remove_fish(self, amount: int):
        index: int = 0
        while index < amount: 
            if len(self,fish) > 0:
                slef.fish.pop(0)
