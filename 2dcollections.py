heavy_vehical = ["Truck", "Bus", "train"]
medium_vehical = ["car", "supercar", "auto"]
light_vehical = ["bike", "cycle", "Rickshaw"]

vehicals = [heavy_vehical, medium_vehical, light_vehical]

# print(vehicals[0][0])

for collections_of_vehicals in vehicals:
    for more_collections in collections_of_vehicals:
        print(more_collections, end=" ")
    print()


