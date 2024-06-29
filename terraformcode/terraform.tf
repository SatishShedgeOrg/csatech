##
# Terraform Configuration
##

terraform {

  backend "azurerm" {
    key                  = "github.terraform.tfstate"
  }

  required_version = ">=0.12"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.110"
    }
  }
}

##
# Providers
##

provider "azurerm" {
  features {}
}