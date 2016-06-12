create database db_monitor character set=utf8;
use db_monitor; 
CREATE TABLE `querystat_pstat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trx_id` varchar(200) DEFAULT NULL,
  `trx_mysql_thread_id` varchar(200) DEFAULT NULL,
  `user` varchar(200) DEFAULT NULL,
  `host` varchar(200) DEFAULT NULL,
  `dhost` varchar(200) DEFAULT NULL,
  `db` varchar(200) DEFAULT NULL,
  `command` varchar(200) DEFAULT NULL,
  `time` varchar(200) DEFAULT NULL,
  `state` varchar(200) DEFAULT NULL,
  `info` text,
  `trx_stat` varchar(200) DEFAULT NULL,
  `trx_wait_started` varchar(200) DEFAULT NULL,
  `trx_query` text,
  `blocking_trx_id` varchar(200) DEFAULT NULL,
  `is_blocker` varchar(200) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_create_time` (`create_time`),
  KEY `idx_time` (`time`),
  KEY `idx_01` (`dhost`,`create_time`),
  KEY `idx_02` (`dhost`)
) ENGINE=InnoDB AUTO_INCREMENT=12795 DEFAULT CHARSET=utf8;
