-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2020 at 04:08 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blogapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `message`, `date`) VALUES
(1, 'first', 'first@gmail.com', '1234456', 'first', '2020-05-21 01:10:56'),
(2, 'Vaibav Paliwal', 'vpaliwal1@gmail.com', '0487607053', 'test message', '2020-05-21 01:18:24'),
(3, 'Vaibav Paliwal', 'vpaliwal1@gmail.com', '0487607053', 'hi test message', '2020-05-25 21:49:51');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(50) NOT NULL,
  `tagline` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `tagline`, `content`, `date`) VALUES
(1, 'First Post', 'first-post', 'post2', 'Abdul Rashid Salim Salman Khan (pronounced [səlˈmaːn ˈxaːn]; Hindi: About this soundpronunciation (help·info); 27 December 1965)[4] is an Indian film actor, producer, occasional singer and television personality. In a film career spanning over thirty years, Khan has received numerous awards, including two National Film Awards as a film producer, and two Filmfare Awards for acting.[5] He has a significant following in Asia and the Indian diaspora worldwide,[6][better source needed] and is cited in the media as one of the most commercially successful actors of both world and Indian cinema.[7][8] According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was the highest ranked Indian with 82nd rank with earnings of $37.7 million', '2020-06-14 01:36:10'),
(2, 'Second post', 'post', 'new post', 'wsdd', '2020-06-14 01:35:50'),
(3, 'Third post', 'third-post', 'new post', 'jhdjfd', '2020-06-14 01:35:36'),
(5, 'Fourth Page', 'fourth-page', 'another post', 'Hi this is my fourth post.', '2020-06-14 16:00:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
