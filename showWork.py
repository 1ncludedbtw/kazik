import matplotlib.pyplot as plt
import numpy as np

def show(dict1):
    # Print dict1 to see the content
    print(dict1)

    days = list(dict1.keys())  
    co2_levels = [float(value) for value in dict1.values()]  
    colors = ['red' if level >= 2000 else 'green' for level in co2_levels]
    
    for i in days:
        if float(dict1[i]) >= 375:
            print(f"KRITISKS LĪMENIS DIENĀ {i}")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(days, co2_levels, label='CO2 levels', color=colors, linewidth=2.0, width=0.5)
    ax.set(xlabel='Day', ylabel='CO2 Concentration (ppm)', title='CO2 Levels Over Days')
    
    ax.set_xticks(days)  
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))  
    
    ax.set_ylim(min(co2_levels) - 10, max(co2_levels) + 10)
    
    # Pievienojam režģi un leģendu
    ax.grid(True)
    ax.legend()
    
    # Rādām diagrammu
    plt.xticks(rotation=45)  
    plt.tight_layout()  
    plt.show()

if __name__ == "__main__":
    pass