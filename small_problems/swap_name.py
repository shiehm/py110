def swap_name(name):
    first_last = name.split()
    last = first_last[-1]
    first = ' '.join(first_last[:-1])
    return f'{last}, {first}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
                
print(swap_name('Joe Roberts'))   # True
print(swap_name('Karl Oskar Henriksson Ragvals'))  # True



def swap_name(name):
    first_last = name.split()
    last = first_last.pop()
    first = ' '.join(first_last)
    return f'{last}, {first}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
                
print(swap_name('Joe Roberts'))   # True
print(swap_name('Karl Oskar Henriksson Ragvals'))  # True