add_library(${PROJECT_NAME} SHARED
    project.cpp
)

target_include_directories(${PROJECT_NAME} PUBLIC
    $<INSTALL_INTERFACE:include>
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
)

set_target_properties(${PROJECT_NAME} PROPERTIES
    POSITION_INDEPENDENT_CODE ON
)

install(TARGETS ${PROJECT_NAME})
