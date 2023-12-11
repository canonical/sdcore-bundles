# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Classes describing the content of each of the applications used in bundles."""

from lib.charm_bundle_generator import Application, Resource


class AMF(Application):
    """SD-Core AMF Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="amf-image",
                value="ghcr.io/canonical/sdcore-amf:1.3",
            )
        ]
        super().__init__(
            name="amf",
            charm="sdcore-amf-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-amf-k8s",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class AUSF(Application):
    """SD-Core AUSF Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="ausf-image",
                value="ghcr.io/canonical/sdcore-ausf:1.3",
            )
        ]
        super().__init__(
            name="ausf",
            charm="sdcore-ausf-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-ausf-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class NMS(Application):
    """SD-Core NMS Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="nms-image",
                value="ghcr.io/canonical/sdcore-nms:0.2.0",
            )
        ]
        super().__init__(
            name="nms",
            charm="sdcore-nms-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-nms-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class NRF(Application):
    """SD-Core NRF Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="nrf-image",
                value="ghcr.io/canonical/sdcore-nrf:1.3",
            )
        ]
        super().__init__(
            name="nrf",
            charm="sdcore-nrf-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-nrf-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class NSSF(Application):
    """SD-Core NSSF Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="nssf-image",
                value="ghcr.io/canonical/sdcore-nssf:1.3",
            )
        ]
        super().__init__(
            name="nssf",
            charm="sdcore-nssf-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-nssf-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class PCF(Application):
    """SD-Core PCF Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="pcf-image",
                value="ghcr.io/canonical/sdcore-pcf:1.3",
            )
        ]
        super().__init__(
            name="pcf",
            charm="sdcore-pcf-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-pcf-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class SMF(Application):
    """SD-Core SMF Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="smf-image",
                value="ghcr.io/canonical/sdcore-smf:1.3",
            )
        ]
        super().__init__(
            name="smf",
            charm="sdcore-smf-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-smf-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class UDM(Application):
    """SD-Core UDM Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="udm-image",
                value="ghcr.io/canonical/sdcore-udm:1.3",
            )
        ]
        super().__init__(
            name="udm",
            charm="sdcore-udm-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-udm-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class UDR(Application):
    """SD-Core UDR Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="udr-image",
                value="ghcr.io/canonical/sdcore-udr:1.3",
            )
        ]
        super().__init__(
            name="udr",
            charm="sdcore-udr-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-udr-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class UPF(Application):
    """SD-Core UPF Application for K8s."""

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
            charm="sdcore-upf-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-upf-k8s",
            trust=True,
            channel=None if local else channel,
            resources=resources if local else None,
        )


class Webui(Application):
    """SD-Core Webui Application for K8s."""

    def __init__(self, local: bool, channel: str):
        resources = [
            Resource(
                name="webui-image",
                value="ghcr.io/canonical/sdcore-webui:1.3",
            )
        ]
        super().__init__(
            name="webui",
            charm="sdcore-webui-k8s_ubuntu-22.04-amd64.charm" if local else "sdcore-webui-k8s",
            channel=None if local else channel,
            resources=resources if local else None,
        )


class MongoDB(Application):
    """MongoDB Application for K8s."""

    def __init__(self):
        super().__init__(
            name="mongodb-k8s",
            charm="mongodb-k8s",
            channel="5/edge",
            trust=True,
        )


class GrafanaAgent(Application):
    """Grafana Agent Application for K8s."""

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


class Traefik(Application):
    """Traefik Application for K8s."""

    def __init__(self):
        super().__init__(
            name="traefik-k8s",
            charm="traefik-k8s",
            channel="latest/stable",
            trust=True,
            options={"routing_mode": "subdomain"},
        )
