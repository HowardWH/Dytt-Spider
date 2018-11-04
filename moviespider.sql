/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : moviespider

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-11-04 18:40:39
*/

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for dytt_download
-- ----------------------------
DROP TABLE IF EXISTS `dytt_download`;
CREATE TABLE `dytt_download` (
  `dlid`        INT(11) NOT NULL AUTO_INCREMENT
  COMMENT '下载ID',
  `mid`         INT(11) NOT NULL
  COMMENT '电影ID',
  `downloadurl` TEXT    NOT NULL
  COMMENT '下载地址',
  `makedate`    DATE             DEFAULT NULL
  COMMENT '创建日期',
  `maketime`    TIME             DEFAULT NULL
  COMMENT '创建时间',
  `modifydate`  DATE             DEFAULT NULL
  COMMENT '修改日期',
  `modifytime`  TIME             DEFAULT NULL
  COMMENT '修改时间',
  PRIMARY KEY (`dlid`, `mid`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Table structure for dytt_log
-- ----------------------------
DROP TABLE IF EXISTS `dytt_log`;
CREATE TABLE `dytt_log` (
  `logid`     INT(11) NOT NULL AUTO_INCREMENT
  COMMENT '日志id',
  `home`      VARCHAR(255)     DEFAULT NULL
  COMMENT '发生对象',
  `errorsql`  TEXT COMMENT '错误SQL',
  `errorinfo` TEXT COMMENT '错误描述',
  `datetime`  DATETIME         DEFAULT NULL
  COMMENT '发生时间',
  PRIMARY KEY (`logid`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Table structure for dytt_movies
-- ----------------------------
DROP TABLE IF EXISTS `dytt_movies`;
CREATE TABLE `dytt_movies` (
  `mid`        INT(11)     NOT NULL AUTO_INCREMENT,
  `mhome`      VARCHAR(10)          DEFAULT ''
  COMMENT '网站名字',
  `classic`    VARCHAR(20)          DEFAULT NULL
  COMMENT '视频分类',
  `mname`      VARCHAR(30) NOT NULL
  COMMENT '电影名称',
  `mdesc`      TEXT,
  `mtime`      DATETIME             DEFAULT NULL
  COMMENT '上映时间',
  `hot`        INT(11)              DEFAULT NULL
  COMMENT '热度',
  `makedate`   DATE                 DEFAULT NULL
  COMMENT '创建日期',
  `maketime`   TIME                 DEFAULT NULL
  COMMENT '创建时间',
  `modifydate` DATE                 DEFAULT NULL
  COMMENT '修改日期',
  `modifytime` TIME                 DEFAULT NULL
  COMMENT '修改时间',
  PRIMARY KEY (`mid`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
