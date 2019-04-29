from glob import glob

from process_packages import Request, Buffer, process_requests


def main():
    for test in glob("tests/*[!*.a]"):
        print(f"Running {test}")
        with open(test, "r") as test_fh:
            test_input_buffer_size, test_input_n_requests = [int(val) for val in test_fh.readline().strip().split()]
            test_input_requests = []
            for line in test_fh:
                arrived_at, time_to_process = [int(val) for val in line.strip().split()]
                test_input_requests.append(Request(arrived_at, time_to_process))

        with open(f"{test}.a") as test_answer_fh:
            test_answer = " ".join([str(val.strip()) for val in test_answer_fh.readlines()])

        try:
            buffer = Buffer(test_input_buffer_size)
            responses = process_requests(test_input_requests, buffer)
            test_output = " ".join(["-1" if response.was_dropped else str(response.started_at) for response in responses])
            assert test_output == test_answer
        except AssertionError:
            print(f"AssertionError at {test}:\n    buffer size: {test_input_buffer_size}\n    n_requests:  {test_input_n_requests}\n    requests: {test_input_requests}\n    expected output: {test_answer}\n    actual output: {test_output}")
            break


if __name__ == "__main__":
    main()
