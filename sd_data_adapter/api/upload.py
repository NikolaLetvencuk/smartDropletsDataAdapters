from typing import Union

from ngsildclient.api.batch import BatchResult

from ..client import DAClient
from ..models import to_ngsi_ld, SmartDataModel, to_object


def upload(obj: SmartDataModel) -> Union[bool, BatchResult]:
    if not isinstance(obj, SmartDataModel):
        raise TypeError(f'Expected a SmartDataModel, got {type(obj)}')

    if obj is None:
        raise ValueError('Object cannot be None')

    with DAClient.get_instance() as client:
        entity = to_ngsi_ld(obj)
        print(f"Saving {entity.id} !")
        return client.create(entity)