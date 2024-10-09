from setuptools import setup

package_name = 'testing'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={
        package_name: [
            'with_obstacle_weights.h5',
            'without_obstacle_weights.h5'
        ],
    },
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='charan',
    maintainer_email='charan@todo.todo',
    description='TODO: Package description',	
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera = testing.camera:main',
            'evaluation=testing.evaluation:main',
            'without_obstacle_evaluation=testing.without_obstacle_evaluation:main',
            'with_obstacle_evaluation=testing.with_obstacle_evaluation:main',
            'without_obstacle_training=testing.without_obstacle_training:main',
            'with_obstacle_training=testing.with_obstacle_training:main'
        ],
    },
)
