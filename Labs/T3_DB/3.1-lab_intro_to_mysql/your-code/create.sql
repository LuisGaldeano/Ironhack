-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lab_mysql` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `lab_mysql` ;

-- -----------------------------------------------------
-- Table `lab_mysql`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Cars` (
  `idCars` INT NOT NULL AUTO_INCREMENT,
  `VIN` CHAR(17) NULL,
  `Manufacture` VARCHAR(255) NULL,
  `Model` VARCHAR(255) NULL,
  `Year` INT(4) NULL,
  `Color` VARCHAR(45) NULL,
  PRIMARY KEY (`idCars`),
  UNIQUE INDEX `idCars_UNIQUE` (`idCars` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Salesperson` (
  `StaffID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NULL,
  `Store` VARCHAR(255) NULL,
  PRIMARY KEY (`StaffID`),
  UNIQUE INDEX `StaffID_UNIQUE` (`StaffID` ASC) VISIBLE)
ENGINE = InnoDB
COMMENT = '\n';


-- -----------------------------------------------------
-- Table `lab_mysql`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Customers` (
  `CustomersID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NULL,
  `Phone` VARCHAR(255) NULL,
  `Email` VARCHAR(255) NULL,
  `Adress` VARCHAR(255) NULL,
  `City` VARCHAR(255) NULL,
  `State` VARCHAR(255) NULL,
  `Country` VARCHAR(255) NULL,
  `Postal` INT NULL,
  PRIMARY KEY (`CustomersID`),
  UNIQUE INDEX `CustomersID_UNIQUE` (`CustomersID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Invoices` (
  `InvoiceID` INT NOT NULL AUTO_INCREMENT,
  `Date` DATE NULL,
  `Cars_idCars` INT NOT NULL,
  `Salesperson_StaffID` INT NOT NULL,
  `Customers_CustomersID` INT NOT NULL,
  PRIMARY KEY (`InvoiceID`, `Cars_idCars`, `Salesperson_StaffID`, `Customers_CustomersID`),
  INDEX `fk_Invoices_Cars_idx` (`Cars_idCars` ASC) VISIBLE,
  INDEX `fk_Invoices_Salesperson1_idx` (`Salesperson_StaffID` ASC) VISIBLE,
  INDEX `fk_Invoices_Customers1_idx` (`Customers_CustomersID` ASC) VISIBLE,
  UNIQUE INDEX `InvoiceID_UNIQUE` (`InvoiceID` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Cars`
    FOREIGN KEY (`Cars_idCars`)
    REFERENCES `lab_mysql`.`Cars` (`idCars`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Salesperson1`
    FOREIGN KEY (`Salesperson_StaffID`)
    REFERENCES `lab_mysql`.`Salesperson` (`StaffID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customers_CustomersID`)
    REFERENCES `lab_mysql`.`Customers` (`CustomersID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
