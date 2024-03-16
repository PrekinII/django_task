import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def student(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return student


@pytest.fixture
def course_factory():
    def course(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return course


@pytest.mark.django_db
def test_get_course_r(client, student_factory, course_factory):  # проверка получения первого курса (retrieve-логика)
    # Arrange
    courses = course_factory(_quantity=10)
    students = student_factory(_quantity=10)
    # Act
    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_get_course_l(client, course_factory):  # проверка получения списка курсов (list-логика)
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.get(f'/api/v1/courses/')
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_get_course_filter(client, course_factory):  # проверка фильтрации списка курсов по id
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.get(f'/api/v1/courses/', data={'id': courses[5].id})
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert data[0]['name'] == courses[5].name


@pytest.mark.django_db
def test_get_course_filter(client, course_factory):  # проверка фильтрации списка курсов по name
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.get(f'/api/v1/courses/', data={'name': courses[5].name})
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert data[0]['name'] == courses[5].name
    assert len(data) == 1


@pytest.mark.django_db
def test_patch_course(client, course_factory):  # тест успешного обновления курса
    # Arrange
    courses = course_factory(_quantity=10)
    course_patch = {'name': 'Нетология'}
    # Act
    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data=course_patch)
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert data['name'] == course_patch['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):  # тест успешного удаления курса
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.delete(f'/api/v1/courses/{courses[0].id}/')
    # Assert
    assert response.status_code == 204


@pytest.mark.django_db
def test_create_course_1(client):  # тест успешного создания курса
    # Arrange
    count = Course.objects.count()
    course = {'name': 'Нетология'}
    # Act
    response = client.post('/api/v1/courses/', data=course)
    data = response.json()
    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert data['name'] == 'Нетология'


#test_courses_api.py
@pytest.mark.parametrize(
    'students_count,status_code', [
    (19, 201),
    (20, 201),
    (21, 400)
    ]
)
@pytest.mark.django_db
def test_max_students_at_course(client, students_factory, students_count, status_code):
    #Arrange
    students = students_factory(_quantity=students_count)
    student_ids = [stud.id for stud in students]
    data = {"name": 'Test', "students": student_ids}
    response = client.post('/api/v1/courses/', data=data)
    assert response.status_code == status_code