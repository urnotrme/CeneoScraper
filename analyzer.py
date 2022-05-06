import os 
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
ID_product = input("Podaj index produktu: ")

opinions = pd.read_json(f"opinions/{ID_product}.json")
print(opinions)