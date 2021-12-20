import re
def calc(equation):
    equation = equation.replace(" ", "")
    equation = "(" + equation + ")"
    def mul(n1, n2):
        value = str(float(n1) * float(n2))
        return value if "-" in value else "+" + value
    def div(n1, n2):
        value = float(n1) / float(n2)
        return str(value) if value < 0  else "+" + str(value)
    def mod(n1, n2):
        value = float(n1) % float(n2)
        return str(value) if value < 0  else "+" + str(value)
    def plas(n1, n2):
        value = float(n1) + float(n2)
        return str(value) if value < 0  else "+" + str(value)
    def minus(n1, n2):
        value = float(n1) - float(n2)
        return str(value) if value < 0  else "+" + str(value)
    def parse_e(string):
        nonlocal equation
        x = float(string)
        result = '{:.70f}'.format(x)
        equation = re.sub(string,result,equation,1)
    def do_math():
        nonlocal equation
        equation = equation.replace("-+","-")
        equation = equation.replace("--","+")
        equation = equation.replace("+-","-")
        equation = equation.replace("++","+")
        list_of_e = re.findall("[.0-9]+e-[0-9]+",equation)
        if list_of_e:
            parse_e(list_of_e[0])
            return 0
        insde_par = re.findall("[(] *([-+/*%0-9 .]*) *[)]", equation)
        first_do = re.findall("(([-+]?[0-9.]+)([%*/])([-+]?[0-9.]+))", insde_par[0])
        second_do = re.findall("(([-+]?[0-9.]+)([-+])([-+]?[0-9.]+))", insde_par[0])
        only_par = re.findall("[(][-+]?[0-9.]+[)]", equation)
        if only_par:
            true_only_par = "".join(only_par[0]).replace("(", "").replace(")", "")
            false_only_par = re.escape("".join(only_par[0]))
            equation = re.sub(false_only_par, true_only_par, equation,1)
        elif first_do:
            change, num1, op, num2 = first_do[0]
            result = mod(num1, num2) if op == "%" else mul(num1, num2) if op == "*" else div(num1, num2)
            change = re.escape(change)
            equation = re.sub(change, result, equation,1)
        elif second_do:
            change, num1, op, num2 = second_do[0]
            result = plas(num1, num2) if op == "+" else minus(num1, num2)
            change = re.escape(change)
            equation = re.sub(change, result, equation,1)
    while "(" in equation:
        do_math()
    return float(equation)


x = input("write your calculation: ")
print(f"answers is: {calc(x)}")