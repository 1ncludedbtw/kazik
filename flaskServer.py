import matplotlib.pyplot as plt
from io import BytesIO
import base64
from flask import Flask, render_template, request
from dictWork import prepare_dict_from_csv  # Pieņemot, ka šī funkcija sagatavo vārdnīcu no CSV
from showWork import show  # Pieņemot, ka šo funkciju varētu izmantot, lai attēlotu diagrammas

app = Flask(__name__)

# Sagatavojam datus no CSV
data = prepare_dict_from_csv("copy.csv")

def create_plot(data):
    """
    Funkcija, lai ģenerētu CO2 līmeņa diagrammu.
    """
    days = list(data.keys())
    co2_levels = [float(value) for value in data.values()]
    colors = ['red' if level >= 2000 else 'green' for level in co2_levels]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(days, co2_levels, label='CO2 levels', color=colors, linewidth=2.0, width=0.5)
    ax.set(xlabel='Day', ylabel='CO2 Concentration (ppm)', title='CO2 Levels Over Days')

    # Režģis un x-ass numuri
    ax.set_xticks(days)  
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))  
    ax.set_ylim(min(co2_levels) - 10, max(co2_levels) + 10)
    
    ax.grid(True)
    ax.legend()

    plt.xticks(rotation=45)  # Rotējam x-asī izmantotos dienu numurus
    plt.tight_layout()

    # Saglabājam attēlu kā base64 stringu
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')  # Pārvērš attēlu par base64 stringu
    plt.close(fig)
    
    return plot_url

def get_co2_level(day):
    print(day)
    print(data.get(str(day)))
    temp = data.get(str(day))
    if temp == None:
        return None
    else:
        return temp

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/day", methods=["GET", "POST"])
def day():
    """
    Maršruts, kas attēlo CO2 līmeni par konkrētu dienu.
    """
    if request.method == "POST":
        try:

            day = int(request.form["day"])  
            co2_level = get_co2_level(day)

            if co2_level is not None:
                return render_template("day.html", day=day, co2_level=co2_level)
            else:

                return render_template("day.html", error="Diena netika atrasta.")
        except ValueError:

            return render_template("day.html", error="Lūdzu, ievadiet derīgu dienas numuru.")
    return render_template("day.html")

@app.route("/chart", methods=["GET", "POST"])
def chart():
    """
    Maršruts, kas attēlo visu diagrammu ar CO2 līmeņiem.
    """
    plot_url = create_plot(data)  
    return render_template("chart.html", plot_url=plot_url)  

if __name__ == "__main__":
    app.run(debug=True)
