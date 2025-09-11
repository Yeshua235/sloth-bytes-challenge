operations = ('+', '-')

def transfer(token: str, starts_with_x: bool = True) -> str:
    if token.isnumeric():
        if starts_with_x:
            return token
        else:
            return '+' + str(-int(token))
    elif token == '+':
        return '-'
    elif token == '-':
        return '+'
    else:
        try:
            if int(token) and starts_with_x:
                return token
            elif int(token) and not starts_with_x:
                return '+' + str(-int(token))
        except ValueError:
            print(f"Invalid token in equation - {token}")

def evalAlgebra(equation: str) -> int:
    token_list = equation.split()
    if '=' not in token_list:
        raise ValueError("Expression not an equation. = is missing")

    mid_point = token_list.index('=')
    lhs = []
    rhs = []
    l_exp = ''
    r_exp = ''

    for i in token_list:
        if token_list.index(i) < mid_point:
            lhs.append(i)
        elif token_list.index(i) > mid_point:
            rhs.append(i)
        else:
            continue

    if 'x' in rhs:
        for tok in lhs:
            l_exp += tok

        if rhs.index('x') == 0:
            for i in range(1, len(rhs)):
                l_exp += transfer(rhs[i], starts_with_x=True)
        else:
            l_exp += transfer(rhs[0], starts_with_x=False)
            for i in range(0, len(rhs) - 1):
                if (rhs[i + 1] != 'x') and ((rhs[i + 1] in operations) or (rhs[i + 1].isnumeric())):
                    l_exp += transfer(rhs[i + 1], starts_with_x=False)
                else:
                    if rhs[i + 1] == 'x':
                        continue

    elif 'x' in lhs:
        for tok in rhs:
            r_exp += tok

        if lhs.index('x') == 0:
            for i in range(1, len(lhs)):
                r_exp += transfer(lhs[i], starts_with_x=True)
        else:
            r_exp += transfer(lhs[0], starts_with_x=False)
            for i in range(0, len(lhs) - 1):
                if (lhs[i + 1] != 'x') and ((lhs[i + 1] in operations) or (lhs[i + 1].isnumeric())):
                    r_exp += transfer(lhs[i + 1], starts_with_x=False)
                else:
                    if lhs[i + 1] == 'x':
                        continue

    else:
        raise ValueError("unknown variable is missing")

    if l_exp:
        total_exp = l_exp
    if r_exp:
        total_exp = r_exp

    if total_exp[-1] in operations:
        answer_signature = transfer(total_exp[-1], starts_with_x=False) + '1'
        evaluation = eval(total_exp[:-1])
        answer = evaluation * int(answer_signature)
    else:
        answer = eval(total_exp)

    return answer
