from glob import glob
import sys

from merging_tables import DisjointSet


def main():
    for test in glob("tests/*[!*.a]"):
        print(f"Running {test}")
        with open(test, "r") as test_fh:
            test_input_n, test_input_m = [int(val) for val in test_fh.readline().strip().split()]
            test_input_lines = [int(val) for val in test_fh.readline().strip().split()]
            test_input_merges = [tuple(map(int, line.strip().split())) for line in test_fh.readlines()]
        with open(f"{test}.a") as test_answer_fh:
            test_answer = test_answer_fh.read().strip()

        try:
            disjoint_set = DisjointSet(test_input_n, test_input_lines)

            test_outputs = []
            for destination, source in test_input_merges:
                disjoint_set.merge(destination - 1, source - 1)
                test_outputs.append(str(disjoint_set.get_max_rows()))

            test_output = "\n".join(test_outputs)
            assert test_output == test_answer
        except AssertionError:
            print(f"AssertionError at {test}:\n    n: {test_input_n}\n    m: {test_input_m}\n    lines: {test_input_lines}\n    merges: {test_input_merges}\n    expected output: {test_answer}\n    actual output: {test_output}")
            break


if __name__ == "__main__":
    main()
