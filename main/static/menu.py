from main.static.permissions import GIVE_ROLE

HIERARCHY: dict[str, list[str] | int] = {
    "root": ["give role"],
    "give role": GIVE_ROLE
}
