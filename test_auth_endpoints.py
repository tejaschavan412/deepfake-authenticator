import os
import sys

# Add backend directory to sys.path
sys.path.insert(0, "/home/arham/Documents/DeepFake/backend")

from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def run_tests():
    test_email = f"test_{uuid.uuid4()}@example.com"
    test_password = "password123"
    test_username = f"user_{uuid.uuid4()}"

    print("--- Starting Auth Endpoint Tests ---")

    # 1. Register with valid email
    print(f"1. Registering with valid email: {test_email}")
    res = client.post("/auth/register", json={
        "username": test_username,
        "email": test_email,
        "password": test_password
    })
    print(f"   Status: {res.status_code}")
    assert res.status_code == 201

    # 2. Register with invalid email
    print("2. Registering with invalid email")
    res = client.post("/auth/register", json={
        "username": f"user_{uuid.uuid4()}",
        "email": "not-an-email",
        "password": test_password
    })
    print(f"   Status: {res.status_code}")
    assert res.status_code == 422

    # 3. Register with existing email
    print("3. Registering with existing email")
    res = client.post("/auth/register", json={
        "username": f"user2_{uuid.uuid4()}",
        "email": test_email,
        "password": test_password
    })
    print(f"   Status: {res.status_code}")
    assert res.status_code in [400, 409]

    # 4. Login with correct password
    print("4. Login with correct password")
    res = client.post("/auth/login", data={
        "username": test_email,
        "password": test_password
    })
    print(f"   Status: {res.status_code}")
    assert res.status_code == 200
    token = res.json()["access_token"]
    
    # 5. Login with wrong password
    print("5. Login with wrong password")
    res = client.post("/auth/login", data={
        "username": test_email,
        "password": "wrongpassword"
    })
    print(f"   Status: {res.status_code}")
    assert res.status_code == 401

    # 6. GET /auth/me with valid JWT
    print("6. GET /auth/me with valid JWT")
    res = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    print(f"   Status: {res.status_code}")
    assert res.status_code == 200
    assert res.json()["email"] == test_email

    # 7. GET /auth/me without JWT
    print("7. GET /auth/me without JWT")
    res = client.get("/auth/me")
    print(f"   Status: {res.status_code}")
    assert res.status_code == 401

    print("--- All tests completed successfully! ---")

if __name__ == "__main__":
    run_tests()
