tab = []
result = []
goalList = ["a", "b", "c", "d", "e"]

def parSolution(N):
    for i in range(N):
        if goalList[i] != result[i]:
            return False
    return True

def Onblock(index, count):
    if count == len(goalList) + 1:
        return True

    block = tab[index]
    result.append(block)
    print(result)

    if parSolution(count):
        print("Pushed a result solution")
        tab.remove(block)
        Onblock(0, count + 1)
    else:
        print("Result solution not possible, back to the tab")
        result.pop()
        Onblock(index + 1, count)

def Ontab(problem):
    if len(problem) != 0:
        tab.append(problem.pop())
        Ontab(problem)

def goal_stack_planing(problem):
    Ontab(problem)
    if Onblock(0, 1):
        print(result)

if __name__ == "__main__":
    problem = ["c", "a", "e", "d", "b"]
    print("Goal Problem")
    for k, j in zip(goalList, problem):
        print(k + " " + j)
    goal_stack_planing(problem)
    print("Result Solution")
    print(result)
