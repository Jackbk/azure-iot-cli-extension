# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DigitalTwinInterfacesPatch(Model):
    """DigitalTwinInterfacesPatch.

    :param interfaces: Interface(s) data to patch in the digital twin.
    :type interfaces: dict[str, ~service.models.DigitalTwinInterfacesPatchInterfacesValue]
    """

    _attribute_map = {
        'interfaces': {'key': 'interfaces', 'type': '{DigitalTwinInterfacesPatchInterfacesValue}'},
    }

    def __init__(self, interfaces=None):
        super(DigitalTwinInterfacesPatch, self).__init__()
        self.interfaces = interfaces
