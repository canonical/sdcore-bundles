# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Classes describing the content of each of the bundle variants."""

from applications import (
    AMF,
    AUSF,
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
    Webui,
)
from lib.charm_bundle_generator import CharmBundle, Relation


class SDCore(CharmBundle):
    """SD-Core Bundle."""

    def __init__(self, local: bool, channel: str):
        amf = AMF(local=local, channel=channel)
        ausf = AUSF(local=local, channel=channel)
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
        super().__init__(
            description="The SD-Core bundle contains applications for running a standalone 5G Core network.",  # noqa: E501
            name="sdcore",
            applications=[
                amf,
                ausf,
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
            ],
            relations=[
                Relation(
                    app_1_name=amf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
                ),
                Relation(
                    app_1_name=ausf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
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
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
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
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
                Relation(
                    app_1_name=upf.name,
                    app_2_name=grafana_agent.name,
                    app_1_relation_name="metrics-endpoint",
                    app_2_relation_name="metrics-endpoint",
                ),
            ],
        )


class SDCoreControlPlane(CharmBundle):
    """SD-Core Control Plane Bundle."""

    def __init__(self, local: bool, channel: str):
        amf = AMF(local=local, channel=channel)
        ausf = AUSF(local=local, channel=channel)
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
        super().__init__(
            description="The SD-Core Control Plane bundle contains the control plane part of the 5G core network.",  # noqa: E501
            name="sdcore-control-plane",
            applications=[
                amf,
                ausf,
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
            ],
            relations=[
                Relation(
                    app_1_name=amf.name,
                    app_2_name=nrf.name,
                    app_1_relation_name="fiveg_nrf",
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
                ),
                Relation(
                    app_1_name=ausf.name,
                    app_2_name=self_signed_certificates.name,
                    app_1_relation_name="certificates",
                    app_2_relation_name="certificates",
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
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
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
                    app_2_relation_name="fiveg-nrf",
                ),
                Relation(
                    app_1_name=udr.name,
                    app_2_name=mongodb.name,
                    app_1_relation_name="database",
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
                    app_1_relation_name="database",
                    app_2_relation_name="database",
                ),
            ],
        )


class SDCoreUserPlane(CharmBundle):
    """SD-Core User Plane Bundle."""

    def __init__(self, local: bool, channel: str):
        upf = UPF(local=local, channel=channel)
        grafana_agent = GrafanaAgent()
        super().__init__(
            description="The SD-Core User Plane bundle contains the 5G User Plane Function (UPF).",
            name="sdcore-user-plane",
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
