import uuid

def new_user():
    """A user with a new name, not yet created."""
    name = "lab-" + uuid.uuid4().hex[:12]
    return {"username": name, "password": "Pizza-2026"}

# A second user with a name that is already taken is refused with 400.
def test_username_already_taken(api):
    user = new_user()
    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}

# user log in with a wrong password and get code 401
def test_login_with_wrong_password(api):
    user = new_user()
    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    wrong = {"username": user["username"], "password": "Pixxa-2024"}
    res = api.post("/api/users/token/login", json=wrong)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}

# user with empty name get 400
def test_user_with_empty_name(api):
    empty = {"username": "", "password": "Pixxa-2024"}
    res = api.post("/api/users", json=empty)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}