# 🚀 API de Ejemplo con Flask

Este proyecto es una API simple desarrollada en **Python + Flask** que incluye varios endpoints de ejemplo:

- **Hola Mundo**
- **Película aleatoria de Netflix** (usando TMDb API)
- **Pokémon aleatorio** (usando PokéAPI)

---

## 📌 Endpoints disponibles

### 1. Hola Mundo
```
GET /api/hola
```
**Respuesta:**
```json
{ "mensaje": "Hola Mundo" }
```

---

### 2. Película aleatoria en Netflix
```
GET /api/netflix/random
```
Devuelve una película aleatoria disponible en Netflix (según TMDb).

**Ejemplo de respuesta:**
```json
{
  "titulo": "El Irlandés",
  "descripcion": "Frank Sheeran, veterano de la Segunda Guerra Mundial...",
  "poster": "https://image.tmdb.org/t/p/w500/xxxx.jpg",
  "link_tmdb": "https://www.themoviedb.org/movie/398978"
}
```

---

### 3. Pokémon aleatorio
```
GET /api/pokemon/random
```
Devuelve un Pokémon aleatorio con datos básicos desde PokéAPI.

**Ejemplo de respuesta:**
```json
{
  "nombre": "pikachu",
  "altura": 4,
  "peso": 60,
  "sprites": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
  "link_pokeapi": "https://pokeapi.co/api/v2/pokemon/25/"
}
```


## 🖼️ Captura de ejemplo

![1 Rama Principal Prod](Capturas/1 Rama Principal Prod.png)

![2 Imagen creada con la rama prod version 1](Capturas/2 Imagen creada con la rama prod version 1.png)

![3 Solicitud al endpoint que retorna la sugerencia de una pelicula para ver](Capturas/3 Solicitud al endpoint que retorna la sugerencia de una pelicula para ver.png)

![4 Docker levantado con la imagen api version 1](Capturas/4 Docker levantado con la imagen api version 1.png)

![5 Logs del contenedor docker version 1](Capturas/5 Logs del contenedor docker version 1.png)

![6 Creación de la nueva rama con la nueva feature](Capturas/6 Creación de la nueva rama con la nueva feature.png)

![7 Imagen con la nueva version 2 con la nueva feature](Capturas/7 Imagen con la nueva version 2 con la nueva feature.png)

![8 Ejecución del docker con la version 2](Capturas/8 Ejecución del docker con la version 2.png)

![9 Docker corriendo con la nueva version 2](Capturas/9 Docker corriendo con la nueva version 2 .png)

![10 Logs del docker con la versión 2](Capturas/10 Logs del docker con la versión 2.png)

![11 respuesta del api version 2 indicando que pokemon eres el día de hoy](Capturas/11 respuesta del api version 2 indicando que pokemon eres el día de hoy.png)


---

## 📜 Licencia
Este proyecto es de uso libre para fines educativos y de práctica.