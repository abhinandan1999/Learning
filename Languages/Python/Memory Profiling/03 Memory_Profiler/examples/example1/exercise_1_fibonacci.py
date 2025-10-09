"""
Memory Profiling Commands (./example1)
1. python -m memory_profiler exercise_1_fibonacci.py (Output is to Standard output) --- Decorator @profile would work even if it is not imported
2. python exercise_1_fibonacci.py (Output is to Standard output) --- Decorator @profile has to be imported (-m memory_profiler is not required)
3. python -m memory_profiler -o output.txt exercise_1_fibonacci.py -- Redirects the output to output.txt file 
   (Make sure to not import profile from memory_profiler import profile)
4. python exercise_1_fibonacci.py -- When Stream is used then don't use -m memory_profiler

To Generate Memory Usage with time and not line by line
3. mprof run python exercise_1_fibonacci.py (mprofile_20251009170023.dat)
   mprof plot

   mprof run -h -- Help on each mprof subcommand can be obtained with the -h flag

4. mprof run --include-children python exercise_1_fibonacci.py
"""
import operator
from functools import reduce
from itertools import chain

from memory_profiler import profile

# @profile(precision=4) # precision 4 specifies the decimal places of memory usage
fp=open('memory_profiler.txt','w+')
@profile(stream=fp) # When Stream is used then don't use -m memory_profiler (python exercise_1_fibonacci.py)
def fibonacci(length):
    # edge cases
    if length < 1:
        return []
    if length == 1:
        return [1]
    if length == 2:
        return [1, 1]

    output = [1, 1]

    for i in range(length - 2):
        output.append(output[i] + output[i + 1])

    return output

@profile(stream=fp)
def generate_fibonacci_hash(length_1, length_2, length_3):
    # We could have used sum(...) here instead of reduce(operator.add, ...),
    # but we choose to use reduce since it yields a more descriptive example
    # of the generated flamegraph for this specific example
    return (
        reduce(
            operator.add,
            chain(fibonacci(length_1), fibonacci(length_2), fibonacci(length_3)),
            0,
        )
        % 10000
    )


if __name__ == "__main__":
    # DO NOT CHANGE
    LENGTH_OF_SEQUENCE_1 = 33_333
    LENGTH_OF_SEQUENCE_2 = 30_000
    LENGTH_OF_SEQUENCE_3 = 34_567
    # DO NOT CHANGE
    generate_fibonacci_hash(
        LENGTH_OF_SEQUENCE_1, LENGTH_OF_SEQUENCE_2, LENGTH_OF_SEQUENCE_3
    )