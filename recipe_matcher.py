#!/usr/bin/env python3
"""
Recipe Matcher Tool
Input: List of ingredients you have (comma-separated)
Process: Matches against recipes in recipes.json
Output: List of recipes you can make
"""

import json
import sys
from pathlib import Path


def load_recipes(filename='recipes.json'):
    """Load recipes from JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data.get('recipes', [])
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please make sure recipes.json exists in the same directory.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: {filename} is not valid JSON.")
        sys.exit(1)


def normalize_ingredient(ingredient):
    """Normalize ingredient name for comparison."""
    return ingredient.lower().strip()


def can_make_recipe(recipe, available_ingredients):
    """Check if we have all required ingredients for a recipe."""
    required = set(normalize_ingredient(ing) for ing in recipe['ingredients'])
    available = set(normalize_ingredient(ing) for ing in available_ingredients)
    
    # Check if all required ingredients are available
    return required.issubset(available)


def find_matching_recipes(available_ingredients, recipes):
    """Find all recipes that can be made with available ingredients."""
    matching = []
    
    for recipe in recipes:
        if can_make_recipe(recipe, available_ingredients):
            matching.append(recipe)
    
    return matching


def display_recipes(recipes):
    """Display recipes in a nice format."""
    if not recipes:
        print("\n❌ No recipes found with your ingredients.")
        print("Try adding more ingredients!\n")
        return
    
    print(f"\n✅ Found {len(recipes)} recipe(s) you can make:\n")
    print("=" * 60)
    
    for i, recipe in enumerate(recipes, 1):
        print(f"\n{i}. {recipe['name']}")
        print(f"   Ingredients needed: {', '.join(recipe['ingredients'])}")
        if 'instructions' in recipe:
            print(f"   Instructions: {recipe['instructions']}")
    
    print("\n" + "=" * 60 + "\n")


def main():
    """Main function to run the recipe matcher."""
    print("=" * 60)
    print("🍳 Welcome to Recipe Matcher! 🍳")
    print("=" * 60)
    
    # Load recipes
    recipes = load_recipes()
    print(f"\nLoaded {len(recipes)} recipes from recipes.json")
    
    # Get user input
    print("\nEnter the ingredients you have (separated by commas):")
    print("Example: eggs, flour, milk, sugar")
    print("-" * 60)
    
    user_input = input("Your ingredients: ").strip()
    
    if not user_input:
        print("\n❌ Error: No ingredients entered. Please try again.\n")
        sys.exit(1)
    
    # Parse ingredients
    available_ingredients = [ing.strip() for ing in user_input.split(',') if ing.strip()]
    
    if not available_ingredients:
        print("\n❌ Error: No valid ingredients found. Please try again.\n")
        sys.exit(1)
    
    print(f"\n🔍 Searching for recipes with: {', '.join(available_ingredients)}")
    
    # Find matching recipes
    matching_recipes = find_matching_recipes(available_ingredients, recipes)
    
    # Display results
    display_recipes(matching_recipes)


if __name__ == "__main__":
    main()
