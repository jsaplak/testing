# Deisgn Patterns of OOP - Factory

class Burger:
    def __init__(self, ingredients):
      self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:
   
   def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)
   
   def createDeluxeCheeseBurger(self):
       ingredients = ["bun", "tomatoe", "lettuce", "cheese", "beef-patty"]
       return Burger(ingredients)

BurgerFactory = BurgerFactory()
BurgerFactory.createCheeseBurger().print()   
BurgerFactory.createDeluxeCheeseBurger().print()

#If it takes a list of ingredients to build a burger, we can instead use a factory which will instantiate ~
# the burger for us and return it to us regardless of what it is. We just have to tell the factory what we want.
