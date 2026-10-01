variable "location" {
  description = "Azure region"
  type        = string
  default     = "centralus"
}

variable "admin_username" {
  description = "Admin username for the Linux VM"
  type        = string
}
variable "ssh_public_key" {
  description = "SSH public key for the Linux VM"
  type        = string
}

