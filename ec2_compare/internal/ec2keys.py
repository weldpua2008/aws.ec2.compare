
from typing import List


def keys_dict() -> dict:
    # pylint: disable=all
    return {'str': ['Hypervisor', 'EncryptionSupport', 'EnaSupport', 'NvmeSupport', 'InstanceType', 'EbsOptimizedSupport', 'NetworkPerformance'], 'bool': ['EfaSupported', 'FreeTierEligible', 'Ipv6Supported', 'HibernationSupported', 'AutoRecoverySupported', 'CurrentGeneration', 'InstanceStorageSupported', 'BareMetal', 'BurstablePerformanceSupported', 'DedicatedHostsSupported', 'EncryptionInTransitSupported'], 'list': ['Disks', 'SupportedArchitectures', 'Fpgas', 'SupportedVirtualizationTypes', 'Gpus', 'SupportedStrategies', 'ValidCores', 'SupportedUsageClasses', 'ValidThreadsPerCore', 'Accelerators', 'NetworkCards', 'SupportedRootDeviceTypes', 'SupportedBootModes'], 'dict': ['PlacementGroupInfo', 'InferenceAcceleratorInfo', 'FpgaInfo', 'EfaInfo', 'MemoryInfo', 'InstanceStorageInfo', 'EbsInfo', 'GpuInfo', 'VCpuInfo', 'ProcessorInfo', 'NetworkInfo', 'EbsOptimizedInfo'], 'int': ['TotalSizeInGB', 'DefaultNetworkCardIndex', 'Ipv4AddressesPerInterface', 'TotalGpuMemoryInMiB', 'FreeTierEligible', 'AutoRecoverySupported', 'MaximumNetworkInterfaces', 'Ipv6AddressesPerInterface', 'EncryptionInTransitSupported', 'DefaultThreadsPerCore', 'EfaSupported', 'CurrentGeneration', 'TotalFpgaMemoryInMiB', 'BareMetal', 'BurstablePerformanceSupported', 'DefaultVCpus', 'MaximumNetworkCards', 'SizeInMiB', 'HibernationSupported', 'Ipv6Supported', 'DefaultCores', 'InstanceStorageSupported', 'DedicatedHostsSupported'], 'float': ['SustainedClockSpeedInGhz'], 'other': []}  # noqa: E501


def keys_structure(*arg, **kw) -> List:
    return [elem for k, v in keys_dict().items()
            if k in arg or not arg for elem in v]
