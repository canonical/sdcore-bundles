# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Classes describing the content of each of the bundle variants."""

from applications import (
    AMF,
    AUSF,
    NMS,
    NRF,
    NSSF,
    PCF,
    SMF,
    UDM,
    UDR,
    UPF,
    GrafanaAgent,
    MongoDB,
    SelfSignedCertificates,
    Traefik,
    Webui,
)
from lib.charm_bundle_generator import CharmBundle, Relation


class SDCore(CharmBundle):
    """SD-Core Bundle for K8s."""

    def __init__(self, local: bool, channel: str):
        amf = AMF(local=local, channel=channel)
        ausf = AUSF(local=local, channel=channel)
        nms = NMS(local=local, channel=channel)
        nrf = NRF(local=local, channel=channel)
        nssf = NSSF(local=local, channel=channel)
        pcf = PCF(local=local, channel=channel)
        smf = SMF(local=local, channel=channel)
        udm = UDM(local=local, channel=channel)
        udr = UDR(local=local, channel=channel)
        upf = UPF(local=local, channel=channel)
        webui = Webui(local=local, channel=channel)
        mongodb = MongoDB()
        grafana_agent = GrafanaAgent()
        self_signed_certificates = SelfSignedCertificates()
        traefik = Traefik()
        super().__init__(
            description="The SD-Core bundle for K8s which contains applications for running a standalone 5G Core network.",  # noqa: E501
            name="sdcore-k8s",
            applications=[
                amf,
                ausf,
                nms,
                nrf,
                nssf,
                pcf,
                smf,
                udm,
                udr,
                upf,
                webui,
                mongodb,
                grafana_agent,
                self_signed_certificates,
                traefik,
            ],
            relations=[
                Relation(
                    app_1_name=amf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=amf.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=amf.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                ),
                Relation(
                    app_1_name=amf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=ausf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=ausf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=nms.name,
                    app_2_name=traefik.name,
                    app_1_relation_name="ingress",
                    app_2_relation_name="ingress",
                ),
                Relation(
                    app_1_name=nms.name,
                    app_2_name=upf.name,
                    app_1_relation_name="fiveg_n4",
                    app_2_relation_name="fiveg_n4",
                ),
                Relation(
                    app_1_name=nms.name,
                    app_2_name=webui.name,
                    app_1_relation_name="sdcore-management",
                    app_2_relation_name="sdcore-management",
                ),
                Relation(
                    app_1_name=nrf.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=nrf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=nssf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=nssf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=pcf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=pcf.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=pcf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=smf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=smf.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=smf.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                ),
                Relation(
                    app_1_name=smf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=udm.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=udm.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="common_database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="auth_database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=webui.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="common_database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=webui.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="auth_database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=upf.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                ),
                Relation(
                    app_1_name=mongodb.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                ),
                Relation(
                    app_1_name=mongodb.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="logging",
                    app_2_relation_name="logging-provider",
                ),
            ],
        )


class SDCoreControlPlane(CharmBundle):
    """SD-Core Control Plane Bundle for K8s."""

    def __init__(self, local: bool, channel: str):
        amf = AMF(local=local, channel=channel)
        ausf = AUSF(local=local, channel=channel)
        nms = NMS(local=local, channel=channel)
        nrf = NRF(local=local, channel=channel)
        nssf = NSSF(local=local, channel=channel)
        pcf = PCF(local=local, channel=channel)
        smf = SMF(local=local, channel=channel)
        udm = UDM(local=local, channel=channel)
        udr = UDR(local=local, channel=channel)
        webui = Webui(local=local, channel=channel)
        mongodb = MongoDB()
        grafana_agent = GrafanaAgent()
        self_signed_certificates = SelfSignedCertificates()
        traefik = Traefik()
        super().__init__(
            description="The SD-Core Control Plane bundle for K8s which contains the control plane part of the 5G core network.",  # noqa: E501
            name="sdcore-control-plane-k8s",
            applications=[
                amf,
                ausf,
                nms,
                nrf,
                nssf,
                pcf,
                smf,
                udm,
                udr,
                webui,
                mongodb,
                grafana_agent,
                self_signed_certificates,
                traefik,
            ],
            relations=[
                Relation(
                    app_1_name=amf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=amf.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=amf.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                ),
                Relation(
                    app_1_name=amf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=ausf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=ausf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=nms.name,
                    app_2_name=traefik.name,
                    app_1_relation_name="ingress",
                    app_2_relation_name="ingress",
                ),
                Relation(
                    app_1_name=nms.name,
                    app_2_name=webui.name,
                    app_1_relation_name="sdcore-management",
                    app_2_relation_name="sdcore-management",
                ),
                Relation(
                    app_1_name=nrf.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=nrf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=nssf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=nssf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=pcf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=pcf.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=pcf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=smf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=smf.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                ),
                Relation(
                    app_1_name=smf.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=smf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=udm.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=udm.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg_nrf",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="common_database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="auth_database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
                ),
                Relation(
                    app_1_name=webui.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="common_database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=webui.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="auth_database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=mongodb.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                ),
                Relation(
                    app_1_name=mongodb.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="logging",
                    app_2_relation_name="logging-provider",
                ),
            ],
        )


class SDCoreUserPlane(CharmBundle):
    """SD-Core User Plane Bundle for K8s."""

    def __init__(self, local: bool, channel: str):
        upf = UPF(local=local, channel=channel)
        grafana_agent = GrafanaAgent()
        super().__init__(
            description="The SD-Core User Plane bundle for K8s which contains the 5G User Plane Function (UPF).",  # noqa: E501
            name="sdcore-user-plane-k8s",
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
