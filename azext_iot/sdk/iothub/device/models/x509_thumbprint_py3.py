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


class X509Thumbprint(Model):
    """X509Thumbprint.

    :param primary_thumbprint:
    :type primary_thumbprint: str
    :param secondary_thumbprint:
    :type secondary_thumbprint: str
    """

    _attribute_map = {
        'primary_thumbprint': {'key': 'primaryThumbprint', 'type': 'str'},
        'secondary_thumbprint': {'key': 'secondaryThumbprint', 'type': 'str'},
    }

    def __init__(self, *, primary_thumbprint: str=None, secondary_thumbprint: str=None, **kwargs) -> None:
        super(X509Thumbprint, self).__init__(**kwargs)
        self.primary_thumbprint = primary_thumbprint
        self.secondary_thumbprint = secondary_thumbprint
