"""
signal k dot 
"""
import sys
import json
import math
from collections import defaultdict

def gen_dot(_args):
    """
    gen json for delta spec schema
    """

    # Function to calculate the distance between two coordinates
    def haversine_distance(coord1, coord2):
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        R = 6371  # Earth radius in km

        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = (math.sin(dLat / 2) * math.sin(dLat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dLon / 2) * math.sin(dLon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    # Read the Signal K data from stdin
    data = sys.stdin.read()

    # Load the data as a Python dictionary
    signal_k_data = json.loads(data)

    # Extract the vessels data
    vessels_data = signal_k_data[0]['vessels']

    # Store vessel positions (latitude, longitude) and names
    vessel_positions = defaultdict(dict)
    vessel_names = {}

    for vessel_id, vessel_info in vessels_data.items():
        lat = vessel_info['navigation']['position']['value']['latitude']
        lon = vessel_info['navigation']['position']['value']['longitude']
        name = vessel_info.get('name', vessel_id)
        vessel_positions[vessel_id] = (lat, lon)
        vessel_names[vessel_id] = name

    # Generate the DOT file content for Graphviz
    dot_file_content = 'digraph {\n'
    dot_file_content += '  graph [splines=polyline]\n'

    for vessel_id, position in vessel_positions.items():
        dot_file_content += f'  "{vessel_id}" [label="{vessel_names[vessel_id]}\\n({position[0]}, {position[1]})"];\n'

    vessel_ids = list(vessel_positions.keys())

    # Add edges with dotted lines and lengths scaled to relative distances
    for i in range(len(vessel_ids)):
        for j in range(i + 1, len(vessel_ids)):
            id1 = vessel_ids[i]
            id2 = vessel_ids[j]
            pos1 = vessel_positions[id1]
            pos2 = vessel_positions[id2]
            distance = haversine_distance(pos1, pos2)
            dot_file_content += f'  "{id1}" -> "{id2}" [style=dotted, len={distance / 10}, dir=none];\n'

    dot_file_content += '}'

    # Write the DOT file content to a file
    with open('vessel_positions.dot', 'w') as dot_file:
        dot_file.write(dot_file_content)
