# coding=utf-8
import unittest
from queries.test_panels import Panels
from queries.test_panel import Panel
from queries.test_tags import Tags
from queries.test_ota import Ota
from queries.test_activity_log import ActivityLogTest
from queries.test_modell_list import ModellList
from queries.test_main_board_firmware_list import MainboardFirmwareList
from queries.test_user_list import UserList
from queries.test_enroll_validation import EnrollValidation
from mutations.test_update_panel_name import UpdatePanelName
from mutations.test_create_tag import CreateTag
from mutations.test_update_tag import UpdateTag
from mutations.test_delete_tag import DeleteTag
from mutations.test_execute_ota import TestExecuteOta
from mutations.test_add_panel_tags import AddPanelTags
from mutations.test_update_panel_tags import UpdatePanelTags
from mutations.test_delete_panel_tags import DeletePanelTags
from mutations.test_execute_appInstall import ExecuteAppInstall
from mutations.test_enroll_and_unenroll import EnrollAndUnenroll

suite = unittest.TestSuite()
suite.addTest(Panels('test_Panels'))
suite.addTest(Panel('test_Panel'))
suite.addTest(Tags('test_tags'))
suite.addTest(Ota('test_ota'))
suite.addTest(ActivityLogTest('test_activitylogs'))
suite.addTest(ModellList('test_modell_list'))
suite.addTest(MainboardFirmwareList('test_main_board_firmware_list'))
suite.addTest(UserList('test_user_list'))
suite.addTest(EnrollValidation('test_enrolled_panel'))
suite.addTest(EnrollValidation('test_error_SN_and_name'))
suite.addTest(EnrollValidation('test_error_SN_and_true_name'))
suite.addTest(EnrollValidation('test_existed_device_server_SN'))
suite.addTest(UpdatePanelName('test_update_panel_name'))
suite.addTest(CreateTag('test_create_tag'))
suite.addTest(UpdateTag('test_updata_tag'))
suite.addTest(DeleteTag('test_delete_tag'))
suite.addTest(TestExecuteOta('test_execute_ota'))
suite.addTest(AddPanelTags('test_add_panel_tags'))
suite.addTest(UpdatePanelTags('test_update_panel_tags'))
suite.addTest(DeletePanelTags('test_delete_panel_tags'))
suite.addTest(ExecuteAppInstall('test_executeAppInstall'))
suite.addTest(EnrollAndUnenroll('test_enroll_panel'))