import random
import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = "fd70eeacca6093c02d0e236eda81461b"


@app.route('/api/hola', methods=['GET'])
def hola_mundo():
    return jsonify({"mensaje": "Hola Mundo"}), 200


@app.route('/api/netflix/random', methods=['GET'])
def random_netflix_movie():
    try:
        url = f"https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": API_KEY,
            "with_watch_providers": "8",
            "watch_region": "US",
            "language": "es-ES",
            "page": random.randint(1, 20)
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "results" not in data or not data["results"]:
            return jsonify({"error": "No se encontraron películas en Netflix"}), 404

        movie = random.choice(data["results"])

        resultado = {
            "titulo": movie.get("title"),
            "descripcion": movie.get("overview"),
            "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get(
                "poster_path") else None,
            "link_tmdb": f"https://www.themoviedb.org/movie/{movie.get('id')}"
        }

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# New feat, qhich pokemon am i
@app.route('/api/pokemon/random', methods=['GET'])
def pokemon_aleatorio():
    try:
        url = "https://pokeapi.co/api/v2/pokemon?limit=1000&offset=0"
        data = requests.get(url).json()
        resultados = data.get("results", [])

        if not resultados:
            return jsonify({"error": "No se encontraron Pokémon"}), 404

        elegido = random.choice(resultados)
        detalles = requests.get(elegido["url"]).json()

        respuesta = {
            "nombre": detalles.get("name"),
            "altura": detalles.get("height"),
            "peso": detalles.get("weight"),
            "imagen": detalles.get("sprites", {}).get("front_default"),
            "link_pokeapi": elegido["url"]
        }

        return jsonify(respuesta), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
