import requests

# Définir la base URL de l'API
BASE_URL = "https://api.aviationstack.com/v1/flights"
API_KEY ="f264c435d91172dbdac3c8ce2770234f"

def get_flight_status(flight_number):
    """
    Fonction pour obtenir le statut d'un vol à partir de son numéro IATA.
    """
    # Construire l'URL complète
    url = f"{BASE_URL}?access_key={API_KEY}&flight_iata={flight_number}"
    
    try:
        # Envoyer la requête HTTP GET à l'API
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        data = response.json()  # Convertir la réponse JSON en dictionnaire Python
        
        # Vérifier si des données sont disponibles
        if "data" in data and len(data["data"]) > 0:
            flight = data["data"][0]
            print(f"Statut du vol {flight_number}:")
            print(f"  Aéroport de départ : {flight['departure']['airport']}")
            print(f"  Aéroport d'arrivée : {flight['arrival']['airport']}")
            print(f"  Compagnie aérienne : {flight['airline']['name']}")
            print(f"  Statut du vol      : {flight['flight_status']}")
        else:
            print(f"Aucune information trouvée pour le vol {flight_number}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la communication avec l'API : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    flight_number = input("Entrez le numéro de vol (exemple : AA100) : ").strip()
    get_flight_status(flight_number)
