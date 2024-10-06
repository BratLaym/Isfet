from main.static.permissions import (
    GIVE_ROLE
)

ADMIN = 0
STAFF = 1
HEAD_C = 2
SECTOR = 3

ROLES_PREMISSION: dict[int, list, int] = {
    ADMIN: [GIVE_ROLE]
}
