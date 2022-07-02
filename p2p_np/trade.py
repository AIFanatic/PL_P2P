import numpy as np
import random
import time
np.set_printoptions(suppress=True)

random.seed(0)

def generate_data(producer_count, consumer_count):
    producers = np.zeros((producer_count))
    consumers = np.zeros((consumer_count))

    for i in range(len(producers)):
        producers[i] = random.randrange(1, 100)

    for i in range(len(consumers)):
        consumers[i] = random.randrange(1, 100)

    return producers, consumers

d = generate_data(1000000, 1000000)
producers = d[0]
consumers = d[1]

# producers = np.zeros((3))
# producers[0] = 100
# producers[1] = 100
# producers[2] = 100

# consumers = np.zeros((3))
# consumers[0] = 10
# consumers[1] = 50
# consumers[2] = 50

print("p", producers)
print("c", consumers)

print("TP", np.sum(producers))
print("TC", np.sum(consumers))
print("TP-TC", np.sum(producers) - np.sum(consumers))

EPSILON = 1e-12
shouldContinue = True

st = time.time_ns()
tradeC = 0
while shouldContinue:
    producers = producers[np.where(producers > EPSILON)]
    consumers = consumers[np.where(consumers > EPSILON)]

    allocation = np.min(consumers) / len(producers)

    if allocation > np.min(producers):
        allocation = np.min(producers)

    if allocation * len(consumers) > np.min(producers):
        allocation = np.min(producers) / len(consumers)

    producers = producers - allocation * len(consumers)
    consumers = consumers - allocation * len(producers)

    print(f"trade{tradeC}")
    print("p", producers)
    print("c", consumers)
    print("a", allocation)
    
    tradeC += 1

    if np.sum(producers) < EPSILON or np.sum(consumers) < EPSILON or allocation < EPSILON:
        shouldContinue = False

et = (time.time_ns() - st) / 1e6
print(f"time: {et}ms")
print("TP", np.sum(producers))
print("TC", np.sum(consumers))
print("TP-TC", np.sum(producers) - np.sum(consumers))