from __future__ import annotations

import json

from piphi_network_openweather.schemas import DeviceConfig
from piphi_network_openweather.state import _split_config, make_entry


def test_api_key_is_kept_out_of_persisted_and_serialized_config() -> None:
    config = DeviceConfig(id="weather-test", api_key="top-secret")

    public, secrets = _split_config(config)
    entry = make_entry(config)

    assert "api_key" not in public
    assert secrets == {"api_key": "top-secret"}
    assert "top-secret" not in json.dumps(entry)
