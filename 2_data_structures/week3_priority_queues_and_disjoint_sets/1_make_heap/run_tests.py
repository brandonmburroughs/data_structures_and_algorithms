from glob import glob
import sys
import io

from build_heap import HeapBuilder


def main():
    for test in glob("tests/*[!*.a]"):
        print(f"Running {test}")
        with open(test, "r") as test_fh:
            test_input = test_fh.read().strip()
            sys.stdin = io.StringIO(test_input)
        with open(f"{test}.a") as test_answer_fh:
            test_answer = test_answer_fh.read().strip()

        try:
            heap_builder = HeapBuilder()
            heap_builder.Solve(write=False)
            test_output = str(len(heap_builder._swaps)) + "\n" + "\n".join([f"{one} {two}" for one, two in heap_builder._swaps])
            assert test_output.strip() == test_answer
        except AssertionError:
            print(f"AssertionError at {test}:\n    input: {test_input}\n    expected output: {test_answer}\n    actual output: {test_output}")
            break


if __name__ == "__main__":
    main()
