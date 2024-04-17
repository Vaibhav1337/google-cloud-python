# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from google.shopping.merchant_lfp import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_lfp_v1beta.services.lfp_inventory_service.async_client import (
    LfpInventoryServiceAsyncClient,
)
from google.shopping.merchant_lfp_v1beta.services.lfp_inventory_service.client import (
    LfpInventoryServiceClient,
)
from google.shopping.merchant_lfp_v1beta.services.lfp_sale_service.async_client import (
    LfpSaleServiceAsyncClient,
)
from google.shopping.merchant_lfp_v1beta.services.lfp_sale_service.client import (
    LfpSaleServiceClient,
)
from google.shopping.merchant_lfp_v1beta.services.lfp_store_service.async_client import (
    LfpStoreServiceAsyncClient,
)
from google.shopping.merchant_lfp_v1beta.services.lfp_store_service.client import (
    LfpStoreServiceClient,
)
from google.shopping.merchant_lfp_v1beta.types.lfpinventory import (
    InsertLfpInventoryRequest,
    LfpInventory,
)
from google.shopping.merchant_lfp_v1beta.types.lfpsale import (
    InsertLfpSaleRequest,
    LfpSale,
)
from google.shopping.merchant_lfp_v1beta.types.lfpstore import (
    DeleteLfpStoreRequest,
    GetLfpStoreRequest,
    InsertLfpStoreRequest,
    LfpStore,
    ListLfpStoresRequest,
    ListLfpStoresResponse,
)

__all__ = (
    "LfpInventoryServiceClient",
    "LfpInventoryServiceAsyncClient",
    "LfpSaleServiceClient",
    "LfpSaleServiceAsyncClient",
    "LfpStoreServiceClient",
    "LfpStoreServiceAsyncClient",
    "InsertLfpInventoryRequest",
    "LfpInventory",
    "InsertLfpSaleRequest",
    "LfpSale",
    "DeleteLfpStoreRequest",
    "GetLfpStoreRequest",
    "InsertLfpStoreRequest",
    "LfpStore",
    "ListLfpStoresRequest",
    "ListLfpStoresResponse",
)
