# coding=utf-8
import unittest
from testcases.mdm_portal.queries.test_panels import Panels
from testcases.mdm_portal.queries.test_panel import Panel
from testcases.mdm_portal.queries.test_tags import Tags
from testcases.mdm_portal.queries.test_ota import Ota
from testcases.mdm_portal.queries.test_activity_log import ActivityLogTest
from testcases.mdm_portal.queries.test_modell_list import ModellList
from testcases.mdm_portal.queries.test_main_board_firmware_list import MainboardFirmwareList
from testcases.mdm_portal.queries.test_user_list import UserList
from testcases.mdm_portal.queries.test_enroll_validation import EnrollValidation
from testcases.mdm_portal.mutations.test_update_panel_name import UpdatePanelName
from testcases.mdm_portal.mutations.test_create_tag import CreateTag
from testcases.mdm_portal.mutations.test_update_tag import UpdateTag
from testcases.mdm_portal.mutations.test_delete_tag import DeleteTag
from testcases.mdm_portal.mutations.test_execute_ota import TestExecuteOta
from testcases.mdm_portal.mutations.test_add_panel_tags import AddPanelTags
from testcases.mdm_portal.mutations.test_update_panel_tags import UpdatePanelTags
from testcases.mdm_portal.mutations.test_delete_panel_tags import DeletePanelTags
from testcases.mdm_portal.mutations.test_execute_appInstall import ExecuteAppInstall
from testcases.mdm_portal.mutations.test_enroll_and_unenroll import EnrollAndUnenroll
from testcases.configuration.queries.test_configuration_list import ConfigurationList
from testcases.configuration.queries.test_configuration_detail import ConfigurationDetail
from testcases.configuration.queries.test_get_applied_panel import GetAppliedPanel
from testcases.configuration.queries.test_get_deploy_config import GetDeployConfig
from testcases.configuration.mutations.test_create_configuration import CreateConfiguration
from testcases.configuration.mutations.test_update_configuration import UpdateConfiguration
from testcases.configuration.mutations.test_delete_configuration import DeleteConfiguration
from testcases.configuration.mutations.test_reapply import Reapply
from testcases.combined_test.test_combined_1 import Combined1
from testcases.combined_test.test_redeploy import Combined2


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

# ConfigurationList 共9个用例 林泳
suite.addTest(ConfigurationList('test_configurationList'))
suite.addTest(ConfigurationList('test_pagenumber_2'))
suite.addTest(ConfigurationList('test_inputpageSize_is0'))
suite.addTest(ConfigurationList('test_inputpageSize_is_plural_1'))
suite.addTest(ConfigurationList('test_inputpageSize_is_plural_2'))
suite.addTest(ConfigurationList('test_filters_name_is_empty'))
suite.addTest(ConfigurationList('test_filters_name_is_true'))
suite.addTest(ConfigurationList('test_configurationId_is_empty'))
suite.addTest(ConfigurationList('test_configurationId_is_error'))

# CreateConfiguration 共2个用例 林泳
suite.addTest(CreateConfiguration('test_create_configuration'))
suite.addTest(CreateConfiguration('test_configurationId_name_is_existed'))

suite.addTest(ConfigurationDetail('test_configuration_detail'))

# GetAppliedPanel 共3个用例 林泳
suite.addTest(GetAppliedPanel('test_get_applied_panel'))
suite.addTest(GetAppliedPanel('test_not_applied_of_Panel'))
suite.addTest(GetAppliedPanel('test_applied_of_Panel'))

suite.addTest(GetDeployConfig('test_get_deploy_config'))

suite.addTest(UpdateConfiguration('test_update_configuration'))
suite.addTest(DeleteConfiguration('test_delete_configuration'))

# reapply 重复测试 丁正辉
suite.addTest(Reapply('test_reapply'))

# 场景测试共7个用例 陈烨婷
suite.addTest(Combined1('test1'))
suite.addTest(Combined1('test2'))
suite.addTest(Combined1('test3'))
suite.addTest(Combined1('test4'))
suite.addTest(Combined1('test5'))
suite.addTest(Combined1('test6'))
suite.addTest(Combined1('test7'))
suite.addTest(Combined1('test8'))
suite.addTest(Combined2('test1'))
