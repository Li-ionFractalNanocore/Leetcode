from typing import List
from collections import defaultdict

from heapq import heappush, heappop


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(list)
        self.foods_cuisines = {}
        self.foods_index = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            food_index = [-rating, food, True]
            self.foods_cuisines[food] = cuisine
            self.foods_index[food] = food_index
            heappush(self.cuisines[cuisine], food_index)

    def changeRating(self, food: str, newRating: int) -> None:
        food_index = self.foods_index[food]
        if newRating != -food_index[0]:
            food_index[2] = False
            new_food_index = [-newRating, food, True]
            self.foods_index[food] = new_food_index
            heappush(self.cuisines[self.foods_cuisines[food]], new_food_index)

    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food, valid = self.cuisines[cuisine][0]
            if valid:
                return food
            heappop(self.cuisines[cuisine])
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)