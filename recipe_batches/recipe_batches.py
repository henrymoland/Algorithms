#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []

  #Base case: If we dont have enough ingredients or the ingredient is not in the recipe 0

  for item in recipe:
    if item not in recipe or recipe[item] > ingredients[item]:
      return 0
    else:
      batches.append(math.floor(ingredients[item]/recipe[item]))
  return min(batches)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5, 'Lemon': 5 }
  ingredients = { 'milk': 250, 'butter': 120, 'flour': 10, 'Lemon': 10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))