import requests

# Définir la base URL de l'API et votre clé d'API
BASE_URL = "https://api.aviationstack.com/v1/airports"
API_KEY = "f264c435d91172dbdac3c8ce2770234f"

def get_airport_info(airport_code):
    """
    Fonction pour obtenir des informations sur un aéroport en utilisant son code IATA.
    """
    # Construire l'URL complète
    url = f"{BASE_URL}?access_key={API_KEY}&iata_code={airport_code}"
    
    try:
        # Envoyer la requête HTTP GET à l'API
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        data = response.json()  # Convertir la réponse JSON en dictionnaire Python
        
        # Vérifier si des données sont disponibles
        if "data" in data and len(data["data"]) > 0:
            airport = data["data"][0]
            print(f"Informations sur l'aéroport {airport_code} :")
            print(f"  Nom          : {airport['airport_name']}")
            print(f"  Ville        : {airport['city']}")
            print(f"  Pays         : {airport['country_name']}")
            print(f"  Code IATA    : {airport['iata_code']}")
            print(f"  Latitude     : {airport['latitude']}")
            print(f"  Longitude    : {airport['longitude']}")
        else:
            print(f"Aucun aéroport trouvé avec le code IATA {airport_code}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la communication avec l'API : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    airport_code = input("Entrez le code IATA de l'aéroport (exemple : JFK) : ").strip().upper()
    get_airport_info(airport_code)
