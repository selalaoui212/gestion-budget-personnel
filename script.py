import pandas as pd
import matplotlib.pyplot as plt
import csv

FILENAME = "transactions.csv"

def initialize_csv():
    try:
        with open(FILENAME, 'r') as file:
            pass  
    except FileNotFoundError:
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Type', 'Montant', 'Catégorie', 'Description'])

def add_transaction(date, t_type, amount, category, description):
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, amount, category, description])

def generate_report():
    data = pd.read_csv(FILENAME)
    
    total_income = data[data['Type'] == 'Revenu']['Montant'].sum()
    total_expenses = data[data['Type'] == 'Dépense']['Montant'].sum()
    balance = total_income - total_expenses

    print(f"Total des revenus: {total_income}€")
    print(f"Total des dépenses: {total_expenses}€")
    print(f"Solde actuel: {balance}€")
    
    expense_data = data[data['Type'] == 'Dépense']
    category_expenses = expense_data.groupby('Catégorie')['Montant'].sum()
    
    print("\nDépenses par catégorie:")
    print(category_expenses)
    
    category_expenses.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
    plt.title("Répartition des Dépenses par Catégorie")
    plt.ylabel("")  
    plt.show()

def main():
    initialize_csv()
    
    while True:
        print("\nMenu:")
        print("1. Ajouter un revenu")
        print("2. Ajouter une dépense")
        print("3. Générer un rapport financier")
        print("4. Quitter")
        
        choice = input("Choisissez une option (1/2/3/4) : ")
        
        if choice == '1':
            date = input("Entrez la date (jj/mm/aaaa) : ")
            amount = float(input("Entrez le montant du revenu : "))
            category = input("Entrez la catégorie (ex : Salaire, Freelance) : ")
            description = input("Entrez une description : ")
            add_transaction(date, 'Revenu', amount, category, description)
            print(f"Revenu de {amount}€ ajouté.")
        
        elif choice == '2':
            date = input("Entrez la date (jj/mm/aaaa) : ")
            amount = float(input("Entrez le montant de la dépense : "))
            category = input("Entrez la catégorie (ex : Alimentation, Loisirs, Logement) : ")
            description = input("Entrez une description : ")
            add_transaction(date, 'Dépense', amount, category, description)
            print(f"Dépense de {amount}€ ajoutée.")
        
        elif choice == '3':
            generate_report()
        
        elif choice == '4':
            print("Au revoir!")
            break
        
        else:
            print("Option invalide. Essayez de nouveau.")


if __name__ == "__main__":
    main()
