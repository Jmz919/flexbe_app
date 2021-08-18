import os
import sys
import ament_index_python
import launch
import launch_ros
import launch_ros.actions
import launch_testing.actions
import launch_testing_ros
import pytest
from ament_index_python.packages import get_package_share_directory

@pytest.mark.rostest
def generate_test_description():

    flexbe_app_dir = get_package_share_directory('flexbe_app')
    TEST_PROC_PATH = os.path.join(flexbe_app_dir, 'bin/test_report')

    # This is necessary to get unbuffered output from the process under test
    proc_env = os.environ.copy()
    proc_env['PYTHONUNBUFFERED'] = '1'

    test_core = launch.actions.ExecuteProcess(
        cmd=[sys.executable, TEST_PROC_PATH],
        env=proc_env, output='screen'
    )

    return (
        launch.LaunchDescription([
            test_report,
            launch_testing.actions.ReadyToTest()
        ]),
        {
            'test_report': test_report,
        }
    )
