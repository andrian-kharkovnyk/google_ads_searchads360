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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore


__protobuf__ = proto.module(
    package='google.ads.searchads360.v0.enums',
    marshal='google.ads.searchads360.v0',
    manifest={
        'AssetEngineStatusEnum',
    },
)


class AssetEngineStatusEnum(proto.Message):
    r"""Container for enum describing possible Asset engine statuses.
    """
    class AssetEngineStatus(proto.Enum):
        r"""Next ID = 11"""
        UNSPECIFIED = 0
        UNKNOWN = 1
        SERVING = 2
        SERVING_LIMITED = 3
        DISAPPROVED = 4
        DISABLED = 5
        REMOVED = 6


__all__ = tuple(sorted(__protobuf__.manifest))
