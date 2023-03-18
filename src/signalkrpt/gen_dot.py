"""
signal k dot 
"""
import sys
import json
import math
from collections import defaultdict

def haversine_distance(coord1, coord2):
    """
    Function to calculate the distance between two coordinates
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    rad = 6371  # Earth radius in km

    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a_var = (math.sin(d_lat / 2) * math.sin(d_lat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(d_lon / 2) * math.sin(d_lon / 2))
    cir = 2 * math.atan2(math.sqrt(a_var), math.sqrt(1 - a_var))
    distance = rad * cir
    return distance

def create_dot_file_content(vessel_positions, vessel_names):
    """
    Add edges with dotted lines and lengths scaled to relative distances
    """
    # Generate the DOT file content for Graphviz
    dot_file_content = 'digraph {\n'
    dot_file_content += '  graph [splines=polyline]\n'

    for vessel_id, position in vessel_positions.items():
        dot_file_content += f'  "{vessel_id}" [label=\
                "{vessel_names[vessel_id]}\\n({position[0]}, {position[1]})"];\n'


    vessel_ids = list(vessel_positions.keys())
    for i, id1 in enumerate(vessel_ids):
        for _j, id2 in enumerate(vessel_ids[i + 1:], i + 1):
            pos1 = vessel_positions[id1]
            pos2 = vessel_positions[id2]
            distance = haversine_distance(pos1, pos2)
            dot_file_content += f'  "{id1}" -> "{id2}" [style=dotted, \
                    len={distance / 10}, dir=none];\n'

    dot_file_content += '}'
    return dot_file_content

def gen_dot(_args):
    """
    gen json for delta spec schema
    """

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

    dot_file_content = create_dot_file_content(vessel_positions, vessel_names)

    # Write the DOT file content to a file
    with open('vessel_positions.dot', 'w', encoding = 'utf8') as dot_file:
        dot_file.write(dot_file_content)
