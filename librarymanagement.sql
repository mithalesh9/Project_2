-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 11, 2021 at 02:30 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `librarymanagement`
--

-- --------------------------------------------------------

--
-- Table structure for table `information`
--

CREATE TABLE `information` (
  `Member` varchar(20) NOT NULL,
  `PRN` varchar(20) NOT NULL,
  `ID` varchar(20) NOT NULL,
  `FirstName` varchar(20) NOT NULL,
  `LastName` varchar(20) NOT NULL,
  `Address1` varchar(20) NOT NULL,
  `Address2` varchar(20) NOT NULL,
  `PostId` varchar(20) NOT NULL,
  `Mobile` varchar(20) NOT NULL,
  `BookId` varchar(20) NOT NULL,
  `Booktitle` varchar(50) NOT NULL,
  `Author` varchar(20) NOT NULL,
  `DateBorrowed` varchar(20) NOT NULL,
  `Datedue` varchar(20) NOT NULL,
  `DaysOnBook` varchar(20) NOT NULL,
  `LateReturnFine` varchar(20) NOT NULL,
  `DateOverDue` varchar(20) NOT NULL,
  `FinalPrice` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `information`
--

INSERT INTO `information` (`Member`, `PRN`, `ID`, `FirstName`, `LastName`, `Address1`, `Address2`, `PostId`, `Mobile`, `BookId`, `Booktitle`, `Author`, `DateBorrowed`, `Datedue`, `DaysOnBook`, `LateReturnFine`, `DateOverDue`, `FinalPrice`) VALUES
('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('Admin staf', '24554666343', '103', 'Bibhav', 'Yadav', 'Noida', 'UP', '4012765', '9743864376', 'BKID1001', 'AI By Example', 'Denis Rothman', '2021-05-14', '2021-05-29', '15', 'Rs.50', 'No', 'Rs.900');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `user` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`user`, `password`) VALUES
('vinay1', '5152'),
('priyesh1', '5152');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `information`
--
ALTER TABLE `information`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
