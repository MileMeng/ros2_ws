from setuptools import find_packages, setup

package_name = 'serial_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='meng',
    maintainer_email='1442346580@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'rgb_sine_publisher = serial_package.rgb_sine_publisher:main',
            'rgb_serial_subscriber = serial_package.rgb_serial_subscriber:main'
        ],
    },
)
