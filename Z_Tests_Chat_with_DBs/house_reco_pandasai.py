from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.helpers.openai_info import get_openai_callback
import pandas as pd

llm = OpenAI(api_token="sk-proj-")

# Create a sample DataFrame with real estate house data
data = {
    "Address": ["123 Main St", "456 Elm St", "789 Oak St", "321 Pine St", "654 Maple St"],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"],
    "Price": [500000, 750000, 600000, 450000, 550000],
    "SquareMeters": [100, 120, 110, 95, 105],
    "Bedrooms": [2, 3, 3, 2, 2],
    "Bathrooms": [1, 2, 2, 1, 1],
    "Garage": [True, True, False, True, False],
    "Backyard": [False, True, True, False, True]
}

df = pd.DataFrame(data)

# Create a SmartDataframe with the real estate house data
sdf = SmartDataframe(df, config={"llm": llm, "conversational": False})

with get_openai_callback() as cb:
    response = sdf.chat("Which house would you recommend for a family based on the given information and why would you say so?")

    print(response)
    print(cb)