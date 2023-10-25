from django.test import TestCase
from education.models import (Course, Favourites_Course,
                              Favourites_Kindergartens, Favourites_School,
                              Kindergartens, School)
from user.models import MyUser

print('tests started')


class MyUserModelTestCase(TestCase):
    """USER TESTS"""
    def setUp(self) -> None:
        print(f'{self.__class__.__name__} tests started')
        return super().setUp()

    def test_create_user(self):
        user = MyUser.objects.create(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            phone="+123456789",
            child_first_name="Test Child",
            child_last_name="Child",
        )

        retrieved_user = MyUser.objects.get(pk=user.pk)

        self.assertEqual(retrieved_user.username, "testuser")
        self.assertEqual(retrieved_user.password, "testpassword")
        self.assertEqual(retrieved_user.email, "test@example.com")
        self.assertEqual(retrieved_user.first_name, "Test")
        self.assertEqual(retrieved_user.last_name, "User")
        self.assertEqual(retrieved_user.phone, "+123456789")
        self.assertEqual(retrieved_user.child_first_name, "Test Child")
        self.assertEqual(retrieved_user.child_last_name, "Child")


class SchoolModelTestCase(TestCase):
    '''SCHOOL MODEL TESTS'''
    def setUp(self):
        print(f'{self.__class__.__name__} tests started')
        # Create a School instance
        self.school = School.objects.create(
            name="Test School",
            description="Test description",
            working_hours="Test working hours",
            telephone="123456789",
            address="Test address",
            email="test@example.com",
            underground="Test underground",
            area="Test area",
            price=100,
            age="Test age",
            price_of_year=1000,
            classes="Test classes",
            name_author="Test author",
            languages="Test languages",
            profile="Test profile",
        )

    def test_school_str(self):
        # Retrieve the created school from the database
        retrieved_school = School.objects.get(pk=self.school.pk)

        # Assert that the retrieved school's
        # string representation is the same as the name
        self.assertEqual(str(retrieved_school), self.school.name)


class FavouritesSchoolModelTestCase(TestCase):
    '''SCHOOL FAVORITE MODEL TESTS'''
    def setUp(self):
        print(f'{self.__class__.__name__} tests started')
        # Create a MyUser instance
        self.user = MyUser.objects.create(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            phone="+123456789",
        )

        # Create a School instance
        self.school = School.objects.create(
            name="Test School",
            description="Test description",
            working_hours="Test working hours",
            telephone="123456789",
            address="Test address",
            email="test@example.com",
            underground="Test underground",
            area="Test area",
            price=100,
            age="Test age",
            price_of_year=1000,
            classes="Test classes",
            name_author="Test author",
            languages="Test languages",
            profile="Test profile",
        )

    def test_create_favourite_school(self):
        # Create a Favourites_School instance
        favourite_school = Favourites_School.objects.create(
            user=self.user, school=self.school
        )

        # Retrieve the created favourite school from the database
        retrieved_favourite_school = Favourites_School.objects.get(
            pk=favourite_school.pk
        )

        # Assert that the retrieved favourite school
        # has the same user and school as the created one
        self.assertEqual(retrieved_favourite_school.user, self.user)
        self.assertEqual(retrieved_favourite_school.school, self.school)


class KindergartensModelTestCase(TestCase):
    '''KINDERGARTENS MODEL TESTS'''
    def setUp(self):
        # Create a Kindergartens instance
        print(f'{self.__class__.__name__} tests started')
        self.kindergarten = Kindergartens.objects.create(
            name="Test Kindergarten",
            description="Test description",
            telephone="123456789",
            address="Test address",
            email="test@example.com",
            underground="Test underground",
            area="Test area",
            price=100,
            age="Test age",
            price_of_year=1000,
            working_hours="Test working hours",
            group_suze="Test group size",
            languages="Test languages",
            sport_dev="Test sport development",
            create_dev="Test creative development",
            music_dev="Test music development",
            intel_dev="Test intellectual development",
        )

    def test_kindergarten_str(self):
        # Retrieve the created kindergarten from the database
        retrieved_kindergarten = Kindergartens.objects.get(
            pk=self.kindergarten.pk
        )

        # Assert that the retrieved kindergarten's
        # string representation is the same as the name
        self.assertEqual(str(retrieved_kindergarten), self.kindergarten.name)


class FavouritesKindergartensModelTestCase(TestCase):
    '''KINDERGARTENS FAVORITE MODEL TESTS'''
    def setUp(self):
        # Create a MyUser instance
        print(f'{self.__class__.__name__} tests started')
        self.user = MyUser.objects.create(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            phone="+123456789",
        )

        # Create a Kindergartens instance
        self.kindergarten = Kindergartens.objects.create(
            name="Test Kindergarten",
            description="Test description",
            telephone="123456789",
            address="Test address",
            email="test@example.com",
            underground="Test underground",
            area="Test area",
            price=100,
            age="Test age",
            price_of_year=1000,
            working_hours="Test working hours",
            group_suze="Test group size",
            languages="Test languages",
            sport_dev="Test sport development",
            create_dev="Test creative development",
            music_dev="Test music development",
            intel_dev="Test intellectual development",
        )

    def test_create_favourite_kindergarten(self):
        # Create a Favourites_Kindergartens instance
        favourite_kindergarten = Favourites_Kindergartens.objects.create(
            user=self.user, kindergartens=self.kindergarten
        )

        # Retrieve the created favourite kindergarten from the database
        retrieved_favourite_kindergarten = (
            Favourites_Kindergartens.objects.get(
                pk=favourite_kindergarten.pk
                )
            )

        # Assert that the retrieved favourite kindergarten
        # has the same user and kindergarten as the created one
        self.assertEqual(retrieved_favourite_kindergarten.user, self.user)
        self.assertEqual(
            retrieved_favourite_kindergarten.kindergartens, self.kindergarten
        )


class CourseModelTestCase(TestCase):
    '''COURSE MODEL TESTS'''
    def setUp(self):
        # Create a Course instance
        print(f'{self.__class__.__name__} tests started')
        self.course = Course.objects.create(
            name="Test Course",
            description="Test description",
            telephone="123456789",
            address="Test address",
            email="test@example.com",
            underground="Test underground",
            area="Test area",
            price=100,
            age="Test age",
        )

    def test_course_str(self):
        # Retrieve the created course from the database
        retrieved_course = Course.objects.get(pk=self.course.pk)

        # Assert that the retrieved course's
        # string representation is the same as the name
        self.assertEqual(str(retrieved_course), self.course.name)


class FavouritesCourseModelTestCase(TestCase):
    '''COURSE FAVORITE MODEL TESTS'''
    def setUp(self):
        print(f'{self.__class__.__name__} tests started')
        # Create a MyUser instance
        self.user = MyUser.objects.create(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            phone="+123456789",
        )

        # Create a Course instance
        self.course = Course.objects.create(
            name="Test Course",
            description="Test description",
            telephone="123456789",
            address="Test address",
            email="test@example.com",
            underground="Test underground",
            area="Test area",
            price=100,
            age="Test age",
        )

    def test_create_favourite_course(self):
        # Create a Favourites_Course instance
        favourite_course = Favourites_Course.objects.create(
            user=self.user, course=self.course
        )

        # Retrieve the created favourite course from the database
        retrieved_favourite_course = Favourites_Course.objects.get(
            pk=favourite_course.pk
        )

        # Assert that the retrieved favourite course has
        # the same user and course as the created one
        self.assertEqual(retrieved_favourite_course.user, self.user)
        self.assertEqual(retrieved_favourite_course.course, self.course)
