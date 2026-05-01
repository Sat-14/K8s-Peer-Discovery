from pydantic.main import BaseModel

import k8speerdiscovery


class DiscoveryRequest(BaseModel):
    node: k8speerdiscovery.NodeAddress


class NodeList(BaseModel):
    nodes: list[k8speerdiscovery.NodeAddress]


class MoodResponse(BaseModel):
    mood: str


class CatchupResponse(BaseModel):
    moods: dict[str, str]
