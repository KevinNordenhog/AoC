import sys
import argparse
import importlib.util

def execute_day(year, day_number, run_tests=False):
    module_path = f"{year}/Aoc{day_number}.py"
    spec = importlib.util.spec_from_file_location(f"Aoc{day_number}", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if run_tests:
        if hasattr(module, 'runTest'):
            module.runTest()
        else:
            print(f"No runTest function found in {module_path}")
    else:
        with open(f"{year}/input{day_number}.txt") as file:
            lines = file.read().splitlines()
        print("Part One:", module.partOne(lines))
        print("Part Two:", module.partTwo(lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int, help="Year of AoC")
    parser.add_argument("day", type=int, help="Day number")
    parser.add_argument("--runTests", action="store_true", help="Run with testdata")
    args = parser.parse_args()

    execute_day(args.year, args.day, args.runTests)
