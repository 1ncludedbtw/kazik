from dictWork import prepare_dict_from_csv
from showWork import show

import io
import random
from flask import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask("app")
def main():
    data = prepare_dict_from_csv("copy.csv")
    day = 1
    print(data)
    print(data.get(day))
    if data.get(day):
        print(data[day])
    else:
        return None

main()