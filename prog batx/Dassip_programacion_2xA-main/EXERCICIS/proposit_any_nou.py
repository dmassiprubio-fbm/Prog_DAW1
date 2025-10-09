def show_menu():
    print("--Menú--")
    print("1. Afegir un propòsit")
    print("2. Veure un propòsit")
    print("3. Marcar un propòsit com a complert")
    print("4. Esborrar propòsit complert")
    print("5. Sortir")

def add_goal(goals):
    new_goal = input("Quin propòsit vols afegir? ")
    goals.append(new_goal)

def view_goals(goals):
    print(goals)

def mark_as_completed(goals):
    view_goals(goals)
    goal = int(input("Quin propòsit vols marcar com a complert? "))
    if 0 <= goal < len(goals):
        goals[goal] = goals[goal] + " (complert)"
    else:
        print("Índex no vàlid")

def delete_goal(goals):
    view_goals(goals)
    goal = int(input("Quin propòsit vols esborrar? "))
    if 0 <= goal < len(goals):
        goals.pop(goal)
    else:
        print("Índex no vàlid")

def main():
    goals = []
    while True:
        show_menu()
        option = int(input("Quina opció vols? "))
        if option == 1:
            add_goal(goals)
        elif option == 2:
            view_goals(goals)
        elif option == 3:
            mark_as_completed(goals)
        elif option == 4:
            delete_goal(goals)
        elif option == 5:
            break
        else:
            print("Opció incorrecta")

if __name__ == "__main__":
    main()