"""Machine-grown domains — the hourly GitHub Action (ragpull grow) appends verified,
gate-passing Wikipedia topics to auto_domains.json; this module folds them into the registry
so they are permanent, first-class packs (no manual wiring). Empty until the grower runs."""

import json
from pathlib import Path

_JSON = Path(__file__).with_name("auto_domains.json")

DOMAINS = {}
if _JSON.exists():
    try:
        for _d in json.loads(_JSON.read_text(encoding="utf-8")):
            _name = _d.get("name")
            if _name and _d.get("pages"):
                DOMAINS[_name] = {"tags": _d.get("tags", []), "license": _d.get("license", "CC-BY-SA-4.0"),
                                  "pages": _d["pages"]}
    except Exception:
        DOMAINS = {}
