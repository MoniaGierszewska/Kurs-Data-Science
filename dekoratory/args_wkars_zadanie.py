def calculations(option, *args):
    result = args[0]
    if len(args) >= 2:
        if option == "suma":
            for i in range(1, len(args)):
                result += args[i]
        elif option == "różnica":
            for i in range(1, len(args)):
                result -= args[i]
        elif option == "iloczyn":
            for i in range(1, len(args)):
                result *= args[i]
        elif option == "iloraz":
            for i in range(1, len(args)):
                try:
                    result /= args[i]
                except (ZeroDivisionError):
                    print("Probowałeś dzielić przez zero.")
                    continue

        return result


print(calculations("iloraz", 10, 0))