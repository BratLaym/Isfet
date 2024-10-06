users_roles = """
    "user_id" INTAGER NOT NULL,
    "role_id" INTAGER NOT NULL,
    PRIMARY KEY ("user_id", "role_id"),
    FOREIGN KEY ("user_id") REFERENCES users("id")
    """
