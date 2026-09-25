import pandas as pd


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100

def calculate_growth_rate(current_revenue: float, previous_revenue: float) -> float:
    """Возвращает темп роста выручки в процентах."""
    if previous_revenue == 0:
        return 0.0
    return (current_revenue - previous_revenue) / previous_revenue * 100

def main():
    data = {
        "Месяц": ["Январь", "Февраль", "Март"],
        "Выручка": [120000, 150000, 135000],
    }

    df = pd.DataFrame(data)

    print(df)
    print("Средняя выручка:", df["Выручка"].mean())

    profitability = calculate_profitability(150000, 100000)
    print("Рентабельность:", profitability, "%")

growth_rate = calculate_growth_rate(150000, 120000)
print("Темп роста выручки:", growth_rate, "%")
if __name__ == "__main__":
    main()