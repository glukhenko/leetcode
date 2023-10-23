from typing import List

NOMINALS = [20, 50, 100, 200, 500]


class ATM:

    def __init__(self):
        self.store = {nominal: 0 for nominal in NOMINALS}

    def __str__(self):
        return f'ATM has: {", ".join([f"{nominal}$ = {self.store[nominal]}" for nominal in NOMINALS])}'

    def add_banknotes(self, banknotes: List[int]) -> None:
        for nominal, count_banknote in zip(NOMINALS, banknotes):
            self.store[nominal] += count_banknote

    def remove_banknotes(self, banknotes: List[int]) -> None:
        for nominal, count_banknote in zip(NOMINALS, banknotes):
            self.store[nominal] -= count_banknote

    def can_use_banknotes(self, amount: int) -> Optional[List[int]]:
        result = []

        for nominal in NOMINALS[::-1]:
            atm_banknotes = self.store.get(nominal)
            can_use_atm_banknotes = atm_banknotes and amount >= nominal
            if can_use_atm_banknotes:
                need_banknotes = amount // nominal
                used_banknotes = min(need_banknotes, atm_banknotes)
                amount -= used_banknotes * nominal
                result.append(used_banknotes)
            else:
                result.append(0)

        is_valid_operation = not amount
        if is_valid_operation:
            return result[::-1]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.add_banknotes(banknotesCount)

    def withdraw(self, amount: int) -> List[int]:
        banknotes = self.can_use_banknotes(amount)
        if banknotes:
            self.remove_banknotes(banknotes)
            return banknotes
        else:
            return [-1]


if __name__ == '__main__':
    operations = ["deposit", "withdraw", "deposit", "withdraw", "withdraw"]
    values = [[0, 0, 1, 2, 1], 600, [0, 1, 0, 1, 1], 600, 550]
    expected_results = [None, [0, 0, 1, 0, 1], None, [-1], [0, 1, 0, 0, 1]]

    obj = ATM()
    for operation, value, expected_result in zip(operations, values, expected_results):
        result = getattr(obj, operation)(value)
        print(f'operation: {operation}, value: {value}, res: {result}. After transaction: {obj}')
        assert result == expected_result, f'Bad result for {operation} with {value}: {result}, but expected: {expected_result}'
        # print(f'After transaction: {obj}')
