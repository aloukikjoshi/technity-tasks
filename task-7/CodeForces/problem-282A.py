def execute_program(program):
    x = 0
    for statement in program:
        if "++" in statement:
            x += 1
        elif "--" in statement:
            x -= 1
    return x

n = int(input())

program = []
for _ in range(n):
    statement = input().strip()
    program.append(statement)

final_value = execute_program(program)
print(final_value)
