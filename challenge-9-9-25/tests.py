from simple_algebra import evalAlgebra

test_cases = [
    "2 + x = 19",
    "4 - x = 1",
    "x + 10 = 53",
    "-23 + x = -20",
    "10 + x = 5",
    "-49 - x = -180",
    "x - 22 = -56"
]

expected_outputs = [17, 3, 43, 3, -5, 131, -34]

assert len(test_cases) == len(expected_outputs)

for i in range(len(test_cases)):
    try:
        assert evalAlgebra(test_cases[i]) == expected_outputs[i]
        print(f'case {i+1} ran successsfully!')
    except AssertionError:
        print(f'case {i+1} was not successsfull!\t{test_cases[i]} ==> {evalAlgebra(test_cases[i])} != {expected_outputs[i]}')
