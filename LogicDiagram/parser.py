import re


def parse_logic(text):
    lines = text.strip().split("\n")
    rules = []

    for line in lines:
        line = line.strip().upper()
        if not line or "IF" not in line or "THEN" not in line:
            continue

        condition_part, result_part = [part.strip() for part in line.split("THEN", 1)]
        condition_part = condition_part.replace("IF", "", 1).strip()

        condition_exprs = _split_expressions(condition_part)
        result_exprs = _split_expressions(result_part)

        for cond in condition_exprs:
            for res in result_exprs:
                rules.append((cond, res))

    return rules


def _split_expressions(expr):
    expr = expr.replace("(", "( ").replace(")", " )")
    tokens = expr.split()
    stack = []
    current = []

    for token in tokens:
        if token == "(":
            stack.append(current)
            current = []
        elif token == ")":
            group = current
            current = stack.pop() if stack else []
            current.append(group)
        elif token in ("AND", "OR"):
            current.append(token)
        else:
            current.append(token)

    return _flatten_expression(current)


def _flatten_expression(expr):
    if isinstance(expr, str):
        return [expr]

    if isinstance(expr, list):
        flat = []
        for item in expr:
            if item in ("AND", "OR"):
                continue  # operator ignored for simple edge generation
            flat.extend(_flatten_expression(item))
        return flat

    return []
