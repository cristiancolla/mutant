-- phpMyAdmin SQL Dump
-- version 2.10.3
-- http://www.phpmyadmin.net
-- 
-- Servidor: localhost
-- Tiempo de generación: 08-08-2019 a las 14:42:34
-- Versión del servidor: 5.0.51
-- Versión de PHP: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- 
-- Base de datos: `test`
-- 

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `dna`
-- 

CREATE TABLE `dna` (
  `id` int(11) NOT NULL auto_increment,
  `dna` text NOT NULL,
  `isMutant` tinyint(1) NOT NULL default '0',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------
