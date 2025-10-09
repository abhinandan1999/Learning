## Libraries
1. memray
2. memory_profiler


### Memray Features
1. Traces every function call so it can accurately represent the call stack, unlike sampling profilers.
2. Also handles native calls in C/C++ libraries so the entire call stack is present in the results.
3. Very Fast
4. Works with Python threads.
5. It can be used from command line and Python API.

### Memray Usecase
1. Analyze allocations in applications to help discover the cause of high memory usage.
2. Find memory leaks.
3. Find hotspots in code which cause a lot of allocations.

### How it works (Coceptually)
1. It intercepts calls to:
    - malloc()
    - calloc()
    - realloc()
    - free()
    - PyObject_New
2. Each Allocation is recorded with a stack trace (Includes both Python-level and C-level frames).
3. Results are stored in .bin file.

### Disadvantages
1. Overhead on huge programs - While efficient, tracing every allocation in memory-intensive apps (GBs of allocations/sec) can produce very large trace files (>GB).
2. Storage space - Output .bin can grow huge for long runs.
3. Visualization rendering time - Flamegraphs for big traces can take several minutes to load.
4. No fine-grained line-level breakdown - It focuses on allocation stacks, not line-by-line memory usage.
5. Requires Python >= 3.8 - No support for older interpreters.

### Platform Supported
1. MacOS and Linux

==================================================================================================================

### Memory Profiler Features
1. Tracks how much memory **each line** of code consumes.
2. It only supports the Python native and cannot measure memory for libraries with C/C++.
3. Supports decorator as well as command line interface
4. It works with IPython and Jupyter notebooks

### Memory Profiler Usecase
1. Small Python functions where you want to see which line grows memory
2. Detecting memory leaks (?)
4. Debugging out-of-memory (OOM) issues

### How it works?
It works by (sampling ?) the (resident set size (RSS) ?) of the process over time using the `psutil` or `ps` command, which gives a good **approximation** of memory usage for each line of Python code.

1. It periodically checks the memory usage of the current Python process (sampling interval default = 0.1s).

2. When a line of code inside a profiled function executes, it records:
   - Current memory usage
   - Incremental difference from the previous line

3. It outputs a detailed report showing per-line memory usage in MiB.

### Disadvantages
1. Sampling-based - Memory values are sampled over time, not exact — small allocations between samples may be missed.
2. Performance overhead - Adds latency due to periodic sampling.
3. Limited to Python memory - Tracks only memory of the Python process — C extensions (like NumPy) may not be precisely tracked.
4. Cannot profile unexecuted code - Works only for lines actually executed.
5. Not suitable for multithreaded / multiprocessing profiling - Each process/thread must be profiled separately.

### Platform Supported
1. MacOS, Linux, Windows
