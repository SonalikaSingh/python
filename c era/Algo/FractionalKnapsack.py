# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    numItems = len(values)
    valuePerWeight = sorted([[values[i] / weights[i], weights[i]] for i in range(numItems)], reverse=True)
    while capacity > 0 and numItems > 0:
        maxi = 0
        idx = None
        for i in range(numItems):
            if valuePerWeight[i][1] > 0 and maxi < valuePerWeight[i][0]:
                maxi = valuePerWeight[i][0]
                idx = i

        if idx is None:
            return 0.
        if valuePerWeight[idx][1] <= capacity:
            value += valuePerWeight[idx][0]*valuePerWeight[idx][1]
            capacity -= valuePerWeight[idx][1]
        else:
            if valuePerWeight[idx][1] > 0:
                value += (capacity / valuePerWeight[idx][1]) * valuePerWeight[idx][1] * valuePerWeight[idx][0]
                return value
        valuePerWeight.pop(idx)
        numItems -= 1
    return value




if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))
