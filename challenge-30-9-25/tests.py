from keyword_based_cipher import keyword_cipher

test_1 = keyword_cipher("keyword", "abchij")
output_1 = "keyabc"

test_2 = keyword_cipher("purplepineapple", "abc")
output_2 = "pur"

test_3 = keyword_cipher("mubashir", "edabit")
output_3 = "samucq"

test_4 = keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "abc")
output_4 = "eta"

test_5 = keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "xyz")
output_5 = "qxz"

test_6 = keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "aeiou")
output_6 = "eirfg"

test_cases = [test_1, test_2, test_3, test_4, test_5, test_6]
outputs = [output_1, output_2, output_3, output_4, output_5, output_6]

for i in range(len(test_cases)):
    try:
        assert test_cases[i] == outputs[i]
        print(f'case {i+1} ran successsfully!')
    except AssertionError:
        print(f'case {i+1} was not successsfull!\n{test_cases[i]} != {outputs[i]}')
    except ValueError as ve:
        print(f'case {i+1} raised an error: {ve}')
