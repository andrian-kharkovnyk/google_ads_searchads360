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
import importlib
import sys


if sys.version_info < (3, 7):
    raise ImportError('This module requires Python 3.7 or later.')


_lazy_type_to_package_map = {
    # Message types
    'AdScheduleInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'AgeRangeInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'AssetInteractionTarget': 'google.ads.searchads360.v0.common.types.segments',
    'AssetUsage': 'google.ads.searchads360.v0.common.types.asset_usage',
    'AudienceInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'BusinessProfileLocation': 'google.ads.searchads360.v0.common.types.asset_types',
    'CallToActionAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'CustomParameter': 'google.ads.searchads360.v0.common.types.custom_parameter',
    'DeviceInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'EnhancedCpc': 'google.ads.searchads360.v0.common.types.bidding',
    'FrequencyCapEntry': 'google.ads.searchads360.v0.common.types.frequency_cap',
    'GenderInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'ImageAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'ImageDimension': 'google.ads.searchads360.v0.common.types.asset_types',
    'Keyword': 'google.ads.searchads360.v0.common.types.segments',
    'KeywordInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'LanguageInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'ListingGroupInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'LocationGroupInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'LocationInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'ManualCpa': 'google.ads.searchads360.v0.common.types.bidding',
    'ManualCpc': 'google.ads.searchads360.v0.common.types.bidding',
    'ManualCpm': 'google.ads.searchads360.v0.common.types.bidding',
    'MaximizeConversions': 'google.ads.searchads360.v0.common.types.bidding',
    'MaximizeConversionValue': 'google.ads.searchads360.v0.common.types.bidding',
    'Metrics': 'google.ads.searchads360.v0.common.types.metrics',
    'MobileAppAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'PercentCpc': 'google.ads.searchads360.v0.common.types.bidding',
    'RealTimeBiddingSetting': 'google.ads.searchads360.v0.common.types.real_time_bidding_setting',
    'SearchAds360ExpandedDynamicSearchAdInfo': 'google.ads.searchads360.v0.common.types.ad_type_infos',
    'SearchAds360ExpandedTextAdInfo': 'google.ads.searchads360.v0.common.types.ad_type_infos',
    'SearchAds360ProductAdInfo': 'google.ads.searchads360.v0.common.types.ad_type_infos',
    'SearchAds360ResponsiveSearchAdInfo': 'google.ads.searchads360.v0.common.types.ad_type_infos',
    'SearchAds360TextAdInfo': 'google.ads.searchads360.v0.common.types.ad_type_infos',
    'Segments': 'google.ads.searchads360.v0.common.types.segments',
    'TargetCpa': 'google.ads.searchads360.v0.common.types.bidding',
    'TargetCpm': 'google.ads.searchads360.v0.common.types.bidding',
    'TargetImpressionShare': 'google.ads.searchads360.v0.common.types.bidding',
    'TargetingSetting': 'google.ads.searchads360.v0.common.types.targeting_setting',
    'TargetOutrankShare': 'google.ads.searchads360.v0.common.types.bidding',
    'TargetRestriction': 'google.ads.searchads360.v0.common.types.targeting_setting',
    'TargetRoas': 'google.ads.searchads360.v0.common.types.bidding',
    'TargetSpend': 'google.ads.searchads360.v0.common.types.bidding',
    'TextAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'TextLabel': 'google.ads.searchads360.v0.common.types.text_label',
    'UnifiedCallAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'UnifiedCalloutAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'UnifiedLocationAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'UnifiedPageFeedAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'UnifiedSitelinkAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'UserListInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'Value': 'google.ads.searchads360.v0.common.types.value',
    'WebpageConditionInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'WebpageInfo': 'google.ads.searchads360.v0.common.types.criteria',
    'YoutubeVideoAsset': 'google.ads.searchads360.v0.common.types.asset_types',
    'AccountStatusEnum': 'google.ads.searchads360.v0.enums.types.account_status',
    'AccountTypeEnum': 'google.ads.searchads360.v0.enums.types.account_type',
    'AdGroupAdEngineStatusEnum': 'google.ads.searchads360.v0.enums.types.ad_group_ad_engine_status',
    'AdGroupAdRotationModeEnum': 'google.ads.searchads360.v0.enums.types.ad_group_ad_rotation_mode',
    'AdGroupAdStatusEnum': 'google.ads.searchads360.v0.enums.types.ad_group_ad_status',
    'AdGroupCriterionEngineStatusEnum': 'google.ads.searchads360.v0.enums.types.ad_group_criterion_engine_status',
    'AdGroupCriterionStatusEnum': 'google.ads.searchads360.v0.enums.types.ad_group_criterion_status',
    'AdGroupEngineStatusEnum': 'google.ads.searchads360.v0.enums.types.ad_group_engine_status',
    'AdGroupStatusEnum': 'google.ads.searchads360.v0.enums.types.ad_group_status',
    'AdGroupTypeEnum': 'google.ads.searchads360.v0.enums.types.ad_group_type',
    'AdNetworkTypeEnum': 'google.ads.searchads360.v0.enums.types.ad_network_type',
    'AdServingOptimizationStatusEnum': 'google.ads.searchads360.v0.enums.types.ad_serving_optimization_status',
    'AdStrengthEnum': 'google.ads.searchads360.v0.enums.types.ad_strength',
    'AdTypeEnum': 'google.ads.searchads360.v0.enums.types.ad_type',
    'AdvertisingChannelSubTypeEnum': 'google.ads.searchads360.v0.enums.types.advertising_channel_sub_type',
    'AdvertisingChannelTypeEnum': 'google.ads.searchads360.v0.enums.types.advertising_channel_type',
    'AgeRangeTypeEnum': 'google.ads.searchads360.v0.enums.types.age_range_type',
    'AssetEngineStatusEnum': 'google.ads.searchads360.v0.enums.types.asset_engine_status',
    'AssetFieldTypeEnum': 'google.ads.searchads360.v0.enums.types.asset_field_type',
    'AssetGroupStatusEnum': 'google.ads.searchads360.v0.enums.types.asset_group_status',
    'AssetLinkStatusEnum': 'google.ads.searchads360.v0.enums.types.asset_link_status',
    'AssetSetAssetStatusEnum': 'google.ads.searchads360.v0.enums.types.asset_set_asset_status',
    'AssetSetLinkStatusEnum': 'google.ads.searchads360.v0.enums.types.asset_set_link_status',
    'AssetStatusEnum': 'google.ads.searchads360.v0.enums.types.asset_status',
    'AssetTypeEnum': 'google.ads.searchads360.v0.enums.types.asset_type',
    'AttributionModelEnum': 'google.ads.searchads360.v0.enums.types.attribution_model',
    'AttributionTypeEnum': 'google.ads.searchads360.v0.enums.types.attribution_type',
    'BiddingStrategyStatusEnum': 'google.ads.searchads360.v0.enums.types.bidding_strategy_status',
    'BiddingStrategySystemStatusEnum': 'google.ads.searchads360.v0.enums.types.bidding_strategy_system_status',
    'BiddingStrategyTypeEnum': 'google.ads.searchads360.v0.enums.types.bidding_strategy_type',
    'BudgetDeliveryMethodEnum': 'google.ads.searchads360.v0.enums.types.budget_delivery_method',
    'BudgetPeriodEnum': 'google.ads.searchads360.v0.enums.types.budget_period',
    'CallConversionReportingStateEnum': 'google.ads.searchads360.v0.enums.types.call_conversion_reporting_state',
    'CallToActionTypeEnum': 'google.ads.searchads360.v0.enums.types.call_to_action_type',
    'CampaignCriterionStatusEnum': 'google.ads.searchads360.v0.enums.types.campaign_criterion_status',
    'CampaignServingStatusEnum': 'google.ads.searchads360.v0.enums.types.campaign_serving_status',
    'CampaignStatusEnum': 'google.ads.searchads360.v0.enums.types.campaign_status',
    'ConversionActionCategoryEnum': 'google.ads.searchads360.v0.enums.types.conversion_action_category',
    'ConversionActionStatusEnum': 'google.ads.searchads360.v0.enums.types.conversion_action_status',
    'ConversionActionTypeEnum': 'google.ads.searchads360.v0.enums.types.conversion_action_type',
    'ConversionStatusEnum': 'google.ads.searchads360.v0.enums.types.conversion_status',
    'ConversionTrackingStatusEnum': 'google.ads.searchads360.v0.enums.types.conversion_tracking_status_enum',
    'CriterionTypeEnum': 'google.ads.searchads360.v0.enums.types.criterion_type',
    'CustomColumnValueTypeEnum': 'google.ads.searchads360.v0.enums.types.custom_column_value_type',
    'CustomerStatusEnum': 'google.ads.searchads360.v0.enums.types.customer_status',
    'DataDrivenModelStatusEnum': 'google.ads.searchads360.v0.enums.types.data_driven_model_status',
    'DayOfWeekEnum': 'google.ads.searchads360.v0.enums.types.day_of_week',
    'DeviceEnum': 'google.ads.searchads360.v0.enums.types.device',
    'GenderTypeEnum': 'google.ads.searchads360.v0.enums.types.gender_type',
    'GeoTargetConstantStatusEnum': 'google.ads.searchads360.v0.enums.types.geo_target_constant_status',
    'InteractionEventTypeEnum': 'google.ads.searchads360.v0.enums.types.interaction_event_type',
    'KeywordMatchTypeEnum': 'google.ads.searchads360.v0.enums.types.keyword_match_type',
    'LabelStatusEnum': 'google.ads.searchads360.v0.enums.types.label_status',
    'ListingGroupFilterBiddingCategoryLevelEnum': 'google.ads.searchads360.v0.enums.types.listing_group_filter_bidding_category_level',
    'ListingGroupFilterCustomAttributeIndexEnum': 'google.ads.searchads360.v0.enums.types.listing_group_filter_custom_attribute_index',
    'ListingGroupFilterProductChannelEnum': 'google.ads.searchads360.v0.enums.types.listing_group_filter_product_channel',
    'ListingGroupFilterProductConditionEnum': 'google.ads.searchads360.v0.enums.types.listing_group_filter_product_condition',
    'ListingGroupFilterProductTypeLevelEnum': 'google.ads.searchads360.v0.enums.types.listing_group_filter_product_type_level',
    'ListingGroupFilterTypeEnum': 'google.ads.searchads360.v0.enums.types.listing_group_filter_type_enum',
    'ListingGroupFilterVerticalEnum': 'google.ads.searchads360.v0.enums.types.listing_group_filter_vertical',
    'ListingGroupTypeEnum': 'google.ads.searchads360.v0.enums.types.listing_group_type',
    'LocationGroupRadiusUnitsEnum': 'google.ads.searchads360.v0.enums.types.location_group_radius_units',
    'LocationOwnershipTypeEnum': 'google.ads.searchads360.v0.enums.types.location_ownership_type',
    'ManagerLinkStatusEnum': 'google.ads.searchads360.v0.enums.types.manager_link_status',
    'MimeTypeEnum': 'google.ads.searchads360.v0.enums.types.mime_type',
    'MinuteOfHourEnum': 'google.ads.searchads360.v0.enums.types.minute_of_hour',
    'MobileAppVendorEnum': 'google.ads.searchads360.v0.enums.types.mobile_app_vendor',
    'NegativeGeoTargetTypeEnum': 'google.ads.searchads360.v0.enums.types.negative_geo_target_type',
    'OptimizationGoalTypeEnum': 'google.ads.searchads360.v0.enums.types.optimization_goal_type',
    'PositiveGeoTargetTypeEnum': 'google.ads.searchads360.v0.enums.types.positive_geo_target_type',
    'ProductBiddingCategoryLevelEnum': 'google.ads.searchads360.v0.enums.types.product_bidding_category_level',
    'ProductBiddingCategoryStatusEnum': 'google.ads.searchads360.v0.enums.types.product_bidding_category_status',
    'ProductChannelEnum': 'google.ads.searchads360.v0.enums.types.product_channel',
    'ProductChannelExclusivityEnum': 'google.ads.searchads360.v0.enums.types.product_channel_exclusivity',
    'ProductConditionEnum': 'google.ads.searchads360.v0.enums.types.product_condition',
    'QualityScoreBucketEnum': 'google.ads.searchads360.v0.enums.types.quality_score_bucket',
    'SearchAds360FieldCategoryEnum': 'google.ads.searchads360.v0.enums.types.search_ads360_field_category',
    'SearchAds360FieldDataTypeEnum': 'google.ads.searchads360.v0.enums.types.search_ads360_field_data_type',
    'ServedAssetFieldTypeEnum': 'google.ads.searchads360.v0.enums.types.served_asset_field_type',
    'SummaryRowSettingEnum': 'google.ads.searchads360.v0.enums.types.summary_row_setting',
    'TargetImpressionShareLocationEnum': 'google.ads.searchads360.v0.enums.types.target_impression_share_location',
    'TargetingDimensionEnum': 'google.ads.searchads360.v0.enums.types.targeting_dimension',
    'UserListTypeEnum': 'google.ads.searchads360.v0.enums.types.user_list_type',
    'WebpageConditionOperandEnum': 'google.ads.searchads360.v0.enums.types.webpage_condition_operand',
    'WebpageConditionOperatorEnum': 'google.ads.searchads360.v0.enums.types.webpage_condition_operator',
    'Ad': 'google.ads.searchads360.v0.resources.types.ad',
    'AdGroup': 'google.ads.searchads360.v0.resources.types.ad_group',
    'AdGroupAd': 'google.ads.searchads360.v0.resources.types.ad_group_ad',
    'AdGroupAdLabel': 'google.ads.searchads360.v0.resources.types.ad_group_ad_label',
    'AdGroupAsset': 'google.ads.searchads360.v0.resources.types.ad_group_asset',
    'AdGroupAssetSet': 'google.ads.searchads360.v0.resources.types.ad_group_asset_set',
    'AdGroupAudienceView': 'google.ads.searchads360.v0.resources.types.ad_group_audience_view',
    'AdGroupBidModifier': 'google.ads.searchads360.v0.resources.types.ad_group_bid_modifier',
    'AdGroupCriterion': 'google.ads.searchads360.v0.resources.types.ad_group_criterion',
    'AdGroupCriterionLabel': 'google.ads.searchads360.v0.resources.types.ad_group_criterion_label',
    'AdGroupLabel': 'google.ads.searchads360.v0.resources.types.ad_group_label',
    'AgeRangeView': 'google.ads.searchads360.v0.resources.types.age_range_view',
    'Asset': 'google.ads.searchads360.v0.resources.types.asset',
    'AssetGroup': 'google.ads.searchads360.v0.resources.types.asset_group',
    'AssetGroupAsset': 'google.ads.searchads360.v0.resources.types.asset_group_asset',
    'AssetGroupAssetCombinationData': 'google.ads.searchads360.v0.resources.types.asset_group_top_combination_view',
    'AssetGroupListingGroupFilter': 'google.ads.searchads360.v0.resources.types.asset_group_listing_group_filter',
    'AssetGroupSignal': 'google.ads.searchads360.v0.resources.types.asset_group_signal',
    'AssetGroupTopCombinationView': 'google.ads.searchads360.v0.resources.types.asset_group_top_combination_view',
    'AssetSet': 'google.ads.searchads360.v0.resources.types.asset_set',
    'AssetSetAsset': 'google.ads.searchads360.v0.resources.types.asset_set_asset',
    'Audience': 'google.ads.searchads360.v0.resources.types.audience',
    'BiddingStrategy': 'google.ads.searchads360.v0.resources.types.bidding_strategy',
    'Campaign': 'google.ads.searchads360.v0.resources.types.campaign',
    'CampaignAsset': 'google.ads.searchads360.v0.resources.types.campaign_asset',
    'CampaignAssetSet': 'google.ads.searchads360.v0.resources.types.campaign_asset_set',
    'CampaignAudienceView': 'google.ads.searchads360.v0.resources.types.campaign_audience_view',
    'CampaignBudget': 'google.ads.searchads360.v0.resources.types.campaign_budget',
    'CampaignCriterion': 'google.ads.searchads360.v0.resources.types.campaign_criterion',
    'CampaignLabel': 'google.ads.searchads360.v0.resources.types.campaign_label',
    'CartDataSalesView': 'google.ads.searchads360.v0.resources.types.cart_data_sales_view',
    'Conversion': 'google.ads.searchads360.v0.resources.types.conversion',
    'ConversionAction': 'google.ads.searchads360.v0.resources.types.conversion_action',
    'ConversionTrackingSetting': 'google.ads.searchads360.v0.resources.types.customer',
    'CustomColumn': 'google.ads.searchads360.v0.resources.types.custom_column',
    'Customer': 'google.ads.searchads360.v0.resources.types.customer',
    'CustomerAsset': 'google.ads.searchads360.v0.resources.types.customer_asset',
    'CustomerAssetSet': 'google.ads.searchads360.v0.resources.types.customer_asset_set',
    'CustomerClient': 'google.ads.searchads360.v0.resources.types.customer_client',
    'CustomerManagerLink': 'google.ads.searchads360.v0.resources.types.customer_manager_link',
    'DoubleClickCampaignManagerSetting': 'google.ads.searchads360.v0.resources.types.customer',
    'DynamicSearchAdsSearchTermView': 'google.ads.searchads360.v0.resources.types.dynamic_search_ads_search_term_view',
    'GenderView': 'google.ads.searchads360.v0.resources.types.gender_view',
    'GeoTargetConstant': 'google.ads.searchads360.v0.resources.types.geo_target_constant',
    'KeywordView': 'google.ads.searchads360.v0.resources.types.keyword_view',
    'Label': 'google.ads.searchads360.v0.resources.types.label',
    'LanguageConstant': 'google.ads.searchads360.v0.resources.types.language_constant',
    'ListingGroupFilterDimension': 'google.ads.searchads360.v0.resources.types.asset_group_listing_group_filter',
    'ListingGroupFilterDimensionPath': 'google.ads.searchads360.v0.resources.types.asset_group_listing_group_filter',
    'LocationView': 'google.ads.searchads360.v0.resources.types.location_view',
    'ProductBiddingCategoryConstant': 'google.ads.searchads360.v0.resources.types.product_bidding_category_constant',
    'ProductGroupView': 'google.ads.searchads360.v0.resources.types.product_group_view',
    'SearchAds360Field': 'google.ads.searchads360.v0.resources.types.search_ads360_field',
    'ShoppingPerformanceView': 'google.ads.searchads360.v0.resources.types.shopping_performance_view',
    'UserList': 'google.ads.searchads360.v0.resources.types.user_list',
    'Visit': 'google.ads.searchads360.v0.resources.types.visit',
    'WebpageView': 'google.ads.searchads360.v0.resources.types.webpage_view',
    'CustomColumnHeader': 'google.ads.searchads360.v0.services.types.search_ads360_service',
    'GetCustomColumnRequest': 'google.ads.searchads360.v0.services.types.custom_column_service',
    'GetSearchAds360FieldRequest': 'google.ads.searchads360.v0.services.types.search_ads360_field_service',
    'ListAccessibleCustomersRequest': 'google.ads.searchads360.v0.services.types.customer_service',
    'ListAccessibleCustomersResponse': 'google.ads.searchads360.v0.services.types.customer_service',
    'ListCustomColumnsRequest': 'google.ads.searchads360.v0.services.types.custom_column_service',
    'ListCustomColumnsResponse': 'google.ads.searchads360.v0.services.types.custom_column_service',
    'SearchAds360Row': 'google.ads.searchads360.v0.services.types.search_ads360_service',
    'SearchSearchAds360FieldsRequest': 'google.ads.searchads360.v0.services.types.search_ads360_field_service',
    'SearchSearchAds360FieldsResponse': 'google.ads.searchads360.v0.services.types.search_ads360_field_service',
    'SearchSearchAds360Request': 'google.ads.searchads360.v0.services.types.search_ads360_service',
    'SearchSearchAds360Response': 'google.ads.searchads360.v0.services.types.search_ads360_service',
    'SearchSearchAds360StreamRequest': 'google.ads.searchads360.v0.services.types.search_ads360_service',
    'SearchSearchAds360StreamResponse': 'google.ads.searchads360.v0.services.types.search_ads360_service',
    # Enum types
    # Client classes and transports
    'CustomColumnServiceClient': 'google.ads.searchads360.v0.services.services.custom_column_service',
    'CustomColumnServiceTransport': 'google.ads.searchads360.v0.services.services.custom_column_service.transports',
    'CustomColumnServiceGrpcTransport': 'google.ads.searchads360.v0.services.services.custom_column_service.transports',
    'CustomerServiceClient': 'google.ads.searchads360.v0.services.services.customer_service',
    'CustomerServiceTransport': 'google.ads.searchads360.v0.services.services.customer_service.transports',
    'CustomerServiceGrpcTransport': 'google.ads.searchads360.v0.services.services.customer_service.transports',
    'SearchAds360FieldServiceClient': 'google.ads.searchads360.v0.services.services.search_ads360_field_service',
    'SearchAds360FieldServiceTransport': 'google.ads.searchads360.v0.services.services.search_ads360_field_service.transports',
    'SearchAds360FieldServiceGrpcTransport': 'google.ads.searchads360.v0.services.services.search_ads360_field_service.transports',
    'SearchAds360ServiceClient': 'google.ads.searchads360.v0.services.services.search_ads360_service',
    'SearchAds360ServiceTransport': 'google.ads.searchads360.v0.services.services.search_ads360_service.transports',
    'SearchAds360ServiceGrpcTransport': 'google.ads.searchads360.v0.services.services.search_ads360_service.transports',
}


# Background on how this behaves: https://www.python.org/dev/peps/pep-0562/
def __getattr__(name):  # Requires Python >= 3.7
    if name == '__all__':
        all_names = globals()['__all__'] = sorted(_lazy_type_to_package_map)
        return all_names
    elif name in _lazy_type_to_package_map:
        module = importlib.import_module(f'{_lazy_type_to_package_map[name]}')
        klass = getattr(module, name)
        globals()[name] = klass
        return klass
    else:
        raise AttributeError(f'unknown type {name!r}.')


def __dir__():
    return globals().get('__all__') or __getattr__('__all__')
