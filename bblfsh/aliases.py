import importlib
import google
import typing

# "in" is a reserved keyword in Python thus can't be used as package name, so
# we import by string

uast_v2_module = importlib.import_module("bblfsh.gopkg.in.bblfsh.sdk.v2.uast.generated_pb2")
protocol_v2_module = importlib.import_module("bblfsh.gopkg.in.bblfsh.sdk.v2.protocol.generated_pb2")
protocol_grpc_v2_module = importlib.import_module("bblfsh.gopkg.in.bblfsh.sdk.v2.protocol.generated_pb2_grpc")
protocol_v1_module = importlib.import_module("bblfsh.gopkg.in.bblfsh.sdk.v1.protocol.generated_pb2")
protocol_grpc_v1_module = importlib.import_module("bblfsh.gopkg.in.bblfsh.sdk.v1.protocol.generated_pb2_grpc")

DESCRIPTOR = uast_v2_module.DESCRIPTOR
ParseRequest = protocol_v2_module.ParseRequest
ParseResponse = protocol_v2_module.ParseResponse
ParseError = protocol_v2_module.ParseError
Mode = protocol_v2_module.Mode
ModeType = google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper
DriverStub = protocol_grpc_v2_module.DriverStub
DriverServicer = protocol_grpc_v2_module.DriverServicer

VersionRequest = protocol_v1_module.VersionRequest
SupportedLanguagesRequest = protocol_v1_module.SupportedLanguagesRequest
SupportedLanguagesResponse = protocol_v1_module.SupportedLanguagesResponse
ProtocolServiceStub = protocol_grpc_v1_module.ProtocolServiceStub
