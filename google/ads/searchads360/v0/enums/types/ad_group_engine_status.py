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
        'AdGroupEngineStatusEnum',
    },
)


class AdGroupEngineStatusEnum(proto.Message):
    r"""Container for enum describing possible AdGroup engine
    statuses.

    """
    class AdGroupEngineStatus(proto.Enum):
        r"""Status of the ad group engine."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_ELIGIBLE = 2
        AD_GROUP_EXPIRED = 3
        AD_GROUP_REMOVED = 4
        AD_GROUP_DRAFT = 5
        AD_GROUP_PAUSED = 6
        AD_GROUP_SERVING = 7
        AD_GROUP_SUBMITTED = 8
        CAMPAIGN_PAUSED = 9
        ACCOUNT_PAUSED = 10


__all__ = tuple(sorted(__protobuf__.manifest))
