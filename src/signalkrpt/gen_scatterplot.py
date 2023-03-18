"""
signal k dot 
"""
import sys
import json
import matplotlib.pyplot as plt

def gen_scatterplot(_args):
    """
    gen json for delta spec schema
    """
    input_data = json.load(sys.stdin)
    vessels_data = input_data[0]["vessels"]

    plt.figure()

    for index, (_vessel_id, vessel_info) in enumerate(vessels_data.items(), start=1):
        if "navigation" in vessel_info and "position" in vessel_info["navigation"]:
            position = vessel_info["navigation"]["position"]["value"]
            latitude = position["latitude"]
            longitude = position["longitude"]

            plt.scatter(longitude, latitude)
            plt.annotate(f"Boat {index}", (longitude, latitude),
                textcoords="offset points", xytext=(0, 5), ha='center')

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Boat Positions")
    plt.grid(True)
    plt.show()
