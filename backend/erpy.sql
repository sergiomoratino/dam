-- MySQL Script generated by MySQL Workbench
-- Mon Jan 13 16:08:56 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema erpy
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema erpy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `erpy` DEFAULT CHARACTER SET utf8 ;
USE `erpy` ;

-- -----------------------------------------------------
-- Table `erpy`.`Clientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `erpy`.`Clientes` ;

CREATE TABLE IF NOT EXISTS `erpy`.`Clientes` (
  `DNI` VARCHAR(9) NOT NULL,
  `Nombre` VARCHAR(30) NOT NULL,
  `Apellidos` VARCHAR(45) NULL,
  `Género` VARCHAR(1) NULL,
  `Dirección` VARCHAR(45) NULL,
  `FNacimiento` DATE NULL,
  `CódigoPostal` INT NULL,
  PRIMARY KEY (`DNI`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

use erpy;
insert into Clientes Values	('15406478T', 'Jofian', 'Rufian', 'V', 'inframundo, 666', '1966-06-06','00666');
insert into Clientes Values	('14785545L', 'Alejandro', 'Vagno', 'V', 'toletum, 45', '1994-08-26','45887');
insert into Clientes Values	('08544554S', 'Paco', 'León', 'V', 'Arsenal, 50', '1980-06-16','48785');
insert into Clientes Values	('14055500N', 'Eva', 'Castrano', 'H', 'Paraiso, 6', '1980-12-06','47588');
insert into Clientes Values	('03004584T', 'Maria', 'Patiño', 'H', 'Pala, 47', '1996-04-04','25666');
insert into Clientes Values	('34594565N', 'Jaime', 'Citroen', 'V', 'España, 155', '1977-02-19','78766');





