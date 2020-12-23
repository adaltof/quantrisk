db.createUser(
    {
	user: "quantr",
        pwd: "test123123",
        roles: [
            {
                role    : "readWrite",
                db      : "quantriskdb"
            }
        ]
    }
)
