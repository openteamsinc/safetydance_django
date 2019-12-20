from safetydance_test import TestStepPrefix
from safetydance_test.step_extension import all_steps_as_step_extensions_from
from type_extensions import extension_property
from . import steps


class Http:
    '''
    Context and steps for interacting with HTTP web services.
    '''
    ...


_HTTP = Http()

@extension_property
def http(self: TestStepPrefix) -> Http:
    return _HTTP


all_steps_as_step_extensions_from(steps, target_type=Http)
