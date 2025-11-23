import sqlite3
import cmd  #for command line interface

class MyCLI(cmd.Cmd):
    def __init__(self):
        super().__init__()

        # Connect to the database
        self.conn = sqlite3.connect("totalrecipes.db")
        self.cursor = self.conn.cursor()

    prompt = '>> '  # for display
    intro = 'Welcome to my recipe database! Type "help" for available commands.'


    def do_list_recipes(self, line):
        """List all recipes."""
        self.cursor.execute("SELECT recipe_id, title FROM recipes")
        recipes = self.cursor.fetchall()

        if recipes:
            print("\nAvailable Recipes:") # printing all recipes
            for recipe_id, title in recipes:
                print(f"{recipe_id}. {title}")

            try:
                choice = int(input("\n\033[1mEnter the number of the 
recipe you want to select:\033[0m ")) # Question is bolded
                if 1 <= choice <= len(recipes): # Making sure the choice is valid
                    selected_recipe = recipes[choice - 1]
                    self.recipe_options(selected_recipe) # selected_recipe contains id, title
                else:
                    print("Invalid choice.")
            except:
                print("Please enter a valid number.")



    def recipe_options(self, selected_recipe):
        recipe_id, title = selected_recipe
        self.cursor.execute("SELECT * FROM recipes WHERE recipe_id = ?", (recipe_id,)) # finding the details for the recipe chosen
        recipe = self.cursor.fetchone() # Gives the matching recipe

        if recipe:
            title, date, author, comment = recipe[1], recipe[2], recipe[3], recipe[4] # getting all the information for the recipe
            while True:
                print("\nWhat would you like to do?") # presenting the options
                print("="* 50)
                print("1. View recipe details")
                print("2. View ingredients")
                print("3. View categories")
                print("4. Go back\n")
                choice = input("\033[1mEnter your choice (1, 2, 3, or 4):\033[0m ").strip() # Question is bolded

                if choice == "1":
                    # Show recipe details
                    print("\nRECIPE DETAILS:")
                    print(f"Title: {title}")
                    print(f"Date: {date}")
                    print(f"Author: {author}")
                    print(f"Comment: {comment}")

                elif choice == "2":
                    # Show ingredients
                    # Joining ingredients where they match
                    self.cursor.execute("""
                        SELECT ingredients.ingredient_name
                        FROM ingredients
                        JOIN recipe_ingredients ON ingredients.ingredient_id = recipe_ingredients.ingredient_id
                        WHERE recipe_ingredients.recipe_id = ?
                    """, (recipe_id,))
                    ingredients = self.cursor.fetchall()

                    # If successfull
                    if ingredients:
                        print("\nINGREDIENTS FOR THIS RECIPE:")
                        for ingredient in ingredients:
                            print(f"- {ingredient[0]}") # Printing all ingredients
                    else:
                        print("No ingredients found.")

                elif choice == "3":
                    # Show categories
                    # Joining categories where they match
                    self.cursor.execute("""
                        SELECT categories.category_name
                        FROM categories
                        JOIN recipe_categories ON categories.category_id = recipe_categories.category_id
                        WHERE recipe_categories.recipe_id = ?
                    """, (recipe_id,))
                    categories = self.cursor.fetchall()

                    # If successfull
                    if categories:
                        print("\nCATEGORY/CATEGORIES:")
                        for category in categories:
                            print(category[0])
                    else:
                        print("No categories found.")

                elif choice == "4":
                    break  # Go back

                else:
                    print("Invalid choice. Please try again.")



    # Search recipes by category
    def do_search_category(self, line):
        """Search recipes by category."""
        print("\nAvailable Categories:")
        self.cursor.execute("SELECT category_name FROM categories")
        categories = self.cursor.fetchall()

        if categories:
            count = 1
            for cat in categories:
                print(f"{count}. {cat[0]}")  # Accessing the first element (category_name)
                count += 1

            try:
                category_choice = int(input("\n\033[1mEnter the number you want to search for:\033[0m "))
                if 1 <= category_choice <= len(categories): # Making sure the choice is valid
                    category_name = categories[category_choice-1][0]
                else:
                    print("Invalid choice.")
            except:
                print("Wrong")


        self.cursor.execute("""
            SELECT recipes.title
            FROM recipes
            JOIN recipe_categories ON recipes.recipe_id = recipe_categories.recipe_id
            JOIN categories ON recipe_categories.category_id = categories.category_id
            WHERE categories.category_name LIKE ?
        """, (f"%{category_name}%",))
        rows = self.cursor.fetchall()

        if rows:
            print(f"\nRecipes in the **{category_name}** category: ")
            for title, in rows:
                print(f"- {title}")
        else:
            print("No recipes found in this category.")

    # Exit the CLI
    def do_quit(self, line):
        """Exit the CLI."""
        print("Goodbye!")
        self.conn.close()  # Close the database connection
        return True


if __name__ == '__main__':
    MyCLI().cmdloop()  # Start the CLI
