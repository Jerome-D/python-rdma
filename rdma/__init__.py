#!/usr/bin/python

import os;

class RDMAError(Exception):
    '''General exception class for RDMA related errors'''

_cached_devices = None;
def get_rdma_devices(refresh = False):
    '''Return a container of RDMADevice objects for all devices in the system'''
    global _cached_devices;
    if _cached_devices and not refresh:
        return _cached_devices;

    import rdma.devices;
    _cached_devices = rdma.devices.DemandList2(
        rdma.devices.SYS_INFINIBAND,
        lambda x:rdma.devices.RDMADevice(x),
        lambda x:x);
    return _cached_devices;

def get_umad(port,**kwargs):
    '''Create a umad instance for the associated EndPort'''
    import rdma.umad;
    return rdma.umad.UMad(port,**kwargs);

def get_verbs(port,**kwargs):
    '''Create a UVerbs instance for the associated Device/EndPort'''
    import rdma.uverbs;
    return rdma.uverbs.UVerbs(port,**kwargs);
