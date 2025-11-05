# Recipe Matcher 🍳

A small Python script that helps you find recipes based on the ingredients you have at home.

---

## Overview

Recipe Matcher is a Python-based tool that demonstrates code literacy through data handling, logic, and user interaction. 
It reads a list of recipes from a JSON file and checks which ones you can make with your available ingredients. 

---

## What It Does

1. You type in your available ingredients (comma-seperated).
2. The program compares your list against all recipes in recipes.json.
3. It prints any recipes that can be made using only those ingredients - including their names and instructions.

This demonstrates how structured data (JSON), conditional logic, and string operations can combine to create a functional code prototype. 

---

## Requirements

- Python 3.7 or higher
- Tested on macOS (works cross-platform)
- No external libraries - uses only Python's standard library. 

Check your Python version:

```bash
python3 --version
```

You should see something like `Python 3.9.x`.

---

## Setup and Running the Program

1. Download the following two files:
   - `recipe_matcher.py`
   - `recipes.json`
  
2. Put both files in the same folder.

3. Open Teriminal and navigate to that folder:

```bash
cd /path/to/recipe-matcher
```

4. Run the program:

```bash
python3 recipe_matcher.py
```

(If `python3` doesn't work, try `python` instead)

---

## How It Works (Code Overview)

1. load_recipes() - Opens and reads recipes.json.
2. normalize_ingredient() - Cleans ingredient names for comparison.
3. can_make_recipe() - Checks if all required ingredients exist in your list.
4. find_matching_recipes() - Loops through all recipes and collects matches.
5. display_recipes() - Neatly prints the results in the terminal.

The process connects directly to Python's fundamental data types (list, dict, set) and shows how conditional logic and iteration can be combined to produce meaningful output. 

### Example Outputs

Example 1: Single Match

Input - 
eggs, butter, cheese

Output - 
1 recipe found: Simple Omelette
Ingredients: eggs, cheese, butter
Instructions: Beat eggs, pour into buttered pan, add cheese, fold and serve. 

Example 2: Multiple Matches

Input - 
bread, cheese, butter

Output - 
2 recipes found:
1. Grilled Cheese Sandwich
2. Cheese Toast

Example 3: No Matches

Input - 
banana, kale

Output:
No recipes found with your ingredients.
Try adding more ingredients!

## Adding Your Own Recipes

You can edit or expand `recipes.json` to add more recipes. It should look like this:

```json
{
  "recipes": [
    {
      "name": "Toast",
      "ingredients": ["bread", "butter"],
      "instructions": "Toast the bread and spread butter on top."
    }
  ]
}
```

**Tips:**

- Ingredient names are not case-sensitive ("Eggs" = "eggs")
- Only recipes with all ingredients available will display
- Keep ingredient names short and consistent

---

## Troubleshooting

Issue: recipes.json not found
Cause: File missing or not in the same folder
Solution: Move recipes.json to same directory as the script

Issue: python3 not found
Cause: Windows systems use python
Solution: Try python recipe_matcher.py

Issue: not valid JSON
Cause: Missing commas or quotes
Solution: Validate JSON online or re-check syntax

Issue: No recipes found
Cause: Ingredients don't fully match
Solution: Try adding more or correcting spelling

---

## Folder Layout

```
recipe-matcher/
├── recipe_matcher.py      # main script
├── recipes.json           # data file
├── README.md              # this document
└── img/
   ├── flowchart           # process diagram
   ├── screenshot   
   ├──
   ├──

```

---

## Future Improvements

Add fuzzy matching (e.g., "tomato" = "tomatoes")
Handle ingredient synonyms (e.g., "courgette" = "zucchini")
Rank recipes by ingredient overlap (partial matches)
Build a user interface or web version for accessibility
