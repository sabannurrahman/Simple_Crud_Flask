-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2024 at 01:27 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_toko`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_item`
--

CREATE TABLE `tb_item` (
  `id` int(10) NOT NULL,
  `name_item` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `stok` int(10) NOT NULL,
  `unit` varchar(15) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created_at` date NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_item`
--

INSERT INTO `tb_item` (`id`, `name_item`, `price`, `stok`, `unit`, `image`, `created_at`, `description`) VALUES
(34, 'sepatu  baru', 20000, 20, 'Buah', '1.jpg', '2024-04-16', 'sepatu baru');

-- --------------------------------------------------------

--
-- Table structure for table `tb_user`
--

CREATE TABLE `tb_user` (
  `id` int(7) NOT NULL,
  `name_user` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `phone_number` varchar(30) NOT NULL,
  `address` text NOT NULL,
  `isAdmin` enum('Admin','Pegawai','','') NOT NULL,
  `password` varchar(200) NOT NULL,
  `created_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_user`
--

INSERT INTO `tb_user` (`id`, `name_user`, `username`, `phone_number`, `address`, `isAdmin`, `password`, `created_at`) VALUES
(8, 'saban', 'saban123', '082237473828', 'jakarta', 'Admin', 'scrypt:32768:8:1$j6W422BNEJ0duvFL$b3659674e1feae9b1c8534d41ea2e75ac1be987b61feb2a8771e4e177bb124bca2f27d390854eab4335e713adf9cf50c398593ab9ca725e0bb7a81922d8b8da0', '2024-04-07'),
(10, 'Saban Nurrahman', 'saban12345', '08223495232', 'Pancoran Jakarta Selatan', 'Pegawai', 'scrypt:32768:8:1$5BEteizSFARAerJf$038b683ea312c44472957291d5cdc89cca41bf8ba4d280100e30569f91ec62f0b47712d24d25c4638cde1fe4516b14b8f370e6cfea33184ba03cb2389a6cd662', '2024-04-12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_item`
--
ALTER TABLE `tb_item`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_item`
--
ALTER TABLE `tb_item`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `tb_user`
--
ALTER TABLE `tb_user`
  MODIFY `id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
