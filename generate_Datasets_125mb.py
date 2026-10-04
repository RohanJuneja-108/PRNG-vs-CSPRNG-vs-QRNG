import secrets
import time

DATASET_SIZE_MB = 125
CHUNK_SIZE = 1024 * 1024  # 1 MB


def generate_csprng(filename="csprng_dataset_125mb.bin", size_mb=DATASET_SIZE_MB):
    start = time.time()
    print(f"Generating {size_mb} MB CSPRNG data...")
    with open(filename, "wb") as f:
        for _ in range(size_mb):
            f.write(secrets.token_bytes(CHUNK_SIZE))
    print(f"Done in {time.time() - start:.2f}s -> {filename}")


def generate_lcg(
    filename="basic_prng_lcg_125mb.bin", size_mb=DATASET_SIZE_MB, seed=42
):
    start = time.time()
    print(f"Generating {size_mb} MB Basic PRNG (LCG) data...")
    a = 1103515245
    c = 12345
    m = 2**31
    state = seed

    with open(filename, "wb") as f:
        for _ in range(size_mb):
            chunk = bytearray(CHUNK_SIZE)
            for i in range(CHUNK_SIZE):
                state = (a * state + c) % m
                chunk[i] = (state >> 16) & 0xFF
            f.write(chunk)
    print(f"Done in {time.time() - start:.2f}s -> {filename}")


if __name__ == "__main__":
    generate_csprng()
    generate_lcg()