# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.device_access
from cdp.device_access import (
    DeviceId,
    DeviceRequestPrompted,
    PromptDevice,
    RequestId
)


async def cancel_prompt(
        id_: RequestId
    ) -> None:
    '''
    Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event.

    :param id_:
    '''
    session = get_session_context('device_access.cancel_prompt')
    return await session.execute(cdp.device_access.cancel_prompt(id_))


async def disable() -> None:
    '''
    Disable events in this domain.
    '''
    session = get_session_context('device_access.disable')
    return await session.execute(cdp.device_access.disable())


async def enable() -> None:
    '''
    Enable events in this domain.
    '''
    session = get_session_context('device_access.enable')
    return await session.execute(cdp.device_access.enable())


async def select_prompt(
        id_: RequestId,
        device_id: DeviceId
    ) -> None:
    '''
    Select a device in response to a DeviceAccess.deviceRequestPrompted event.

    :param id_:
    :param device_id:
    '''
    session = get_session_context('device_access.select_prompt')
    return await session.execute(cdp.device_access.select_prompt(id_, device_id))