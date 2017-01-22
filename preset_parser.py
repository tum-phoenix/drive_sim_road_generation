import ruamel.yaml as yaml
import primitive
import math

class Preset:
    def __init__(self):
        # set sensitve defaults
        self.road_width = 1
        self.primitives = []

def parse(path):
    with open(path, "r") as file:
        data = yaml.load(file, Loader=yaml.RoundTripLoader)
    preset = Preset()
    preset.road_width = data["road_width"]
    for p in data["primitives"]:
        if "straight_line" in p:
            preset.primitives.append(
                primitive.StraightLine(p["straight_line"]["length"]))
        elif "right_arc" in p:
            preset.primitives.append(primitive.RightCircularArc(
                p["right_arc"]["radius"],
                math.radians(p["right_arc"]["angle"])))
        elif "left_arc" in p:
            preset.primitives.append(primitive.RightCircularArc(
                p["left_arc"]["radius"],
                math.radians(p["left_arc"]["angle"])))
        else:
            print("Unknown primitive type")
    return preset