import argparse
import time
import traceback
from datetime import datetime, timedelta, timezone
from subprocess import call


def run(filename="filename"):
    try:
        start = time.monotonic_ns()
        call(["python", filename])
        end = time.monotonic_ns()
        print(f"[{(end - start) / 10 ** 6:.3f} ms]")
    except:
        traceback.print_exc()


if __name__ == "__main__":
    now = datetime.now(timezone(timedelta(hours=-5)))
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    args = parser.parse_args()

    module_name = f"py.day{args.day}"
    print(f"----- Day {args.day} -----")
    for i in ("task1", "task2"):
        print(f"--- {i} ---")
        run(f"day{args.day}/{i}.py")
