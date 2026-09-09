from __future__ import annotations

from typing import Any

ENDPOINTS = {
    "health": "/health",
    "diagnostics": "/diagnostics",
    "discover": "/discover",
    "entities": "/entities",
    "state": "/state",
    "config": "/config",
    "config_sync": "/config/sync",
    "deconfigure": "/deconfigure",
    "ui_config": "/ui-config",
    "events": "/events",
    "command": "/command",
}

REQUIRED_ENDPOINTS = ["health", "entities", "command", "config", "ui_config"]

CAPABILITIES: dict[str, dict[str, Any]] = {
    "connected": {"kind": "sensor", "unit": "bool"},
    "refresh": {"kind": "action"},
}

COMMANDS: dict[str, dict[str, Any]] = {
    "refresh": {
        "description": "Refresh the integration state.",
        "timeout_ms": 5000,
    },
}

CONFIG_SCHEMA: dict[str, Any] = {
    "schema": {
        "title": "PiPhi Network OpenWeather Setup",
        "type": "object",
        "required": ["host"],
        "properties": {
    "host": {
        "type": "string",
        "title": "API Host",
        "default": "api.openweathermap.org"
    },
    "alias": {
        "type": "string",
        "title": "Location Name"
    },
    "api_key": {
        "type": "string",
        "title": "API Key",
        "format": "password",
        "writeOnly": True
    },
    "latitude": {
        "type": "number",
        "title": "Latitude",
        "minimum": -90,
        "maximum": 90
    },
    "longitude": {
        "type": "number",
        "title": "Longitude",
        "minimum": -180,
        "maximum": 180
    },
    "units": {
        "type": "string",
        "title": "Units",
        "enum": [
            "standard",
            "metric",
            "imperial"
        ],
        "default": "metric"
    },
    "language": {
        "type": "string",
        "title": "Language",
        "default": "en"
    },
    "poll_interval_seconds": {
        "type": "integer",
        "title": "Poll Interval Seconds",
        "minimum": 600,
        "default": 600
    }
},
    },
    "uiSchema": {
        "host": {"placeholder": "api.openweathermap.org"},
        "alias": {"placeholder": "OpenWeather Location"},
    },
}

FALLBACK_ENTITY: dict[str, Any] = {
    "id": "openweather-location",
    "name": "OpenWeather Location",
    "device_id": "openweather-location",
    "entity_type": "weather_location",
    "capabilities": ["connected", "refresh"],
    "available_commands": [
        {"id": "refresh", "label": "Refresh", "kind": "action"},
    ],
    "dashboard": {
        "allowed_widgets": [
    "weather",
    "weather-alert-card",
    "chart",
    "stat"
],
        "default_widget": "weather",
    },
}
