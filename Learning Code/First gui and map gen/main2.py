from map import Map

def run() -> None:
    while True:
        game_map.display_map()
        input("> ")


if __name__ == "__main__":
    map_w, map_h = 30, 15
    game_map = Map(map_w, map_h)
    run()