from fuzzywuzzy import fuzz
import pandas as pd
from prettytable import PrettyTable

# Read in specific sheets of the Excel file
xl = pd.read_excel('pricelist_2023_03.xlsx', sheet_name=['Price List', 'MIST AI Access'])

while True:
    # Get the name of the product to search for
    product_name = input("Enter the name of the product: ")

    x = PrettyTable()
    x.field_names = ["Product Number", "Quantity", "Total Price","List Price","LOD","ADD","EOL Rep","Status"]

    flag = 0
    similar_list = []
    for sheet_name, df in xl.items():
        df["Product Number"] = df["Product Number"].str.lower()
        match = df.loc[df['Product Number'] == product_name.lower()]
        if not match.empty:
            flag = 1
            if pd.isna(match['Product List Price'].values[0]):
                price = match['Service Price CAT 4'].values[0]
            else:
                price = match['Product List Price'].values[0]
            while True:
                try:
                    quantity = int(input("Enter the quantity of the product: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            if not isinstance(price, str):
                total_price = price * quantity
            else:
                total_price = "N/A"
            description = match['Long Description'].values[0]
            lod = str(match['LOD (Last Order Date)'].values[0])[0:10]
            pbd = str(match['Price Book Date'].values[0])[0:10]
            EOL_Replacement = match['EOL Replacement'].values[0]
            material_status = match['Material Status'].values[0]
            x.add_row([product_name.upper(),quantity, total_price,price,lod,pbd,EOL_Replacement,material_status])
            print(x)
            print(str(description))
            print('\n')
            break
        else:
            for product in df["Product Number"]:
                ratio = fuzz.ratio(product_name.lower(), product.lower())
                if ratio > 55:
                    similar_list.append(product)
    if similar_list and flag == 0:
        print("Did you mean:")
        for item in similar_list:
            print(f"{item.upper()}")
        print("Please check again.")
    if flag == 0:
        print(f"{product_name} not found in any sheet.")
