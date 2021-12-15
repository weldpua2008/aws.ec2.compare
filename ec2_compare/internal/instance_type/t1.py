
# Automatically generated

# pylint: disable=all
get = [{'SupportedArchitectures': ['i386', 'x86_64'], 'DefaultVCpus': 1, 'DefaultCores': 1, 'DefaultThreadsPerCore': 1, 'SizeInMiB': 627, 'EbsOptimizedSupport': 'unsupported', 'EncryptionSupport': 'unsupported', 'NvmeSupport': 'unsupported', 'NetworkPerformance': 'Very Low', 'MaximumNetworkInterfaces': 2, 'MaximumNetworkCards': 1, 'DefaultNetworkCardIndex': 0, 'NetworkCards': [{'NetworkCardIndex': 0, 'NetworkPerformance': 'Very Low', 'MaximumNetworkInterfaces': 2}], 'Ipv4AddressesPerInterface': 2, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported', 'EfaSupported': False, 'EncryptionInTransitSupported': False, 'SupportedStrategies': ['partition', 'spread'], 'InstanceType': 't1.micro', 'CurrentGeneration': False, 'FreeTierEligible': True, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs'], 'SupportedVirtualizationTypes': ['hvm', 'paravirtual'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['i386', 'x86_64']}, 'VCpuInfo': {'DefaultVCpus': 1, 'DefaultCores': 1, 'DefaultThreadsPerCore': 1}, 'MemoryInfo': {'SizeInMiB': 627}, 'InstanceStorageSupported': False, 'EbsInfo': {'EbsOptimizedSupport': 'unsupported', 'EncryptionSupport': 'unsupported', 'NvmeSupport': 'unsupported'}, 'NetworkInfo': {'NetworkPerformance': 'Very Low', 'MaximumNetworkInterfaces': 2, 'MaximumNetworkCards': 1, 'DefaultNetworkCardIndex': 0, 'NetworkCards': [{'NetworkCardIndex': 0, 'NetworkPerformance': 'Very Low', 'MaximumNetworkInterfaces': 2}], 'Ipv4AddressesPerInterface': 2, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported', 'EfaSupported': False, 'EncryptionInTransitSupported': False}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': False, 'SupportedBootModes': ['legacy-bios']}]  # noqa: E501


def get_instances_list() -> list:
    '''Returns list EC2 instances with InstanceType = t1 .'''
    # pylint: disable=all
    return get
