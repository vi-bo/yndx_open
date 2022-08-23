from unittest.mock import patch

def test_classroom_post_save():
    with patch('calendars.recievers.create_layer.delay') as mock:
        ClassroomFactory()
        mock.assert_not_called()

        classroom = ClassroomFactory(calendar_enabled=True)
        mock.assert_called_once_with(course_id=classroom.course_id)

        classroom.save()
        mock.assert_called_once_with(course_id=classroom.course_id)