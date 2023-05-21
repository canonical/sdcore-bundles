# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Classes describing the content of each of the bundle variants."""

from applications import UPF, GrafanaAgent
from lib.charm_bundle_generator import CharmBundle, Relation


class SDCoreUP(CharmBundle):
    """SDCORE User Plane Bundle."""

    def __init__(self, local: bool, channel: str):
        upf = UPF(local=local, channel=channel)
        grafana_agent = GrafanaAgent()
        super().__init__(
            description="The SDCORE User Plane bundle contains the 5G User Plane Function (UPF).",
            name="sdcore-up",
            applications=[
                upf,
                grafana_agent,
            ],
            relations=[
                Relation(
                    app_1_name=upf.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                )
            ],
        )
