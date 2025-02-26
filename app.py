from flask import Flask, render_template, request 
import requests
import datetime

app= Flask(__name__)

#La liste des villes marocaines dans un fichier Villes
Villes= [
    "Casablanca", "Rabat", "Marrakech", "Fès", "Tanger", "Agadir", "Meknès", "Oujda", "Kenitra", "Tetouan",
    "Safi", "El Jadida", "Nador", "Beni Mellal", "Taza", "Mohammedia", "Khouribga", "Settat", "Laayoune", "Essaouira",
    "Berkane", "Errachidia", "Guelmim", "Khenifra", "Taroudant", "Ouarzazate", "Al Hoceima", "Bouskoura",
    "Youssoufia", "Ben Guerir", "Sidi Kacem", "Tiznit", "Larache", "Sidi Ifni", "Dakhla"
]
# récuperer les horaires de prieres 
def get_monthly_prayer_times(city, month, year):
    url = f"https://api.aladhan.com/v1/calendarByCity?city={city}&country=Morocco&method=2&month={month}&year={year}"
    response= requests.get(url)
    if response.status_code== 200:
        return response.json()["data"]
    return []

@app.route("/", methods=["GET", "POST"]) 
def index():
    selected_city = request.form.get("city", "Casablanca")
    today= datetime.date.today()
    month = today.month
    year= today.year
    
    prayer_times= get_monthly_prayer_times(selected_city, month, year)
    return render_template("index.html", cities=Villes, selected_city=selected_city, prayer_times=prayer_times)

if __name__ == "__main__":
    app.run(debug=True)