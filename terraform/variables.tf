variable "location" {
  description = "Azure region"
  type        = string
  default     = "centralus"
}

variable "resource_group_name" {
  description = "Azure resource group name"
  type        = string
  default     = "rg-gitlab-cloura"
}

variable "vm_name" {
  description = "GitLab virtual machine name"
  type        = string
  default     = "vm-gitlab-cloura"
}

variable "vm_size" {
  description = "Azure VM size"
  type        = string
  default     = "Standard_D2s_v7"
}

variable "admin_username" {
  description = "Admin username for the Linux VM"
  type        = string
  default     = "azureuser"
}

variable "ssh_public_key" {
  description = "SSH public key used to access the Linux VM"
  type        = string
}