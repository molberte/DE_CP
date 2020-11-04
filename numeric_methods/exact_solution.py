import pandas as pd
from numeric_methods.functions import Functions


class ExactSolution(Functions):
    @staticmethod
    def solve(x0, y0, X, n, solution):
        h = (X - x0) / n
        data = {'xi': [x0] * n, 'yi': [y0] * n}
        df = pd.DataFrame(data)
        for i in range(1, n+1):
            df.loc[i, 'xi'] = df.loc[i - 1, 'xi'] + h
            df.loc[i, 'yi'] = solution(df.loc[i, 'xi'], x0, y0)
        return df['xi'].tolist(), df['yi'].tolist()
