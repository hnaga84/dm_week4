

import datasets
import regression

if __name__ == "__main__":
    X, Y = datasets.load_linear_example1()
    model = regression.LinearRegression()

    print(model.x)
    


