# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Classes describing the content of each of the applications used in bundles."""

from lib.charm_bundle_generator import Application, Resource


class AMF(Application):
    """SD-Core AMF Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="amf-image",
                value="ghcr.io/canonical/sdcore-amf:1.3",
            )
        ]
        super().__init__(
            name="amf",
            charm="sdcore-amf_ubuntu-22.04-amd64.charm" if local else "sdcore-amf",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class AUSF(Application):
    """SD-Core AUSF Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="ausf-image",
                value="ghcr.io/canonical/sdcore-ausf:1.3",
            )
        ]
        super().__init__(
            name="ausf",
            charm="sdcore-ausf_ubuntu-22.04-amd64.charm" if local else "sdcore-ausf",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class NRF(Application):
    """SD-Core NRF Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="nrf-image",
                value="ghcr.io/canonical/sdcore-nrf:1.3",
            )
        ]
        super().__init__(
            name="nrf",
            charm="sdcore-nrf_ubuntu-22.04-amd64.charm" if local else "sdcore-nrf",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class NSSF(Application):
    """SD-Core NSSF Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="nssf-image",
                value="ghcr.io/canonical/sdcore-nssf:1.3",
            )
        ]
        super().__init__(
            name="nssf",
            charm="sdcore-nssf_ubuntu-22.04-amd64.charm" if local else "sdcore-nssf",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class PCF(Application):
    """SD-Core PCF Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="pcf-image",
                value="ghcr.io/canonical/sdcore-pcf:1.3",
            )
        ]
        super().__init__(
            name="pcf",
            charm="sdcore-pcf_ubuntu-22.04-amd64.charm" if local else "sdcore-pcf",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class SMF(Application):
    """SD-Core SMF Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="smf-image",
                value="ghcr.io/canonical/sdcore-smf:1.3",
            )
        ]
        super().__init__(
            name="smf",
            charm="sdcore-smf_ubuntu-22.04-amd64.charm" if local else "sdcore-smf",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class UDM(Application):
    """SD-Core UDM Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="udm-image",
                value="ghcr.io/canonical/sdcore-udm:1.3",
            )
        ]
        super().__init__(
            name="udm",
            charm="sdcore-udm_ubuntu-22.04-amd64.charm" if local else "sdcore-udm",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class UDR(Application):
    """SD-Core UDR Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="udr-image",
                value="ghcr.io/canonical/sdcore-udr:1.3",
            )
        ]
        super().__init__(
            name="udr",
            charm="sdcore-udr_ubuntu-22.04-amd64.charm" if local else "sdcore-udr",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class UPF(Application):
    """SD-Core UPF Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="bessd-image",
                value="ghcr.io/canonical/sdcore-upf-bess:1.3",
            ),
            Resource(
                name="pfcp-agent-image",
                value="ghcr.io/canonical/sdcore-upf-pfcpiface:1.3",
            ),
        ]
        super().__init__(
            name="upf",
            charm="sdcore-upf_ubuntu-22.04-amd64.charm" if local else "sdcore-upf",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class Webui(Application):
    """SD-Core Webui Application."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="webui-image",
                value="ghcr.io/canonical/sdcore-webui:1.3",
            )
        ]
        super().__init__(
            name="webui",
            charm="sdcore-webui_ubuntu-22.04-amd64.charm" if local else "sdcore-webui",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class MongoDB(Application):
    """MongoDB Application."""

    def __init__(self):
        super().__init__(
            name="mongodb-k8s",
            charm="mongodb-k8s",
            channel="6/beta",
            trust=True,
        )


class GrafanaAgent(Application):
    """Grafana Agent Application."""

    def __init__(self):
        super().__init__(
            name="grafana-agent-k8s",
            charm="grafana-agent-k8s",
            channel="latest/stable",
        )


class SelfSignedCertificates(Application):
    """Self Signed Certificates Application."""

    def __init__(self):
        super().__init__(
            name="self-signed-certificates",
            charm="self-signed-certificates",
            channel="beta",
        )
