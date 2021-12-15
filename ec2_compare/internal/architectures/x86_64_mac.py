
# Automatically generated

# pylint: disable=all
get = [{'SupportedArchitectures': ['x86_64_mac'], 'SustainedClockSpeedInGhz': 3.2, 'DefaultVCpus': 12, 'DefaultCores': 6, 'DefaultThreadsPerCore': 2, 'SizeInMiB': 32768, 'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported', 'EbsOptimizedInfo': {'BaselineBandwidthInMbps': 14000, 'BaselineThroughputInMBps': 1750.0, 'BaselineIops': 80000, 'MaximumBandwidthInMbps': 14000, 'MaximumThroughputInMBps': 1750.0, 'MaximumIops': 80000}, 'NvmeSupport': 'required', 'NetworkPerformance': '25 Gigabit', 'MaximumNetworkInterfaces': 8, 'MaximumNetworkCards': 1, 'DefaultNetworkCardIndex': 0, 'NetworkCards': [{'NetworkCardIndex': 0, 'NetworkPerformance': '25 Gigabit', 'MaximumNetworkInterfaces': 8}], 'Ipv4AddressesPerInterface': 30, 'Ipv6AddressesPerInterface': 30, 'Ipv6Supported': True, 'EnaSupport': 'required', 'EfaSupported': False, 'EncryptionInTransitSupported': False, 'SupportedStrategies': ['cluster', 'partition', 'spread'], 'InstanceType': 'mac1.metal', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand'], 'SupportedRootDeviceTypes': ['ebs'], 'SupportedVirtualizationTypes': ['hvm'], 'BareMetal': True, 'ProcessorInfo': {'SupportedArchitectures': ['x86_64_mac'], 'SustainedClockSpeedInGhz': 3.2}, 'VCpuInfo': {'DefaultVCpus': 12, 'DefaultCores': 6, 'DefaultThreadsPerCore': 2}, 'MemoryInfo': {'SizeInMiB': 32768}, 'InstanceStorageSupported': False, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported', 'EbsOptimizedInfo': {'BaselineBandwidthInMbps': 14000, 'BaselineThroughputInMBps': 1750.0, 'BaselineIops': 80000, 'MaximumBandwidthInMbps': 14000, 'MaximumThroughputInMBps': 1750.0, 'MaximumIops': 80000}, 'NvmeSupport': 'required'}, 'NetworkInfo': {'NetworkPerformance': '25 Gigabit', 'MaximumNetworkInterfaces': 8, 'MaximumNetworkCards': 1, 'DefaultNetworkCardIndex': 0, 'NetworkCards': [{'NetworkCardIndex': 0, 'NetworkPerformance': '25 Gigabit', 'MaximumNetworkInterfaces': 8}], 'Ipv4AddressesPerInterface': 30, 'Ipv6AddressesPerInterface': 30, 'Ipv6Supported': True, 'EnaSupport': 'required', 'EfaSupported': False, 'EncryptionInTransitSupported': False}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': True, 'SupportedBootModes': ['legacy-bios']}]  # noqa: E501


def get_instances_list() -> list:
    '''Returns list EC2 instances with SupportedArchitectures = x86_64_mac .'''
    # pylint: disable=all
    return get
