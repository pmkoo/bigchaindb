"""Database configuration functions."""
from functools import singledispatch


@singledispatch
def get_config(connection, *, table):
    raise NotImplementedError


@singledispatch
def reconfigure(connection, *, table, shards, replicas, **kwargs):
    raise NotImplementedError


@singledispatch
def set_shards(connection, *, shards):
    raise NotImplementedError


@singledispatch
def set_replicas(connection, *, replicas):
    raise NotImplementedError
