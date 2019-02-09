STATE_QUOTE = "0"
STATE_ANALYZE = "1"
STATE_ACCEPT = "2"
STATE_DENY = "3"

STATE_MAP = {
    STATE_QUOTE: _("Quote"),
    STATE_ANALYZE: _("Analyze"),
    STATE_ACCEPT: _("Accept"),
    STATE_DENY: _("Deny"),
}

STATE_LIST = [
    STATE_MAP[STATE_QUOTE],
    STATE_MAP[STATE_ANALYZE],
    STATE_MAP[STATE_ACCEPT],
    STATE_MAP[STATE_DENY],
]