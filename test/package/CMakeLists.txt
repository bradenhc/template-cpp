cmake_minimum_required(VERSION 3.20)

project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

find_package(project_template REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example project_template::project_template)
