def branchAndBound(values, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err):
    print(start_index, unassigned_value)
    print(test_assignment, test_value, best_assignment, best_err)
    if start_index >= len(values):
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err[0]:
            best_err[0] = test_err
            best_assignment[0] = test_assignment[:]
    else:
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            unassigned_value -= values[start_index]

            test_assignment[start_index] = True
            branchAndBound(values, start_index + 1,
                                        total_value, unassigned_value,
                                        test_assignment, test_value + values[start_index],
                                        best_assignment, best_err)

            test_assignment[start_index] = False
            branchAndBound(values, start_index + 1,
                                        total_value, unassigned_value,
                                        test_assignment, test_value,
                                        best_assignment, best_err)

values = [3, 1, 2]
start_index = 0
total_value = sum(values)
unassigned_value = total_value
test_assignment = [False] * len(values)
test_value = 0
best_assignment = [None]
best_err = [float('inf')]

branchAndBound(values, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err)
print(best_assignment[0])
print(best_err[0])
print()

