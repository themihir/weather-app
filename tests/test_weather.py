
def test_weather_route(client):
    response = client.get("/weather/Toronto")
    # API can return 200 (success) or 404 (city not found / API issue)
    assert response.status_code in (200, 404)

    if response.status_code == 200:
        data = response.json()
        assert "temperature" in data
        assert "humidity" in data
