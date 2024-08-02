-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 25, 2024 at 09:08 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ref` int(15) NOT NULL,
  `name` varchar(200) NOT NULL,
  `mother` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `post` int(150) NOT NULL,
  `mobile` bigint(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `nationality` varchar(100) NOT NULL,
  `idproof` varchar(100) NOT NULL,
  `idnumber` int(100) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ref`, `name`, `mother`, `gender`, `post`, `mobile`, `email`, `nationality`, `idproof`, `idnumber`, `address`) VALUES
(3066, 'harman', 'supinderjitkaur', 'Male', 144001, 6239200462, 'harmanjot1251@gmail.com', 'Indian', 'AdhaarCard', 2147483647, 'Jalandhar'),
(2477, 'harsh jalaf', 'veena', 'Male', 144022, 66616116616, 'jalafharsh@gmail.com', 'Indian', 'PY_VAR9', 321484184, 'jalandhar'),
(5345, 'harmanjot singh', 'supinderjit kaur', 'Male', 144001, 6239200462, 'harmanjot1251@gmail.com', 'Indian', 'AdhaarCard', 623920045, 'Jalandhar'),
(9507, 'karan singh', 'xyz', 'Male', 144001, 5433146649, 'karans@gmail.com', 'Indian', 'AdhaarCard', 451456, 'jalandhar');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `floor` varchar(100) NOT NULL,
  `roomno` varchar(100) NOT NULL,
  `roomtype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`floor`, `roomno`, `roomtype`) VALUES
('11', '101', 'single');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `contact` varchar(200) NOT NULL,
  `check_in` varchar(200) NOT NULL,
  `check_out` varchar(10) NOT NULL,
  `roomtype` varchar(10) NOT NULL,
  `roomavailiable` varchar(100) NOT NULL,
  `meal` varchar(100) NOT NULL,
  `noofdays` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`contact`, `check_in`, `check_out`, `roomtype`, `roomavailiable`, `meal`, `noofdays`) VALUES
('9872090280', '25/11/2024', '5/12/2024', 'Single', '1000', 'lunch', '10'),
('6284721515', '10/2/2024', '20/2/2024', 'Double', '2002', 'lunch', '10');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`username`, `password`, `usertype`) VALUES
('harman', '1234', 'Admin'),
('harsh', '123', 'Employee'),
('harman', '1234', 'Admin'),
('harman', '1234', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`roomno`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`roomavailiable`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
