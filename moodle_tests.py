import unittest
import moodle_locators as locators
import moodle_methods as methods


class MoodleAppPositiveTestCases(unittest.TestCase):  # Create Class

    @staticmethod  # signal to unittest this is a  statix method
    def test_create_new_user():
        methods.setUp()
        methods.log_in(locators.admin_userename, locators.admin_password)
        methods.create_new_user()
        methods.search_user()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_new_user_can_login()
        methods.log_out()
        methods.log_in(locators.admin_userename, locators.admin_password)
        methods.delete_user()
        methods.log_out()
        methods.tearDown()
