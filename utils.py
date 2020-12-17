import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
    
def make_bar_chart(data, title):
    plt.figure()
    plt.bar(data.index, data, color = "blue")
    plt.title(title)
    plt.xlabel("Weekdays")
    plt.xticks(rotation=45)
    plt.ylabel("Mean value")
    plt.show()
