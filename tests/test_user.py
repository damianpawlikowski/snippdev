from snippdev.user.models import User


def test_register_user(app, client):
    response = client.post(
        "/api/user",
        json={
            "email": "tester@email.com",
            "password": "secret?@",
        },
        follow_redirects=True
    )

    assert response.status_code == 201

    with app.app_context():
        assert User.query.filter(
            User.email == "tester@email.com"
        ).first() is not None
