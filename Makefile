all: build run

build:
    python3.9 setup.py build_ext --inplace

run:
    python3.9 pep.py
