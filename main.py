def square_root(lim_up, lim_down, max_iterations, tolerance, number):
    for i in range(max_iterations):
        result = (lim_up + lim_down) / 2
        square = result*result
        if (lim_up - lim_down) < tolerance:
            print(f'The square root of {number} is approximately {result}')
            return result
        elif (lim_up - lim_down) > tolerance and (square - number) > 0:
            lim_up = result
        elif (lim_up - lim_down) > tolerance and (square - number) < 0:
            lim_down = result
    print(f'Failed to converge within {max_iterations} iterations')
    return None

def square_root_bisection(number, tolerance = 0.01, max_iterations = 25):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number
    if number > 1:
        lim_up = number 
        lim_down = 0
        result = square_root(lim_up, lim_down, max_iterations,tolerance, number)
    else:
        lim_up = 1 
        lim_down = number
        result = square_root(lim_up, lim_down, max_iterations,tolerance, number)
    return result

if __name__ == '__main__':
    square_root_bisection(0.25, 1e-7, 50)