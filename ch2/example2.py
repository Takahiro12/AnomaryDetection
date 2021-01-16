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

    X = df[['weight', 'height']].values

    plt.scatter(X.T[0], X.T[1])
    plt.xlabel('weight')
    plt.ylabel('height')
    plt.show()
    plt.close()

    mx = X.mean(axis=0)
    Xc = X - np.ones((len(X), 1)) * mx
    Sx = Xc.T.dot(Xc) / len(X)
    a = (Xc.dot(np.linalg.inv(Sx)) * Xc).sum(axis=1)  # マハラノビス距離計算

    plt.scatter(np.arange(0, len(a)), a)
    plt.xlabel('index')
    plt.ylabel('anomaly score')
    th = chi2.ppf(0.99, 1)
    plt.plot(np.arange(0, 200), [th] * 200, color='red', linestyle='dotted')
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
