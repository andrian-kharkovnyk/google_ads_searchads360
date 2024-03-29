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

from google.ads.searchads360.v0.enums.types import asset_field_type
from google.ads.searchads360.v0.enums.types import asset_link_status


__protobuf__ = proto.module(
    package='google.ads.searchads360.v0.resources',
    marshal='google.ads.searchads360.v0',
    manifest={
        'AssetGroupAsset',
    },
)


class AssetGroupAsset(proto.Message):
    r"""AssetGroupAsset is the link between an asset and an asset
    group. Adding an AssetGroupAsset links an asset with an asset
    group.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the asset group asset. Asset
            group asset resource name have the form:

            ``customers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}``
        asset_group (str):
            Immutable. The asset group which this asset
            group asset is linking.
        asset (str):
            Immutable. The asset which this asset group
            asset is linking.
        field_type (google.ads.searchads360.v0.enums.types.AssetFieldTypeEnum.AssetFieldType):
            The description of the placement of the asset within the
            asset group. For example: HEADLINE, YOUTUBE_VIDEO etc
        status (google.ads.searchads360.v0.enums.types.AssetLinkStatusEnum.AssetLinkStatus):
            The status of the link between an asset and
            asset group.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_group: str = proto.Field(
        proto.STRING,
        number=2,
    )
    asset: str = proto.Field(
        proto.STRING,
        number=3,
    )
    field_type: asset_field_type.AssetFieldTypeEnum.AssetFieldType = proto.Field(
        proto.ENUM,
        number=4,
        enum=asset_field_type.AssetFieldTypeEnum.AssetFieldType,
    )
    status: asset_link_status.AssetLinkStatusEnum.AssetLinkStatus = proto.Field(
        proto.ENUM,
        number=5,
        enum=asset_link_status.AssetLinkStatusEnum.AssetLinkStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
