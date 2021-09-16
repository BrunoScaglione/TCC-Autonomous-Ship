from setuptools import setup

package_name = 'pydyna_simple'

setup(
    name=package_name,
    version='0.0.0',
    packages=[pydyna_simple],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['config']),
        ('share/' + package_name, ['logs']),
        ('share/' + package_name, glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bruno',
    maintainer_email='bruno.c.scaglione@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simul = pydyna_simple.pydyna_simple:main',
        ],
    },
)
