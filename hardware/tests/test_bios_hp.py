#
# Copyright (C) 2019 Criteo
#
# Author: Erwan Velu <e.velu@criteo.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

from hardware import bios_hp
from hardware.tests.utils import sample


class TestBiosHP(unittest.TestCase):

    def test_bios_hp(self):
        hardware_lst = []
        bios_hp.dump_hp_bios(hardware_lst, sample('conrep.dat'))
        self.assertEqual(
            hardware_lst,
            [(u'hp', u'bios', u'Language', u'English'),
             (u'hp', u'bios', u'Setup_Browser_Selection', u'Auto'),
             (u'hp', u'bios', u'Workload_Profile', u'Custom'),
             (u'hp', u'bios', u'Dynamic_Power_Capping_Functionality', u'Disabled'),
             (u'hp', u'bios', u'Extended_Memory_Test', u'Disabled'),
             (u'hp', u'bios', u'Memory_Fast_Training', u'Enabled'),
             (u'hp', u'bios', u'UEFI_POST_Discovery_Mode', u'Auto'),
             (u'hp', u'bios', u'Memory_Clear_on_Warm_Reset', u'Disabled'),
             (u'hp', u'bios', u'Embedded_Serial_Port', u'COM1_IRQ4'),
             (u'hp', u'bios', u'Virtual_Serial_Port', u'COM2_IRQ3'),
             (u'hp', u'bios', u'BIOS_Serial_Console_Port', u'Auto'),
             (u'hp', u'bios', u'BIOS_Serial_Console_Emulation_Mode', u'VT100+'),
             (u'hp', u'bios', u'BIOS_Serial_Console_Baud_Rate', u'115200'),
             (u'hp', u'bios', u'EMS_Console', u'Virtual_Serial_Port'),
             (u'hp', u'bios', u'USB_Control', u'All_USB_Ports_Enabled'),
             (u'hp', u'bios', u'USB_Boot_Support', u'Enabled'),
             (u'hp', u'bios', u'Removable_Flash_Media_Boot_Sequence',
              u'Internal_DriveKeys_First'),
             (u'hp', u'bios', u'Virtual_Install_Disk', u'Disabled'),
             (u'hp', u'bios', u'Internal_SD_Card_Slot', u'Enabled'),
             (u'hp', u'bios', u'ASR_Status', u'Enabled'),
             (u'hp', u'bios', u'ASR_Timeout', u'10_Minutes'),
             (u'hp', u'bios', u'Wake-On_LAN', u'Enabled'),
             (u'hp', u'bios', u'POST_F1_Prompt', u'Delayed_20_seconds'),
             (u'hp', u'bios', u'Power_Button_Mode', u'Enabled'),
             (u'hp', u'bios', u'Automatic_Power-On', u'Always_Power_Off'),
             (u'hp', u'bios', u'Power-On_Delay', u'No_Delay'),
             (u'hp', u'bios', u'Server_Name', u'testsmart01-am6'),
             (u'hp', u'bios', u'Server_Primary_OS', None),
             (u'hp', u'bios', u'Server_Other_Information', None),
             (u'hp', u'bios', u'Power-On_Logo', u'Enabled'),
             (u'hp', u'bios', u'Administrator_Name', None),
             (u'hp', u'bios', u'Administrator_Phone_Number', None),
             (u'hp', u'bios', u'Administrator_E-mail_Address', None),
             (u'hp', u'bios', u'Administrator_Other_Information', None),
             (u'hp', u'bios', u'Service_Contact_Name', None),
             (u'hp', u'bios', u'Service_Contact_Phone_Number', None),
             (u'hp', u'bios', u'Service_Contact_E-mail_Address', None),
             (u'hp', u'bios', u'Service_Contact_Other_Information', None),
             (u'hp', u'bios', u'Custom_POST_Message', None),
             (u'hp', u'bios', u'Embedded_Diagnostics', u'Enabled'),
             (u'hp', u'bios', u'Embedded_Diagnostics_Mode', u'Auto'),
             (u'hp', u'bios', u'Intel_Hyper-Threading', u'Enabled'),
             (u'hp', u'bios', u'Enabled_Cores_per_Processor', u'00'),
             (u'hp', u'bios', u'Processor_x2APIC_Support', u'Disabled'),
             (u'hp', u'bios', u'Intel_TXT_Support', u'Disabled'),
             (u'hp', u'bios', u'Advanced_Memory_Protection', u'Advanced_ECC_Support'),
             (u'hp', u'bios', u'Memory_Refresh_Rate', u'1x_Refresh'),
             (u'hp', u'bios', u'Channel_Interleaving', u'Enabled'),
             (u'hp', u'bios', u'Maximum_Memory_Bus_Frequency', u'Auto'),
             (u'hp', u'bios', u'Memory_Patrol_Scrubbing', u'Enabled'),
             (u'hp', u'bios', u'Node_Interleaving', u'Disabled'),
             (u'hp', u'bios', u'Memory_Mirroring_Mode', u'Full_Mirroring'),
             (u'hp', u'bios', u'Memory_Remap', u'No_Action'),
             (u'hp', u'bios', u'NVDIMM-N_Support', u'Enabled'),
             (u'hp', u'bios', u'NVDIMM-N_Interleaving', u'Disabled'),
             (u'hp', u'bios', u'NVDIMM-N_ACPI_Objects', u'Disabled'),
             (u'hp', u'bios', u'Persistent_Memory_Backup_Power_Policy', u'Enabled'),
             (u'hp', u'bios', u'Persistent_Memory_Integrity_Check', u'Enabled'),
             (u'hp', u'bios', u'Persistent_Memory_Address_Range_Scrub', u'Enabled'),
             (u'hp', u'bios', u'Intel_VT', u'Disabled'),
             (u'hp', u'bios', u'Intel_VT-d', u'Disabled'),
             (u'hp', u'bios', u'SR-IOV', u'Enabled'),
             (u'hp', u'bios', u'Boot_Mode', u'Legacy_BIOS_Mode'),
             (u'hp', u'bios', u'UEFI_Optimized_Boot', u'Disabled'),
             (u'hp', u'bios', u'Boot_Order_Policy',
              u'Retry_Boot_Order_Indefinitely'),
             (u'hp', u'bios', u'Legacy_Boot_Order',
              u'02 04 00 03 ff ff ff ff ff ff ff ff ff ff ff ff'),
             (u'hp', u'bios', u'Legacy_Boot_Order_Size', u'04'),
             (u'hp', u'bios', u'Legacy_Boot_Controller_Order', None),
             (u'hp', u'bios', u'Pre-Boot_Network_Environment', u'Auto'),
             (u'hp', u'bios', u'IPv6_DHCP_Unique_Identifier', u'Auto'),
             (u'hp', u'bios', u'Network_Boot_Retry_Support', u'Enabled'),
             (u'hp', u'bios', u'Network_Boot_Retry_Count', u'00 14'),
             (u'hp', u'bios', u'UEFI_HTTP_Boot', u'Auto'),
             (u'hp', u'bios', u'UEFI_iSCSI_Boot_Policy', u'Software_Initiator'),
             (u'hp', u'bios', u'Embedded_Network_Boot',
              u'00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00'),
             (u'hp', u'bios', u'PCIe_Slot_Network_Boot',
              u'01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00'),
             (u'hp', u'bios', u'Pre-Boot_Network_Interface', u'00 00'),
             (u'hp', u'bios', u'Pre-Boot_Network_Proxy', None),
             (u'hp', u'bios', u'Pre-Boot_DHCPv4', u'Enabled'),
             (u'hp', u'bios', u'Pre-Boot_IPv4_Address', u'0.0.0.0'),
             (u'hp', u'bios', u'Pre-Boot_IPv4_Subnet_Mask', u'0.0.0.0'),
             (u'hp', u'bios', u'Pre-Boot_IPv4_Gateway', u'0.0.0.0'),
             (u'hp', u'bios', u'Pre-Boot_IPv4_Primary_DNS', u'0.0.0.0'),
             (u'hp', u'bios', u'Pre-Boot_IPv4_Secondary_DNS', u'0.0.0.0'),
             (u'hp', u'bios', u'Pre-Boot_IPv6_Config_Policy', u'Automatic'),
             (u'hp', u'bios', u'Pre-Boot_IPv6_Address', u'::'),
             (u'hp', u'bios', u'Pre-Boot_IPv6_Gateway', u'::'),
             (u'hp', u'bios', u'Pre-Boot_IPv6_Primary_DNS', u'::'),
             (u'hp', u'bios', u'Pre-Boot_IPv6_Secondary_DNS', u'::'),
             (u'hp', u'bios', u'Pre-Boot_Boot_from_URL_1', None),
             (u'hp', u'bios', u'Pre-Boot_Boot_from_URL_2', None),
             (u'hp', u'bios', u'Pre-Boot_Boot_from_URL_3', None),
             (u'hp', u'bios', u'Pre-Boot_Boot_from_URL_4', None),
             (u'hp', u'bios', u'VLAN_Settings', None),
             (u'hp', u'bios', u'Fibre_Channel/FCoE_Scan_Policy',
              u'Scan_Configured_Targets_Only'),
             (u'hp', u'bios', u'Embedded_SATA_Configuration', u'Enable_AHCI_Support'),
             (u'hp', u'bios', u'SATA_Secure_Erase', u'Disabled'),
             (u'hp', u'bios', u'Embedded_Storage_Boot_Policy', u'18 18'),
             (u'hp', u'bios', u'PCIe_Slot_Storage_Boot_Policy',
              u'18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18'),
             (u'hp', u'bios', u'Embedded_NVM_Express_Option_ROM', u'Enabled'),
             (u'hp', u'bios', u'Power_Regulator', u'Static_High_Performance_Mode'),
             (u'hp', u'bios', u'Minimum_Processor_Idle_Power_Core_C-State', u'C6_State'),
             (u'hp', u'bios', u'Minimum_Processor_Idle_Power_Package_C-State',
              u'Package_C6_(retention)_State'),
             (u'hp', u'bios', u'Intel_Turbo_Boost_Technology', u'Enabled'),
             (u'hp', u'bios', u'Energy/Performance_Bias', u'Balanced_Performance'),
             (u'hp', u'bios', u'Collaborative_Power_Control', u'Enabled'),
             (u'hp', u'bios', u'Intel_DMI_Link_Frequency', u'Auto'),
             (u'hp', u'bios', u'NUMA_Group_Size_Optimization', u'Flat'),
             (u'hp', u'bios', u'Intel_Performance_Monitoring_Support', u'Disabled'),
             (u'hp', u'bios', u'Uncore_Frequency_Scaling', u'Auto'),
             (u'hp', u'bios', u'Sub-NUMA_Clustering', u'Disabled'),
             (u'hp', u'bios', u'Energy_Efficient_Turbo', u'Enabled'),
             (u'hp', u'bios', u'Local/Remote_Threshold', u'Auto'),
             (u'hp', u'bios', u'LLC_Dead_Line_Allocation', u'Enabled'),
             (u'hp', u'bios', u'Stale_A_to_S', u'Disabled'),
             (u'hp', u'bios', u'HW_Prefetcher', u'Enabled'),
             (u'hp', u'bios', u'Adjacent_Sector_Prefetch', u'Enabled'),
             (u'hp', u'bios', u'DCU_Stream_Prefetcher', u'Enabled'),
             (u'hp', u'bios', u'DCU_IP_Prefetcher', u'Enabled'),
             (u'hp', u'bios', u'LLC_Prefetch', u'Disabled'),
             (u'hp', u'bios', u'XPT_Prefetcher', u'Enabled'),
             (u'hp', u'bios', u'ACPI_SLIT', u'Enabled'),
             (u'hp', u'bios', u'Intel_NIC_DMA_Channels_(IOAT)', u'Enabled'),
             (u'hp', u'bios', u'Memory_Proximity_Reporting_for_I/O', u'Enabled'),
             (u'hp', u'bios', u'Intel_UPI_Link_Enablement', u'Auto'),
             (u'hp', u'bios', u'Intel_UPI_Link_Power_Management', u'Enabled'),
             (u'hp', u'bios', u'Intel_UPI_Link_Frequency', u'Auto'),
             (u'hp', u'bios', u'UPI_Prefetcher', u'Enabled'),
             (u'hp', u'bios', u'Processor_Jitter_Control', None),
             (u'hp', u'bios', u'Core_Boosting', u'Disabled'),
             (u'hp', u'bios', u'Redundant_Power_Supply_Mode', u'Balanced_Mode'),
             (u'hp', u'bios', u'Embedded_UEFI_Shell', u'Enabled'),
             (u'hp', u'bios', u'Add_Embedded_UEFI_Shell_to_Boot_Order', u'Disabled'),
             (u'hp', u'bios', u'UEFI_Shell_Script_Auto-Start', u'Disabled'),
             (u'hp', u'bios', u'Shell_Script_Verification', u'Disabled'),
             (u'hp', u'bios', u'Shell_Auto-Start_Script_Location', u'Auto'),
             (u'hp', u'bios', u'Discover_Shell_Auto-Start_Script_using_DHCP', u'Disabled'),
             (u'hp', u'bios', u'Network_Location_for_Shell_Auto-Start_Script', None),
             (u'hp', u'bios', u'One-Time_Boot_Menu_(F11 Prompt)', u'Enabled'),
             (u'hp', u'bios', u'Intelligent_Provisioning_(F10 Prompt)', u'Enabled'),
             (u'hp', u'bios', u'System_Intrusion_Detection', u'Disabled'),
             (u'hp', u'bios', u'Processor_AES-NI_Support', u'Enabled'),
             (u'hp', u'bios', u'Backup_ROM_Image_Authentication', u'Disabled'),
             (u'hp', u'bios', u'TPM_12_Operation', u'No_Action'),
             (u'hp', u'bios', u'TPM_20_Operation', u'No_Action'),
             (u'hp', u'bios', u'TPM_Visibility', u'Visible'),
             (u'hp', u'bios', u'TPM_UEFI_Option_ROM_Measurement', u'Enabled'),
             (u'hp', u'bios', u'NVMe_PCIe_Resource_Padding', u'Normal'),
             (u'hp', u'bios', u'Maximum_PCI_Express_Speed', u'Per_Port_Control'),
             (u'hp', u'bios', u'PCIe_Device_Disable_Embedded_Mezz', u'04 00 00 00 00 00'),
             (u'hp', u'bios', u'PCIe_Device_Disable_SATA_Slots', u'00 00 00 00 00 00'),
             (u'hp', u'bios', u'ROM_Selection', u'Use_Current_ROM'),
             (u'hp', u'bios', u'Embedded_Video_Connection', u'Auto'),
             (u'hp', u'bios', u'Consistent_Device_Naming',
              u'CDN_Support_for_LOMs_and_Slots'),
             (u'hp', u'bios', u'Mixed_Power_Supply_Reporting', u'Enabled'),
             (u'hp', u'bios', u'High_Precision_Event_Timer_(HPET)_ACPI_Support', u'Enabled'),
             (u'hp', u'bios', u'Power_Supply_Requirements',
              u'Configured_for_1+1_Redundancy'),
             (u'hp', u'bios', u'Thermal_Configuration', u'Optimal_Cooling'),
             (u'hp', u'bios', u'Thermal_Shutdown', u'Enabled'),
             (u'hp', u'bios', u'Fan_Installation_Requirements', u'Enable_Messaging'),
             (u'hp', u'bios', u'Fan_Failure_Policy',
              u'Allow_Operation_with_Critical_Fan_Failures'),
             (u'hp', u'bios', u'Extended_Ambient_Temperature_Support', u'Disabled'),
             (u'hp', u'bios', u'UEFI_Serial_Debug_Message_Level', u'Disabled'),
             (u'hp', u'bios', u'POST_Verbose_Boot_Progress', u'Disabled'),
             (u'hp', u'bios', u'Time_Format', u'Coordinated_Universal_Time_(UTC)'),
             (u'hp', u'bios', u'Time_Zone', u'UTC-00:00'),
             (u'hp', u'bios', u'Asset_Tag_UEFI', None),
             (u'hp', u'bios', u'Asset_Tag_Protection_UEFI', u'Locked')]
        )
