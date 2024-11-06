vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

def count_occurrences(lst):
    counts = {}
    for item in set(lst):
        counts[item] = lst.count(item)
    
    for item, count in counts.items():
        print(f"{item} => {count}")

count_occurrences(vehicles)