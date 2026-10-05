## Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, 
# and sum of the rows, columns, and elements in a 3 x 3 matrix.

#The input of the function should be a list containing 9 digits. 
# The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, 
# standard deviation, max, min, and sum along both axes and for the flattened matrix.

#The returned dictionary should follow this format:
                 # {
#{  'mean': [axis1, axis2, flattened],
#  'variance': [axis1, axis2, flattened],
# 'standard deviation': [axis1, axis2, flattened],
#  'max': [axis1, axis2, flattened],
#  'min': [axis1, axis2, flattened],
#  'sum': [axis1, axis2, flattened]
#}

# If a list containing less than 9 elements is passed into the function, 
# it should raise a ValueError exception with the message: "List must contain nine numbers." 
# The values in the returned dictionary should be lists and not Numpy arrays.

#For example, calculate([0,1,2,3,4,5,6,7,8]) should return:
#{
  #'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
 # 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
 # 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
 # 'max': [[6, 7, 8], [2, 5, 8], 8],
  #'min': [[0, 1, 2], [0, 3, 6], 0],
 # 'sum': [[9, 12, 15], [3, 12, 21], 36]
#}

# lets import numpy as np
import numpy as np

def calculate(list_numbers):
    if len(list_numbers) != 9:
        raise ValueError("List must contain nine numbers.")

# now lets convert the list into a 3 x 3 Numpy array
    matrix = np.array(list_numbers).reshape(3, 3)

    mean_column = matrix.mean(axis=0).tolist()
    mean_row = matrix.mean(axis=1).tolist()
    mean_flattened = float(matrix.mean())

    variance_column = matrix.var(axis=0).tolist()
    variance_row = matrix.var(axis=1).tolist()
    variance_flattened = float(matrix.var())

    std_column = matrix.std(axis=0).tolist()
    std_row = matrix.std(axis=1).tolist()
    std_flattened = float(matrix.std())

    max_column = matrix.max(axis=0).tolist()
    max_row = matrix.max(axis=1).tolist()
    max_flattened = int(matrix.max())

    min_column = matrix.min(axis=0).tolist()
    min_row = matrix.min(axis=1).tolist()
    min_flattened = int(matrix.min())

    sum_column = matrix.sum(axis=0).tolist()
    sum_row = matrix.sum(axis=1).tolist()
    sum_flattened = int(matrix.sum())

    return {
        'mean': [mean_column, mean_row, mean_flattened],
        'variance': [variance_column, variance_row, variance_flattened],
        'standard deviation': [std_column, std_row, std_flattened],
        'max': [max_column, max_row, max_flattened],
        'min': [min_column, min_row, min_flattened],
        'sum': [sum_column, sum_row, sum_flattened]
    }

print(calculate([0,1,2,3,4,5,6,7,8]))