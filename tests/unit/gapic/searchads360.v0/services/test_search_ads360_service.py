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
# try/except added for compatibility with python < 3.8
try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    import mock

import grpc
from grpc.experimental import aio
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule


from google.ads.searchads360.v0.enums.types import summary_row_setting
from google.ads.searchads360.v0.services.services.search_ads360_service import SearchAds360ServiceClient
from google.ads.searchads360.v0.services.services.search_ads360_service import pagers
from google.ads.searchads360.v0.services.services.search_ads360_service import transports
from google.ads.searchads360.v0.services.types import search_ads360_service
from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import path_template
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.oauth2 import service_account
from google.protobuf import field_mask_pb2  # type: ignore
import google.auth


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return "foo.googleapis.com" if ("localhost" in client.DEFAULT_ENDPOINT) else client.DEFAULT_ENDPOINT


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert SearchAds360ServiceClient._get_default_mtls_endpoint(None) is None
    assert SearchAds360ServiceClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert SearchAds360ServiceClient._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    assert SearchAds360ServiceClient._get_default_mtls_endpoint(sandbox_endpoint) == sandbox_mtls_endpoint
    assert SearchAds360ServiceClient._get_default_mtls_endpoint(sandbox_mtls_endpoint) == sandbox_mtls_endpoint
    assert SearchAds360ServiceClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize("client_class,transport_name", [
    (SearchAds360ServiceClient, "grpc"),
])
def test_search_ads360_service_client_from_service_account_info(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'searchads360.googleapis.com:443'
        )


@pytest.mark.parametrize("transport_class,transport_name", [
    (transports.SearchAds360ServiceGrpcTransport, "grpc"),
])
def test_search_ads360_service_client_service_account_always_use_jwt(transport_class, transport_name):
    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize("client_class,transport_name", [
    (SearchAds360ServiceClient, "grpc"),
])
def test_search_ads360_service_client_from_service_account_file(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'searchads360.googleapis.com:443'
        )


def test_search_ads360_service_client_get_transport_class():
    transport = SearchAds360ServiceClient.get_transport_class()
    available_transports = [
        transports.SearchAds360ServiceGrpcTransport,
    ]
    assert transport in available_transports

    transport = SearchAds360ServiceClient.get_transport_class("grpc")
    assert transport == transports.SearchAds360ServiceGrpcTransport


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (SearchAds360ServiceClient, transports.SearchAds360ServiceGrpcTransport, "grpc"),
])
@mock.patch.object(SearchAds360ServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(SearchAds360ServiceClient))
def test_search_ads360_service_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(SearchAds360ServiceClient, 'get_transport_class') as gtc:
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials()
        )
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(SearchAds360ServiceClient, 'get_transport_class') as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class(transport=transport_name)

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        with pytest.raises(ValueError):
            client = client_class(transport=transport_name)

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,use_client_cert_env", [
    (SearchAds360ServiceClient, transports.SearchAds360ServiceGrpcTransport, "grpc", "true"),
    (SearchAds360ServiceClient, transports.SearchAds360ServiceGrpcTransport, "grpc", "false"),
])
@mock.patch.object(SearchAds360ServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(SearchAds360ServiceClient))
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_search_ads360_service_client_mtls_env_auto(client_class, transport_class, transport_name, use_client_cert_env):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        options = client_options.ClientOptions(client_cert_source=client_cert_source_callback)
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
                with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=client_cert_source_callback):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch("google.auth.transport.mtls.has_default_client_cert_source", return_value=False):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                )


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (SearchAds360ServiceClient, transports.SearchAds360ServiceGrpcTransport, "grpc"),
])
def test_search_ads360_service_client_client_options_scopes(client_class, transport_class, transport_name):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (SearchAds360ServiceClient, transports.SearchAds360ServiceGrpcTransport, "grpc"),
])
def test_search_ads360_service_client_client_options_credentials_file(client_class, transport_class, transport_name):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

def test_search_ads360_service_client_client_options_from_dict():
    with mock.patch('google.ads.searchads360.v0.services.services.search_ads360_service.transports.SearchAds360ServiceGrpcTransport.__init__') as grpc_transport:
        grpc_transport.return_value = None
        client = SearchAds360ServiceClient(
            client_options={'api_endpoint': 'squid.clam.whelk'}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (SearchAds360ServiceClient, transports.SearchAds360ServiceGrpcTransport, "grpc"),
])
def test_search_ads360_service_client_create_channel_credentials_file(client_class, transport_class, transport_name):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "searchads360.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                'https://www.googleapis.com/auth/doubleclicksearch',
),
            scopes=None,
            default_host="searchads360.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("request_type", [
  search_ads360_service.SearchSearchAds360Request,
  dict,
])
def test_search(request_type, transport: str = 'grpc'):
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = search_ads360_service.SearchSearchAds360Response(
            next_page_token='next_page_token_value',
            total_results_count=2077,
        )
        response = client.search(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == search_ads360_service.SearchSearchAds360Request()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.SearchPager)
    assert response.next_page_token == 'next_page_token_value'
    assert response.total_results_count == 2077


def test_search_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search),
            '__call__') as call:
        client.search()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == search_ads360_service.SearchSearchAds360Request()


def test_search_field_headers():
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = search_ads360_service.SearchSearchAds360Request()

    request.customer_id = 'customer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search),
            '__call__') as call:
        call.return_value = search_ads360_service.SearchSearchAds360Response()
        client.search(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'customer_id=customer_id_value',
    ) in kw['metadata']


def test_search_flattened():
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = search_ads360_service.SearchSearchAds360Response()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.search(
            customer_id='customer_id_value',
            query='query_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].customer_id
        mock_val = 'customer_id_value'
        assert arg == mock_val
        arg = args[0].query
        mock_val = 'query_value'
        assert arg == mock_val


def test_search_flattened_error():
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.search(
            search_ads360_service.SearchSearchAds360Request(),
            customer_id='customer_id_value',
            query='query_value',
        )


def test_search_pager(transport_name: str = "grpc"):
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            search_ads360_service.SearchSearchAds360Response(
                results=[
                    search_ads360_service.SearchAds360Row(),
                    search_ads360_service.SearchAds360Row(),
                    search_ads360_service.SearchAds360Row(),
                ],
                next_page_token='abc',
            ),
            search_ads360_service.SearchSearchAds360Response(
                results=[],
                next_page_token='def',
            ),
            search_ads360_service.SearchSearchAds360Response(
                results=[
                    search_ads360_service.SearchAds360Row(),
                ],
                next_page_token='ghi',
            ),
            search_ads360_service.SearchSearchAds360Response(
                results=[
                    search_ads360_service.SearchAds360Row(),
                    search_ads360_service.SearchAds360Row(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ('customer_id', ''),
            )),
        )
        pager = client.search(request={})

        assert pager._metadata == metadata

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, search_ads360_service.SearchAds360Row)
                   for i in results)


def test_search_pages(transport_name: str = "grpc"):
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
         type(client.transport.search),
        '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            search_ads360_service.SearchSearchAds360Response(
                results=[
                    search_ads360_service.SearchAds360Row(),
                    search_ads360_service.SearchAds360Row(),
                    search_ads360_service.SearchAds360Row(),
                ],
                next_page_token='abc',
            ),
            search_ads360_service.SearchSearchAds360Response(
                results=[],
                next_page_token='def',
            ),
            search_ads360_service.SearchSearchAds360Response(
                results=[
                    search_ads360_service.SearchAds360Row(),
                ],
                next_page_token='ghi',
            ),
            search_ads360_service.SearchSearchAds360Response(
                results=[
                    search_ads360_service.SearchAds360Row(),
                    search_ads360_service.SearchAds360Row(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.search(request={}).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize("request_type", [
  search_ads360_service.SearchSearchAds360StreamRequest,
  dict,
])
def test_search_stream(request_type, transport: str = 'grpc'):
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search_stream),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([search_ads360_service.SearchSearchAds360StreamResponse()])
        response = client.search_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == search_ads360_service.SearchSearchAds360StreamRequest()

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, search_ads360_service.SearchSearchAds360StreamResponse)


def test_search_stream_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search_stream),
            '__call__') as call:
        client.search_stream()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == search_ads360_service.SearchSearchAds360StreamRequest()


def test_search_stream_field_headers():
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = search_ads360_service.SearchSearchAds360StreamRequest()

    request.customer_id = 'customer_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search_stream),
            '__call__') as call:
        call.return_value = iter([search_ads360_service.SearchSearchAds360StreamResponse()])
        client.search_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'customer_id=customer_id_value',
    ) in kw['metadata']


def test_search_stream_flattened():
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.search_stream),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([search_ads360_service.SearchSearchAds360StreamResponse()])
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.search_stream(
            customer_id='customer_id_value',
            query='query_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].customer_id
        mock_val = 'customer_id_value'
        assert arg == mock_val
        arg = args[0].query
        mock_val = 'query_value'
        assert arg == mock_val


def test_search_stream_flattened_error():
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.search_stream(
            search_ads360_service.SearchSearchAds360StreamRequest(),
            customer_id='customer_id_value',
            query='query_value',
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.SearchAds360ServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SearchAds360ServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.SearchAds360ServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SearchAds360ServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.SearchAds360ServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SearchAds360ServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.SearchAds360ServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = SearchAds360ServiceClient(transport=transport)
    assert client.transport is transport

def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.SearchAds360ServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize("transport_class", [
    transports.SearchAds360ServiceGrpcTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, 'default') as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()

def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.SearchAds360ServiceGrpcTransport,
    )

def test_search_ads360_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.SearchAds360ServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_search_ads360_service_base_transport():
    # Instantiate the base transport.
    with mock.patch('google.ads.searchads360.v0.services.services.search_ads360_service.transports.SearchAds360ServiceTransport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.SearchAds360ServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'search',
        'search_stream',
       )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()


def test_search_ads360_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(google.auth, 'load_credentials_from_file', autospec=True) as load_creds, mock.patch('google.ads.searchads360.v0.services.services.search_ads360_service.transports.SearchAds360ServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.SearchAds360ServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json",
            scopes=None,
            default_scopes=(
            'https://www.googleapis.com/auth/doubleclicksearch',
),
            quota_project_id="octopus",
        )


def test_search_ads360_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc, mock.patch('google.ads.searchads360.v0.services.services.search_ads360_service.transports.SearchAds360ServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.SearchAds360ServiceTransport()
        adc.assert_called_once()


def test_search_ads360_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        SearchAds360ServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
            'https://www.googleapis.com/auth/doubleclicksearch',
),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.SearchAds360ServiceGrpcTransport,
    ],
)
def test_search_ads360_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(                'https://www.googleapis.com/auth/doubleclicksearch',),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.SearchAds360ServiceGrpcTransport, grpc_helpers),
    ],
)
def test_search_ads360_service_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(
            quota_project_id="octopus",
            scopes=["1", "2"]
        )

        create_channel.assert_called_with(
            "searchads360.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                'https://www.googleapis.com/auth/doubleclicksearch',
),
            scopes=["1", "2"],
            default_host="searchads360.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("transport_class",
    [
      transports.SearchAds360ServiceGrpcTransport,
])
def test_search_ads360_service_grpc_transport_client_cert_source_for_mtls(
    transport_class
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert,
                private_key=expected_key
            )


@pytest.mark.parametrize("transport_name", [
    "grpc",
])
def test_search_ads360_service_host_no_port(transport_name):
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='searchads360.googleapis.com'),
        transport=transport_name,
    )
    assert client.transport._host == (
        'searchads360.googleapis.com:443'
    )


@pytest.mark.parametrize("transport_name", [
    "grpc",
])
def test_search_ads360_service_host_with_port(transport_name):
    client = SearchAds360ServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='searchads360.googleapis.com:8000'),
        transport=transport_name,
    )
    assert client.transport._host == (
        'searchads360.googleapis.com:8000'
    )

def test_search_ads360_service_grpc_transport_channel():
    channel = grpc.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.SearchAds360ServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class",
    [
      transports.SearchAds360ServiceGrpcTransport,
    ])
def test_search_ads360_service_transport_channel_mtls_with_client_cert_source(
    transport_class
):
    with mock.patch("grpc.ssl_channel_credentials", autospec=True) as grpc_ssl_channel_cred:
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, 'default') as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class",
    [
      transports.SearchAds360ServiceGrpcTransport,
    ])
def test_search_ads360_service_transport_channel_mtls_with_adc(
    transport_class
):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_ad_path():
    customer_id = "squid"
    ad_id = "clam"
    expected = "customers/{customer_id}/ads/{ad_id}".format(customer_id=customer_id, ad_id=ad_id, )
    actual = SearchAds360ServiceClient.ad_path(customer_id, ad_id)
    assert expected == actual


def test_parse_ad_path():
    expected = {
        "customer_id": "whelk",
        "ad_id": "octopus",
    }
    path = SearchAds360ServiceClient.ad_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_path(path)
    assert expected == actual

def test_ad_group_path():
    customer_id = "oyster"
    ad_group_id = "nudibranch"
    expected = "customers/{customer_id}/adGroups/{ad_group_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, )
    actual = SearchAds360ServiceClient.ad_group_path(customer_id, ad_group_id)
    assert expected == actual


def test_parse_ad_group_path():
    expected = {
        "customer_id": "cuttlefish",
        "ad_group_id": "mussel",
    }
    path = SearchAds360ServiceClient.ad_group_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_path(path)
    assert expected == actual

def test_ad_group_ad_path():
    customer_id = "winkle"
    ad_group_id = "nautilus"
    ad_id = "scallop"
    expected = "customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, ad_id=ad_id, )
    actual = SearchAds360ServiceClient.ad_group_ad_path(customer_id, ad_group_id, ad_id)
    assert expected == actual


def test_parse_ad_group_ad_path():
    expected = {
        "customer_id": "abalone",
        "ad_group_id": "squid",
        "ad_id": "clam",
    }
    path = SearchAds360ServiceClient.ad_group_ad_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_ad_path(path)
    assert expected == actual

def test_ad_group_ad_label_path():
    customer_id = "whelk"
    ad_group_id = "octopus"
    ad_id = "oyster"
    entity_id = "nudibranch"
    expected = "customers/{customer_id}/adGroupAdLabels/{ad_group_id}~{ad_id}~{entity_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, ad_id=ad_id, entity_id=entity_id, )
    actual = SearchAds360ServiceClient.ad_group_ad_label_path(customer_id, ad_group_id, ad_id, entity_id)
    assert expected == actual


def test_parse_ad_group_ad_label_path():
    expected = {
        "customer_id": "cuttlefish",
        "ad_group_id": "mussel",
        "ad_id": "winkle",
        "entity_id": "nautilus",
    }
    path = SearchAds360ServiceClient.ad_group_ad_label_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_ad_label_path(path)
    assert expected == actual

def test_ad_group_asset_path():
    customer_id = "scallop"
    ad_group_id = "abalone"
    asset_id = "squid"
    field_type = "clam"
    expected = "customers/{customer_id}/adGroupAssets/{ad_group_id}~{asset_id}~{field_type}".format(customer_id=customer_id, ad_group_id=ad_group_id, asset_id=asset_id, field_type=field_type, )
    actual = SearchAds360ServiceClient.ad_group_asset_path(customer_id, ad_group_id, asset_id, field_type)
    assert expected == actual


def test_parse_ad_group_asset_path():
    expected = {
        "customer_id": "whelk",
        "ad_group_id": "octopus",
        "asset_id": "oyster",
        "field_type": "nudibranch",
    }
    path = SearchAds360ServiceClient.ad_group_asset_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_asset_path(path)
    assert expected == actual

def test_ad_group_asset_set_path():
    customer_id = "cuttlefish"
    ad_group_id = "mussel"
    asset_set_id = "winkle"
    expected = "customers/{customer_id}/adGroupAssetSets/{ad_group_id}~{asset_set_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, asset_set_id=asset_set_id, )
    actual = SearchAds360ServiceClient.ad_group_asset_set_path(customer_id, ad_group_id, asset_set_id)
    assert expected == actual


def test_parse_ad_group_asset_set_path():
    expected = {
        "customer_id": "nautilus",
        "ad_group_id": "scallop",
        "asset_set_id": "abalone",
    }
    path = SearchAds360ServiceClient.ad_group_asset_set_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_asset_set_path(path)
    assert expected == actual

def test_ad_group_audience_view_path():
    customer_id = "squid"
    ad_group_id = "clam"
    criterion_id = "whelk"
    expected = "customers/{customer_id}/adGroupAudienceViews/{ad_group_id}~{criterion_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.ad_group_audience_view_path(customer_id, ad_group_id, criterion_id)
    assert expected == actual


def test_parse_ad_group_audience_view_path():
    expected = {
        "customer_id": "octopus",
        "ad_group_id": "oyster",
        "criterion_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.ad_group_audience_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_audience_view_path(path)
    assert expected == actual

def test_ad_group_bid_modifier_path():
    customer_id = "cuttlefish"
    ad_group_id = "mussel"
    criterion_id = "winkle"
    expected = "customers/{customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.ad_group_bid_modifier_path(customer_id, ad_group_id, criterion_id)
    assert expected == actual


def test_parse_ad_group_bid_modifier_path():
    expected = {
        "customer_id": "nautilus",
        "ad_group_id": "scallop",
        "criterion_id": "abalone",
    }
    path = SearchAds360ServiceClient.ad_group_bid_modifier_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_bid_modifier_path(path)
    assert expected == actual

def test_ad_group_criterion_path():
    customer_id = "squid"
    ad_group_id = "clam"
    criterion_id = "whelk"
    expected = "customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.ad_group_criterion_path(customer_id, ad_group_id, criterion_id)
    assert expected == actual


def test_parse_ad_group_criterion_path():
    expected = {
        "customer_id": "octopus",
        "ad_group_id": "oyster",
        "criterion_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.ad_group_criterion_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_criterion_path(path)
    assert expected == actual

def test_ad_group_criterion_label_path():
    customer_id = "cuttlefish"
    ad_group_id = "mussel"
    criterion_id = "winkle"
    entity_id = "nautilus"
    expected = "customers/{customer_id}/adGroupCriterionLabels/{ad_group_id}~{criterion_id}~{entity_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criterion_id=criterion_id, entity_id=entity_id, )
    actual = SearchAds360ServiceClient.ad_group_criterion_label_path(customer_id, ad_group_id, criterion_id, entity_id)
    assert expected == actual


def test_parse_ad_group_criterion_label_path():
    expected = {
        "customer_id": "scallop",
        "ad_group_id": "abalone",
        "criterion_id": "squid",
        "entity_id": "clam",
    }
    path = SearchAds360ServiceClient.ad_group_criterion_label_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_criterion_label_path(path)
    assert expected == actual

def test_ad_group_label_path():
    customer_id = "whelk"
    ad_group_id = "octopus"
    entity_id = "oyster"
    expected = "customers/{customer_id}/adGroupLabels/{ad_group_id}~{entity_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, entity_id=entity_id, )
    actual = SearchAds360ServiceClient.ad_group_label_path(customer_id, ad_group_id, entity_id)
    assert expected == actual


def test_parse_ad_group_label_path():
    expected = {
        "customer_id": "nudibranch",
        "ad_group_id": "cuttlefish",
        "entity_id": "mussel",
    }
    path = SearchAds360ServiceClient.ad_group_label_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_ad_group_label_path(path)
    assert expected == actual

def test_age_range_view_path():
    customer_id = "winkle"
    ad_group_id = "nautilus"
    criterion_id = "scallop"
    expected = "customers/{customer_id}/ageRangeViews/{ad_group_id}~{criterion_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.age_range_view_path(customer_id, ad_group_id, criterion_id)
    assert expected == actual


def test_parse_age_range_view_path():
    expected = {
        "customer_id": "abalone",
        "ad_group_id": "squid",
        "criterion_id": "clam",
    }
    path = SearchAds360ServiceClient.age_range_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_age_range_view_path(path)
    assert expected == actual

def test_asset_path():
    customer_id = "whelk"
    asset_id = "octopus"
    expected = "customers/{customer_id}/assets/{asset_id}".format(customer_id=customer_id, asset_id=asset_id, )
    actual = SearchAds360ServiceClient.asset_path(customer_id, asset_id)
    assert expected == actual


def test_parse_asset_path():
    expected = {
        "customer_id": "oyster",
        "asset_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.asset_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_asset_path(path)
    assert expected == actual

def test_asset_group_path():
    customer_id = "cuttlefish"
    asset_group_id = "mussel"
    expected = "customers/{customer_id}/assetGroups/{asset_group_id}".format(customer_id=customer_id, asset_group_id=asset_group_id, )
    actual = SearchAds360ServiceClient.asset_group_path(customer_id, asset_group_id)
    assert expected == actual


def test_parse_asset_group_path():
    expected = {
        "customer_id": "winkle",
        "asset_group_id": "nautilus",
    }
    path = SearchAds360ServiceClient.asset_group_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_asset_group_path(path)
    assert expected == actual

def test_asset_group_asset_path():
    customer_id = "scallop"
    asset_group_id = "abalone"
    asset_id = "squid"
    field_type = "clam"
    expected = "customers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}".format(customer_id=customer_id, asset_group_id=asset_group_id, asset_id=asset_id, field_type=field_type, )
    actual = SearchAds360ServiceClient.asset_group_asset_path(customer_id, asset_group_id, asset_id, field_type)
    assert expected == actual


def test_parse_asset_group_asset_path():
    expected = {
        "customer_id": "whelk",
        "asset_group_id": "octopus",
        "asset_id": "oyster",
        "field_type": "nudibranch",
    }
    path = SearchAds360ServiceClient.asset_group_asset_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_asset_group_asset_path(path)
    assert expected == actual

def test_asset_group_listing_group_filter_path():
    customer_id = "cuttlefish"
    asset_group_id = "mussel"
    listing_group_filter_id = "winkle"
    expected = "customers/{customer_id}/assetGroupListingGroupFilters/{asset_group_id}~{listing_group_filter_id}".format(customer_id=customer_id, asset_group_id=asset_group_id, listing_group_filter_id=listing_group_filter_id, )
    actual = SearchAds360ServiceClient.asset_group_listing_group_filter_path(customer_id, asset_group_id, listing_group_filter_id)
    assert expected == actual


def test_parse_asset_group_listing_group_filter_path():
    expected = {
        "customer_id": "nautilus",
        "asset_group_id": "scallop",
        "listing_group_filter_id": "abalone",
    }
    path = SearchAds360ServiceClient.asset_group_listing_group_filter_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_asset_group_listing_group_filter_path(path)
    assert expected == actual

def test_asset_group_signal_path():
    customer_id = "squid"
    asset_group_id = "clam"
    criterion_id = "whelk"
    expected = "customers/{customer_id}/assetGroupSignals/{asset_group_id}~{criterion_id}".format(customer_id=customer_id, asset_group_id=asset_group_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.asset_group_signal_path(customer_id, asset_group_id, criterion_id)
    assert expected == actual


def test_parse_asset_group_signal_path():
    expected = {
        "customer_id": "octopus",
        "asset_group_id": "oyster",
        "criterion_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.asset_group_signal_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_asset_group_signal_path(path)
    assert expected == actual

def test_asset_group_top_combination_view_path():
    customer_id = "cuttlefish"
    asset_group_id = "mussel"
    asset_combination_category = "winkle"
    expected = "customers/{customer_id}/assetGroupTopCombinationViews/{asset_group_id}~{asset_combination_category}".format(customer_id=customer_id, asset_group_id=asset_group_id, asset_combination_category=asset_combination_category, )
    actual = SearchAds360ServiceClient.asset_group_top_combination_view_path(customer_id, asset_group_id, asset_combination_category)
    assert expected == actual


def test_parse_asset_group_top_combination_view_path():
    expected = {
        "customer_id": "nautilus",
        "asset_group_id": "scallop",
        "asset_combination_category": "abalone",
    }
    path = SearchAds360ServiceClient.asset_group_top_combination_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_asset_group_top_combination_view_path(path)
    assert expected == actual

def test_asset_set_path():
    customer_id = "squid"
    asset_set_id = "clam"
    expected = "customers/{customer_id}/assetSets/{asset_set_id}".format(customer_id=customer_id, asset_set_id=asset_set_id, )
    actual = SearchAds360ServiceClient.asset_set_path(customer_id, asset_set_id)
    assert expected == actual


def test_parse_asset_set_path():
    expected = {
        "customer_id": "whelk",
        "asset_set_id": "octopus",
    }
    path = SearchAds360ServiceClient.asset_set_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_asset_set_path(path)
    assert expected == actual

def test_asset_set_asset_path():
    customer_id = "oyster"
    asset_set_id = "nudibranch"
    asset_id = "cuttlefish"
    expected = "customers/{customer_id}/assetSetAssets/{asset_set_id}~{asset_id}".format(customer_id=customer_id, asset_set_id=asset_set_id, asset_id=asset_id, )
    actual = SearchAds360ServiceClient.asset_set_asset_path(customer_id, asset_set_id, asset_id)
    assert expected == actual


def test_parse_asset_set_asset_path():
    expected = {
        "customer_id": "mussel",
        "asset_set_id": "winkle",
        "asset_id": "nautilus",
    }
    path = SearchAds360ServiceClient.asset_set_asset_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_asset_set_asset_path(path)
    assert expected == actual

def test_audience_path():
    customer_id = "scallop"
    audience_id = "abalone"
    expected = "customers/{customer_id}/audiences/{audience_id}".format(customer_id=customer_id, audience_id=audience_id, )
    actual = SearchAds360ServiceClient.audience_path(customer_id, audience_id)
    assert expected == actual


def test_parse_audience_path():
    expected = {
        "customer_id": "squid",
        "audience_id": "clam",
    }
    path = SearchAds360ServiceClient.audience_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_audience_path(path)
    assert expected == actual

def test_bidding_strategy_path():
    customer_id = "whelk"
    bidding_strategy_id = "octopus"
    expected = "customers/{customer_id}/biddingStrategies/{bidding_strategy_id}".format(customer_id=customer_id, bidding_strategy_id=bidding_strategy_id, )
    actual = SearchAds360ServiceClient.bidding_strategy_path(customer_id, bidding_strategy_id)
    assert expected == actual


def test_parse_bidding_strategy_path():
    expected = {
        "customer_id": "oyster",
        "bidding_strategy_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.bidding_strategy_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_bidding_strategy_path(path)
    assert expected == actual

def test_campaign_path():
    customer_id = "cuttlefish"
    campaign_id = "mussel"
    expected = "customers/{customer_id}/campaigns/{campaign_id}".format(customer_id=customer_id, campaign_id=campaign_id, )
    actual = SearchAds360ServiceClient.campaign_path(customer_id, campaign_id)
    assert expected == actual


def test_parse_campaign_path():
    expected = {
        "customer_id": "winkle",
        "campaign_id": "nautilus",
    }
    path = SearchAds360ServiceClient.campaign_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_campaign_path(path)
    assert expected == actual

def test_campaign_asset_path():
    customer_id = "scallop"
    campaign_id = "abalone"
    asset_id = "squid"
    field_type = "clam"
    expected = "customers/{customer_id}/campaignAssets/{campaign_id}~{asset_id}~{field_type}".format(customer_id=customer_id, campaign_id=campaign_id, asset_id=asset_id, field_type=field_type, )
    actual = SearchAds360ServiceClient.campaign_asset_path(customer_id, campaign_id, asset_id, field_type)
    assert expected == actual


def test_parse_campaign_asset_path():
    expected = {
        "customer_id": "whelk",
        "campaign_id": "octopus",
        "asset_id": "oyster",
        "field_type": "nudibranch",
    }
    path = SearchAds360ServiceClient.campaign_asset_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_campaign_asset_path(path)
    assert expected == actual

def test_campaign_asset_set_path():
    customer_id = "cuttlefish"
    campaign_id = "mussel"
    asset_set_id = "winkle"
    expected = "customers/{customer_id}/campaignAssetSets/{campaign_id}~{asset_set_id}".format(customer_id=customer_id, campaign_id=campaign_id, asset_set_id=asset_set_id, )
    actual = SearchAds360ServiceClient.campaign_asset_set_path(customer_id, campaign_id, asset_set_id)
    assert expected == actual


def test_parse_campaign_asset_set_path():
    expected = {
        "customer_id": "nautilus",
        "campaign_id": "scallop",
        "asset_set_id": "abalone",
    }
    path = SearchAds360ServiceClient.campaign_asset_set_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_campaign_asset_set_path(path)
    assert expected == actual

def test_campaign_audience_view_path():
    customer_id = "squid"
    campaign_id = "clam"
    criterion_id = "whelk"
    expected = "customers/{customer_id}/campaignAudienceViews/{campaign_id}~{criterion_id}".format(customer_id=customer_id, campaign_id=campaign_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.campaign_audience_view_path(customer_id, campaign_id, criterion_id)
    assert expected == actual


def test_parse_campaign_audience_view_path():
    expected = {
        "customer_id": "octopus",
        "campaign_id": "oyster",
        "criterion_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.campaign_audience_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_campaign_audience_view_path(path)
    assert expected == actual

def test_campaign_budget_path():
    customer_id = "cuttlefish"
    budget_id = "mussel"
    expected = "customers/{customer_id}/campaignBudgets/{budget_id}".format(customer_id=customer_id, budget_id=budget_id, )
    actual = SearchAds360ServiceClient.campaign_budget_path(customer_id, budget_id)
    assert expected == actual


def test_parse_campaign_budget_path():
    expected = {
        "customer_id": "winkle",
        "budget_id": "nautilus",
    }
    path = SearchAds360ServiceClient.campaign_budget_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_campaign_budget_path(path)
    assert expected == actual

def test_campaign_criterion_path():
    customer_id = "scallop"
    campaign_id = "abalone"
    criterion_id = "squid"
    expected = "customers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}".format(customer_id=customer_id, campaign_id=campaign_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.campaign_criterion_path(customer_id, campaign_id, criterion_id)
    assert expected == actual


def test_parse_campaign_criterion_path():
    expected = {
        "customer_id": "clam",
        "campaign_id": "whelk",
        "criterion_id": "octopus",
    }
    path = SearchAds360ServiceClient.campaign_criterion_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_campaign_criterion_path(path)
    assert expected == actual

def test_campaign_label_path():
    customer_id = "oyster"
    campaign_id = "nudibranch"
    entity_id = "cuttlefish"
    expected = "customers/{customer_id}/campaignLabels/{campaign_id}~{entity_id}".format(customer_id=customer_id, campaign_id=campaign_id, entity_id=entity_id, )
    actual = SearchAds360ServiceClient.campaign_label_path(customer_id, campaign_id, entity_id)
    assert expected == actual


def test_parse_campaign_label_path():
    expected = {
        "customer_id": "mussel",
        "campaign_id": "winkle",
        "entity_id": "nautilus",
    }
    path = SearchAds360ServiceClient.campaign_label_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_campaign_label_path(path)
    assert expected == actual

def test_cart_data_sales_view_path():
    customer_id = "scallop"
    expected = "customers/{customer_id}/cartDataSalesView".format(customer_id=customer_id, )
    actual = SearchAds360ServiceClient.cart_data_sales_view_path(customer_id)
    assert expected == actual


def test_parse_cart_data_sales_view_path():
    expected = {
        "customer_id": "abalone",
    }
    path = SearchAds360ServiceClient.cart_data_sales_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_cart_data_sales_view_path(path)
    assert expected == actual

def test_conversion_path():
    customer_id = "squid"
    ad_group_id = "clam"
    criteria_id = "whelk"
    ds_conversion_id = "octopus"
    expected = "customers/{customer_id}/conversions/{ad_group_id}~{criteria_id}~{ds_conversion_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criteria_id=criteria_id, ds_conversion_id=ds_conversion_id, )
    actual = SearchAds360ServiceClient.conversion_path(customer_id, ad_group_id, criteria_id, ds_conversion_id)
    assert expected == actual


def test_parse_conversion_path():
    expected = {
        "customer_id": "oyster",
        "ad_group_id": "nudibranch",
        "criteria_id": "cuttlefish",
        "ds_conversion_id": "mussel",
    }
    path = SearchAds360ServiceClient.conversion_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_conversion_path(path)
    assert expected == actual

def test_conversion_action_path():
    customer_id = "winkle"
    conversion_type_id = "nautilus"
    expected = "customers/{customer_id}/conversionActions/{conversion_type_id}".format(customer_id=customer_id, conversion_type_id=conversion_type_id, )
    actual = SearchAds360ServiceClient.conversion_action_path(customer_id, conversion_type_id)
    assert expected == actual


def test_parse_conversion_action_path():
    expected = {
        "customer_id": "scallop",
        "conversion_type_id": "abalone",
    }
    path = SearchAds360ServiceClient.conversion_action_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_conversion_action_path(path)
    assert expected == actual

def test_customer_path():
    customer_id = "squid"
    expected = "customers/{customer_id}".format(customer_id=customer_id, )
    actual = SearchAds360ServiceClient.customer_path(customer_id)
    assert expected == actual


def test_parse_customer_path():
    expected = {
        "customer_id": "clam",
    }
    path = SearchAds360ServiceClient.customer_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_customer_path(path)
    assert expected == actual

def test_customer_asset_path():
    customer_id = "whelk"
    asset_id = "octopus"
    field_type = "oyster"
    expected = "customers/{customer_id}/customerAssets/{asset_id}~{field_type}".format(customer_id=customer_id, asset_id=asset_id, field_type=field_type, )
    actual = SearchAds360ServiceClient.customer_asset_path(customer_id, asset_id, field_type)
    assert expected == actual


def test_parse_customer_asset_path():
    expected = {
        "customer_id": "nudibranch",
        "asset_id": "cuttlefish",
        "field_type": "mussel",
    }
    path = SearchAds360ServiceClient.customer_asset_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_customer_asset_path(path)
    assert expected == actual

def test_customer_asset_set_path():
    customer_id = "winkle"
    asset_set_id = "nautilus"
    expected = "customers/{customer_id}/customerAssetSets/{asset_set_id}".format(customer_id=customer_id, asset_set_id=asset_set_id, )
    actual = SearchAds360ServiceClient.customer_asset_set_path(customer_id, asset_set_id)
    assert expected == actual


def test_parse_customer_asset_set_path():
    expected = {
        "customer_id": "scallop",
        "asset_set_id": "abalone",
    }
    path = SearchAds360ServiceClient.customer_asset_set_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_customer_asset_set_path(path)
    assert expected == actual

def test_customer_client_path():
    customer_id = "squid"
    client_external_customer_id = "clam"
    expected = "customers/{customer_id}/customerClients/{client_external_customer_id}".format(customer_id=customer_id, client_external_customer_id=client_external_customer_id, )
    actual = SearchAds360ServiceClient.customer_client_path(customer_id, client_external_customer_id)
    assert expected == actual


def test_parse_customer_client_path():
    expected = {
        "customer_id": "whelk",
        "client_external_customer_id": "octopus",
    }
    path = SearchAds360ServiceClient.customer_client_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_customer_client_path(path)
    assert expected == actual

def test_customer_manager_link_path():
    customer_id = "oyster"
    manager_customer_id = "nudibranch"
    manager_link_id = "cuttlefish"
    expected = "customers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}".format(customer_id=customer_id, manager_customer_id=manager_customer_id, manager_link_id=manager_link_id, )
    actual = SearchAds360ServiceClient.customer_manager_link_path(customer_id, manager_customer_id, manager_link_id)
    assert expected == actual


def test_parse_customer_manager_link_path():
    expected = {
        "customer_id": "mussel",
        "manager_customer_id": "winkle",
        "manager_link_id": "nautilus",
    }
    path = SearchAds360ServiceClient.customer_manager_link_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_customer_manager_link_path(path)
    assert expected == actual

def test_dynamic_search_ads_search_term_view_path():
    customer_id = "scallop"
    ad_group_id = "abalone"
    query_fp = "squid"
    line1_fp = "clam"
    url_fp = "whelk"
    feed_item_lp_url_fp = "octopus"
    expected = "customers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{query_fp}~{line1_fp}~{url_fp}~{feed_item_lp_url_fp}".format(customer_id=customer_id, ad_group_id=ad_group_id, query_fp=query_fp, line1_fp=line1_fp, url_fp=url_fp, feed_item_lp_url_fp=feed_item_lp_url_fp, )
    actual = SearchAds360ServiceClient.dynamic_search_ads_search_term_view_path(customer_id, ad_group_id, query_fp, line1_fp, url_fp, feed_item_lp_url_fp)
    assert expected == actual


def test_parse_dynamic_search_ads_search_term_view_path():
    expected = {
        "customer_id": "oyster",
        "ad_group_id": "nudibranch",
        "query_fp": "cuttlefish",
        "line1_fp": "mussel",
        "url_fp": "winkle",
        "feed_item_lp_url_fp": "nautilus",
    }
    path = SearchAds360ServiceClient.dynamic_search_ads_search_term_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_dynamic_search_ads_search_term_view_path(path)
    assert expected == actual

def test_gender_view_path():
    customer_id = "scallop"
    ad_group_id = "abalone"
    criterion_id = "squid"
    expected = "customers/{customer_id}/genderViews/{ad_group_id}~{criterion_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.gender_view_path(customer_id, ad_group_id, criterion_id)
    assert expected == actual


def test_parse_gender_view_path():
    expected = {
        "customer_id": "clam",
        "ad_group_id": "whelk",
        "criterion_id": "octopus",
    }
    path = SearchAds360ServiceClient.gender_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_gender_view_path(path)
    assert expected == actual

def test_geo_target_constant_path():
    criterion_id = "oyster"
    expected = "geoTargetConstants/{criterion_id}".format(criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.geo_target_constant_path(criterion_id)
    assert expected == actual


def test_parse_geo_target_constant_path():
    expected = {
        "criterion_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.geo_target_constant_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_geo_target_constant_path(path)
    assert expected == actual

def test_keyword_view_path():
    customer_id = "cuttlefish"
    ad_group_id = "mussel"
    criterion_id = "winkle"
    expected = "customers/{customer_id}/keywordViews/{ad_group_id}~{criterion_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.keyword_view_path(customer_id, ad_group_id, criterion_id)
    assert expected == actual


def test_parse_keyword_view_path():
    expected = {
        "customer_id": "nautilus",
        "ad_group_id": "scallop",
        "criterion_id": "abalone",
    }
    path = SearchAds360ServiceClient.keyword_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_keyword_view_path(path)
    assert expected == actual

def test_label_path():
    customer_id = "squid"
    label_id = "clam"
    expected = "customers/{customer_id}/labels/{label_id}".format(customer_id=customer_id, label_id=label_id, )
    actual = SearchAds360ServiceClient.label_path(customer_id, label_id)
    assert expected == actual


def test_parse_label_path():
    expected = {
        "customer_id": "whelk",
        "label_id": "octopus",
    }
    path = SearchAds360ServiceClient.label_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_label_path(path)
    assert expected == actual

def test_language_constant_path():
    criterion_id = "oyster"
    expected = "languageConstants/{criterion_id}".format(criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.language_constant_path(criterion_id)
    assert expected == actual


def test_parse_language_constant_path():
    expected = {
        "criterion_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.language_constant_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_language_constant_path(path)
    assert expected == actual

def test_location_view_path():
    customer_id = "cuttlefish"
    campaign_id = "mussel"
    criterion_id = "winkle"
    expected = "customers/{customer_id}/locationViews/{campaign_id}~{criterion_id}".format(customer_id=customer_id, campaign_id=campaign_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.location_view_path(customer_id, campaign_id, criterion_id)
    assert expected == actual


def test_parse_location_view_path():
    expected = {
        "customer_id": "nautilus",
        "campaign_id": "scallop",
        "criterion_id": "abalone",
    }
    path = SearchAds360ServiceClient.location_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_location_view_path(path)
    assert expected == actual

def test_product_bidding_category_constant_path():
    country_code = "squid"
    level = "clam"
    canonical_value = "whelk"
    expected = "productBiddingCategoryConstants/{country_code}~{level}~{canonical_value}".format(country_code=country_code, level=level, canonical_value=canonical_value, )
    actual = SearchAds360ServiceClient.product_bidding_category_constant_path(country_code, level, canonical_value)
    assert expected == actual


def test_parse_product_bidding_category_constant_path():
    expected = {
        "country_code": "octopus",
        "level": "oyster",
        "canonical_value": "nudibranch",
    }
    path = SearchAds360ServiceClient.product_bidding_category_constant_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_product_bidding_category_constant_path(path)
    assert expected == actual

def test_product_group_view_path():
    customer_id = "cuttlefish"
    adgroup_id = "mussel"
    criterion_id = "winkle"
    expected = "customers/{customer_id}/productGroupViews/{adgroup_id}~{criterion_id}".format(customer_id=customer_id, adgroup_id=adgroup_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.product_group_view_path(customer_id, adgroup_id, criterion_id)
    assert expected == actual


def test_parse_product_group_view_path():
    expected = {
        "customer_id": "nautilus",
        "adgroup_id": "scallop",
        "criterion_id": "abalone",
    }
    path = SearchAds360ServiceClient.product_group_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_product_group_view_path(path)
    assert expected == actual

def test_shopping_performance_view_path():
    customer_id = "squid"
    expected = "customers/{customer_id}/shoppingPerformanceView".format(customer_id=customer_id, )
    actual = SearchAds360ServiceClient.shopping_performance_view_path(customer_id)
    assert expected == actual


def test_parse_shopping_performance_view_path():
    expected = {
        "customer_id": "clam",
    }
    path = SearchAds360ServiceClient.shopping_performance_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_shopping_performance_view_path(path)
    assert expected == actual

def test_user_list_path():
    customer_id = "whelk"
    user_list_id = "octopus"
    expected = "customers/{customer_id}/userLists/{user_list_id}".format(customer_id=customer_id, user_list_id=user_list_id, )
    actual = SearchAds360ServiceClient.user_list_path(customer_id, user_list_id)
    assert expected == actual


def test_parse_user_list_path():
    expected = {
        "customer_id": "oyster",
        "user_list_id": "nudibranch",
    }
    path = SearchAds360ServiceClient.user_list_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_user_list_path(path)
    assert expected == actual

def test_visit_path():
    customer_id = "cuttlefish"
    ad_group_id = "mussel"
    criteria_id = "winkle"
    ds_visit_id = "nautilus"
    expected = "customers/{customer_id}/visits/{ad_group_id}~{criteria_id}~{ds_visit_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criteria_id=criteria_id, ds_visit_id=ds_visit_id, )
    actual = SearchAds360ServiceClient.visit_path(customer_id, ad_group_id, criteria_id, ds_visit_id)
    assert expected == actual


def test_parse_visit_path():
    expected = {
        "customer_id": "scallop",
        "ad_group_id": "abalone",
        "criteria_id": "squid",
        "ds_visit_id": "clam",
    }
    path = SearchAds360ServiceClient.visit_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_visit_path(path)
    assert expected == actual

def test_webpage_view_path():
    customer_id = "whelk"
    ad_group_id = "octopus"
    criterion_id = "oyster"
    expected = "customers/{customer_id}/webpageViews/{ad_group_id}~{criterion_id}".format(customer_id=customer_id, ad_group_id=ad_group_id, criterion_id=criterion_id, )
    actual = SearchAds360ServiceClient.webpage_view_path(customer_id, ad_group_id, criterion_id)
    assert expected == actual


def test_parse_webpage_view_path():
    expected = {
        "customer_id": "nudibranch",
        "ad_group_id": "cuttlefish",
        "criterion_id": "mussel",
    }
    path = SearchAds360ServiceClient.webpage_view_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_webpage_view_path(path)
    assert expected == actual

def test_common_billing_account_path():
    billing_account = "winkle"
    expected = "billingAccounts/{billing_account}".format(billing_account=billing_account, )
    actual = SearchAds360ServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "nautilus",
    }
    path = SearchAds360ServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_common_billing_account_path(path)
    assert expected == actual

def test_common_folder_path():
    folder = "scallop"
    expected = "folders/{folder}".format(folder=folder, )
    actual = SearchAds360ServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "abalone",
    }
    path = SearchAds360ServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_common_folder_path(path)
    assert expected == actual

def test_common_organization_path():
    organization = "squid"
    expected = "organizations/{organization}".format(organization=organization, )
    actual = SearchAds360ServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "clam",
    }
    path = SearchAds360ServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_common_organization_path(path)
    assert expected == actual

def test_common_project_path():
    project = "whelk"
    expected = "projects/{project}".format(project=project, )
    actual = SearchAds360ServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "octopus",
    }
    path = SearchAds360ServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_common_project_path(path)
    assert expected == actual

def test_common_location_path():
    project = "oyster"
    location = "nudibranch"
    expected = "projects/{project}/locations/{location}".format(project=project, location=location, )
    actual = SearchAds360ServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "cuttlefish",
        "location": "mussel",
    }
    path = SearchAds360ServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = SearchAds360ServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.SearchAds360ServiceTransport, '_prep_wrapped_messages') as prep:
        client = SearchAds360ServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.SearchAds360ServiceTransport, '_prep_wrapped_messages') as prep:
        transport_class = SearchAds360ServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close():
    transports = {
        "grpc": "_grpc_channel",
    }

    for transport, close_name in transports.items():
        client = SearchAds360ServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        with mock.patch.object(type(getattr(client.transport, close_name)), "close") as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()

def test_client_ctx():
    transports = [
        'grpc',
    ]
    for transport in transports:
        client = SearchAds360ServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()
