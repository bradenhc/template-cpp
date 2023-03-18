####################################################################################################
## Copyright (c) 2022 Braden Hitchcock - MIT License (https://opensource.org/licenses/MIT)        ##
####################################################################################################
from conans import ConanFile, CMake, tools


class ProjectConan(ConanFile):
    name = "project_template"
    version = "0.1.0"
    description = "<Description of Project here>"

    license = "<Put the package license here>"

    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"

    topics = ("<Put some tag here>", "<here>", "<and here>")

    settings = "os", "compiler", "build_type", "arch"

    options = {"shared": [True, False] }
    default_options = {"shared": False }

    generators = "cmake_find_package"

    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def build_requirements(self):
        self.build_requires("gtest/1.10.0")

    def requirements(self):
        pass

    def _setup_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CONAN_PKG_NAME"] = self.name
        cmake.definitions["CONAN_PKG_VERSION"] = self.version
        return cmake

    def build(self):
        cmake = self._setup_cmake()
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = self._setup_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
