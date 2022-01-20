find_package(GTest 1.10.0 REQUIRED)
include(GoogleTest)

set(TEST test_project)
add_executable(${TEST} TestProject.cpp)
target_link_libraries(${TEST} PRIVATE
    ${PROJECT_NAME}
    GTest::gtest_main
)
gtest_discover_tests(${TEST})
