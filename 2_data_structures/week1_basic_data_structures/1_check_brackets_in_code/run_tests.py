from glob import glob

from check_brackets import find_mismatch


def main():
    for test in glob("tests/*[!*.a]"):
        with open(test, "r") as test_fh:
            test_input = test_fh.read().strip()
        with open(f"{test}.a") as test_answer_fh:
            test_answer = test_answer_fh.read().strip()

        try:
            test_output = str(find_mismatch(test_input))
            assert test_output == test_answer
        except AssertionError:
            print(f"AssertionError at {test}:\n    input: {test_input}\n    expected output: {test_answer}\n    actual output: {test_output}")
            break
        except:
            print(f"Error at {test}")
            break


if __name__ == "__main__":
    main()
