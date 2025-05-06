import pandas as pd

print("Starting the script...")
df = pd.read_csv("glycemic_index_data.csv")
print("CSV file loaded successfully!")

def get_glycemic_index(food_name):
    search_term = food_name.lower().strip()

    # Try an exact match first
    exact_match = df[df["Food"].str.lower().str.strip() == search_term]
    if not exact_match.empty:
        glycemic_index = exact_match["Glycemic Index"].values[0]
        category = exact_match["Category"].values[0]
        food_display = exact_match["Food"].values[0]
        return f"The glycemic index of {food_display} is {glycemic_index} and it is classified as {category}."

    # If no exact match, search for partial matches
    partial_match = df[df["Food"].str.lower().str.contains(search_term, na=False)]
    if not partial_match.empty:
        response = f"No exact match for '{food_name.title()}'.\nHere are similar results:\n"
        for index, row in partial_match.iterrows():
            response += f"- {row['Food']}: Glycemic Index {row['Glycemic Index']}, Category {row['Category']}\n"
        return response

    return f"Sorry, I don't have data for '{food_name.title()}'. Try another food item!"

while True:
    food = input("Enter a food name (or type 'exit' to quit): ")
    if food.lower().strip() == 'exit':
        print("Goodbye!")
        break
    print(get_glycemic_index(food))

