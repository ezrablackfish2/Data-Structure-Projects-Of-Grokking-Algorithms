import importlib.util
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_problem.py <problem-folder>")
        return
    folder = Path(sys.argv[1])
    solution = folder / "solution.py"
    spec = importlib.util.spec_from_file_location("solution", solution)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print("Loaded", solution)

if __name__ == "__main__":
    main()
