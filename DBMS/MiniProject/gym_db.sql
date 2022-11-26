-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2022 at 04:33 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gym_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `id` int(30) NOT NULL,
  `member_id` int(30) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `middlename` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `address` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `date_created` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`id`, `member_id`, `firstname`, `middlename`, `lastname`, `gender`, `contact`, `address`, `email`, `date_created`) VALUES
(1, 103197, 'Mythreya', 'H', 'M', 'Male', '8310712803', 'ABC', 'hm.mythreya@gmail.com', '2022-03-11 00:00:00'),
(2, 199087, 'Bhavya', 'N', '', 'Female', '1234567890', 'XYZ', 'bhavya@gmail.com', '2022-03-10 11:41:06'),
(3, 199233, 'Random', 'Name', 'hi', 'Male', '1231231231', 'Secret', 'rand@yahoo.com', '2016-03-10 11:41:06'),
(4, 129653, 'Hello', 'World', '', 'Other', '9998887771', 'who knows', 'hello@world.com', '2019-11-07 19:36:42'),
(5, 111246, 'DBMS', 'Mini', 'Project', 'Other', '2468246824', 'PES University', 'dbms@project.com', '2022-11-19 19:39:10');

-- --------------------------------------------------------

--
-- Table structure for table `packages`
--

CREATE TABLE `packages` (
  `id` int(30) NOT NULL,
  `package` varchar(200) NOT NULL,
  `description` text NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `packages`
--

INSERT INTO `packages` (`id`, `package`, `description`, `amount`) VALUES
(1, 'Basic Trial Package', '1 Week Trial For those who want to trial the facilities', 0),
(2, 'Basic GYM Package', '6 Months of GYM Package. Does not include trainers or any additional facilities', 5000),
(3, 'Pro Gym Package', '6 Months of Pro GYM Package. Members will recieve 10 trainer sessions, 2 professional diets according to your needs, and unlimited workout plans. Other facilities not included.', 7000),
(4, 'Premium GYM Package', '12 Months of ultimate premium GYM Package. 20 Trainer sessions, 4 personilized diets, unlimited workout plans, unlimited zoomba, boxing and yoga classes, access to jacuzzi and steamhouse.', 24000);

-- --------------------------------------------------------

--
-- Table structure for table `registration_info`
--

CREATE TABLE `registration_info` (
  `id` int(30) NOT NULL,
  `member_id` int(30) NOT NULL,
  `package_id` int(30) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `trainer_id` tinyint(30) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '0=Inactive, 1= Active',
  `date_created` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration_info`
--

INSERT INTO `registration_info` (`id`, `member_id`, `package_id`, `start_date`, `end_date`, `trainer_id`, `status`, `date_created`) VALUES
(1, 1, 4, '2022-03-11', '2023-03-11', 0, 1, '2022-03-11 00:00:00'),
(2, 2, 2, '2022-09-10', '2023-02-10', 0, 1, '2022-03-10 11:41:06'),
(3, 3, 2, '2016-03-10', '2016-09-10', 0, 0, '2016-03-10 00:00:00'),
(4, 4, 3, '2019-11-07', '2020-05-07', 0, 0, '2019-11-07 19:36:42'),
(5, 5, 1, '2022-11-19', '2022-11-26', 0, 1, '2022-11-19 19:39:10');

-- --------------------------------------------------------

--
-- Table structure for table `schedules`
--

CREATE TABLE `schedules` (
  `id` int(30) NOT NULL,
  `member_id` int(30) NOT NULL,
  `dow` text NOT NULL,
  `date_from` date NOT NULL,
  `date_to` date NOT NULL,
  `time_from` time NOT NULL,
  `time_to` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `trainers`
--

CREATE TABLE `trainers` (
  `id` int(30) NOT NULL,
  `name` text NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `rate` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trainers`
--

INSERT INTO `trainers` (`id`, `name`, `contact`, `email`, `rate`) VALUES
(1, 'Adones Chad', '7777777777', 'adones@gmail.com', 30000);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(30) NOT NULL,
  `name` text NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` text NOT NULL,
  `type` tinyint(1) NOT NULL DEFAULT 3 COMMENT '1=Admin,2=Staff, 3= subscriber'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `password`, `type`) VALUES
(1, 'Angel Jude Suarez', 'admin', '21232f297a57a5a743894a0e4a801fc3', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `packages`
--
ALTER TABLE `packages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registration_info`
--
ALTER TABLE `registration_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `schedules`
--
ALTER TABLE `schedules`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `trainers`
--
ALTER TABLE `trainers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `packages`
--
ALTER TABLE `packages`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `registration_info`
--
ALTER TABLE `registration_info`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `schedules`
--
ALTER TABLE `schedules`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `trainers`
--
ALTER TABLE `trainers`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
