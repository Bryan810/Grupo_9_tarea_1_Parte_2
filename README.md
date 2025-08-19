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

![1 Rama Principal Prod](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/1%20Rama%20Principal%20Prod.png)

![2 Imagen creada con la rama prod version 1](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/2%20Imagen%20creada%20con%20la%20rama%20prod%20version%201.png)

![3 Solicitud al endpoint que retorna la sugerencia de una pelicula para ver](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/3%20Solicitud%20al%20endpoint%20que%20retorna%20la%20sugerencia%20de%20una%20pelicula%20para%20ver.png)

![4 Docker levantado con la imagen api version 1](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/4%20Docker%20levantado%20con%20la%20imagen%20api%20version%201.png)

![5 Logs del contenedor docker version 1](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/5%20Logs%20del%20contenedor%20docker%20version%201.png)

![6 Creación de la nueva rama con la nueva feature](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/6%20Creación%20de%20la%20nueva%20rama%20con%20la%20nueva%20feature.png)

![7 Imagen con la nueva version 2 con la nueva feature](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/7%20Imagen%20con%20la%20nueva%20version%202%20con%20la%20nueva%20feature.png)

![8 Ejecución del docker con la version 2](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/8%20Ejecución%20del%20docker%20con%20la%20version%202.png)

![9 Docker corriendo con la nueva version 2](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/9%20Docker%20corriendo%20con%20la%20nueva%20version%202%20.png)

![10 Logs del docker con la versión 2](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/10%20Logs%20del%20docker%20con%20la%20versión%202.png)

![11 respuesta del api version 2 indicando que pokemon eres el día de hoy](https://raw.githubusercontent.com/Bryan810/Grupo_9_tarea_1_Parte_2/feat/what_pokemon_am_i_today/Capturas/11%20respuesta%20del%20api%20version%202%20indicando%20que%20pokemon%20eres%20el%20día%20de%20hoy.png)


---

## 📜 Licencia
Este proyecto es de uso libre para fines educativos y de práctica.