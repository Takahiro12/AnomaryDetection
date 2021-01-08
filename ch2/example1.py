import io
import numpy as np
import pandas as pd
import requests
from statistics import mean, variance
import matplotlib.pyplot as plt


def main():
    with requests.Session() as s:
        download = s.get(
            'https://vincentarelbundock.github.io/Rdatasets/csv/carData/Davis.csv')

    df = pd.read_csv(io.StringIO(download.content.decode('UTF-8')))

    plt.hist(df['weight'], range=(35, 105), bins=14)
    plt.show()

    mu = mean(df['weight'])  # 標本平均
    s2 = mean((df['weight'] - mu)**2)
    print(mu, s2)


if __name__ == '__main__':
    main()
