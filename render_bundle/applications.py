# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Classes describing the content of each of the applications used in bundles."""

from lib.charm_bundle_generator import Application, Resource


class UPF(Application):
    """UPF Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="bessd-image",
                value="omecproject/upf-epc-bess:master-5786085",
            ),
            Resource(
                name="routectl-image",
                value="omecproject/upf-epc-bess:master-5786085",
            ),
            Resource(
                name="web-image",
                value="omecproject/upf-epc-bess:master-5786085",
            ),
            Resource(
                name="pfcp-agent-image",
                value="omecproject/upf-epc-pfcpiface:master-5786085",
            ),
        ]
        super().__init__(
            name="upf",
            charm="sdcore-upf_ubuntu-22.04-amd64.charm" if local else "sdcore-upf",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class GrafanaAgent(Application):
    """Grafana Agent Application."""

    def __init__(self):
        super().__init__(
            name="grafana-agent-k8s", charm="grafana-agent-k8s", channel="latest/stable"
        )
