"""pipeline_versions — pipeline capability, packaged standalone.

Contract, validation and CLI for one capability bit extracted from the
GBT V8 registry. Nothing here is invented: the spec is copied verbatim from
the registry snapshot, and the atlas page it came from is linked in the README.

    >>> from gbt_pipeline_versions import SPEC, run
    >>> SPEC.name
    'pipeline_versions'
    >>> run({"name": "<在此填写>"}).status   # doctest: +SKIP
    'validated'
"""

from .core import Result, run
from .errors import BackendRequired, CapError, PayloadError
from .spec import SPEC, CapSpec

__version__ = "1.0.0"
__all__ = [
    "SPEC",
    "CapSpec",
    "run",
    "Result",
    "CapError",
    "PayloadError",
    "BackendRequired",
    "__version__",
]
