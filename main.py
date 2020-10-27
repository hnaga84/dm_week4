

import datasets

if __name__ == "__main__":
    X, Y = datasets.load_linear_example1()
    print(X)
    print(X[0])
    print(Y)
    