output "resource_group_name" {
  description = "Azure resource group name"
  value       = azurerm_resource_group.main.name
}

output "vm_name" {
  description = "Azure virtual machine name"
  value       = azurerm_linux_virtual_machine.main.name
}

output "public_ip_address" {
  description = "Public IP address of the Azure VM"
  value       = azurerm_public_ip.main.ip_address
}