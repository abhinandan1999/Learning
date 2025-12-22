import multiprocessing as mp
import time

import numpy as np


def compute_distances_batch(X_batch: np.ndarray, q: np.ndarray) -> np.ndarray:
    """
    Compute Euclidean distances for a batch of points.
    """
    diff = X_batch[:, None, :] - q[None, :, :]  # (batch_size, num_queries, dim)
    return np.linalg.norm(diff, axis=2)


def split_into_batches(X: np.ndarray, n_batches: int):
    """
    Split X into n nearly equal batches.
    """
    X_splits = np.array_split(X, n_batches, axis=0)
    print(
        f"Number of batches created: {len(X_splits)} each with shape {[batch.shape for batch in X_splits]}"
    )
    return X_splits


def bruteforce_knn_batch_processing(X, q, n_processes):
    start = time.time()

    batches = split_into_batches(X, n_processes)

    with mp.Pool(processes=n_processes) as pool:
        results = pool.starmap(
            compute_distances_batch, [(batch, q) for batch in batches]
        )
        distances = np.concatenate(results)

    print(f"Multiprocessing ({n_processes} processes) took {time.time() - start:.4f}s")
    return distances


if __name__ == "__main__":

    X = np.random.rand(1_000_000, 50)  # 1_000_000 Data Points in 50D

    Y = np.random.rand(10, 50)  # 10 Query Points in 50D

    print(f"Shape of X: {X.shape}")
    print(f"Shape of Y: {Y.shape}")

    distances_batch_multiprocessing = bruteforce_knn_batch_processing(
        X, Y, n_processes=3
    )
    print(f"Shape of distance matrix: {distances_batch_multiprocessing.shape}\n\n")
