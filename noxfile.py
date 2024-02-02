# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
#
import os

import nox  # type: ignore


ALL_PYTHON = [
    "3.7",
    "3.8",
    "3.9",
    "3.10",
    "3.11",
]

@nox.session(python=ALL_PYTHON)
def unit(session):
    """Run the unit test suite."""

    session.install('coverage', 'pytest', 'pytest-cov')
    session.install('-e', '.')

    session.run(
        'py.test',
        '--quiet',
        '--cov=google/ads/searchads360.v0/',
        '--cov=tests/',
        '--cov-config=.coveragerc',
        '--cov-report=term',
        '--cov-report=html',
        os.path.join('tests', 'unit', 'gapic', 'searchads360.v0'),
    )


@nox.session(python=ALL_PYTHON)
def mypy(session):
    """Run the type checker."""
    session.install('mypy')
    session.install('.')
    session.run(
        'mypy',
        'google',
    )
