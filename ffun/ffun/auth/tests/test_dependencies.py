from unittest import mock

import pytest
from starlette.datastructures import Headers

from ffun.auth.dependencies import _idp_user
from ffun.auth.settings import settings, single_user_service_id
from ffun.users import domain as u_domain


class TestIdPUser:
    user_accessor = staticmethod(_idp_user)  # type: ignore

    @pytest.mark.asyncio
    async def test_ignores_headers_and_forces_single_user(self) -> None:
        request = mock.MagicMock()

        request.headers = Headers({
            settings.header_user_id: "other-user",
            settings.header_identity_provider_id: "other-idp",
        })

        user = await self.user_accessor(request)  # type: ignore

        external_ids = await u_domain.get_user_external_ids(user.id)

        assert external_ids == {single_user_service_id: settings.force_external_user_id}

    @pytest.mark.asyncio
    async def test_no_headers_still_returns_user(self) -> None:
        request = mock.MagicMock()

        request.headers = Headers({})

        user = await self.user_accessor(request)  # type: ignore

        external_ids = await u_domain.get_user_external_ids(user.id)

        assert external_ids == {single_user_service_id: settings.force_external_user_id}
