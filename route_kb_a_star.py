import math
import argparse

def load_kb(filename):
    estaciones = {}
    conexiones = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = line.split()

            if len(parts) == 4 and parts[0].lower() == "station":
                nombre = parts[1]
                lat = float(parts[2])
                lon = float(parts[3])
                estaciones[nombre] = (lat, lon)

            elif len(parts) == 4 and parts[0].lower() == "edge":
                a = parts[1]
                b = parts[2]
                costo = float(parts[3])
                conexiones.append((a, b, costo))
                conexiones.append((b, a, costo))  # grafo no dirigido

    return estaciones, conexiones

def heuristic(a, b, estaciones):
    (x1, y1) = estaciones[a]
    (x2, y2) = estaciones[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def a_star(start, goal, estaciones, conexiones):
    open_set = {start}
    came_from = {}
    g_score = {node: float("inf") for node in estaciones}
    g_score[start] = 0
    f_score = {node: float("inf") for node in estaciones}
    f_score[start] = heuristic(start, goal, estaciones)

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        open_set.remove(current)

        for (a, b, costo) in conexiones:
            if a == current:
                tentative_g = g_score[current] + costo
                if tentative_g < g_score[b]:
                    came_from[b] = current
                    g_score[b] = tentative_g
                    f_score[b] = tentative_g + heuristic(b, goal, estaciones)
                    open_set.add(b)

    return None, float("inf")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--kb", required=True, help="Archivo con la base de conocimiento")
    parser.add_argument("--start", required=True, help="Estación inicial")
    parser.add_argument("--goal", required=True, help="Estación destino")
    args = parser.parse_args()

    estaciones, conexiones = load_kb(args.kb)

    if args.start not in estaciones or args.goal not in estaciones:
        print("❌ Error: La estación inicial o destino no está en la base de conocimiento.")
    else:
        path, cost = a_star(args.start, args.goal, estaciones, conexiones)
        if path:
            print("\n✅ Ruta encontrada:")
            print(" → ".join(path))
            print(f"⏱️ Costo total: {cost} minutos")
        else:
            print("⚠️ No se encontró ruta posible.")









                    










