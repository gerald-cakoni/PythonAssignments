-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema books_authors
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `books_authors` ;

-- -----------------------------------------------------
-- Schema books_authors
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books_authors` DEFAULT CHARACTER SET utf8 ;
USE `books_authors` ;

-- -----------------------------------------------------
-- Table `books_authors`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_authors`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `num_of_pages` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_authors`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_authors`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_authors`.`favourites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_authors`.`favourites` (
  `book_id` INT NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`book_id`, `author_id`),
  INDEX `fk_books_has_authors_authors1_idx` (`author_id` ASC) VISIBLE,
  INDEX `fk_books_has_authors_books_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_has_authors_books`
    FOREIGN KEY (`book_id`)
    REFERENCES `books_authors`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_books_has_authors_authors1`
    FOREIGN KEY (`author_id`)
    REFERENCES `books_authors`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
