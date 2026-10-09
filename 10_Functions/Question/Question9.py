# def even_generator(limit):
#     even=2;
#     while(even<limit):
#         print(even)
#         even +=2;

# even_generator(7)

# def even_generator(limit):
#     even_numbers = []

#     for i in range(2, limit + 1, 2):
#         even_numbers.append(i)

#     return even_numbers


# print(even_generator(7))

# yield: The yield keyword is used in a generator function to produce values one at a time.
# It pauses the function's execution and saves its state.
# When the next value is requested, the function resumes from where it paused.
# Unlike return, yield does not terminate the function permanently.
# Generators produce values lazily, which can help save memory.


def even_generator(limit):

    for i in range(2, limit + 1, 2):
        yield i


for num in even_generator(7):
    print(num)

#    ┌───────────────────────────┐
#    │   Generator Function      │
#    │   even_generator(7)       │
#    └─────────────┬─────────────┘
#                  ↓
#    ┌───────────────────────────┐
#    │  Inner for loop           │
#    │  i = 2, 4, 6              │
#    └─────────────┬─────────────┘
#                  ↓
#    ┌───────────────────────────┐
#    │       yield i             │
#    │ Produces one value        │
#    │ and pauses execution      │
#    └─────────────┬─────────────┘
#                  ↓
#    ┌───────────────────────────┐
#    │   Outer for loop          │
#    │   num = yielded value     │
#    └─────────────┬─────────────┘
#                  ↓
#    ┌───────────────────────────┐
#    │      print(num)           │
#    │      Output: 2            │
#    └─────────────┬─────────────┘
#                  ↓
#       Request the next value
#                  ↓
#    ┌───────────────────────────┐
#    │   Generator resumes       │
#    │   yield 4 → print(4)      │
#    │   yield 6 → print(6)      │
#    └─────────────┬─────────────┘
#                  ↓
#    ┌───────────────────────────┐
#    │   No more values          │
#    │   Generator stops         │
#    └───────────────────────────┘
