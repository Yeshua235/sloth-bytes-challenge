from word_path_tracer import trace_word_path

test_1 = trace_word_path("BISCUIT", [
  ["B", "I", "T", "R"],
  ["I", "U", "A", "S"],
  ["S", "C", "V", "W"],
  ["D", "O", "N", "E"]
])

output_1 = [[0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [0, 1], [0, 2]]

test_2 = trace_word_path("HELPFUL", [
  ["L","I","T","R"],
  ["U","U","A","S"],
  ["L","U","P","O"],
  ["E","F","E","H"]
])

output_2 = "Not present"

test_3 = trace_word_path("UKULELE", [
  ["N", "H", "B", "W"],
  ["E", "X", "A", "D"],
  ["L", "A", "U", "U"],
  ["E", "L", "U", "K"]
])

output_3 = [[2, 3], [3, 3], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0]]

test_4 = trace_word_path("SURVIVAL", [
  ["V", "L", "R", "L"],
  ["V", "A", "I", "V"],
  ["I", "O", "S", "C"],
  ["V", "R", "U", "F"]
])

output_4 = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [1, 1], [0, 1]]

test_cases = [test_1, test_2, test_3, test_4]
outputs = [output_1, output_2, output_3, output_4]

for i in range(len(test_cases)):
    try:
        assert test_cases[i] == outputs[i]
        print(f'case {i+1} ran successsfully!')
    except AssertionError:
        print(f'case {i+1} was not successsfull!\n{test_cases[i]} != {outputs[i]}')
