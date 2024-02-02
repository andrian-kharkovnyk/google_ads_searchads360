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
import pytest


def test_module_level_imports():
    expected_names = []

    # Message types
    from google.ads.searchads360 import AccountStatusEnum
    expected_names.append(AccountStatusEnum.__name__)
    from google.ads.searchads360 import AccountTypeEnum
    expected_names.append(AccountTypeEnum.__name__)
    from google.ads.searchads360 import AdGroupAdEngineStatusEnum
    expected_names.append(AdGroupAdEngineStatusEnum.__name__)
    from google.ads.searchads360 import AdGroupAdRotationModeEnum
    expected_names.append(AdGroupAdRotationModeEnum.__name__)
    from google.ads.searchads360 import AdGroupAdStatusEnum
    expected_names.append(AdGroupAdStatusEnum.__name__)
    from google.ads.searchads360 import AdGroupCriterionEngineStatusEnum
    expected_names.append(AdGroupCriterionEngineStatusEnum.__name__)
    from google.ads.searchads360 import AdGroupCriterionStatusEnum
    expected_names.append(AdGroupCriterionStatusEnum.__name__)
    from google.ads.searchads360 import AdGroupEngineStatusEnum
    expected_names.append(AdGroupEngineStatusEnum.__name__)
    from google.ads.searchads360 import AdGroupStatusEnum
    expected_names.append(AdGroupStatusEnum.__name__)
    from google.ads.searchads360 import AdGroupTypeEnum
    expected_names.append(AdGroupTypeEnum.__name__)
    from google.ads.searchads360 import AdNetworkTypeEnum
    expected_names.append(AdNetworkTypeEnum.__name__)
    from google.ads.searchads360 import AdServingOptimizationStatusEnum
    expected_names.append(AdServingOptimizationStatusEnum.__name__)
    from google.ads.searchads360 import AdStrengthEnum
    expected_names.append(AdStrengthEnum.__name__)
    from google.ads.searchads360 import AdTypeEnum
    expected_names.append(AdTypeEnum.__name__)
    from google.ads.searchads360 import AdvertisingChannelSubTypeEnum
    expected_names.append(AdvertisingChannelSubTypeEnum.__name__)
    from google.ads.searchads360 import AdvertisingChannelTypeEnum
    expected_names.append(AdvertisingChannelTypeEnum.__name__)
    from google.ads.searchads360 import AgeRangeTypeEnum
    expected_names.append(AgeRangeTypeEnum.__name__)
    from google.ads.searchads360 import AssetEngineStatusEnum
    expected_names.append(AssetEngineStatusEnum.__name__)
    from google.ads.searchads360 import AssetFieldTypeEnum
    expected_names.append(AssetFieldTypeEnum.__name__)
    from google.ads.searchads360 import AssetGroupStatusEnum
    expected_names.append(AssetGroupStatusEnum.__name__)
    from google.ads.searchads360 import AssetLinkStatusEnum
    expected_names.append(AssetLinkStatusEnum.__name__)
    from google.ads.searchads360 import AssetSetAssetStatusEnum
    expected_names.append(AssetSetAssetStatusEnum.__name__)
    from google.ads.searchads360 import AssetSetLinkStatusEnum
    expected_names.append(AssetSetLinkStatusEnum.__name__)
    from google.ads.searchads360 import AssetStatusEnum
    expected_names.append(AssetStatusEnum.__name__)
    from google.ads.searchads360 import AssetTypeEnum
    expected_names.append(AssetTypeEnum.__name__)
    from google.ads.searchads360 import AttributionModelEnum
    expected_names.append(AttributionModelEnum.__name__)
    from google.ads.searchads360 import AttributionTypeEnum
    expected_names.append(AttributionTypeEnum.__name__)
    from google.ads.searchads360 import BiddingStrategyStatusEnum
    expected_names.append(BiddingStrategyStatusEnum.__name__)
    from google.ads.searchads360 import BiddingStrategySystemStatusEnum
    expected_names.append(BiddingStrategySystemStatusEnum.__name__)
    from google.ads.searchads360 import BiddingStrategyTypeEnum
    expected_names.append(BiddingStrategyTypeEnum.__name__)
    from google.ads.searchads360 import BudgetDeliveryMethodEnum
    expected_names.append(BudgetDeliveryMethodEnum.__name__)
    from google.ads.searchads360 import BudgetPeriodEnum
    expected_names.append(BudgetPeriodEnum.__name__)
    from google.ads.searchads360 import CallConversionReportingStateEnum
    expected_names.append(CallConversionReportingStateEnum.__name__)
    from google.ads.searchads360 import CallToActionTypeEnum
    expected_names.append(CallToActionTypeEnum.__name__)
    from google.ads.searchads360 import CampaignCriterionStatusEnum
    expected_names.append(CampaignCriterionStatusEnum.__name__)
    from google.ads.searchads360 import CampaignServingStatusEnum
    expected_names.append(CampaignServingStatusEnum.__name__)
    from google.ads.searchads360 import CampaignStatusEnum
    expected_names.append(CampaignStatusEnum.__name__)
    from google.ads.searchads360 import ConversionActionCategoryEnum
    expected_names.append(ConversionActionCategoryEnum.__name__)
    from google.ads.searchads360 import ConversionActionStatusEnum
    expected_names.append(ConversionActionStatusEnum.__name__)
    from google.ads.searchads360 import ConversionActionTypeEnum
    expected_names.append(ConversionActionTypeEnum.__name__)
    from google.ads.searchads360 import ConversionStatusEnum
    expected_names.append(ConversionStatusEnum.__name__)
    from google.ads.searchads360 import ConversionTrackingStatusEnum
    expected_names.append(ConversionTrackingStatusEnum.__name__)
    from google.ads.searchads360 import CriterionTypeEnum
    expected_names.append(CriterionTypeEnum.__name__)
    from google.ads.searchads360 import CustomColumnValueTypeEnum
    expected_names.append(CustomColumnValueTypeEnum.__name__)
    from google.ads.searchads360 import CustomerStatusEnum
    expected_names.append(CustomerStatusEnum.__name__)
    from google.ads.searchads360 import DataDrivenModelStatusEnum
    expected_names.append(DataDrivenModelStatusEnum.__name__)
    from google.ads.searchads360 import DayOfWeekEnum
    expected_names.append(DayOfWeekEnum.__name__)
    from google.ads.searchads360 import DeviceEnum
    expected_names.append(DeviceEnum.__name__)
    from google.ads.searchads360 import GenderTypeEnum
    expected_names.append(GenderTypeEnum.__name__)
    from google.ads.searchads360 import GeoTargetConstantStatusEnum
    expected_names.append(GeoTargetConstantStatusEnum.__name__)
    from google.ads.searchads360 import InteractionEventTypeEnum
    expected_names.append(InteractionEventTypeEnum.__name__)
    from google.ads.searchads360 import KeywordMatchTypeEnum
    expected_names.append(KeywordMatchTypeEnum.__name__)
    from google.ads.searchads360 import LabelStatusEnum
    expected_names.append(LabelStatusEnum.__name__)
    from google.ads.searchads360 import ListingGroupFilterBiddingCategoryLevelEnum
    expected_names.append(ListingGroupFilterBiddingCategoryLevelEnum.__name__)
    from google.ads.searchads360 import ListingGroupFilterCustomAttributeIndexEnum
    expected_names.append(ListingGroupFilterCustomAttributeIndexEnum.__name__)
    from google.ads.searchads360 import ListingGroupFilterProductChannelEnum
    expected_names.append(ListingGroupFilterProductChannelEnum.__name__)
    from google.ads.searchads360 import ListingGroupFilterProductConditionEnum
    expected_names.append(ListingGroupFilterProductConditionEnum.__name__)
    from google.ads.searchads360 import ListingGroupFilterProductTypeLevelEnum
    expected_names.append(ListingGroupFilterProductTypeLevelEnum.__name__)
    from google.ads.searchads360 import ListingGroupFilterTypeEnum
    expected_names.append(ListingGroupFilterTypeEnum.__name__)
    from google.ads.searchads360 import ListingGroupFilterVerticalEnum
    expected_names.append(ListingGroupFilterVerticalEnum.__name__)
    from google.ads.searchads360 import ListingGroupTypeEnum
    expected_names.append(ListingGroupTypeEnum.__name__)
    from google.ads.searchads360 import LocationGroupRadiusUnitsEnum
    expected_names.append(LocationGroupRadiusUnitsEnum.__name__)
    from google.ads.searchads360 import LocationOwnershipTypeEnum
    expected_names.append(LocationOwnershipTypeEnum.__name__)
    from google.ads.searchads360 import ManagerLinkStatusEnum
    expected_names.append(ManagerLinkStatusEnum.__name__)
    from google.ads.searchads360 import MimeTypeEnum
    expected_names.append(MimeTypeEnum.__name__)
    from google.ads.searchads360 import MinuteOfHourEnum
    expected_names.append(MinuteOfHourEnum.__name__)
    from google.ads.searchads360 import MobileAppVendorEnum
    expected_names.append(MobileAppVendorEnum.__name__)
    from google.ads.searchads360 import NegativeGeoTargetTypeEnum
    expected_names.append(NegativeGeoTargetTypeEnum.__name__)
    from google.ads.searchads360 import OptimizationGoalTypeEnum
    expected_names.append(OptimizationGoalTypeEnum.__name__)
    from google.ads.searchads360 import PositiveGeoTargetTypeEnum
    expected_names.append(PositiveGeoTargetTypeEnum.__name__)
    from google.ads.searchads360 import ProductBiddingCategoryLevelEnum
    expected_names.append(ProductBiddingCategoryLevelEnum.__name__)
    from google.ads.searchads360 import ProductBiddingCategoryStatusEnum
    expected_names.append(ProductBiddingCategoryStatusEnum.__name__)
    from google.ads.searchads360 import ProductChannelEnum
    expected_names.append(ProductChannelEnum.__name__)
    from google.ads.searchads360 import ProductChannelExclusivityEnum
    expected_names.append(ProductChannelExclusivityEnum.__name__)
    from google.ads.searchads360 import ProductConditionEnum
    expected_names.append(ProductConditionEnum.__name__)
    from google.ads.searchads360 import QualityScoreBucketEnum
    expected_names.append(QualityScoreBucketEnum.__name__)
    from google.ads.searchads360 import SearchAds360FieldCategoryEnum
    expected_names.append(SearchAds360FieldCategoryEnum.__name__)
    from google.ads.searchads360 import SearchAds360FieldDataTypeEnum
    expected_names.append(SearchAds360FieldDataTypeEnum.__name__)
    from google.ads.searchads360 import ServedAssetFieldTypeEnum
    expected_names.append(ServedAssetFieldTypeEnum.__name__)
    from google.ads.searchads360 import SummaryRowSettingEnum
    expected_names.append(SummaryRowSettingEnum.__name__)
    from google.ads.searchads360 import TargetImpressionShareLocationEnum
    expected_names.append(TargetImpressionShareLocationEnum.__name__)
    from google.ads.searchads360 import TargetingDimensionEnum
    expected_names.append(TargetingDimensionEnum.__name__)
    from google.ads.searchads360 import UserListTypeEnum
    expected_names.append(UserListTypeEnum.__name__)
    from google.ads.searchads360 import WebpageConditionOperandEnum
    expected_names.append(WebpageConditionOperandEnum.__name__)
    from google.ads.searchads360 import WebpageConditionOperatorEnum
    expected_names.append(WebpageConditionOperatorEnum.__name__)
    from google.ads.searchads360 import SearchAds360TextAdInfo
    expected_names.append(SearchAds360TextAdInfo.__name__)
    from google.ads.searchads360 import SearchAds360ExpandedTextAdInfo
    expected_names.append(SearchAds360ExpandedTextAdInfo.__name__)
    from google.ads.searchads360 import SearchAds360ExpandedDynamicSearchAdInfo
    expected_names.append(SearchAds360ExpandedDynamicSearchAdInfo.__name__)
    from google.ads.searchads360 import SearchAds360ProductAdInfo
    expected_names.append(SearchAds360ProductAdInfo.__name__)
    from google.ads.searchads360 import SearchAds360ResponsiveSearchAdInfo
    expected_names.append(SearchAds360ResponsiveSearchAdInfo.__name__)
    from google.ads.searchads360 import KeywordInfo
    expected_names.append(KeywordInfo.__name__)
    from google.ads.searchads360 import LocationInfo
    expected_names.append(LocationInfo.__name__)
    from google.ads.searchads360 import DeviceInfo
    expected_names.append(DeviceInfo.__name__)
    from google.ads.searchads360 import ListingGroupInfo
    expected_names.append(ListingGroupInfo.__name__)
    from google.ads.searchads360 import AdScheduleInfo
    expected_names.append(AdScheduleInfo.__name__)
    from google.ads.searchads360 import AgeRangeInfo
    expected_names.append(AgeRangeInfo.__name__)
    from google.ads.searchads360 import GenderInfo
    expected_names.append(GenderInfo.__name__)
    from google.ads.searchads360 import UserListInfo
    expected_names.append(UserListInfo.__name__)
    from google.ads.searchads360 import LanguageInfo
    expected_names.append(LanguageInfo.__name__)
    from google.ads.searchads360 import WebpageInfo
    expected_names.append(WebpageInfo.__name__)
    from google.ads.searchads360 import WebpageConditionInfo
    expected_names.append(WebpageConditionInfo.__name__)
    from google.ads.searchads360 import LocationGroupInfo
    expected_names.append(LocationGroupInfo.__name__)
    from google.ads.searchads360 import AudienceInfo
    expected_names.append(AudienceInfo.__name__)
    from google.ads.searchads360 import YoutubeVideoAsset
    expected_names.append(YoutubeVideoAsset.__name__)
    from google.ads.searchads360 import ImageAsset
    expected_names.append(ImageAsset.__name__)
    from google.ads.searchads360 import ImageDimension
    expected_names.append(ImageDimension.__name__)
    from google.ads.searchads360 import TextAsset
    expected_names.append(TextAsset.__name__)
    from google.ads.searchads360 import UnifiedCalloutAsset
    expected_names.append(UnifiedCalloutAsset.__name__)
    from google.ads.searchads360 import UnifiedSitelinkAsset
    expected_names.append(UnifiedSitelinkAsset.__name__)
    from google.ads.searchads360 import UnifiedPageFeedAsset
    expected_names.append(UnifiedPageFeedAsset.__name__)
    from google.ads.searchads360 import MobileAppAsset
    expected_names.append(MobileAppAsset.__name__)
    from google.ads.searchads360 import UnifiedCallAsset
    expected_names.append(UnifiedCallAsset.__name__)
    from google.ads.searchads360 import CallToActionAsset
    expected_names.append(CallToActionAsset.__name__)
    from google.ads.searchads360 import UnifiedLocationAsset
    expected_names.append(UnifiedLocationAsset.__name__)
    from google.ads.searchads360 import BusinessProfileLocation
    expected_names.append(BusinessProfileLocation.__name__)
    from google.ads.searchads360 import AssetUsage
    expected_names.append(AssetUsage.__name__)
    from google.ads.searchads360 import EnhancedCpc
    expected_names.append(EnhancedCpc.__name__)
    from google.ads.searchads360 import ManualCpa
    expected_names.append(ManualCpa.__name__)
    from google.ads.searchads360 import ManualCpc
    expected_names.append(ManualCpc.__name__)
    from google.ads.searchads360 import ManualCpm
    expected_names.append(ManualCpm.__name__)
    from google.ads.searchads360 import MaximizeConversions
    expected_names.append(MaximizeConversions.__name__)
    from google.ads.searchads360 import MaximizeConversionValue
    expected_names.append(MaximizeConversionValue.__name__)
    from google.ads.searchads360 import TargetCpa
    expected_names.append(TargetCpa.__name__)
    from google.ads.searchads360 import TargetCpm
    expected_names.append(TargetCpm.__name__)
    from google.ads.searchads360 import TargetImpressionShare
    expected_names.append(TargetImpressionShare.__name__)
    from google.ads.searchads360 import TargetOutrankShare
    expected_names.append(TargetOutrankShare.__name__)
    from google.ads.searchads360 import TargetRoas
    expected_names.append(TargetRoas.__name__)
    from google.ads.searchads360 import TargetSpend
    expected_names.append(TargetSpend.__name__)
    from google.ads.searchads360 import PercentCpc
    expected_names.append(PercentCpc.__name__)
    from google.ads.searchads360 import CustomParameter
    expected_names.append(CustomParameter.__name__)
    from google.ads.searchads360 import FrequencyCapEntry
    expected_names.append(FrequencyCapEntry.__name__)
    from google.ads.searchads360 import Metrics
    expected_names.append(Metrics.__name__)
    from google.ads.searchads360 import RealTimeBiddingSetting
    expected_names.append(RealTimeBiddingSetting.__name__)
    from google.ads.searchads360 import Segments
    expected_names.append(Segments.__name__)
    from google.ads.searchads360 import Keyword
    expected_names.append(Keyword.__name__)
    from google.ads.searchads360 import AssetInteractionTarget
    expected_names.append(AssetInteractionTarget.__name__)
    from google.ads.searchads360 import TargetingSetting
    expected_names.append(TargetingSetting.__name__)
    from google.ads.searchads360 import TargetRestriction
    expected_names.append(TargetRestriction.__name__)
    from google.ads.searchads360 import TextLabel
    expected_names.append(TextLabel.__name__)
    from google.ads.searchads360 import Value
    expected_names.append(Value.__name__)
    from google.ads.searchads360 import Ad
    expected_names.append(Ad.__name__)
    from google.ads.searchads360 import AdGroup
    expected_names.append(AdGroup.__name__)
    from google.ads.searchads360 import AdGroupAd
    expected_names.append(AdGroupAd.__name__)
    from google.ads.searchads360 import AdGroupAdLabel
    expected_names.append(AdGroupAdLabel.__name__)
    from google.ads.searchads360 import AdGroupAsset
    expected_names.append(AdGroupAsset.__name__)
    from google.ads.searchads360 import AdGroupAssetSet
    expected_names.append(AdGroupAssetSet.__name__)
    from google.ads.searchads360 import AdGroupAudienceView
    expected_names.append(AdGroupAudienceView.__name__)
    from google.ads.searchads360 import AdGroupBidModifier
    expected_names.append(AdGroupBidModifier.__name__)
    from google.ads.searchads360 import AdGroupCriterion
    expected_names.append(AdGroupCriterion.__name__)
    from google.ads.searchads360 import AdGroupCriterionLabel
    expected_names.append(AdGroupCriterionLabel.__name__)
    from google.ads.searchads360 import AdGroupLabel
    expected_names.append(AdGroupLabel.__name__)
    from google.ads.searchads360 import AgeRangeView
    expected_names.append(AgeRangeView.__name__)
    from google.ads.searchads360 import Asset
    expected_names.append(Asset.__name__)
    from google.ads.searchads360 import AssetGroup
    expected_names.append(AssetGroup.__name__)
    from google.ads.searchads360 import AssetGroupAsset
    expected_names.append(AssetGroupAsset.__name__)
    from google.ads.searchads360 import AssetGroupListingGroupFilter
    expected_names.append(AssetGroupListingGroupFilter.__name__)
    from google.ads.searchads360 import ListingGroupFilterDimensionPath
    expected_names.append(ListingGroupFilterDimensionPath.__name__)
    from google.ads.searchads360 import ListingGroupFilterDimension
    expected_names.append(ListingGroupFilterDimension.__name__)
    from google.ads.searchads360 import AssetGroupSignal
    expected_names.append(AssetGroupSignal.__name__)
    from google.ads.searchads360 import AssetGroupTopCombinationView
    expected_names.append(AssetGroupTopCombinationView.__name__)
    from google.ads.searchads360 import AssetGroupAssetCombinationData
    expected_names.append(AssetGroupAssetCombinationData.__name__)
    from google.ads.searchads360 import AssetSet
    expected_names.append(AssetSet.__name__)
    from google.ads.searchads360 import AssetSetAsset
    expected_names.append(AssetSetAsset.__name__)
    from google.ads.searchads360 import Audience
    expected_names.append(Audience.__name__)
    from google.ads.searchads360 import BiddingStrategy
    expected_names.append(BiddingStrategy.__name__)
    from google.ads.searchads360 import Campaign
    expected_names.append(Campaign.__name__)
    from google.ads.searchads360 import CampaignAsset
    expected_names.append(CampaignAsset.__name__)
    from google.ads.searchads360 import CampaignAssetSet
    expected_names.append(CampaignAssetSet.__name__)
    from google.ads.searchads360 import CampaignAudienceView
    expected_names.append(CampaignAudienceView.__name__)
    from google.ads.searchads360 import CampaignBudget
    expected_names.append(CampaignBudget.__name__)
    from google.ads.searchads360 import CampaignCriterion
    expected_names.append(CampaignCriterion.__name__)
    from google.ads.searchads360 import CampaignLabel
    expected_names.append(CampaignLabel.__name__)
    from google.ads.searchads360 import CartDataSalesView
    expected_names.append(CartDataSalesView.__name__)
    from google.ads.searchads360 import Conversion
    expected_names.append(Conversion.__name__)
    from google.ads.searchads360 import ConversionAction
    expected_names.append(ConversionAction.__name__)
    from google.ads.searchads360 import CustomColumn
    expected_names.append(CustomColumn.__name__)
    from google.ads.searchads360 import Customer
    expected_names.append(Customer.__name__)
    from google.ads.searchads360 import ConversionTrackingSetting
    expected_names.append(ConversionTrackingSetting.__name__)
    from google.ads.searchads360 import DoubleClickCampaignManagerSetting
    expected_names.append(DoubleClickCampaignManagerSetting.__name__)
    from google.ads.searchads360 import CustomerAsset
    expected_names.append(CustomerAsset.__name__)
    from google.ads.searchads360 import CustomerAssetSet
    expected_names.append(CustomerAssetSet.__name__)
    from google.ads.searchads360 import CustomerClient
    expected_names.append(CustomerClient.__name__)
    from google.ads.searchads360 import CustomerManagerLink
    expected_names.append(CustomerManagerLink.__name__)
    from google.ads.searchads360 import DynamicSearchAdsSearchTermView
    expected_names.append(DynamicSearchAdsSearchTermView.__name__)
    from google.ads.searchads360 import GenderView
    expected_names.append(GenderView.__name__)
    from google.ads.searchads360 import GeoTargetConstant
    expected_names.append(GeoTargetConstant.__name__)
    from google.ads.searchads360 import KeywordView
    expected_names.append(KeywordView.__name__)
    from google.ads.searchads360 import Label
    expected_names.append(Label.__name__)
    from google.ads.searchads360 import LanguageConstant
    expected_names.append(LanguageConstant.__name__)
    from google.ads.searchads360 import LocationView
    expected_names.append(LocationView.__name__)
    from google.ads.searchads360 import ProductBiddingCategoryConstant
    expected_names.append(ProductBiddingCategoryConstant.__name__)
    from google.ads.searchads360 import ProductGroupView
    expected_names.append(ProductGroupView.__name__)
    from google.ads.searchads360 import SearchAds360Field
    expected_names.append(SearchAds360Field.__name__)
    from google.ads.searchads360 import ShoppingPerformanceView
    expected_names.append(ShoppingPerformanceView.__name__)
    from google.ads.searchads360 import UserList
    expected_names.append(UserList.__name__)
    from google.ads.searchads360 import Visit
    expected_names.append(Visit.__name__)
    from google.ads.searchads360 import WebpageView
    expected_names.append(WebpageView.__name__)
    from google.ads.searchads360 import GetCustomColumnRequest
    expected_names.append(GetCustomColumnRequest.__name__)
    from google.ads.searchads360 import ListCustomColumnsRequest
    expected_names.append(ListCustomColumnsRequest.__name__)
    from google.ads.searchads360 import ListCustomColumnsResponse
    expected_names.append(ListCustomColumnsResponse.__name__)
    from google.ads.searchads360 import ListAccessibleCustomersRequest
    expected_names.append(ListAccessibleCustomersRequest.__name__)
    from google.ads.searchads360 import ListAccessibleCustomersResponse
    expected_names.append(ListAccessibleCustomersResponse.__name__)
    from google.ads.searchads360 import GetSearchAds360FieldRequest
    expected_names.append(GetSearchAds360FieldRequest.__name__)
    from google.ads.searchads360 import SearchSearchAds360FieldsRequest
    expected_names.append(SearchSearchAds360FieldsRequest.__name__)
    from google.ads.searchads360 import SearchSearchAds360FieldsResponse
    expected_names.append(SearchSearchAds360FieldsResponse.__name__)
    from google.ads.searchads360 import SearchSearchAds360Request
    expected_names.append(SearchSearchAds360Request.__name__)
    from google.ads.searchads360 import SearchSearchAds360Response
    expected_names.append(SearchSearchAds360Response.__name__)
    from google.ads.searchads360 import SearchSearchAds360StreamRequest
    expected_names.append(SearchSearchAds360StreamRequest.__name__)
    from google.ads.searchads360 import SearchSearchAds360StreamResponse
    expected_names.append(SearchSearchAds360StreamResponse.__name__)
    from google.ads.searchads360 import SearchAds360Row
    expected_names.append(SearchAds360Row.__name__)
    from google.ads.searchads360 import CustomColumnHeader
    expected_names.append(CustomColumnHeader.__name__)

    # Client and transport classes
    from google.ads.searchads360 import SearchAds360ServiceClient
    expected_names.append(SearchAds360ServiceClient.__name__)
    from google.ads.searchads360 import SearchAds360ServiceTransport
    expected_names.append(SearchAds360ServiceTransport.__name__)
    from google.ads.searchads360 import SearchAds360ServiceGrpcTransport
    expected_names.append(SearchAds360ServiceGrpcTransport.__name__)
    from google.ads.searchads360 import SearchAds360FieldServiceClient
    expected_names.append(SearchAds360FieldServiceClient.__name__)
    from google.ads.searchads360 import SearchAds360FieldServiceTransport
    expected_names.append(SearchAds360FieldServiceTransport.__name__)
    from google.ads.searchads360 import SearchAds360FieldServiceGrpcTransport
    expected_names.append(SearchAds360FieldServiceGrpcTransport.__name__)
    from google.ads.searchads360 import CustomerServiceClient
    expected_names.append(CustomerServiceClient.__name__)
    from google.ads.searchads360 import CustomerServiceTransport
    expected_names.append(CustomerServiceTransport.__name__)
    from google.ads.searchads360 import CustomerServiceGrpcTransport
    expected_names.append(CustomerServiceGrpcTransport.__name__)
    from google.ads.searchads360 import CustomColumnServiceClient
    expected_names.append(CustomColumnServiceClient.__name__)
    from google.ads.searchads360 import CustomColumnServiceTransport
    expected_names.append(CustomColumnServiceTransport.__name__)
    from google.ads.searchads360 import CustomColumnServiceGrpcTransport
    expected_names.append(CustomColumnServiceGrpcTransport.__name__)

    expected_names.sort()
    from google.ads import searchads360
    actual_names = dir(searchads360)
    assert expected_names == actual_names

    # Verify the logic for handling non-existant names
    with pytest.raises(ImportError):
        from google.ads.searchads360 import GiantSquid


def test_versionsed_module_level_imports():
    expected_names = []

    # Message types
    from google.ads.searchads360.v0 import AccountStatusEnum
    expected_names.append(AccountStatusEnum.__name__)
    from google.ads.searchads360.v0 import AccountTypeEnum
    expected_names.append(AccountTypeEnum.__name__)
    from google.ads.searchads360.v0 import AdGroupAdEngineStatusEnum
    expected_names.append(AdGroupAdEngineStatusEnum.__name__)
    from google.ads.searchads360.v0 import AdGroupAdRotationModeEnum
    expected_names.append(AdGroupAdRotationModeEnum.__name__)
    from google.ads.searchads360.v0 import AdGroupAdStatusEnum
    expected_names.append(AdGroupAdStatusEnum.__name__)
    from google.ads.searchads360.v0 import AdGroupCriterionEngineStatusEnum
    expected_names.append(AdGroupCriterionEngineStatusEnum.__name__)
    from google.ads.searchads360.v0 import AdGroupCriterionStatusEnum
    expected_names.append(AdGroupCriterionStatusEnum.__name__)
    from google.ads.searchads360.v0 import AdGroupEngineStatusEnum
    expected_names.append(AdGroupEngineStatusEnum.__name__)
    from google.ads.searchads360.v0 import AdGroupStatusEnum
    expected_names.append(AdGroupStatusEnum.__name__)
    from google.ads.searchads360.v0 import AdGroupTypeEnum
    expected_names.append(AdGroupTypeEnum.__name__)
    from google.ads.searchads360.v0 import AdNetworkTypeEnum
    expected_names.append(AdNetworkTypeEnum.__name__)
    from google.ads.searchads360.v0 import AdServingOptimizationStatusEnum
    expected_names.append(AdServingOptimizationStatusEnum.__name__)
    from google.ads.searchads360.v0 import AdStrengthEnum
    expected_names.append(AdStrengthEnum.__name__)
    from google.ads.searchads360.v0 import AdTypeEnum
    expected_names.append(AdTypeEnum.__name__)
    from google.ads.searchads360.v0 import AdvertisingChannelSubTypeEnum
    expected_names.append(AdvertisingChannelSubTypeEnum.__name__)
    from google.ads.searchads360.v0 import AdvertisingChannelTypeEnum
    expected_names.append(AdvertisingChannelTypeEnum.__name__)
    from google.ads.searchads360.v0 import AgeRangeTypeEnum
    expected_names.append(AgeRangeTypeEnum.__name__)
    from google.ads.searchads360.v0 import AssetEngineStatusEnum
    expected_names.append(AssetEngineStatusEnum.__name__)
    from google.ads.searchads360.v0 import AssetFieldTypeEnum
    expected_names.append(AssetFieldTypeEnum.__name__)
    from google.ads.searchads360.v0 import AssetGroupStatusEnum
    expected_names.append(AssetGroupStatusEnum.__name__)
    from google.ads.searchads360.v0 import AssetLinkStatusEnum
    expected_names.append(AssetLinkStatusEnum.__name__)
    from google.ads.searchads360.v0 import AssetSetAssetStatusEnum
    expected_names.append(AssetSetAssetStatusEnum.__name__)
    from google.ads.searchads360.v0 import AssetSetLinkStatusEnum
    expected_names.append(AssetSetLinkStatusEnum.__name__)
    from google.ads.searchads360.v0 import AssetStatusEnum
    expected_names.append(AssetStatusEnum.__name__)
    from google.ads.searchads360.v0 import AssetTypeEnum
    expected_names.append(AssetTypeEnum.__name__)
    from google.ads.searchads360.v0 import AttributionModelEnum
    expected_names.append(AttributionModelEnum.__name__)
    from google.ads.searchads360.v0 import AttributionTypeEnum
    expected_names.append(AttributionTypeEnum.__name__)
    from google.ads.searchads360.v0 import BiddingStrategyStatusEnum
    expected_names.append(BiddingStrategyStatusEnum.__name__)
    from google.ads.searchads360.v0 import BiddingStrategySystemStatusEnum
    expected_names.append(BiddingStrategySystemStatusEnum.__name__)
    from google.ads.searchads360.v0 import BiddingStrategyTypeEnum
    expected_names.append(BiddingStrategyTypeEnum.__name__)
    from google.ads.searchads360.v0 import BudgetDeliveryMethodEnum
    expected_names.append(BudgetDeliveryMethodEnum.__name__)
    from google.ads.searchads360.v0 import BudgetPeriodEnum
    expected_names.append(BudgetPeriodEnum.__name__)
    from google.ads.searchads360.v0 import CallConversionReportingStateEnum
    expected_names.append(CallConversionReportingStateEnum.__name__)
    from google.ads.searchads360.v0 import CallToActionTypeEnum
    expected_names.append(CallToActionTypeEnum.__name__)
    from google.ads.searchads360.v0 import CampaignCriterionStatusEnum
    expected_names.append(CampaignCriterionStatusEnum.__name__)
    from google.ads.searchads360.v0 import CampaignServingStatusEnum
    expected_names.append(CampaignServingStatusEnum.__name__)
    from google.ads.searchads360.v0 import CampaignStatusEnum
    expected_names.append(CampaignStatusEnum.__name__)
    from google.ads.searchads360.v0 import ConversionActionCategoryEnum
    expected_names.append(ConversionActionCategoryEnum.__name__)
    from google.ads.searchads360.v0 import ConversionActionStatusEnum
    expected_names.append(ConversionActionStatusEnum.__name__)
    from google.ads.searchads360.v0 import ConversionActionTypeEnum
    expected_names.append(ConversionActionTypeEnum.__name__)
    from google.ads.searchads360.v0 import ConversionStatusEnum
    expected_names.append(ConversionStatusEnum.__name__)
    from google.ads.searchads360.v0 import ConversionTrackingStatusEnum
    expected_names.append(ConversionTrackingStatusEnum.__name__)
    from google.ads.searchads360.v0 import CriterionTypeEnum
    expected_names.append(CriterionTypeEnum.__name__)
    from google.ads.searchads360.v0 import CustomColumnValueTypeEnum
    expected_names.append(CustomColumnValueTypeEnum.__name__)
    from google.ads.searchads360.v0 import CustomerStatusEnum
    expected_names.append(CustomerStatusEnum.__name__)
    from google.ads.searchads360.v0 import DataDrivenModelStatusEnum
    expected_names.append(DataDrivenModelStatusEnum.__name__)
    from google.ads.searchads360.v0 import DayOfWeekEnum
    expected_names.append(DayOfWeekEnum.__name__)
    from google.ads.searchads360.v0 import DeviceEnum
    expected_names.append(DeviceEnum.__name__)
    from google.ads.searchads360.v0 import GenderTypeEnum
    expected_names.append(GenderTypeEnum.__name__)
    from google.ads.searchads360.v0 import GeoTargetConstantStatusEnum
    expected_names.append(GeoTargetConstantStatusEnum.__name__)
    from google.ads.searchads360.v0 import InteractionEventTypeEnum
    expected_names.append(InteractionEventTypeEnum.__name__)
    from google.ads.searchads360.v0 import KeywordMatchTypeEnum
    expected_names.append(KeywordMatchTypeEnum.__name__)
    from google.ads.searchads360.v0 import LabelStatusEnum
    expected_names.append(LabelStatusEnum.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterBiddingCategoryLevelEnum
    expected_names.append(ListingGroupFilterBiddingCategoryLevelEnum.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterCustomAttributeIndexEnum
    expected_names.append(ListingGroupFilterCustomAttributeIndexEnum.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterProductChannelEnum
    expected_names.append(ListingGroupFilterProductChannelEnum.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterProductConditionEnum
    expected_names.append(ListingGroupFilterProductConditionEnum.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterProductTypeLevelEnum
    expected_names.append(ListingGroupFilterProductTypeLevelEnum.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterTypeEnum
    expected_names.append(ListingGroupFilterTypeEnum.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterVerticalEnum
    expected_names.append(ListingGroupFilterVerticalEnum.__name__)
    from google.ads.searchads360.v0 import ListingGroupTypeEnum
    expected_names.append(ListingGroupTypeEnum.__name__)
    from google.ads.searchads360.v0 import LocationGroupRadiusUnitsEnum
    expected_names.append(LocationGroupRadiusUnitsEnum.__name__)
    from google.ads.searchads360.v0 import LocationOwnershipTypeEnum
    expected_names.append(LocationOwnershipTypeEnum.__name__)
    from google.ads.searchads360.v0 import ManagerLinkStatusEnum
    expected_names.append(ManagerLinkStatusEnum.__name__)
    from google.ads.searchads360.v0 import MimeTypeEnum
    expected_names.append(MimeTypeEnum.__name__)
    from google.ads.searchads360.v0 import MinuteOfHourEnum
    expected_names.append(MinuteOfHourEnum.__name__)
    from google.ads.searchads360.v0 import MobileAppVendorEnum
    expected_names.append(MobileAppVendorEnum.__name__)
    from google.ads.searchads360.v0 import NegativeGeoTargetTypeEnum
    expected_names.append(NegativeGeoTargetTypeEnum.__name__)
    from google.ads.searchads360.v0 import OptimizationGoalTypeEnum
    expected_names.append(OptimizationGoalTypeEnum.__name__)
    from google.ads.searchads360.v0 import PositiveGeoTargetTypeEnum
    expected_names.append(PositiveGeoTargetTypeEnum.__name__)
    from google.ads.searchads360.v0 import ProductBiddingCategoryLevelEnum
    expected_names.append(ProductBiddingCategoryLevelEnum.__name__)
    from google.ads.searchads360.v0 import ProductBiddingCategoryStatusEnum
    expected_names.append(ProductBiddingCategoryStatusEnum.__name__)
    from google.ads.searchads360.v0 import ProductChannelEnum
    expected_names.append(ProductChannelEnum.__name__)
    from google.ads.searchads360.v0 import ProductChannelExclusivityEnum
    expected_names.append(ProductChannelExclusivityEnum.__name__)
    from google.ads.searchads360.v0 import ProductConditionEnum
    expected_names.append(ProductConditionEnum.__name__)
    from google.ads.searchads360.v0 import QualityScoreBucketEnum
    expected_names.append(QualityScoreBucketEnum.__name__)
    from google.ads.searchads360.v0 import SearchAds360FieldCategoryEnum
    expected_names.append(SearchAds360FieldCategoryEnum.__name__)
    from google.ads.searchads360.v0 import SearchAds360FieldDataTypeEnum
    expected_names.append(SearchAds360FieldDataTypeEnum.__name__)
    from google.ads.searchads360.v0 import ServedAssetFieldTypeEnum
    expected_names.append(ServedAssetFieldTypeEnum.__name__)
    from google.ads.searchads360.v0 import SummaryRowSettingEnum
    expected_names.append(SummaryRowSettingEnum.__name__)
    from google.ads.searchads360.v0 import TargetImpressionShareLocationEnum
    expected_names.append(TargetImpressionShareLocationEnum.__name__)
    from google.ads.searchads360.v0 import TargetingDimensionEnum
    expected_names.append(TargetingDimensionEnum.__name__)
    from google.ads.searchads360.v0 import UserListTypeEnum
    expected_names.append(UserListTypeEnum.__name__)
    from google.ads.searchads360.v0 import WebpageConditionOperandEnum
    expected_names.append(WebpageConditionOperandEnum.__name__)
    from google.ads.searchads360.v0 import WebpageConditionOperatorEnum
    expected_names.append(WebpageConditionOperatorEnum.__name__)
    from google.ads.searchads360.v0 import SearchAds360TextAdInfo
    expected_names.append(SearchAds360TextAdInfo.__name__)
    from google.ads.searchads360.v0 import SearchAds360ExpandedTextAdInfo
    expected_names.append(SearchAds360ExpandedTextAdInfo.__name__)
    from google.ads.searchads360.v0 import SearchAds360ExpandedDynamicSearchAdInfo
    expected_names.append(SearchAds360ExpandedDynamicSearchAdInfo.__name__)
    from google.ads.searchads360.v0 import SearchAds360ProductAdInfo
    expected_names.append(SearchAds360ProductAdInfo.__name__)
    from google.ads.searchads360.v0 import SearchAds360ResponsiveSearchAdInfo
    expected_names.append(SearchAds360ResponsiveSearchAdInfo.__name__)
    from google.ads.searchads360.v0 import KeywordInfo
    expected_names.append(KeywordInfo.__name__)
    from google.ads.searchads360.v0 import LocationInfo
    expected_names.append(LocationInfo.__name__)
    from google.ads.searchads360.v0 import DeviceInfo
    expected_names.append(DeviceInfo.__name__)
    from google.ads.searchads360.v0 import ListingGroupInfo
    expected_names.append(ListingGroupInfo.__name__)
    from google.ads.searchads360.v0 import AdScheduleInfo
    expected_names.append(AdScheduleInfo.__name__)
    from google.ads.searchads360.v0 import AgeRangeInfo
    expected_names.append(AgeRangeInfo.__name__)
    from google.ads.searchads360.v0 import GenderInfo
    expected_names.append(GenderInfo.__name__)
    from google.ads.searchads360.v0 import UserListInfo
    expected_names.append(UserListInfo.__name__)
    from google.ads.searchads360.v0 import LanguageInfo
    expected_names.append(LanguageInfo.__name__)
    from google.ads.searchads360.v0 import WebpageInfo
    expected_names.append(WebpageInfo.__name__)
    from google.ads.searchads360.v0 import WebpageConditionInfo
    expected_names.append(WebpageConditionInfo.__name__)
    from google.ads.searchads360.v0 import LocationGroupInfo
    expected_names.append(LocationGroupInfo.__name__)
    from google.ads.searchads360.v0 import AudienceInfo
    expected_names.append(AudienceInfo.__name__)
    from google.ads.searchads360.v0 import YoutubeVideoAsset
    expected_names.append(YoutubeVideoAsset.__name__)
    from google.ads.searchads360.v0 import ImageAsset
    expected_names.append(ImageAsset.__name__)
    from google.ads.searchads360.v0 import ImageDimension
    expected_names.append(ImageDimension.__name__)
    from google.ads.searchads360.v0 import TextAsset
    expected_names.append(TextAsset.__name__)
    from google.ads.searchads360.v0 import UnifiedCalloutAsset
    expected_names.append(UnifiedCalloutAsset.__name__)
    from google.ads.searchads360.v0 import UnifiedSitelinkAsset
    expected_names.append(UnifiedSitelinkAsset.__name__)
    from google.ads.searchads360.v0 import UnifiedPageFeedAsset
    expected_names.append(UnifiedPageFeedAsset.__name__)
    from google.ads.searchads360.v0 import MobileAppAsset
    expected_names.append(MobileAppAsset.__name__)
    from google.ads.searchads360.v0 import UnifiedCallAsset
    expected_names.append(UnifiedCallAsset.__name__)
    from google.ads.searchads360.v0 import CallToActionAsset
    expected_names.append(CallToActionAsset.__name__)
    from google.ads.searchads360.v0 import UnifiedLocationAsset
    expected_names.append(UnifiedLocationAsset.__name__)
    from google.ads.searchads360.v0 import BusinessProfileLocation
    expected_names.append(BusinessProfileLocation.__name__)
    from google.ads.searchads360.v0 import AssetUsage
    expected_names.append(AssetUsage.__name__)
    from google.ads.searchads360.v0 import EnhancedCpc
    expected_names.append(EnhancedCpc.__name__)
    from google.ads.searchads360.v0 import ManualCpa
    expected_names.append(ManualCpa.__name__)
    from google.ads.searchads360.v0 import ManualCpc
    expected_names.append(ManualCpc.__name__)
    from google.ads.searchads360.v0 import ManualCpm
    expected_names.append(ManualCpm.__name__)
    from google.ads.searchads360.v0 import MaximizeConversions
    expected_names.append(MaximizeConversions.__name__)
    from google.ads.searchads360.v0 import MaximizeConversionValue
    expected_names.append(MaximizeConversionValue.__name__)
    from google.ads.searchads360.v0 import TargetCpa
    expected_names.append(TargetCpa.__name__)
    from google.ads.searchads360.v0 import TargetCpm
    expected_names.append(TargetCpm.__name__)
    from google.ads.searchads360.v0 import TargetImpressionShare
    expected_names.append(TargetImpressionShare.__name__)
    from google.ads.searchads360.v0 import TargetOutrankShare
    expected_names.append(TargetOutrankShare.__name__)
    from google.ads.searchads360.v0 import TargetRoas
    expected_names.append(TargetRoas.__name__)
    from google.ads.searchads360.v0 import TargetSpend
    expected_names.append(TargetSpend.__name__)
    from google.ads.searchads360.v0 import PercentCpc
    expected_names.append(PercentCpc.__name__)
    from google.ads.searchads360.v0 import CustomParameter
    expected_names.append(CustomParameter.__name__)
    from google.ads.searchads360.v0 import FrequencyCapEntry
    expected_names.append(FrequencyCapEntry.__name__)
    from google.ads.searchads360.v0 import Metrics
    expected_names.append(Metrics.__name__)
    from google.ads.searchads360.v0 import RealTimeBiddingSetting
    expected_names.append(RealTimeBiddingSetting.__name__)
    from google.ads.searchads360.v0 import Segments
    expected_names.append(Segments.__name__)
    from google.ads.searchads360.v0 import Keyword
    expected_names.append(Keyword.__name__)
    from google.ads.searchads360.v0 import AssetInteractionTarget
    expected_names.append(AssetInteractionTarget.__name__)
    from google.ads.searchads360.v0 import TargetingSetting
    expected_names.append(TargetingSetting.__name__)
    from google.ads.searchads360.v0 import TargetRestriction
    expected_names.append(TargetRestriction.__name__)
    from google.ads.searchads360.v0 import TextLabel
    expected_names.append(TextLabel.__name__)
    from google.ads.searchads360.v0 import Value
    expected_names.append(Value.__name__)
    from google.ads.searchads360.v0 import Ad
    expected_names.append(Ad.__name__)
    from google.ads.searchads360.v0 import AdGroup
    expected_names.append(AdGroup.__name__)
    from google.ads.searchads360.v0 import AdGroupAd
    expected_names.append(AdGroupAd.__name__)
    from google.ads.searchads360.v0 import AdGroupAdLabel
    expected_names.append(AdGroupAdLabel.__name__)
    from google.ads.searchads360.v0 import AdGroupAsset
    expected_names.append(AdGroupAsset.__name__)
    from google.ads.searchads360.v0 import AdGroupAssetSet
    expected_names.append(AdGroupAssetSet.__name__)
    from google.ads.searchads360.v0 import AdGroupAudienceView
    expected_names.append(AdGroupAudienceView.__name__)
    from google.ads.searchads360.v0 import AdGroupBidModifier
    expected_names.append(AdGroupBidModifier.__name__)
    from google.ads.searchads360.v0 import AdGroupCriterion
    expected_names.append(AdGroupCriterion.__name__)
    from google.ads.searchads360.v0 import AdGroupCriterionLabel
    expected_names.append(AdGroupCriterionLabel.__name__)
    from google.ads.searchads360.v0 import AdGroupLabel
    expected_names.append(AdGroupLabel.__name__)
    from google.ads.searchads360.v0 import AgeRangeView
    expected_names.append(AgeRangeView.__name__)
    from google.ads.searchads360.v0 import Asset
    expected_names.append(Asset.__name__)
    from google.ads.searchads360.v0 import AssetGroup
    expected_names.append(AssetGroup.__name__)
    from google.ads.searchads360.v0 import AssetGroupAsset
    expected_names.append(AssetGroupAsset.__name__)
    from google.ads.searchads360.v0 import AssetGroupListingGroupFilter
    expected_names.append(AssetGroupListingGroupFilter.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterDimensionPath
    expected_names.append(ListingGroupFilterDimensionPath.__name__)
    from google.ads.searchads360.v0 import ListingGroupFilterDimension
    expected_names.append(ListingGroupFilterDimension.__name__)
    from google.ads.searchads360.v0 import AssetGroupSignal
    expected_names.append(AssetGroupSignal.__name__)
    from google.ads.searchads360.v0 import AssetGroupTopCombinationView
    expected_names.append(AssetGroupTopCombinationView.__name__)
    from google.ads.searchads360.v0 import AssetGroupAssetCombinationData
    expected_names.append(AssetGroupAssetCombinationData.__name__)
    from google.ads.searchads360.v0 import AssetSet
    expected_names.append(AssetSet.__name__)
    from google.ads.searchads360.v0 import AssetSetAsset
    expected_names.append(AssetSetAsset.__name__)
    from google.ads.searchads360.v0 import Audience
    expected_names.append(Audience.__name__)
    from google.ads.searchads360.v0 import BiddingStrategy
    expected_names.append(BiddingStrategy.__name__)
    from google.ads.searchads360.v0 import Campaign
    expected_names.append(Campaign.__name__)
    from google.ads.searchads360.v0 import CampaignAsset
    expected_names.append(CampaignAsset.__name__)
    from google.ads.searchads360.v0 import CampaignAssetSet
    expected_names.append(CampaignAssetSet.__name__)
    from google.ads.searchads360.v0 import CampaignAudienceView
    expected_names.append(CampaignAudienceView.__name__)
    from google.ads.searchads360.v0 import CampaignBudget
    expected_names.append(CampaignBudget.__name__)
    from google.ads.searchads360.v0 import CampaignCriterion
    expected_names.append(CampaignCriterion.__name__)
    from google.ads.searchads360.v0 import CampaignLabel
    expected_names.append(CampaignLabel.__name__)
    from google.ads.searchads360.v0 import CartDataSalesView
    expected_names.append(CartDataSalesView.__name__)
    from google.ads.searchads360.v0 import Conversion
    expected_names.append(Conversion.__name__)
    from google.ads.searchads360.v0 import ConversionAction
    expected_names.append(ConversionAction.__name__)
    from google.ads.searchads360.v0 import CustomColumn
    expected_names.append(CustomColumn.__name__)
    from google.ads.searchads360.v0 import Customer
    expected_names.append(Customer.__name__)
    from google.ads.searchads360.v0 import ConversionTrackingSetting
    expected_names.append(ConversionTrackingSetting.__name__)
    from google.ads.searchads360.v0 import DoubleClickCampaignManagerSetting
    expected_names.append(DoubleClickCampaignManagerSetting.__name__)
    from google.ads.searchads360.v0 import CustomerAsset
    expected_names.append(CustomerAsset.__name__)
    from google.ads.searchads360.v0 import CustomerAssetSet
    expected_names.append(CustomerAssetSet.__name__)
    from google.ads.searchads360.v0 import CustomerClient
    expected_names.append(CustomerClient.__name__)
    from google.ads.searchads360.v0 import CustomerManagerLink
    expected_names.append(CustomerManagerLink.__name__)
    from google.ads.searchads360.v0 import DynamicSearchAdsSearchTermView
    expected_names.append(DynamicSearchAdsSearchTermView.__name__)
    from google.ads.searchads360.v0 import GenderView
    expected_names.append(GenderView.__name__)
    from google.ads.searchads360.v0 import GeoTargetConstant
    expected_names.append(GeoTargetConstant.__name__)
    from google.ads.searchads360.v0 import KeywordView
    expected_names.append(KeywordView.__name__)
    from google.ads.searchads360.v0 import Label
    expected_names.append(Label.__name__)
    from google.ads.searchads360.v0 import LanguageConstant
    expected_names.append(LanguageConstant.__name__)
    from google.ads.searchads360.v0 import LocationView
    expected_names.append(LocationView.__name__)
    from google.ads.searchads360.v0 import ProductBiddingCategoryConstant
    expected_names.append(ProductBiddingCategoryConstant.__name__)
    from google.ads.searchads360.v0 import ProductGroupView
    expected_names.append(ProductGroupView.__name__)
    from google.ads.searchads360.v0 import SearchAds360Field
    expected_names.append(SearchAds360Field.__name__)
    from google.ads.searchads360.v0 import ShoppingPerformanceView
    expected_names.append(ShoppingPerformanceView.__name__)
    from google.ads.searchads360.v0 import UserList
    expected_names.append(UserList.__name__)
    from google.ads.searchads360.v0 import Visit
    expected_names.append(Visit.__name__)
    from google.ads.searchads360.v0 import WebpageView
    expected_names.append(WebpageView.__name__)
    from google.ads.searchads360.v0 import GetCustomColumnRequest
    expected_names.append(GetCustomColumnRequest.__name__)
    from google.ads.searchads360.v0 import ListCustomColumnsRequest
    expected_names.append(ListCustomColumnsRequest.__name__)
    from google.ads.searchads360.v0 import ListCustomColumnsResponse
    expected_names.append(ListCustomColumnsResponse.__name__)
    from google.ads.searchads360.v0 import ListAccessibleCustomersRequest
    expected_names.append(ListAccessibleCustomersRequest.__name__)
    from google.ads.searchads360.v0 import ListAccessibleCustomersResponse
    expected_names.append(ListAccessibleCustomersResponse.__name__)
    from google.ads.searchads360.v0 import GetSearchAds360FieldRequest
    expected_names.append(GetSearchAds360FieldRequest.__name__)
    from google.ads.searchads360.v0 import SearchSearchAds360FieldsRequest
    expected_names.append(SearchSearchAds360FieldsRequest.__name__)
    from google.ads.searchads360.v0 import SearchSearchAds360FieldsResponse
    expected_names.append(SearchSearchAds360FieldsResponse.__name__)
    from google.ads.searchads360.v0 import SearchSearchAds360Request
    expected_names.append(SearchSearchAds360Request.__name__)
    from google.ads.searchads360.v0 import SearchSearchAds360Response
    expected_names.append(SearchSearchAds360Response.__name__)
    from google.ads.searchads360.v0 import SearchSearchAds360StreamRequest
    expected_names.append(SearchSearchAds360StreamRequest.__name__)
    from google.ads.searchads360.v0 import SearchSearchAds360StreamResponse
    expected_names.append(SearchSearchAds360StreamResponse.__name__)
    from google.ads.searchads360.v0 import SearchAds360Row
    expected_names.append(SearchAds360Row.__name__)
    from google.ads.searchads360.v0 import CustomColumnHeader
    expected_names.append(CustomColumnHeader.__name__)

    # Client and transport classes
    from google.ads.searchads360.v0 import SearchAds360ServiceClient
    expected_names.append(SearchAds360ServiceClient.__name__)
    from google.ads.searchads360.v0 import SearchAds360ServiceTransport
    expected_names.append(SearchAds360ServiceTransport.__name__)
    from google.ads.searchads360.v0 import SearchAds360ServiceGrpcTransport
    expected_names.append(SearchAds360ServiceGrpcTransport.__name__)
    from google.ads.searchads360.v0 import SearchAds360FieldServiceClient
    expected_names.append(SearchAds360FieldServiceClient.__name__)
    from google.ads.searchads360.v0 import SearchAds360FieldServiceTransport
    expected_names.append(SearchAds360FieldServiceTransport.__name__)
    from google.ads.searchads360.v0 import SearchAds360FieldServiceGrpcTransport
    expected_names.append(SearchAds360FieldServiceGrpcTransport.__name__)
    from google.ads.searchads360.v0 import CustomerServiceClient
    expected_names.append(CustomerServiceClient.__name__)
    from google.ads.searchads360.v0 import CustomerServiceTransport
    expected_names.append(CustomerServiceTransport.__name__)
    from google.ads.searchads360.v0 import CustomerServiceGrpcTransport
    expected_names.append(CustomerServiceGrpcTransport.__name__)
    from google.ads.searchads360.v0 import CustomColumnServiceClient
    expected_names.append(CustomColumnServiceClient.__name__)
    from google.ads.searchads360.v0 import CustomColumnServiceTransport
    expected_names.append(CustomColumnServiceTransport.__name__)
    from google.ads.searchads360.v0 import CustomColumnServiceGrpcTransport
    expected_names.append(CustomColumnServiceGrpcTransport.__name__)

    expected_names.sort()
    from google.ads.searchads360 import v0
    actual_names = dir(v0)
    assert expected_names == actual_names

    # Verify the logic for handling non-existant names
    with pytest.raises(ImportError):
        from google.ads.searchads360.v0 import GiantSquid
