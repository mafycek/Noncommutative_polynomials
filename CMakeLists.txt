cmake_minimum_required(VERSION 3.16)
project(zarja)

set(CMAKE_CXX_STANDARD 14)

include_directories(src)

add_executable(polynomials superalgebra-decomposer-3.cpp constants.cpp)
