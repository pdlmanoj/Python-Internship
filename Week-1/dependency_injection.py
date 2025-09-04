class UserService:
    def __init__(self, db):
        # Dependency is injected from outside
        self.db = db

    def get_users(self):
        return self.db.query("SELECT * FROM users")


# Example dependencies
class DatabaseConnection:
    def __init__(self, url):
        self.url = url
    def query(self, sql):
        return f"Querying {sql} on {self.url}"


# Inject a real DB
real_db = DatabaseConnection("prod-db-url")
service = UserService(real_db)
print(service.get_users())

# Inject a fake DB for testing
class FakeDB:
    def query(self, sql):
        return ["test_user1", "test_user2"]

test_service = UserService(FakeDB())
print(test_service.get_users())
