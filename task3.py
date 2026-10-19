def tax_report(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        print("Звіт для податкової:", data["company"])
        print("Прибуток:", data["income"] - data["expenses"])
        print()
    return wrapper


def bank_report(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        print("Звіт для банку:", data["company"])
        print("Дохід:", data["income"])
        print("Витрати:", data["expenses"])
        print()
    return wrapper


def get_data(company, income, expenses):
    return {"company": company, "income": income, "expenses": expenses}


for_tax = tax_report(get_data)
for_bank = bank_report(get_data)

for_tax("Ромашка", 1000, 600)
for_bank("Ромашка", 1000, 600)

for_tax("Сонечко", 5000, 3000)
for_bank("Сонечко", 5000, 3000)