from glob import glob

from tree_height import compute_height


def main():
    for test in glob("tests/*[!*.a]"):
        print(f"Running {test}")
        with open(test, "r") as test_fh:
            test_input_n, test_input_parents = test_fh.readlines()
            test_input_n = int(test_input_n.strip())
            test_input_parents = [int(parent) for parent in test_input_parents.strip().split()]
        with open(f"{test}.a") as test_answer_fh:
            test_answer = test_answer_fh.read().strip()

        try:
            test_output = str(compute_height(test_input_n, test_input_parents))
            assert test_output == test_answer
        except AssertionError:
            print(f"AssertionError at {test}:\n    input n: {test_input_n}\n    input parents:  {test_input_parents}\n    expected output: {test_answer}\n    actual output: {test_output}")
            break


if __name__ == "__main__":
    main()
