#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('human_camlidar_det_uol'),
        'config',
        'camera_with_lidar_cloud.yaml'
    )

    return LaunchDescription([
        Node(
            package='human_camlidar_det_uol',
            executable='detect_with_lidar_cloud.py',
            name='tracker_with_cloud_node',
            output='screen',
            parameters=[config]
        )
    ])