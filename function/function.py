def FUN(p, tab, a):
    if a == "javascript":
        p[0] = "\t" * tab + f"function {p[2]}{p[3]}{p[4]}" + "{"
    elif a == "python":
        p[0] = "\t" * tab + f"def {p[2]}{p[3]}{p[4]}:"
    elif a == "ruby":
        p[0] = "\t" * tab + f"def {p[2]}{p[3]}{p[4]}"
