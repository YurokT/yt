class Axe:
    """Тимчасовий клас, емулюючий наш головний клас Меча, використовується для тестів"""
    def __init__(self) -> None:
        self.name = "Сокира"
        self.damag = 0
        self.vitality = 0

    def __str__(self) -> str:
        return f"Name: {self.name}"

axe = Axe()
print(axe)
