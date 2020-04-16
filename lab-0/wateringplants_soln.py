"""
You are given a list representing the amount of water
required by some plants. Your water container can hold
only 1000mL (1L) at a time. Your task is to find the
number of times you will need to fill your container in
order to water all the plants. Your container starts
empty, i.e. with 0 mL.

Assume that you can NOT begin watering a plant unless you
have all of the water you need in your container. That
is, if a plant requires 800mL of water, and you only
have 400mL in your container, you MUST refill immediately.
i.e. You can't pour half now, and half after you've refilled.

Hint - you will need a loop, and some variables
"""

containerMax = 800
plants = [120, 250, 250, 150, 420, 250, 300, 750, 180, 450]

container = 0
fills = 0
for plant in plants:
    if plant > container:
        fills += 1
        container = containerMax
    container -= plant

print(fills)
