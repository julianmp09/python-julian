def main():
        tower_height = 48.3
        tank_height = 12.8
        respuesta = water_column_height (tower_height, tank_height)
        print(f"{respuesta:.1f}")

def water_column_height(tower_height, tank_height):
        height = tower_height
        resultado = height + (3 * tank_height / 4)
        return resultado


main()    