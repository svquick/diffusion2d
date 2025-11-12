# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description

This code solves the diffusion equation over a two dimensional square domain which is at a certain temperature, and a circular disc at its center which is at a higher temperature. The diffusion equation is solved using the finite-difference method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

The following Python tools:
* Python (version >= 3.6)
* pip
* NumPy
* Matplotlib
* build
* twine

## Running this package

You can run the diffusion solver by calling:
```
from diffusion2d import solve

solve(dx=0.1, dy=0.1, D=4.)
```

## Citing

> https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/