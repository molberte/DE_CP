import pandas as pd
from numeric_methods.functions import Functions


class EulerMethod(Functions):
    @staticmethod
    def solve(x0, y0, xmax, n, func):
        h = (xmax - x0) / n
        data = {'xi': [x0] * n, 'yi': [y0] * n}
        df = pd.DataFrame(data)

        for i in range(1, n + 1):
            df.loc[i, 'xi'] = df.loc[i - 1, 'xi'] + h
            df.loc[i, 'yi'] = (df.loc[i - 1, 'yi'] + h * func(df.loc[i - 1, 'xi'], df.loc[i - 1, 'yi']))
        return df['xi'].tolist(), df['yi'].tolist()
