import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def test_criterion_1_report_exists():
    """instruction.md success criterion 1: /app/report.json exists."""
    assert REPORT_PATH.exists(), f"no report.json found at {REPORT_PATH}"


def test_criterion_2_valid_json_schema():
    """instruction.md success criterion 2: report is valid JSON with required keys."""
    data = json.loads(REPORT_PATH.read_text())
    assert isinstance(data, dict), f"report must be a JSON object, got {type(data).__name__}"
    for key in ("total_requests", "unique_ips", "top_path"):
        assert key in data, f"missing required key: {key}"


def test_criterion_3_total_requests_correct():
    """instruction.md success criterion 3: total_requests equals non-empty line count."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["total_requests"] == EXPECTED_TOTAL_REQUESTS, (
        f"total_requests: expected {EXPECTED_TOTAL_REQUESTS}, got {data['total_requests']!r}"
    )


def test_criterion_4_unique_ips_correct():
    """instruction.md success criterion 4: unique_ips equals distinct client IP count."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"unique_ips: expected {EXPECTED_UNIQUE_IPS}, got {data['unique_ips']!r}"
    )


def test_criterion_5_top_path_correct():
    """instruction.md success criterion 5: top_path is the most frequent request path."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["top_path"] == EXPECTED_TOP_PATH, (
        f"top_path: expected {EXPECTED_TOP_PATH!r}, got {data['top_path']!r}"
    )
