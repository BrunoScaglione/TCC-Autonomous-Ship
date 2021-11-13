import os
from glob import glob
from setuptools import setup
from glob import glob

package_name = 'path_following'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'logs', 'mylogs'), []),
        (os.path.join('share', package_name, 'logs', 'pydynalogs'), []),
        (os.path.join('share', package_name, 'logs', 'roslogs'), []),
        (os.path.join('share', package_name, 'db', 'rosbags'), []),
        (os.path.join('share', package_name, 'db', 'waypoints'), []),
        (os.path.join('share', package_name, 'plots', 'state'), []),
        (os.path.join('share', package_name, 'plots', 'simulatedState'), []),
        (os.path.join('share', package_name, 'plots', 'filteredState'), []),
        (os.path.join('share', package_name, 'plots', 'estimatedState'), []),
        (os.path.join('share', package_name, 'plots', 'setpoints'), []),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bruno',
    maintainer_email='bruno.c.scaglione@gmail.com',
    description='Path-Following Ship',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yaw_controller = path_following.yaw_controller:main',
            'surge_controller = path_following.surge_controller:main',
            'backend = path_following.backend:main',
            'control_allocation = path_following.control_allocation:main',
            'gps_imu_simul = path_following.gps_imu_simul:main',
            'venus = path_following.venus:main',
            'wave_filter = path_following.wave_filter:main',
            'los_guidance = path_following.los_guidance:main',
            'kalman_filter = path_following.kalman_filter:main',
        ],
    },
)
