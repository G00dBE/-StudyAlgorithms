for tc in range(1,11):
    input_len = int(input())
    token = input()                       #문자열 입력
    stack = []                            # 빈스택 생성
    stack_int = []                        # 숫자를 append할 스택
    for i in range(input_len):
        if token[i].isdigit():   # 숫자면 무조건 append
            stack_int.append(int(token[i]))
        elif token[i] == '(' or token[i] == '*':
            stack.append(token[i])
        elif token[i] == '+':   # +의 경우 우선순위가 낮기 때문에 이전이 *인 경우 *를 전부 pop한 뒤 append
            while len(stack) != 0 and stack[-1] == '*':
                stack_int.append(stack.pop())
            stack.append(token[i])
        elif token[i] == ')':           # '(' 이 나올 때 까지 pop
            pop_ent = stack.pop()
            while pop_ent != '(':
                stack_int.append(pop_ent)
    while len(stack) != 0:          # 남아있는 스택원소 전부 pop 해서 append
        pop_ent = stack.pop()
        if pop_ent != '(':
            stack_int.append(pop_ent)
    stack2 = []  # 계산 결과를 저장할 스택
    for i in range(len(stack_int)):
        if type(stack_int[i]) == int:
            stack2.append(stack_int[i])
        else:
            num1 = stack2.pop()  # 두 원소를 pop
            num2 = stack2.pop()
            if stack_int[i] == "+":
                stack2.append(num1+num2)
            elif stack_int[i] == "*":
                stack2.append(num1*num2)

    print(f"#{tc} {stack2[0]}")

