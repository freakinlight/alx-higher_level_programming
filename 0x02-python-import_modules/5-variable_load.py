#!/usr/bin/python3
import importlib.util

def main():
    spec = importlib.util.spec_from_file_location("variable_load_5", "./variable_load_5.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    print(module.a)

if __name__ == "__main__":
    main()
