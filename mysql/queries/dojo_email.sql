-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojo_email_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojo_email_schema` ;

-- -----------------------------------------------------
-- Schema dojo_email_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojo_email_schema` DEFAULT CHARACTER SET utf8 ;
USE `dojo_email_schema` ;

-- -----------------------------------------------------
-- Table `dojo_email_schema`.`dojo_email`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_email_schema`.`dojo_email` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
