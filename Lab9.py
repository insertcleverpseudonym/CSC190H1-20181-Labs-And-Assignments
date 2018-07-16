'''
Lab 9:

1. Develop the towers of Hanoi problem-solver

2. Write a quicksort function with the required partition function

'''
def hanoi(accum,n,source,auxiliary,target):
   if n > 0:
        hanoi(accum,n - 1,source, target, auxiliary)
        target.append(source.pop())
        hanoi(accum,n - 1,auxiliary, source, target)
        accum += [source,auxiliary,target]
        return True
   else:
        return True

def quick_sort(u,ini,fin):
        if ini<fin:
                pIndex = partition(u,ini,fin)
                quick_sort(u, ini, pIndex-1)
                quick_sort(u, pIndex+1,fin)
        return True

def partition(u,ini,fin):
    i = (ini-1)
    pivot = u[fin]
    for j in range(ini , fin):
        if   u[j] <= pivot:
            i = i+1
            u[i],u[j] = u[j],u[i]

    u[i+1],u[fin] = u[fin],u[i+1]
    return (i+1)
