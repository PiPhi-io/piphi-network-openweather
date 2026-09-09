from __future__ import annotations

from piphi_runtime_kit_python import RuntimeConfig


class DeviceConfig(RuntimeConfig):
    host: str = "api.openweathermap.org"
    alias: str | None = None
    api_key: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    units: str = "metric"
    language: str = "en"
    poll_interval_seconds: int = 600
