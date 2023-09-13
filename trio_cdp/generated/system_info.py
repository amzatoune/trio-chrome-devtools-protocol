# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.system_info
from cdp.system_info import (
    GPUDevice,
    GPUInfo,
    ImageDecodeAcceleratorCapability,
    ImageType,
    ProcessInfo,
    Size,
    SubsamplingFormat,
    VideoDecodeAcceleratorCapability,
    VideoEncodeAcceleratorCapability
)


async def get_feature_state(
        feature_state: str
    ) -> bool:
    '''
    Returns information about the feature state.

    :param feature_state:
    :returns: 
    '''
    session = get_session_context('system_info.get_feature_state')
    return await session.execute(cdp.system_info.get_feature_state(feature_state))


async def get_info() -> typing.Tuple[GPUInfo, str, str, str]:
    '''
    Returns information about the system.

    :returns: A tuple with the following items:

        0. **gpu** - Information about the GPUs on the system.
        1. **modelName** - A platform-dependent description of the model of the machine. On Mac OS, this is, for example, 'MacBookPro'. Will be the empty string if not supported.
        2. **modelVersion** - A platform-dependent description of the version of the machine. On Mac OS, this is, for example, '10.1'. Will be the empty string if not supported.
        3. **commandLine** - The command line string used to launch the browser. Will be the empty string if not supported.
    '''
    session = get_session_context('system_info.get_info')
    return await session.execute(cdp.system_info.get_info())


async def get_process_info() -> typing.List[ProcessInfo]:
    '''
    Returns information about all running processes.

    :returns: An array of process info blocks.
    '''
    session = get_session_context('system_info.get_process_info')
    return await session.execute(cdp.system_info.get_process_info())