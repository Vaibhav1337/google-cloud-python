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
from google.cloud.channel_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.cloud_channel_reports_service import (
    CloudChannelReportsServiceAsyncClient,
    CloudChannelReportsServiceClient,
)
from .services.cloud_channel_service import (
    CloudChannelServiceAsyncClient,
    CloudChannelServiceClient,
)
from .types.channel_partner_links import (
    ChannelPartnerLink,
    ChannelPartnerLinkState,
    ChannelPartnerLinkView,
)
from .types.common import AdminUser, CloudIdentityInfo, EduData, Value
from .types.customers import ContactInfo, Customer
from .types.entitlement_changes import EntitlementChange
from .types.entitlements import (
    AssociationInfo,
    CommitmentSettings,
    Entitlement,
    Parameter,
    ProvisionedService,
    RenewalSettings,
    TransferableSku,
    TransferEligibility,
    TrialSettings,
)
from .types.offers import (
    Constraints,
    CustomerConstraints,
    Offer,
    ParameterDefinition,
    PaymentPlan,
    PaymentType,
    Period,
    PeriodType,
    Plan,
    Price,
    PriceByResource,
    PricePhase,
    PriceTier,
    PromotionalOrderType,
    ResourceType,
)
from .types.operations import OperationMetadata
from .types.products import MarketingInfo, Media, MediaType, Product, Sku
from .types.reports_service import (
    Column,
    DateRange,
    FetchReportResultsRequest,
    FetchReportResultsResponse,
    ListReportsRequest,
    ListReportsResponse,
    Report,
    ReportJob,
    ReportResultsMetadata,
    ReportStatus,
    ReportValue,
    Row,
    RunReportJobRequest,
    RunReportJobResponse,
)
from .types.repricing import (
    ChannelPartnerRepricingConfig,
    ConditionalOverride,
    CustomerRepricingConfig,
    PercentageAdjustment,
    RebillingBasis,
    RepricingAdjustment,
    RepricingCondition,
    RepricingConfig,
    SkuGroupCondition,
)
from .types.service import (
    ActivateEntitlementRequest,
    BillableSku,
    CancelEntitlementRequest,
    ChangeOfferRequest,
    ChangeParametersRequest,
    ChangeRenewalSettingsRequest,
    CheckCloudIdentityAccountsExistRequest,
    CheckCloudIdentityAccountsExistResponse,
    CloudIdentityCustomerAccount,
    CreateChannelPartnerLinkRequest,
    CreateChannelPartnerRepricingConfigRequest,
    CreateCustomerRepricingConfigRequest,
    CreateCustomerRequest,
    CreateEntitlementRequest,
    DeleteChannelPartnerRepricingConfigRequest,
    DeleteCustomerRepricingConfigRequest,
    DeleteCustomerRequest,
    GetChannelPartnerLinkRequest,
    GetChannelPartnerRepricingConfigRequest,
    GetCustomerRepricingConfigRequest,
    GetCustomerRequest,
    GetEntitlementRequest,
    ImportCustomerRequest,
    ListChannelPartnerLinksRequest,
    ListChannelPartnerLinksResponse,
    ListChannelPartnerRepricingConfigsRequest,
    ListChannelPartnerRepricingConfigsResponse,
    ListCustomerRepricingConfigsRequest,
    ListCustomerRepricingConfigsResponse,
    ListCustomersRequest,
    ListCustomersResponse,
    ListEntitlementChangesRequest,
    ListEntitlementChangesResponse,
    ListEntitlementsRequest,
    ListEntitlementsResponse,
    ListOffersRequest,
    ListOffersResponse,
    ListProductsRequest,
    ListProductsResponse,
    ListPurchasableOffersRequest,
    ListPurchasableOffersResponse,
    ListPurchasableSkusRequest,
    ListPurchasableSkusResponse,
    ListSkuGroupBillableSkusRequest,
    ListSkuGroupBillableSkusResponse,
    ListSkuGroupsRequest,
    ListSkuGroupsResponse,
    ListSkusRequest,
    ListSkusResponse,
    ListSubscribersRequest,
    ListSubscribersResponse,
    ListTransferableOffersRequest,
    ListTransferableOffersResponse,
    ListTransferableSkusRequest,
    ListTransferableSkusResponse,
    LookupOfferRequest,
    ProvisionCloudIdentityRequest,
    PurchasableOffer,
    PurchasableSku,
    RegisterSubscriberRequest,
    RegisterSubscriberResponse,
    SkuGroup,
    StartPaidServiceRequest,
    SuspendEntitlementRequest,
    TransferableOffer,
    TransferEntitlementsRequest,
    TransferEntitlementsResponse,
    TransferEntitlementsToGoogleRequest,
    UnregisterSubscriberRequest,
    UnregisterSubscriberResponse,
    UpdateChannelPartnerLinkRequest,
    UpdateChannelPartnerRepricingConfigRequest,
    UpdateCustomerRepricingConfigRequest,
    UpdateCustomerRequest,
)
from .types.subscriber_event import CustomerEvent, EntitlementEvent, SubscriberEvent

__all__ = (
    "CloudChannelReportsServiceAsyncClient",
    "CloudChannelServiceAsyncClient",
    "ActivateEntitlementRequest",
    "AdminUser",
    "AssociationInfo",
    "BillableSku",
    "CancelEntitlementRequest",
    "ChangeOfferRequest",
    "ChangeParametersRequest",
    "ChangeRenewalSettingsRequest",
    "ChannelPartnerLink",
    "ChannelPartnerLinkState",
    "ChannelPartnerLinkView",
    "ChannelPartnerRepricingConfig",
    "CheckCloudIdentityAccountsExistRequest",
    "CheckCloudIdentityAccountsExistResponse",
    "CloudChannelReportsServiceClient",
    "CloudChannelServiceClient",
    "CloudIdentityCustomerAccount",
    "CloudIdentityInfo",
    "Column",
    "CommitmentSettings",
    "ConditionalOverride",
    "Constraints",
    "ContactInfo",
    "CreateChannelPartnerLinkRequest",
    "CreateChannelPartnerRepricingConfigRequest",
    "CreateCustomerRepricingConfigRequest",
    "CreateCustomerRequest",
    "CreateEntitlementRequest",
    "Customer",
    "CustomerConstraints",
    "CustomerEvent",
    "CustomerRepricingConfig",
    "DateRange",
    "DeleteChannelPartnerRepricingConfigRequest",
    "DeleteCustomerRepricingConfigRequest",
    "DeleteCustomerRequest",
    "EduData",
    "Entitlement",
    "EntitlementChange",
    "EntitlementEvent",
    "FetchReportResultsRequest",
    "FetchReportResultsResponse",
    "GetChannelPartnerLinkRequest",
    "GetChannelPartnerRepricingConfigRequest",
    "GetCustomerRepricingConfigRequest",
    "GetCustomerRequest",
    "GetEntitlementRequest",
    "ImportCustomerRequest",
    "ListChannelPartnerLinksRequest",
    "ListChannelPartnerLinksResponse",
    "ListChannelPartnerRepricingConfigsRequest",
    "ListChannelPartnerRepricingConfigsResponse",
    "ListCustomerRepricingConfigsRequest",
    "ListCustomerRepricingConfigsResponse",
    "ListCustomersRequest",
    "ListCustomersResponse",
    "ListEntitlementChangesRequest",
    "ListEntitlementChangesResponse",
    "ListEntitlementsRequest",
    "ListEntitlementsResponse",
    "ListOffersRequest",
    "ListOffersResponse",
    "ListProductsRequest",
    "ListProductsResponse",
    "ListPurchasableOffersRequest",
    "ListPurchasableOffersResponse",
    "ListPurchasableSkusRequest",
    "ListPurchasableSkusResponse",
    "ListReportsRequest",
    "ListReportsResponse",
    "ListSkuGroupBillableSkusRequest",
    "ListSkuGroupBillableSkusResponse",
    "ListSkuGroupsRequest",
    "ListSkuGroupsResponse",
    "ListSkusRequest",
    "ListSkusResponse",
    "ListSubscribersRequest",
    "ListSubscribersResponse",
    "ListTransferableOffersRequest",
    "ListTransferableOffersResponse",
    "ListTransferableSkusRequest",
    "ListTransferableSkusResponse",
    "LookupOfferRequest",
    "MarketingInfo",
    "Media",
    "MediaType",
    "Offer",
    "OperationMetadata",
    "Parameter",
    "ParameterDefinition",
    "PaymentPlan",
    "PaymentType",
    "PercentageAdjustment",
    "Period",
    "PeriodType",
    "Plan",
    "Price",
    "PriceByResource",
    "PricePhase",
    "PriceTier",
    "Product",
    "PromotionalOrderType",
    "ProvisionCloudIdentityRequest",
    "ProvisionedService",
    "PurchasableOffer",
    "PurchasableSku",
    "RebillingBasis",
    "RegisterSubscriberRequest",
    "RegisterSubscriberResponse",
    "RenewalSettings",
    "Report",
    "ReportJob",
    "ReportResultsMetadata",
    "ReportStatus",
    "ReportValue",
    "RepricingAdjustment",
    "RepricingCondition",
    "RepricingConfig",
    "ResourceType",
    "Row",
    "RunReportJobRequest",
    "RunReportJobResponse",
    "Sku",
    "SkuGroup",
    "SkuGroupCondition",
    "StartPaidServiceRequest",
    "SubscriberEvent",
    "SuspendEntitlementRequest",
    "TransferEligibility",
    "TransferEntitlementsRequest",
    "TransferEntitlementsResponse",
    "TransferEntitlementsToGoogleRequest",
    "TransferableOffer",
    "TransferableSku",
    "TrialSettings",
    "UnregisterSubscriberRequest",
    "UnregisterSubscriberResponse",
    "UpdateChannelPartnerLinkRequest",
    "UpdateChannelPartnerRepricingConfigRequest",
    "UpdateCustomerRepricingConfigRequest",
    "UpdateCustomerRequest",
    "Value",
)
