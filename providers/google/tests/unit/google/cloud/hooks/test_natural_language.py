#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from typing import Any
from unittest import mock

from google.api_core.gapic_v1.method import DEFAULT
from google.cloud.language_v1 import Document

from airflow.providers.google.cloud.hooks.natural_language import CloudNaturalLanguageHook
from airflow.providers.google.common.consts import CLIENT_INFO

from unit.google.cloud.utils.base_gcp_mock import mock_base_gcp_hook_no_default_project_id

API_RESPONSE: dict[Any, Any] = {}
DOCUMENT = Document(
    content="Airflow is a platform to programmatically author, schedule and monitor workflows."
)
ENCODING_TYPE = "UTF32"


class TestCloudNaturalLanguageHook:
    def setup_method(self):
        with mock.patch(
            "airflow.providers.google.common.hooks.base_google.GoogleBaseHook.__init__",
            new=mock_base_gcp_hook_no_default_project_id,
        ):
            self.hook = CloudNaturalLanguageHook(gcp_conn_id="test")

    @mock.patch(
        "airflow.providers.google.cloud.hooks.natural_language.CloudNaturalLanguageHook.get_credentials"
    )
    @mock.patch("airflow.providers.google.cloud.hooks.natural_language.LanguageServiceClient")
    def test_language_service_client_creation(self, mock_client, mock_get_creds):
        result = self.hook.get_conn()
        mock_client.assert_called_once_with(credentials=mock_get_creds.return_value, client_info=CLIENT_INFO)
        assert mock_client.return_value == result
        assert self.hook._conn == result

    @mock.patch(
        "airflow.providers.google.cloud.hooks.natural_language.CloudNaturalLanguageHook.get_conn",
    )
    def test_analyze_entities(self, get_conn):
        get_conn.return_value.analyze_entities.return_value = API_RESPONSE
        result = self.hook.analyze_entities(document=DOCUMENT, encoding_type=ENCODING_TYPE)

        assert result == API_RESPONSE

        get_conn.return_value.analyze_entities.assert_called_once_with(
            document=DOCUMENT, encoding_type=ENCODING_TYPE, retry=DEFAULT, timeout=None, metadata=()
        )

    @mock.patch(
        "airflow.providers.google.cloud.hooks.natural_language.CloudNaturalLanguageHook.get_conn",
    )
    def test_analyze_entity_sentiment(self, get_conn):
        get_conn.return_value.analyze_entity_sentiment.return_value = API_RESPONSE
        result = self.hook.analyze_entity_sentiment(document=DOCUMENT, encoding_type=ENCODING_TYPE)

        assert result == API_RESPONSE

        get_conn.return_value.analyze_entity_sentiment.assert_called_once_with(
            document=DOCUMENT, encoding_type=ENCODING_TYPE, retry=DEFAULT, timeout=None, metadata=()
        )

    @mock.patch(
        "airflow.providers.google.cloud.hooks.natural_language.CloudNaturalLanguageHook.get_conn",
    )
    def test_analyze_sentiment(self, get_conn):
        get_conn.return_value.analyze_sentiment.return_value = API_RESPONSE
        result = self.hook.analyze_sentiment(document=DOCUMENT, encoding_type=ENCODING_TYPE)

        assert result == API_RESPONSE

        get_conn.return_value.analyze_sentiment.assert_called_once_with(
            document=DOCUMENT, encoding_type=ENCODING_TYPE, retry=DEFAULT, timeout=None, metadata=()
        )

    @mock.patch(
        "airflow.providers.google.cloud.hooks.natural_language.CloudNaturalLanguageHook.get_conn",
    )
    def test_analyze_syntax(self, get_conn):
        get_conn.return_value.analyze_syntax.return_value = API_RESPONSE
        result = self.hook.analyze_syntax(document=DOCUMENT, encoding_type=ENCODING_TYPE)

        assert result == API_RESPONSE

        get_conn.return_value.analyze_syntax.assert_called_once_with(
            document=DOCUMENT, encoding_type=ENCODING_TYPE, retry=DEFAULT, timeout=None, metadata=()
        )

    @mock.patch(
        "airflow.providers.google.cloud.hooks.natural_language.CloudNaturalLanguageHook.get_conn",
    )
    def test_annotate_text(self, get_conn):
        get_conn.return_value.annotate_text.return_value = API_RESPONSE
        result = self.hook.annotate_text(document=DOCUMENT, encoding_type=ENCODING_TYPE, features=None)

        assert result == API_RESPONSE

        get_conn.return_value.annotate_text.assert_called_once_with(
            document=DOCUMENT,
            encoding_type=ENCODING_TYPE,
            features=None,
            retry=DEFAULT,
            timeout=None,
            metadata=(),
        )

    @mock.patch(
        "airflow.providers.google.cloud.hooks.natural_language.CloudNaturalLanguageHook.get_conn",
    )
    def test_classify_text(self, get_conn):
        get_conn.return_value.classify_text.return_value = API_RESPONSE
        result = self.hook.classify_text(document=DOCUMENT)

        assert result == API_RESPONSE

        get_conn.return_value.classify_text.assert_called_once_with(
            document=DOCUMENT, retry=DEFAULT, timeout=None, metadata=()
        )
