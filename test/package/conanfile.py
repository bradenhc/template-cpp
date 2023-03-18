####################################################################################################
## Copyright (c) 2022 Braden Hitchcock - MIT License (https://opensource.org/licenses/MIT)        ##
####################################################################################################

import os

from conans import ConanFile, CMake, tools


class ProjectTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            self.run(".%sexample" % os.sep)
