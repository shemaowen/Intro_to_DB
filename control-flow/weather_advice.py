# weather_advice.py

# Function to get clothing recommendation based on weather
def get_clothing_recommendation(weather):
    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

# Main function
def main():
    # Ask the user for the current weather
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # Get the recommendation based on the input
    recommendation = get_clothing_recommendation(weather)

    # Print the recommendation
    print(recommendation)

# Run the main function
if __name__ == "__main__":
    main()
