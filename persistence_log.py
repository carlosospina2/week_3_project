import os

def add_blocker():
    """Paso 2 y 4: Añadir datos con validación"""
    # Verificamos si el archivo ya existe para alertar al usuario (Paso 4)
    if os.path.exists("database.txt"):
        print("Note: 'database.txt' already exists. Data will be appended.")
    
    blocker = input("Enter your daily blocker: ")
    
    # Modo 'a' (append) para persistencia sin borrar lo anterior
    with open("database.txt", "a") as file:
        file.write(blocker + "\n")
    print("Success: Blocked saved to persistence storage.")

def get_blockers():
    """Paso 3 y 4: Recuperación de datos y Manejo de errores"""
    if os.path.exists("database.txt"):
        print("\n--- Current Daily Blockers ---")
        with open("database.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("The database is empty.")
            else:
                for line in lines:
                    print(f"- {line.strip()}")
    else:
        print("Error: The file 'database.txt' does not exist. Please add a blocker first.")

def main():
    while True:
        print("\n--- Team Daily Status System ---")
        print("1. Add Daily Blocker")
        print("2. View All Blockers")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == "1":
            add_blocker()
        elif choice == "2":
            get_blockers()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

"""
PASO 5: PRÁCTICA DE INGLÉS

1. SELECCIÓN DE PROTOCOLO:
I will use Slack to report any file-related bugs because the issue requires immediate 
attention from the team. I'll post a clear description in the engineering channel 
to ensure the blocker is resolved quickly. Please let me know if you need the 
error logs to investigate further.

2. INTEGRACIÓN DE VOCABULARIO:
This script focuses on data persistence by storing user input in a permanent text file. 
I implemented a function to fetch (obtener) the logs, and I used the append mode 
to ensure we do not accidentally overwrite (sobrescribir) existing information. 
Effective scripts help us communicate (comunicar) team status updates clearly and efficiently.
"""