import io
import numpy as np
import pandas as pd
import requests
from statistics import mean, variance
import matplotlib.pyplot as plt
from scipy.stats import chi2


def main():
    with requests.Session() as s:
        download = s.get(
            'https://vincentarelbundock.github.io/Rdatasets/csv/carData/Davis.csv')

    df = pd.read_csv(io.StringIO(download.content.decode('UTF-8')))

    plt.hist(df['weight'], range=(35, 105), bins=14)
    plt.show()

    mu = mean(df['weight'])  # 標本平均
    s2 = mean((df['weight'] - mu)**2)  # 標本分散
    print(mu, s2)

    a = (df['weight'] - mu)**2/s2  # 異常度
    th = chi2.ppf(0.99, 1)
    plt.scatter(np.arange(0, 200), a)
    plt.plot(np.arange(0, 200), [th] * 200, color='red', linestyle='dotted')
    plt.xlabel('index')
    plt.ylabel('anomaly score')
    plt.show()


if __name__ == '__main__':
    main()
