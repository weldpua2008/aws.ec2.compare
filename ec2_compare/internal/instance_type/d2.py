
# Automatically generated

# pylint: disable=all
get = [{'InstanceType': 'd2.2xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.4}, 'VCpuInfo': {'DefaultVCpus': 8, 'DefaultCores': 4, 'DefaultThreadsPerCore': 2, 'ValidCores': [1, 2, 3, 4], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 62464}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 12288, 'Disks': [{'SizeInGB': 2048, 'Count': 6, 'Type': 'hdd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'High', 'MaximumNetworkInterfaces': 4, 'Ipv4AddressesPerInterface': 15, 'Ipv6AddressesPerInterface': 15, 'Ipv6Supported': True, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': False}, {'InstanceType': 'd2.4xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.4}, 'VCpuInfo': {'DefaultVCpus': 16, 'DefaultCores': 8, 'DefaultThreadsPerCore': 2, 'ValidCores': [1, 2, 3, 4, 5, 6, 7, 8], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 124928}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 24576, 'Disks': [{'SizeInGB': 2048, 'Count': 12, 'Type': 'hdd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'High', 'MaximumNetworkInterfaces': 8, 'Ipv4AddressesPerInterface': 30, 'Ipv6AddressesPerInterface': 30, 'Ipv6Supported': True, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': False}, {'InstanceType': 'd2.8xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.4}, 'VCpuInfo': {'DefaultVCpus': 36, 'DefaultCores': 18, 'DefaultThreadsPerCore': 2, 'ValidCores': [2, 4, 6, 8, 10, 12, 14, 16, 18], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 249856}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 49152, 'Disks': [{'SizeInGB': 2048, 'Count': 24, 'Type': 'hdd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': '10 Gigabit', 'MaximumNetworkInterfaces': 8, 'Ipv4AddressesPerInterface': 30, 'Ipv6AddressesPerInterface': 30, 'Ipv6Supported': True, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': False}, {'InstanceType': 'd2.xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.4}, 'VCpuInfo': {'DefaultVCpus': 4, 'DefaultCores': 2, 'DefaultThreadsPerCore': 2, 'ValidCores': [1, 2], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 31232}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 6144, 'Disks': [{'SizeInGB': 2048, 'Count': 3, 'Type': 'hdd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'Moderate', 'MaximumNetworkInterfaces': 4, 'Ipv4AddressesPerInterface': 15, 'Ipv6AddressesPerInterface': 15, 'Ipv6Supported': True, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': False}]  # noqa: E501


def get_instances_list() -> list:
    '''Returns list EC2 instances with InstanceType = d2 .'''
    # pylint: disable=all
    return get