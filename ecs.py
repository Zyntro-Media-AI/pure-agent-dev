from __future__ import annotations

from app.providers.base import ComputeProvider
from app.providers.byteplus.client import BytePlusECSClient


class BytePlusECSProvider(ComputeProvider):

    def __init__(self, client: BytePlusECSClient) -> None:
        self._client = client

    async def run_instance(
        self,
        image_id: str,
        instance_type: str,
        command: str | None = None,
    ) -> str:

        # SDK request/model construction stays here.
        #
        # Exact generated model names should be locked
        # against the installed SDK version.

        request = self._build_run_instances_request(
            image_id=image_id,
            instance_type=instance_type,
            command=command,
        )

        response = self._client.api.run_instances(
            request
        )

        return self._extract_instance_id(response)
