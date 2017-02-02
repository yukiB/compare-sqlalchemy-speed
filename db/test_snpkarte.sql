SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


-- -----------------------------------------------------
-- Table `subject`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `subject` (
  `id` BIGINT(20) NOT NULL ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `institute`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `institute` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL DEFAULT '' ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `method`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `method` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL DEFAULT '' ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `datatype`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `datatype` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL DEFAULT '' ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `dataclass`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `dataclass` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL DEFAULT '' ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `type`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `type` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `question`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `question` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `wid` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL DEFAULT '' ,
  `pid` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL ,
  `description` TEXT NOT NULL ,
  `datatype_id` BIGINT(20) NOT NULL ,
  `institute_id` BIGINT(20) NOT NULL ,
  `dataclass_id` BIGINT(20) NOT NULL ,
  `unit` VARCHAR(255) NULL ,
  `method_id` BIGINT(20) NOT NULL ,
  `note` TEXT NULL ,
  `upper_limit` FLOAT NULL ,
  `lower_limit` FLOAT NULL ,
  `type_id` BIGINT(20) NOT NULL ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_question_institute_idx` (`institute_id` ASC) ,
  INDEX `fk_question_method1_idx` (`method_id` ASC) ,
  INDEX `fk_question_datatype1_idx` (`datatype_id` ASC) ,
  INDEX `fk_question_dataclass1_idx` (`dataclass_id` ASC) ,
  INDEX `fk_question_type1_idx` (`type_id` ASC) ,
  CONSTRAINT `fk_question_institute`
    FOREIGN KEY (`institute_id` )
    REFERENCES `institute` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_question_method1`
    FOREIGN KEY (`method_id` )
    REFERENCES `method` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_question_datatype1`
    FOREIGN KEY (`datatype_id` )
    REFERENCES `datatype` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_question_dataclass1`
    FOREIGN KEY (`dataclass_id` )
    REFERENCES `dataclass` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_question_type1`
    FOREIGN KEY (`type_id` )
    REFERENCES `type` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `answer`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `answer` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  `question_id` BIGINT(20) NOT NULL ,
  `subject_id` BIGINT(20) NOT NULL ,
  `val_int` INT(11) NULL ,
  `val_float` FLOAT NULL ,
  `val_text` TEXT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_answer_question1_idx` (`question_id` ASC) ,
  INDEX `fk_answer_subject1_idx` (`subject_id` ASC) ,
  CONSTRAINT `fk_answer_question1`
    FOREIGN KEY (`question_id` )
    REFERENCES `question` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_answer_subject1`
    FOREIGN KEY (`subject_id` )
    REFERENCES `subject` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `selection`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `selection` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  `question_id` BIGINT(20) NOT NULL ,
  `selection_num` INT(11) NOT NULL ,
  `name` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_answer_detail_question1_idx` (`question_id` ASC) ,
  CONSTRAINT `fk_answer_detail_question1`
    FOREIGN KEY (`question_id` )
    REFERENCES `question` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `rs`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `rs` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `marker_id` VARCHAR(45) NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  `ref` VARCHAR(4) NOT NULL ,
  `var` VARCHAR(4) NOT NULL ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) ,
  UNIQUE INDEX `marker_id_UNIQUE` (`marker_id` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `allele`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `allele` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL DEFAULT '' ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `snp`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `snp` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `rs_id` BIGINT(20) NOT NULL ,
  `subject_id` BIGINT(20) NOT NULL ,
  `allele_id` BIGINT(20) NOT NULL ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_snp_rs1_idx` (`rs_id` ASC) ,
  INDEX `fk_snp_subject1_idx` (`subject_id` ASC) ,
  INDEX `fk_snp_allele1_idx` (`allele_id` ASC) ,
  CONSTRAINT `fk_snp_rs1`
    FOREIGN KEY (`rs_id` )
    REFERENCES `rs` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_snp_subject1`
    FOREIGN KEY (`subject_id` )
    REFERENCES `subject` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_snp_allele1`
    FOREIGN KEY (`allele_id` )
    REFERENCES `allele` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `question_rs`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `question_rs` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT ,
  `updated_at` BIGINT(20) NOT NULL ,
  `created_at` BIGINT(20) NOT NULL ,
  `question_id` BIGINT(20) NOT NULL ,
  `rs_id` BIGINT(20) NOT NULL ,
  `p_val` FLOAT NOT NULL ,
  `or_val` FLOAT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_question_rs_rs1_idx` (`rs_id` ASC) ,
  INDEX `fk_question_rs_question1_idx` (`question_id` ASC) ,
  CONSTRAINT `fk_question_rs_rs1`
    FOREIGN KEY (`rs_id` )
    REFERENCES `rs` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_question_rs_question1`
    FOREIGN KEY (`question_id` )
    REFERENCES `question` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
