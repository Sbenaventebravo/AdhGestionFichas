SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `practica` ;
CREATE SCHEMA IF NOT EXISTS `practica` DEFAULT CHARACTER SET utf8 ;
USE `practica` ;

-- -----------------------------------------------------
-- Table `practica`.`adhesivo_coldfoil`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`adhesivo_coldfoil` ;

CREATE  TABLE IF NOT EXISTS `practica`.`adhesivo_coldfoil` (
  `idAdhColdFoil` INT(11) NOT NULL AUTO_INCREMENT ,
  `proveedor` VARCHAR(45) NOT NULL ,
  `ancho` FLOAT(3,1) NOT NULL ,
  PRIMARY KEY (`idAdhColdFoil`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`adhesivo_laminacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`adhesivo_laminacion` ;

CREATE  TABLE IF NOT EXISTS `practica`.`adhesivo_laminacion` (
  `idAdhLam` INT(11) NOT NULL AUTO_INCREMENT ,
  `proveedor` VARCHAR(45) NOT NULL ,
  `anilox` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`idAdhLam`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`categoria`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`categoria` ;

CREATE  TABLE IF NOT EXISTS `practica`.`categoria` (
  `idCategoria` INT(11) NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`idCategoria`) )
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`cliente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`cliente` ;

CREATE  TABLE IF NOT EXISTS `practica`.`cliente` (
  `idCliente` INT(11) NOT NULL AUTO_INCREMENT ,
  `rutCliente` VARCHAR(11) NOT NULL ,
  `nombreCliente` VARCHAR(70) NOT NULL ,
  PRIMARY KEY (`idCliente`) )
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`cold_foil`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`cold_foil` ;

CREATE  TABLE IF NOT EXISTS `practica`.`cold_foil` (
  `idColdFoil` INT(11) NOT NULL AUTO_INCREMENT ,
  `proveedor` VARCHAR(45) NOT NULL ,
  `ancho` FLOAT(3,1) NOT NULL ,
  PRIMARY KEY (`idColdFoil`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`maquina`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`maquina` ;

CREATE  TABLE IF NOT EXISTS `practica`.`maquina` (
  `idMaquina` INT(11) NOT NULL AUTO_INCREMENT ,
  `codigo` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`idMaquina`) )
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`ficha_tecnica_etiqueta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`ficha_tecnica_etiqueta` ;

CREATE  TABLE IF NOT EXISTS `practica`.`ficha_tecnica_etiqueta` (
  `idFicha` INT(11) NOT NULL AUTO_INCREMENT ,
  `pedido` VARCHAR(45) NOT NULL ,
  `etiqueta` VARCHAR(45) NOT NULL ,
  `fecha` DATE NOT NULL ,
  `clisses` TINYINT(1) NOT NULL ,
  `velocidad` FLOAT(3,1) NOT NULL ,
  `idCliente` INT(11) NOT NULL ,
  `idCategoria` INT(11) NOT NULL ,
  `idMaquina` INT(11) NOT NULL ,
  PRIMARY KEY (`idFicha`) ,
  CONSTRAINT `fk_ficha_tecnica_etiqueta_cliente1`
    FOREIGN KEY (`idCliente` )
    REFERENCES `practica`.`cliente` (`idCliente` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ficha_tecnica_etiqueta_categoria1`
    FOREIGN KEY (`idCategoria` )
    REFERENCES `practica`.`categoria` (`idCategoria` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ficha_tecnica_etiqueta_maquina1`
    FOREIGN KEY (`idMaquina` )
    REFERENCES `practica`.`maquina` (`idMaquina` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = utf8;

CREATE INDEX `fk_ficha_tecnica_etiqueta_cliente1_idx` ON `practica`.`ficha_tecnica_etiqueta` (`idCliente` ASC) ;

CREATE INDEX `fk_ficha_tecnica_etiqueta_categoria1_idx` ON `practica`.`ficha_tecnica_etiqueta` (`idCategoria` ASC) ;

CREATE INDEX `fk_ficha_tecnica_etiqueta_maquina1_idx` ON `practica`.`ficha_tecnica_etiqueta` (`idMaquina` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`film_micronaje`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`film_micronaje` ;

CREATE  TABLE IF NOT EXISTS `practica`.`film_micronaje` (
  `idFilmMi` INT(11) NOT NULL AUTO_INCREMENT ,
  `proveedor` VARCHAR(45) NOT NULL ,
  `ancho` FLOAT(3,1) NOT NULL ,
  PRIMARY KEY (`idFilmMi`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`malla`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`malla` ;

CREATE  TABLE IF NOT EXISTS `practica`.`malla` (
  `idMalla` INT(11) NOT NULL AUTO_INCREMENT ,
  `tipo` VARCHAR(45) NOT NULL ,
  `int_o_ext` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`idMalla`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`material`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`material` ;

CREATE  TABLE IF NOT EXISTS `practica`.`material` (
  `idMaterial` INT(11) NOT NULL AUTO_INCREMENT ,
  `codigo` VARCHAR(45) NOT NULL ,
  `nombre` VARCHAR(45) NOT NULL ,
  `proveedor` VARCHAR(45) NOT NULL ,
  `ancho` FLOAT(3,1) NOT NULL ,
  `TC` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`idMaterial`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`tinta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`tinta` ;

CREATE  TABLE IF NOT EXISTS `practica`.`tinta` (
  `idTinta` INT(11) NOT NULL AUTO_INCREMENT ,
  `color` VARCHAR(45) NOT NULL ,
  `tipo` VARCHAR(45) NOT NULL ,
  `anilox` VARCHAR(45) NOT NULL ,
  `proveedor` VARCHAR(45) NOT NULL ,
  `proveedor2` VARCHAR(45) NULL DEFAULT NULL ,
  `proveedor3` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`idTinta`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`tipo_barniz`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`tipo_barniz` ;

CREATE  TABLE IF NOT EXISTS `practica`.`tipo_barniz` (
  `idTBarniz` INT(11) NOT NULL AUTO_INCREMENT ,
  `tipo` VARCHAR(45) NOT NULL ,
  `proveedor` VARCHAR(45) NOT NULL ,
  `anilox` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`idTBarniz`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`troquel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`troquel` ;

CREATE  TABLE IF NOT EXISTS `practica`.`troquel` (
  `idTroquel` INT(11) NOT NULL AUTO_INCREMENT ,
  `proveedor` VARCHAR(45) NOT NULL ,
  `fecha` DATE NOT NULL ,
  PRIMARY KEY (`idTroquel`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `practica`.`material_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`material_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`material_ficha` (
  `idMaterial_Ficha` INT NULL AUTO_INCREMENT ,
  `idMaterial` INT(11) NOT NULL ,
  `idFicha` INT(11) NOT NULL ,
  PRIMARY KEY (`idMaterial_Ficha`, `idMaterial`, `idFicha`) ,
  CONSTRAINT `fk_Material_Ficha_material1`
    FOREIGN KEY (`idMaterial` )
    REFERENCES `practica`.`material` (`idMaterial` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Material_Ficha_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Material_Ficha_material1_idx` ON `practica`.`material_ficha` (`idMaterial` ASC) ;

CREATE INDEX `fk_Material_Ficha_ficha_tecnica_etiqueta1_idx` ON `practica`.`material_ficha` (`idFicha` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`malla_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`malla_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`malla_ficha` (
  `idMalla_Ficha` INT NOT NULL AUTO_INCREMENT ,
  `idFicha` INT(11) NOT NULL ,
  `idMalla` INT(11) NOT NULL ,
  PRIMARY KEY (`idMalla_Ficha`, `idFicha`, `idMalla`) ,
  CONSTRAINT `fk_Malla_ficha_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Malla_ficha_malla1`
    FOREIGN KEY (`idMalla` )
    REFERENCES `practica`.`malla` (`idMalla` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Malla_ficha_ficha_tecnica_etiqueta1_idx` ON `practica`.`malla_ficha` (`idFicha` ASC) ;

CREATE INDEX `fk_Malla_ficha_malla1_idx` ON `practica`.`malla_ficha` (`idMalla` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`tinta_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`tinta_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`tinta_ficha` (
  `idTinta_ficha` INT NOT NULL AUTO_INCREMENT ,
  `idTinta` INT(11) NOT NULL ,
  `idFicha` INT(11) NOT NULL ,
  PRIMARY KEY (`idTinta_ficha`, `idTinta`, `idFicha`) ,
  CONSTRAINT `fk_TINTA_FICHA_tinta1`
    FOREIGN KEY (`idTinta` )
    REFERENCES `practica`.`tinta` (`idTinta` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TINTA_FICHA_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_TINTA_FICHA_tinta1_idx` ON `practica`.`tinta_ficha` (`idTinta` ASC) ;

CREATE INDEX `fk_TINTA_FICHA_ficha_tecnica_etiqueta1_idx` ON `practica`.`tinta_ficha` (`idFicha` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`adhlam_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`adhlam_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`adhlam_ficha` (
  `idAdhLam_Ficha` INT NOT NULL AUTO_INCREMENT ,
  `idAdhLam` INT(11) NOT NULL ,
  `idFicha` INT(11) NOT NULL ,
  PRIMARY KEY (`idAdhLam_Ficha`, `idAdhLam`, `idFicha`) ,
  CONSTRAINT `fk_AdhLam_Ficha_adhesivo_laminacion1`
    FOREIGN KEY (`idAdhLam` )
    REFERENCES `practica`.`adhesivo_laminacion` (`idAdhLam` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AdhLam_Ficha_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_AdhLam_Ficha_adhesivo_laminacion1_idx` ON `practica`.`adhlam_ficha` (`idAdhLam` ASC) ;

CREATE INDEX `fk_AdhLam_Ficha_ficha_tecnica_etiqueta1_idx` ON `practica`.`adhlam_ficha` (`idFicha` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`adhcofo_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`adhcofo_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`adhcofo_ficha` (
  `idAdhCoFo_Ficha` INT NOT NULL AUTO_INCREMENT ,
  `idAdhColdFoil` INT(11) NOT NULL ,
  `idFicha` INT(11) NOT NULL ,
  PRIMARY KEY (`idAdhCoFo_Ficha`, `idAdhColdFoil`, `idFicha`) ,
  CONSTRAINT `fk_AdhCoFo_Ficha_adhesivo_coldfoil1`
    FOREIGN KEY (`idAdhColdFoil` )
    REFERENCES `practica`.`adhesivo_coldfoil` (`idAdhColdFoil` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AdhCoFo_Ficha_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_AdhCoFo_Ficha_adhesivo_coldfoil1_idx` ON `practica`.`adhcofo_ficha` (`idAdhColdFoil` ASC) ;

CREATE INDEX `fk_AdhCoFo_Ficha_ficha_tecnica_etiqueta1_idx` ON `practica`.`adhcofo_ficha` (`idFicha` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`coldfoil_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`coldfoil_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`coldfoil_ficha` (
  `idColdFoil_Ficha` INT NOT NULL AUTO_INCREMENT ,
  `idColdFoil` INT(11) NOT NULL ,
  `idFicha` INT(11) NOT NULL ,
  PRIMARY KEY (`idColdFoil_Ficha`, `idColdFoil`, `idFicha`) ,
  CONSTRAINT `fk_ColdFoil_Ficha_cold_foil1`
    FOREIGN KEY (`idColdFoil` )
    REFERENCES `practica`.`cold_foil` (`idColdFoil` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ColdFoil_Ficha_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_ColdFoil_Ficha_cold_foil1_idx` ON `practica`.`coldfoil_ficha` (`idColdFoil` ASC) ;

CREATE INDEX `fk_ColdFoil_Ficha_ficha_tecnica_etiqueta1_idx` ON `practica`.`coldfoil_ficha` (`idFicha` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`filmmi_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`filmmi_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`filmmi_ficha` (
  `idFilmMi_Ficha` INT NOT NULL AUTO_INCREMENT ,
  `idFilmMi` INT(11) NOT NULL ,
  `idFicha` INT(11) NOT NULL ,
  PRIMARY KEY (`idFilmMi_Ficha`, `idFilmMi`, `idFicha`) ,
  CONSTRAINT `fk_FilmMi_Ficha_film_micronaje1`
    FOREIGN KEY (`idFilmMi` )
    REFERENCES `practica`.`film_micronaje` (`idFilmMi` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FilmMi_Ficha_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_FilmMi_Ficha_film_micronaje1_idx` ON `practica`.`filmmi_ficha` (`idFilmMi` ASC) ;

CREATE INDEX `fk_FilmMi_Ficha_ficha_tecnica_etiqueta1_idx` ON `practica`.`filmmi_ficha` (`idFicha` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`tbarniz_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`tbarniz_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`tbarniz_ficha` (
  `idTBarniz_Ficha` INT NOT NULL AUTO_INCREMENT ,
  `idTBARNIZ` INT(11) NOT NULL ,
  `idFicha` INT(11) NOT NULL ,
  PRIMARY KEY (`idTBarniz_Ficha`, `idTBARNIZ`, `idFicha`) ,
  CONSTRAINT `fk_TBarniz_Ficha_tipo_barniz1`
    FOREIGN KEY (`idTBARNIZ` )
    REFERENCES `practica`.`tipo_barniz` (`idTBarniz` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TBarniz_Ficha_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_TBarniz_Ficha_tipo_barniz1_idx` ON `practica`.`tbarniz_ficha` (`idTBARNIZ` ASC) ;

CREATE INDEX `fk_TBarniz_Ficha_ficha_tecnica_etiqueta1_idx` ON `practica`.`tbarniz_ficha` (`idFicha` ASC) ;


-- -----------------------------------------------------
-- Table `practica`.`troquel_ficha`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `practica`.`troquel_ficha` ;

CREATE  TABLE IF NOT EXISTS `practica`.`troquel_ficha` (
  `idTroquel_Ficha` INT NOT NULL AUTO_INCREMENT ,
  `idTroquel` INT(11) NOT NULL ,
  `idFicha` INT(11) NOT NULL ,
  PRIMARY KEY (`idTroquel_Ficha`, `idTroquel`, `idFicha`) ,
  CONSTRAINT `fk_Troquel_Ficha_troquel1`
    FOREIGN KEY (`idTroquel` )
    REFERENCES `practica`.`troquel` (`idTroquel` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Troquel_Ficha_ficha_tecnica_etiqueta1`
    FOREIGN KEY (`idFicha` )
    REFERENCES `practica`.`ficha_tecnica_etiqueta` (`idFicha` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Troquel_Ficha_troquel1_idx` ON `practica`.`troquel_ficha` (`idTroquel` ASC) ;

CREATE INDEX `fk_Troquel_Ficha_ficha_tecnica_etiqueta1_idx` ON `practica`.`troquel_ficha` (`idFicha` ASC) ;

USE `practica` ;

-- -----------------------------------------------------
-- Placeholder table for view `practica`.`vinfoetiqueta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `practica`.`vinfoetiqueta` (`Categoria` INT, `Cliente` INT, `Pedido` INT, `Etiqueta` INT, `Maquina` INT);

-- -----------------------------------------------------
-- View `practica`.`vinfoetiqueta`
-- -----------------------------------------------------
DROP VIEW IF EXISTS `practica`.`vinfoetiqueta` ;
DROP TABLE IF EXISTS `practica`.`vinfoetiqueta`;
USE `practica`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `practica`.`vinfoetiqueta` AS select `cat`.`nombre` AS `Categoria`,`c`.`nombreCliente` AS `Cliente`,`f`.`pedido` AS `Pedido`,`f`.`etiqueta` AS `Etiqueta`,`m`.`codigo` AS `Maquina` from (((`practica`.`ficha_tecnica_etiqueta` `f` left join `practica`.`cliente` `c` on((`c`.`idCliente` = `f`.`idCliente`))) left join `practica`.`categoria` `cat` on((`f`.`idCategoria` = `cat`.`idCategoria`))) left join `practica`.`maquina` `m` on((`m`.`idMaquina` = `f`.`idMAQUINA`)));


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
