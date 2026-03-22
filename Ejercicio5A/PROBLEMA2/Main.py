
if __name__ == "__main__":
    pico_pro = Pico("diamante", 3)
    
    # Tarea 2: Bucle hasta que se rompa
    print("--- Probando durabilidad del Pico ---")
    while not pico_pro.rota:
        print(pico_pro.usar("Piedra negra"))
        pico_pro.estado()
    
    print("\n--- Bonus: Arco ---")
    mi_arco = Arco("madera", 10, 2)
    print(mi_arco.usar("Esqueleto"))
    print(mi_arco.usar("Zombie"))
    print(mi_arco.usar("Creeper"))