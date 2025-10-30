# Recipe Matcher 🍳

A small Python script that helps you find recipes based on the ingredients you have at home.

---

## What It Does

You type in your ingredients, and it checks a list of recipes to see which ones you can make. It then shows the matching recipes and how to make them.

---

## What You Need

- Python 3.7 or higher
- macOS (tested on macOS)
- No extra installs — it only uses the standard Python library

To check your Python version:

```bash
python3 --version
```

You should see something like `Python 3.9.x`.

---

## Setup

1. Download these two files:
   - `recipe_matcher.py`
   - `recipes.json`

2. Put them in the same folder.

3. Open Terminal and go to that folder:

```bash
cd /path/to/recipe-matcher
```

4. Run the program:

```bash
python3 recipe_matcher.py
```

(If `python3` doesn't work, try `python`.)

---

## How to Use

1. Run the script
2. When asked, type in the ingredients you have (separated by commas)
3. The program will show recipes that match what you've got

### Example

```
🍳 Welcome to Recipe Matcher! 🍳
------------------------------------------------------------
Enter your ingredients (separated by commas):
> eggs, butter, cheese

✅ Found 1 recipe you can make:

1. Simple Omelette
   Ingredients: eggs, cheese, butter
   Instructions: Beat eggs, pour into buttered pan, add cheese, fold and serve.
```

---

## Try These

**Example 1:**

Input:
```
eggs, butter, salt
```

Output:
```
Scrambled Eggs
```

**Example 2:**

Input:
```
bread, cheese, butter
```

Output:
```
Grilled Cheese Sandwich, Cheese Toast
```

**Example 3:**

Input:
```
flour, eggs, milk, sugar, butter
```

Output:
```
Classic Pancakes
```

---

## Adding Your Own Recipes

You can edit `recipes.json` to add more recipes. It should look like this:

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
- It only shows recipes where you have all the ingredients
- Keep ingredient names simple and consistent

---

## Troubleshooting

- **"recipes.json not found"** → Make sure it's in the same folder as the script
- **"python3 not found"** → Try running with `python` instead
- **"not valid JSON"** → There's probably a missing comma or quote in your `recipes.json`
- **No recipes found** → Check spelling and make sure all ingredients match

---

## Folder Layout

```
recipe-matcher/
├── recipe_matcher.py
├── recipes.json
└── README.md
```
