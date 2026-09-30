-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema USUARIOS_CRUD
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema USUARIOS_CRUD
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `USUARIOS_CRUD` DEFAULT CHARACTER SET utf8 ;
USE `USUARIOS_CRUD` ;

-- -----------------------------------------------------
-- Table `USUARIOS_CRUD`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `USUARIOS_CRUD`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT current_timestamp,
  `updated_at` DATETIME NOT NULL DEFAULT on_update_current_timestamp,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
