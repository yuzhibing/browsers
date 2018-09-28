CREATE TABLE `ud_address_details` (
  `Address` varchar(60) DEFAULT NULL,
  `Total_Received` float DEFAULT NULL,
  `Total_Sent` float DEFAULT NULL,
  `Final_Balance` float DEFAULT NULL,
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `update_time` timestamp NULL DEFAULT NULL,
  `trans_no` int(10) DEFAULT NULL,
  `mined_time` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;



CREATE TABLE `ud_block_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `height` int(10) DEFAULT NULL,
  `json_date` varchar(5000) DEFAULT NULL,
  `rsync_date` timestamp NULL DEFAULT NULL,
  `date_type` varchar(10) DEFAULT NULL,
  `block_hash` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `ud_block` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `height` int(10) DEFAULT NULL,
  `mined_by` varchar(10) DEFAULT NULL,
  `difficulty` float DEFAULT NULL,
  `transactions_number` int(10) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `Size` int(10) DEFAULT NULL,
  `Bits` varchar(10) DEFAULT NULL,
  `Block_reward` float DEFAULT NULL,
  `Previous_Block` varchar(100) DEFAULT NULL,
  `Next_Block` varchar(100) DEFAULT NULL,
  `BlockHash` varchar(100) DEFAULT NULL,
  `total_trans` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `block_height_index` (`height`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


CREATE TABLE `ud_price` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  `platform` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


CREATE TABLE `ud_trans_address` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `create_date` timestamp NULL DEFAULT NULL,
  `gt10000_address` int(10) DEFAULT NULL,
  `gt0_address` int(10) DEFAULT NULL,
  `trans_num` int(10) DEFAULT NULL,
  `address_num` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `ud_transaction_records` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `HEIGHT` int(10) DEFAULT NULL,
  `TX_ID` varchar(100) DEFAULT NULL,
  `confirmations` int(60) DEFAULT NULL,
  `time` int(10) DEFAULT NULL,
  `blocktime` int(10) DEFAULT NULL,
  `version` int(10) DEFAULT NULL,
  `fees` float DEFAULT NULL,
  `ud_blockid` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


CREATE TABLE `ud_transaction_recods_vin` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `txid` varchar(100) DEFAULT NULL,
  `vout` int(10) DEFAULT NULL,
  `vin_txid` varchar(100) DEFAULT NULL,
  `ud_transaction_recordsid` int(10) NOT NULL,
  `coinbase` varchar(100) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `vout_vin_txid_index` (`vin_txid`),
  KEY `vout_height_index` (`height`),
  KEY `index_vin_txid` (`txid`),
  KEY `index_vin_vout` (`vout`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


CREATE TABLE `ud_transaction_recods_vout` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `value` float DEFAULT NULL,
  `n` int(10) DEFAULT NULL,
  `txid` varchar(100) DEFAULT NULL,
  `ud_transaction_recordsid` int(10) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `mined_time` timestamp NULL DEFAULT NULL,
  `has_vin` int(10) DEFAULT NULL,
  `coinbase` varchar(100) DEFAULT NULL,
  `height` int(10) DEFAULT NULL,
  `has_trans` varchar(10) DEFAULT NULL,
  `mined_day` varchar(30) DEFAULT NULL,
  `trans_value` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `vout_txid_index` (`txid`),
  KEY `vout_has_vin_index` (`has_vin`),
  KEY `vout_address_index` (`address`),
  KEY `idx_vout_vin` (`has_vin`),
  KEY `index_vout_mined_day` (`mined_day`),
  KEY `index_vout_height` (`height`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;



CREATE TABLE `ud_transaction_recods_address` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `address` varchar(100) DEFAULT NULL,
  `ud_transaction_recods_voutid` int(10) NOT NULL,
  `current_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mined_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `recods_address_index` (`address`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;