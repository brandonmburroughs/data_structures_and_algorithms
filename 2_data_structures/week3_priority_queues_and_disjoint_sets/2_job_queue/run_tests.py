from glob import glob
import sys
import io

from job_queue import JobQueue


def main():
    for test in glob("tests/*[!*.a]"):
        print(f"Running {test}")
        with open(test, "r") as test_fh:
            test_input = test_fh.read().strip()
            sys.stdin = io.StringIO(test_input)
        with open(f"{test}.a") as test_answer_fh:
            test_answer = test_answer_fh.read().strip()

        try:
            job_queue = JobQueue()
            job_queue.solve(write=False)
            test_output = "\n".join(
                [f"{assigned_worker} {start_time}"
                 for assigned_worker, start_time in zip(job_queue.assigned_workers, job_queue.start_times)]
            )
            assert test_output.strip() == test_answer
        except AssertionError:
            print(f"AssertionError at {test}:\n    input: {test_input}\n    expected output: {test_answer}\n    actual output: {test_output}")
            break


if __name__ == "__main__":
    main()
