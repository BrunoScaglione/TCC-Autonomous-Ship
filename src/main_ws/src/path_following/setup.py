import os
from setuptools import setup

package_name = 'path_following'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'control_allocation = path_following.control_allocation:main',
        ],
    },
)
