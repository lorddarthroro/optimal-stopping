import random

# creates a dataset of numbers from 1 to 1000000 to use for selection and testing. Shouldn't use n>1000000
def generate_dataset(n):
    dataset = list(range(1, n + 1))
    random.shuffle(dataset)
    return dataset

# returns the optimal choice for the list (greatest number)
def optimal_choice(dataset):
    return max(dataset)

# starts looking for the best option in a dataset after k steps
def optimal_stopping(dataset, k):
    visited = []
    for i in range(len(dataset)):
        
        value = dataset[i]
        
        if i >= k and value > max(visited):
            return value, i # return value and index

        visited.append(value)

    return(dataset[-1], i) # fallback to last if none better found

# n = 100
# p=.37
# k = int(n*p)

# dataset = generate_dataset(n)
# choice = optimal_stopping(dataset, k)
# print(choice, optimal_choice(dataset))

def run_simulation(n=100, p=0.37, trials=100000):
    k = int(n * p)
    successes = 0

    for _ in range(trials):
        dataset = generate_dataset(n)
        optimal_val = optimal_choice(dataset)
        choice, index = optimal_stopping(dataset, k)

        if choice == optimal_val:
            successes += 1

    print(f"Trials: {trials}")
    print(f"Successes: {successes}")
    print(f"Success rate: {successes / trials:.4f}")

run_simulation()