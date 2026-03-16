1: ### Matmul profile

The profiling results show that most of the runtime is spent in the `matmul` function rather than in the data generation step. The `make_data` function takes about **0.75 s**, mainly to generate the random matrices `X` and `Y`.

In comparison, the `matmul` function takes about **12.03 s**, which dominates the total execution time. The profiling output indicates that the innermost computation `result[i][j] += X[i][k] * Y[k][j]` accounts for about **57.2%** of the runtime, while the loop `for k in range(len(Y))` accounts for about **42.7%**.

This shows that nearly all of the computation time is spent inside the triple nested loops performing the matrix multiplication. Therefore, the main performance bottleneck is the inner multiplication and accumulation step of the matrix multiplication algorithm.

2: ### Euler72 profile

The profiling results show that most of the execution time is spent in the `fast_phi` function, which takes about **0.33 s** in total. Within this function, the call to `factorize(n, primes)` accounts for the majority of the runtime, using about **84.9%** of the total time in `fast_phi`. This indicates that computing the prime factorization for each number is the main performance bottleneck.

The `factorize` function itself takes about **0.18 s**, with most of the time spent in the loop `while(n % p == 0)` and the condition `if(p > sqrt(n))`, which are executed many times when factoring numbers.

The `gen_primes` function takes only about **0.013 s**, so generating the list of primes is relatively inexpensive compared to the repeated factorization work.

3: ### Improved code `matmult_speedier.py` 

The profiling results show that the improved script is significantly faster than the original version from part 1;. In `matmult_speedier.py`, the `matmul_fast` function takes only about **0.018 s**, whereas in part 1; the original `matmul` function took about **12.03 s**. 

The profiling output also shows that the matrix multiplication is now performed entirely by the single line `return X @ Y`. This means the expensive triple nested Python loops seen in part 1; have been replaced by NumPy’s optimized matrix multiplication implementation.

The `make_data` function now takes about **0.143 s**, with most of that time spent generating the random NumPy arrays. Even this setup stage is faster than in part 1;, where data generation took about **0.75 s**.

