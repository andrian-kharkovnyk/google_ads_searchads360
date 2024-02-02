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
        'AdGroupCriterionStatusEnum',
    },
)


class AdGroupCriterionStatusEnum(proto.Message):
    r"""Message describing AdGroupCriterion statuses.
    """
    class AdGroupCriterionStatus(proto.Enum):
        r"""The possible statuses of an AdGroupCriterion."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        PAUSED = 3
        REMOVED = 4


__all__ = tuple(sorted(__protobuf__.manifest))