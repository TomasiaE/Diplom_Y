# Тамара Егорова, 24-я когорта — Финальный проект. Инженер по тестированию плюс

# Импорт sender_stand_request, содержащий функции для отправки HTTP-запросов к API
import sender_stand_request

# Импорт data, в котором определены данные, необходимые для HTTP-запросов
import data


def test_0_get_order_by_track_success_response():
    track = sender_stand_request.post_new_order(data.body).json()["track"]
    response = sender_stand_request.get_an_order(track)
    assert response.status_code == 200
