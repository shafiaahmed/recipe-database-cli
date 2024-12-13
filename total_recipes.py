import sqlite3

def setup_database():
    conn = sqlite3.connect("totalrecipes.db")
    cursor = conn.cursor()

    # Drop prior tables if they exist
    cursor.execute("DROP TABLE IF EXISTS recipes")
    cursor.execute("DROP TABLE IF EXISTS ingredients")
    cursor.execute("DROP TABLE IF EXISTS categories")
    cursor.execute("DROP TABLE IF EXISTS recipe_ingredients")
    cursor.execute("DROP TABLE IF EXISTS recipe_categories")

    # Create tables
    cursor.execute('''
        CREATE TABLE recipes (
            recipe_id INTEGER PRIMARY KEY,
            title TEXT,
            date TEXT,
            author TEXT,
            comment TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE ingredients (
            ingredient_id INTEGER PRIMARY KEY,
            ingredient_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE recipe_ingredients (
            recipe_id INTEGER,
            ingredient_id INTEGER,
            FOREIGN KEY(recipe_id) REFERENCES Recipes(recipe_id),
            FOREIGN KEY(ingredient_id) REFERENCES Ingredients(ingredient_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE recipe_categories (
            recipe_id INTEGER,
            category_id INTEGER,
            FOREIGN KEY(recipe_id) REFERENCES Recipes(recipe_id),
            FOREIGN KEY(category_id) REFERENCES Categories(category_id)
        )
    ''')



    # Insert sample data
    recipes = [
        (1, "Fried Olives!", "2020-08-20", "green_amethyst",
         '''
         You can use any of your favorite olive bar ingredients! Stuff your favorite olives with sweet pepper, pickled garlic, cheese of your choice.

         **INGREDIENTS**:
         ----------------
         *breading*:
         * 1/2 cup flour
         * 1/2 cup bread crumb
         * 1 egg
         * \~2 cups frying oil

         *olives*:
         * 1/2 cup pimento stuffed manzanilla olives, or
         * 1/2 cup pitted castelvetrano olives
         * 2 peppadew peppers, sliced

         **METHOD**:
         -----------
         1. Cut peppers into thin strips and stuff olives.
         2. Coat olives in flour, egg, and bread crumbs.
         3. Fry at 350°F for ~20 seconds until golden.
         Enjoy!
         '''),
        (2, "Easy Tiramisu", "2021-03-15", "chef_bella",
         '''
         **Easy Tiramisu Recipe (no raw eggs!)**

         **INGREDIENTS**:
         ----------------
         * About 1.5 packages worth of lady fingers (I got mine at an Italian market, ran out, and then had my husband run out to get more at Whole Foods - he got the store-brand, which is also imported from Italy). Make sure these are the HARD lady fingers, NOT the soft ones!
         * 2 C strong coffee/espresso
         * 1 C heavy cream
         * 1-1.5 lb mascarpone
         * 2/3 C sugar, divided
         * 1 tsp vanilla extract
         * 2-3 Tbsp cocoa powder

         **METHOD**:
         -----------
         1. **Prepare coffee/alcohol for dipping:** Combine coffee in a wide, shallow bowl, and combine with about 5 Tbsp of the rum. Set side.
         2. **Prepare mascarpone/cream mixture:** Whip heavy cream with 1/3 C sugar, 1 tsp vanilla extract, and 2 Tbsp rum, until you have soft peaks. Then, slowly fold in the mascarpone along with the other 1/3 C sugar and 2 Tbsp rum. Whip altogether until nice and fluffy. Set aside.
         3. **Prepare tiramisu layers:** Dip each side of a lady finger into the coffee mixture for no more than 1-2 seconds per side (DO NOT DIP TOO LONG; This is the biggest mistake in making tiramisu. NO SOGGINESS!). Then, carefully lay in a pan (8x5 in), making sure all the ladyfingers are lined up side by side; trim if needed to fix snuggly into pan. Then, add a generous, even layer of the mascarpone/cream mixture on top of the ladyfingers, smoothing them out on the edges with a spatula. Dust with some cocoa powder with a colander/sieve. Repeat the ladyfinger layer with the final mascarpone layer, and dust the top with cocoa powder and chocolate shavings if using.
         4. **Refrigerate tiramisu** for at least 6 hours to allow it to set, and allowing the lady fingers to soften well. Cut with a clean knife, wiping off between slices for the cleanest edges, and enjoy!
         '''),
         (3, "Spicy Buttermilk Fried Chicken Sandwich","2021-02-05", "elle-cookerru",
         '''
         Sharing my go-to fried chicken sandwich recipe to celebrate the weekend!
         This recipe features crispy, juicy, tender pieces of chicken wrapped in buttery brioche buns made to perfection in the comfort of your home!

         **INGREDIENTS**:
         ----------------
         **Buttermilk Marinade**
         * 4 pieces boneless skinless chicken thighs, pounded to even thickness
         * 1 cup buttermilk
         * 2 tbsp Sriracha, or your favorite hot sauce
         * 1 tsp each salt, pepper

         **Flour Mixture**
         * 1 cup all-purpose flour
         * 3 tbsp cornstarch
         * 1 tbsp paprika powder
         * 1 tsp each salt, pepper, garlic powder, cayenne powder

         **Sriracha Mayo**
         * 1/2 cup mayonnaise
         * 2 tbsp hot sauce

         **To assemble**
         * cooking oil, for frying
         * 4 brioche buns, lightly toasted with butter
         * lettuce

         **METHOD**:
         -----------
         1. In a medium bowl, combine buttermilk, Sriracha, salt, pepper, and garlic powder. Add chicken thighs and marinate overnight, or at least for 4 hours.
         2. Prepare the flour mixture by whisking together flour, cornstarch, salt and pepper in a shallow bowl.
         3. Add about 2 tbsp of the marinade into the mixture and mix through with a fork. Working with one piece at a time, dredge the chicken with the flour mixture, making sure it is completely coated.
         4. In a small bowl, prepare the sauce by mixing together hot sauce and mayonnaise.
         5. Heat the oil in a deep pan until it reaches 350F (180C). Fry the chicken for about 3-4 minutes on each side, or until cooked through and golden brown.
         6. Generously spread the Sriracha mayo on the toasted brioche buns, and top with lettuce. Serve immediately and enjoy!
         '''
         ),
         (4, "Pavlova with Mango Cream and Raspberries", "2021-01-15", "AlvaroMenduina",
         '''
         Pavlova is a meringue-based cake with a crunchy exterior and a soft marshmallowy inside.

         **INGREDIENTS**:
         ----------------
         *For the Pavlova meringue*
         * 4 egg whites
         * 200 g caster sugar (you might not need it all)
         * 2 tsp flour
         * 1 tsp vanilla extract
         * 2 tsps lemon juice

         *For the toppings*
         * A very ripe sweet mango
         * Raspberries

         **METHOD**:
         -----------
         1. In a stand mixer whisk the egg whites until they form ""soft peaks"". At this point start adding the sugar while mixing until it forms ""stiff peaks"" and it's glossy.
         2. Once the egg white + sugar mix has formed stiff peaks, add the vanilla extract, lemon juice, and flour and mix until combined.
         3. Preheat the oven to 150C. Cover a baking tray with parchment paper. Scoop the meringue out of the mixing bowl and onto the tray. Use a thin spatula of a flat knife to decorate the cake.
         4. Bake at 150C for only 10 minutes. Turn the temperature down to 100C and keep cooking for around 1h 15. Next, switch off the oven and let the Pavlova slowly cool inside the oven.

         *Decorating the cake*
         1. Get a very ripe mango and use a blender to make puree. Pop it in the fridge. Once the cake has cooled down and you are ready to serve, pour the mango puree over the cake.
         2. Add the raspberries on top and dust some icing sugar over them.
         '''
         )
    ]

    ingredients = [
        (1, "Flour"),(2, "Bread Crumbs"),(3, "Eggs"),(4, "Frying Oil"),
        (5, "Ladyfingers"),(6, "Mascarpone"),(7, "Coffee"),(8, "Cocoa Powder"),(9, "Heavy cream"),(10, "Sugar"),(11, "Vanilla extract"),
        (12, "Chicken thighs"),(13, "Buttermilk"),(14, "Hot sauce"),(15, "Salt/Pepper"),(16, "Cornstarch"),(17, "Paprika powder"),(18, "Mayonnaise"), (19, "Brioche buns"), (20, "Lettuce"),
        (21, "Vanilla extract"), (22, "Lemon juice"), (23, "Mango"), (24, "Raspberries")
    ]

    # Inserting data for Categories
    categories = [
        (1, "Appetizer"),
        (2, "Main"),
        (3, "Dessert"),
        (4, "Vegetarian")
    ]

    recipe_ingredients = [
        (1, 1), (1, 2), (1, 3), (1, 4),  # Ingredients for Fried Olives
        (2, 5), (2, 6), (2, 7), (2, 8), (2,9), (2,10), (2,11),   # Ingredients for Easy Tiramisu
        (3, 1), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 19), (3, 20), # Ingredients for chicken sandwhich
        (4, 3), (4, 10), (4, 1), (4, 21), (4, 22), (4, 23), (4, 24)  # Ingredients for Pavlova

    ]

    # Insert relationships for RecipeCategories
    recipe_categories = [
        (1, 1),  # Fried Olives! is an Appetizer
        (1, 4),  # Fried Olives! is Vegetarian
        (2, 3),  # Easy Tiramisu is a Dessert
        (3, 2),  # Chicken sandwhich is a Main
        (4, 3)   # Pavlova is a Dessert
    ]

    cursor.executemany("INSERT INTO recipes VALUES (?, ?, ?, ?, ?)", recipes)
    cursor.executemany("INSERT INTO ingredients VALUES (?, ?)", ingredients)
    cursor.executemany("INSERT INTO categories VALUES (?, ?)", categories)
    cursor.executemany("INSERT INTO recipe_ingredients VALUES (?, ?)", recipe_ingredients)
    cursor.executemany("INSERT INTO recipe_categories VALUES (?, ?)", recipe_categories)


    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
