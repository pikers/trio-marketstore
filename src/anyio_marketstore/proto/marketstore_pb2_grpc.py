# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import marketstore_pb2 as proto_dot_marketstore__pb2


class MarketstoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Query = channel.unary_unary(
                '/proto.Marketstore/Query',
                request_serializer=proto_dot_marketstore__pb2.MultiQueryRequest.SerializeToString,
                response_deserializer=proto_dot_marketstore__pb2.MultiQueryResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/proto.Marketstore/Create',
                request_serializer=proto_dot_marketstore__pb2.MultiCreateRequest.SerializeToString,
                response_deserializer=proto_dot_marketstore__pb2.MultiServerResponse.FromString,
                )
        self.Write = channel.unary_unary(
                '/proto.Marketstore/Write',
                request_serializer=proto_dot_marketstore__pb2.MultiWriteRequest.SerializeToString,
                response_deserializer=proto_dot_marketstore__pb2.MultiServerResponse.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/proto.Marketstore/Destroy',
                request_serializer=proto_dot_marketstore__pb2.MultiKeyRequest.SerializeToString,
                response_deserializer=proto_dot_marketstore__pb2.MultiServerResponse.FromString,
                )
        self.ListSymbols = channel.unary_unary(
                '/proto.Marketstore/ListSymbols',
                request_serializer=proto_dot_marketstore__pb2.ListSymbolsRequest.SerializeToString,
                response_deserializer=proto_dot_marketstore__pb2.ListSymbolsResponse.FromString,
                )
        self.ServerVersion = channel.unary_unary(
                '/proto.Marketstore/ServerVersion',
                request_serializer=proto_dot_marketstore__pb2.ServerVersionRequest.SerializeToString,
                response_deserializer=proto_dot_marketstore__pb2.ServerVersionResponse.FromString,
                )


class MarketstoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSymbols(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketstoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=proto_dot_marketstore__pb2.MultiQueryRequest.FromString,
                    response_serializer=proto_dot_marketstore__pb2.MultiQueryResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=proto_dot_marketstore__pb2.MultiCreateRequest.FromString,
                    response_serializer=proto_dot_marketstore__pb2.MultiServerResponse.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=proto_dot_marketstore__pb2.MultiWriteRequest.FromString,
                    response_serializer=proto_dot_marketstore__pb2.MultiServerResponse.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=proto_dot_marketstore__pb2.MultiKeyRequest.FromString,
                    response_serializer=proto_dot_marketstore__pb2.MultiServerResponse.SerializeToString,
            ),
            'ListSymbols': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSymbols,
                    request_deserializer=proto_dot_marketstore__pb2.ListSymbolsRequest.FromString,
                    response_serializer=proto_dot_marketstore__pb2.ListSymbolsResponse.SerializeToString,
            ),
            'ServerVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.ServerVersion,
                    request_deserializer=proto_dot_marketstore__pb2.ServerVersionRequest.FromString,
                    response_serializer=proto_dot_marketstore__pb2.ServerVersionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.Marketstore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Marketstore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Marketstore/Query',
            proto_dot_marketstore__pb2.MultiQueryRequest.SerializeToString,
            proto_dot_marketstore__pb2.MultiQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Marketstore/Create',
            proto_dot_marketstore__pb2.MultiCreateRequest.SerializeToString,
            proto_dot_marketstore__pb2.MultiServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Marketstore/Write',
            proto_dot_marketstore__pb2.MultiWriteRequest.SerializeToString,
            proto_dot_marketstore__pb2.MultiServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Marketstore/Destroy',
            proto_dot_marketstore__pb2.MultiKeyRequest.SerializeToString,
            proto_dot_marketstore__pb2.MultiServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSymbols(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Marketstore/ListSymbols',
            proto_dot_marketstore__pb2.ListSymbolsRequest.SerializeToString,
            proto_dot_marketstore__pb2.ListSymbolsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServerVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Marketstore/ServerVersion',
            proto_dot_marketstore__pb2.ServerVersionRequest.SerializeToString,
            proto_dot_marketstore__pb2.ServerVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)