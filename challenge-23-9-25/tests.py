from can_exit_maze import canExit

test_1 = canExit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
])
output_1 = True

test_2 = canExit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
])
output_2 = False    # This maze only has dead ends!

test_3 = canExit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
])
output_3 = False    # Exit only one block away, but unreachable!

test_4 = canExit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
])
output_4 = True

test_cases = [test_1, test_2, test_3, test_4]
outputs = [output_1, output_2, output_3, output_4]

for i in range(len(test_cases)):
    try:
        assert test_cases[i] == outputs[i]
        print(f'case {i+1} ran successsfully!')
    except AssertionError:
        print(f'case {i+1} was not successsfull!\n{test_cases[i]} != {outputs[i]}')
