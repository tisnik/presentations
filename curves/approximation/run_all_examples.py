# Copyright © 2021 Pavel Tisnovsky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Script to run all examples found in current directory."""

from os import system
from pathlib import Path
from sys import argv


def main():
    """Find and run all example in current directory."""
    scripts = list(Path(".").rglob("*.py"))

    for script in scripts:
        if str(script) != argv[0]:
            system("python3 {}".format(script))


if __name__ == "__main__":
    main()
