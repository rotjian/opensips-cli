#!/usr/bin/env python
##
## This file is part of OpenSIPS CLI
## (see https://github.com/OpenSIPS/opensips-cli).
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.
##

"""
Installs OpenSIPS Command Line Interface
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
print(setuptools.find_namespace_packages())

setuptools.setup(
    name = "opensipscli",
    version = "1.0.0",
    author = "OpenSIPS Project",
    author_email = "project@opensips.org",
    description = "OpenSIPS Command Line Interface",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/OpenSIPS/opensips-cli",
    packages = setuptools.find_namespace_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    scripts = [
        "bin/opensips-cli"
    ],
    project_urls = {
        "Source Code": "https://github.com/OpenSIPS/opensips-cli",
        "Issues Tracker": "https://github.com/OpenSIPS/opensips-cli/issues",
    },
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
