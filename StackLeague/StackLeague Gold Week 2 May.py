def next_bigger(number):
    number = str(number)
    lst = []
    for i in number:
        lst.append(int(i))
    for i in range(len(number)-1,0,-1):
        if number[i-1] < number[i]:
            mx, ind = 10**18, -1
            for j in range(len(number)-1,i-1,-1):
                if int(number[j]) < mx and int(number[j]) > int(number[i-1]):
                    mx = int(number[j])
                    ind = j
            lst[i-1], lst[ind] = lst[ind], lst[i-1]
            lst[i:].sort()
            q = sorted(lst[i:])
            ans = ''
            for j in range(i):
                ans += str(lst[j])
            for j in q:
                ans += str(j)
            return int(ans)
    return -1
print(next_bigger(790))
    
class Recipe:
    def __init__(self, name, min_servings, max_servings):
        self.name = name
        self.min_servings = min_servings
        self.max_servings = max_servings
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def find_ingredient(self, ingredient_name):
        for i in self.ingredients:
            if i == ingredient_name:
                
        return None
        pass # return the Ingredient object, or None if ingredient_name can't be found in recipe
        # search is case-insensitive

    def adjust_numbers(self, basis_ingredient_name, quantity_in_fridge, unit):
        pass # adjust all quantities and serving amounts

class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity  # quantity prescribed by the recipe
        self.unit = unit

    def get_ratio(self, quantity_in_fridge, unit):
        pass # get the ratio,
        # e.g. if recipe requires 800g chicken, but you have 1.2kg, then ratio is 1.5
        # e.g. if recipe requires 800g chicken, but you only have 300g, then ratio is 0.375

    def adjust(self, ratio):
        if self.unit in ['kg', 'g']:
            pass # complete this code
        elif self.unit in ['cloves', 'pcs']:
            pass # complete this code
        else:
            pass # complete this one

    def __eq__(self, other):
        # don't remove, needed by the test cases
        return isinstance(other, Ingredient) and \
               self.name == other.name and \
               abs(self.quantity - other.quantity) <= 0.001 and \
               self.unit == other.unit

def test___OO___add_ingredients(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))

    self.assertEqual(recipe.ingredients, [
        Ingredient('Chicken', 1, 'kg'),
        Ingredient('Brocolli', 400, 'g')
    ])

def test___OO___get_ratio_1(self):
    apple = Ingredient('apple', 5, 'pcs')
    self.assertEqual(apple.get_ratio(2, 'pcs'), 0.4)

def test___OO___get_ratio_2(self):
    apple = Ingredient('apple', 5, 'kg')
    self.assertEqual(apple.get_ratio(500, 'g'), 0.1)

def test___SE___adjust_make_grams(self):
    chicken = Ingredient('chicken', 2, 'kg')
    chicken.adjust(0.3)
    self.assertEqual(chicken, Ingredient('chicken', 600, 'g'))

def test___SE___adjust_make_kilograms(self):
    chicken = Ingredient('chicken', 500, 'g')
    chicken.adjust(3)
    self.assertEqual(chicken, Ingredient('chicken', 1.5, 'kg'))

def test___SE___adjust_retain_kilograms(self):
    chicken = Ingredient('chicken', 2, 'kg')
    chicken.adjust(1.5)
    self.assertEqual(chicken, Ingredient('chicken', 3, 'kg'))

def test___SE___adjust_retain_grams(self):
    chicken = Ingredient('chicken', 500, 'g')
    chicken.adjust(1.25)
    self.assertEqual(chicken, Ingredient('chicken', 625, 'g'))

def test___AL___find_ingredient(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
    recipe.add_ingredient(Ingredient('Water', 3, 'cups'))
    recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
    recipe.add_ingredient(Ingredient('Garlic', 3, 'cloves'))

    self.assertEqual(recipe.find_ingredient('Water'), Ingredient('Water', 3, 'cups'))

def test___SL___find_ingredient(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
    recipe.add_ingredient(Ingredient('Water', 3, 'cups'))
    recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
    recipe.add_ingredient(Ingredient('Garlic', 3, 'cloves'))

    self.assertEqual(recipe.find_ingredient('MUSHROOM'), Ingredient('Mushroom', 300, 'g'))

def test___AL___adjust_numbers(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
    recipe.add_ingredient(Ingredient('Water', 4, 'cups'))
    recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
    recipe.add_ingredient(Ingredient('Garlic', 6, 'cloves'))
    recipe.adjust_numbers('chicken', 400, 'g')

    self.assertEqual(recipe.min_servings, 1)
    self.assertEqual(recipe.max_servings, 2)
    self.assertEqual(recipe.ingredients, [
        Ingredient('Chicken', 400, 'g'),
        Ingredient('Brocolli', 160, 'g'),
        Ingredient('Water', 1.6, 'cups'),
        Ingredient('Mushroom', 120, 'g'),
        Ingredient('Garlic', 3, 'cloves')
    ])

def test___AL___adjust_numbers_bigger(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 5)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
    recipe.add_ingredient(Ingredient('Water', 3, 'cups'))
    recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
    recipe.add_ingredient(Ingredient('Garlic', 6, 'cloves'))
    recipe.add_ingredient(Ingredient('Bell Pepper', 1, 'pcs'))
    recipe.adjust_numbers('mushroom', 1.2, 'kg')

    self.assertEqual(recipe.min_servings, 12)
    self.assertEqual(recipe.max_servings, 20)
    self.assertEqual(recipe.ingredients, [
        Ingredient('Chicken', 4, 'kg'),
        Ingredient('Brocolli', 1.6, 'kg'),
        Ingredient('Water', 12, 'cups'),
        Ingredient('Mushroom', 1.2, 'kg'),
        Ingredient('Garlic', 24, 'cloves'),
        Ingredient('Bell Pepper', 4, 'pcs')
    ])

def word_to_number(string):
    # code here
    pass

def test_small_numbers(self):
    self.assertEqual(word_to_number('fourteen'), 14)

def test_dashed_compound_numbers(self):
    self.assertEqual(word_to_number('seventy-two'), 72)

def test_spaced_compound_numbers(self):
    self.assertEqual(word_to_number('seventy two'), 72)

def test_huge_numbers(self):
    word = "eight thousand one hundred and three"
    self.assertEqual(word_to_number(word), 8_103)

def test_millions(self):
    word = "nine hundred ninety-nine million nine hundred ninety nine thousand " + \
           "nine hundred ninety nine"
    self.assertEqual(word_to_number(word), 999_999_999)

def decompose(n):
  #code here
def is_numeric(n):
  #code here

def test___AL___sample_test_1 (self):
  self.assertEqual(decompose('0'), [])

def test___AL___sample_test_2 (self):
  self.assertEqual(decompose('3/4'), ["1/2", "1/4"])
  
def test___AL___sample_test_3 (self):
  self.assertEqual(decompose('4/5'), ["1/2", "1/4", "1/20"])
  
def test___AL___sample_test_4 (self):
  self.assertEqual(decompose('0.66'), ["1/2", "1/7", "1/59", "1/5163", "1/53307975"])
  
def test___AL___sample_test_5 (self):
  self.assertEqual(decompose('75/3'), ["25"])

def test___AL___sample_test_6 (self):
  self.assertEqual(decompose('13/12'),["1","1/12"])
