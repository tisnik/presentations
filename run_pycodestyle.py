# Copyright © 2020 Pavel Tisnovsky
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

"""Simple checker of all Python sources in the given directory (usually repository)."""

from pathlib import Path
from sys import exit
import pycodestyle


def main():
    files = list(Path(".").rglob("*.py"))

    style = pycodestyle.StyleGuide(quiet=False, config_file='setup.cfg')
    result = style.check_files(files)
    print("Total errors:", result.total_errors)
    if result.total_errors > 0:
        exit(1)


if __name__ == "__main__":
    main()
