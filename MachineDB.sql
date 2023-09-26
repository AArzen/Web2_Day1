CREATE TABLE `TraceDataHead` (
  `ID_Trace_Data_Head` integer PRIMARY KEY AUTO_INCREMENT,
  `Date` datetime NOT NULL DEFAULT (now()),
  `Serial_Num` varchar(50),
  `Order_Num` varchar(50),
  `Quality` integer COMMENT '0 = in progress, 1 = good, 2 = bad',
  `Error_Num` varchar(50),
  `Error_Desc` varchar(255),
  `Plant` varchar(50)
);

CREATE TABLE `TraceProductParameters` (
  `ID_Trace_Product_Parameter` integer PRIMARY KEY AUTO_INCREMENT,
  `ID_Trace_Data_Head` integer NOT NULL,
  `ID_Product_Paramater` integer,
  `ID_Parameter_Type` integer,
  `Toleranc_Min` float,
  `Toleranc_Max` float,
  `Target_Value` float,
  `Actual_value` varchar(255),
  `Unit` varchar(50),
  `Quality` integer COMMENT '0 = indefinable, 1 = good, 2 = bad'
);

CREATE TABLE `ProductParameterList` (
  `ID_Product_Paramater` integer PRIMARY KEY AUTO_INCREMENT,
  `ID_Worker` integer,
  `Work_Station` varchar(50),
  `Paramater_Num` integer,
  `Paramater_desc_short` varchar(50),
  `Paramater_desc_long` varchar(255)
);

CREATE TABLE `ParameterTypeList` (
  `ID_Parameter_Type` integer PRIMARY KEY AUTO_INCREMENT,
  `Type` varchar(50) NOT NULL COMMENT '1 - String
2 - LongString
3 - Float
4 - TimeStamp
5 - Boolean
6 - Integer'
);

CREATE TABLE `TraceProductComponents` (
  `ID_Trace_Product_Component` integer PRIMARY KEY AUTO_INCREMENT,
  `ID_Trace_Data_Head` integer NOT NULL,
  `ID_Worker` integer,
  `Number` varchar(50),
  `Batch` varchar(50),
  `SSCC` varchar(50),
  `Serial` varchar(50),
  `Quantity` decimal(13, 3),
  `Unit` varchar(50)
);

CREATE TABLE `StoredMachineParamaters` (
  `ID_Machine_Paramater` integer PRIMARY KEY AUTO_INCREMENT,
  `ID_ParamaterTypeList` integer,
  `Date` datetime DEFAULT (now()),
  `Plant` varchar(50),
  `WorkStation` varchar(50),
  `Tolerance_Min` float,
  `Toleranc_Max` float,
  `Target_Value` float,
  `Actual_Value` varchar(255),
  `Unit` varchar(50),
  `Description` varchar(100)
);

CREATE TABLE `WorkerList` (
  `ID_Worker` integer PRIMARY KEY AUTO_INCREMENT,
  `Code` integer UNIQUE NOT NULL,
  `Date` datetime DEFAULT (now()),
  `Name` varchar(50),
  `ID_Security_Level` integer NOT NULL
);

CREATE TABLE `Security_Level` (
  `ID_Security_Level` integer PRIMARY KEY AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Description` varchar(255)
);

ALTER TABLE `TraceDataHead` COMMENT = 'Parts
  Kos ima več zapisov, sortiramo po Serial_Num in Order_Num.
  Povežemo lahko vse paramatre in uporabljene materiale.';

ALTER TABLE `TraceProductParameters` COMMENT = 'Part paramaters';

ALTER TABLE `ProductParameterList` COMMENT = 'Paramater list';

ALTER TABLE `TraceProductComponents` COMMENT = 'Material list';

ALTER TABLE `StoredMachineParamaters` COMMENT = 'Stored machine paramaters';

ALTER TABLE `TraceProductParameters` ADD FOREIGN KEY (`ID_Trace_Data_Head`) REFERENCES `TraceDataHead` (`ID_Trace_Data_Head`);

ALTER TABLE `TraceProductParameters` ADD FOREIGN KEY (`ID_Product_Paramater`) REFERENCES `ProductParameterList` (`ID_Product_Paramater`);

ALTER TABLE `TraceProductComponents` ADD FOREIGN KEY (`ID_Trace_Data_Head`) REFERENCES `TraceDataHead` (`ID_Trace_Data_Head`);

ALTER TABLE `TraceProductComponents` ADD FOREIGN KEY (`ID_Worker`) REFERENCES `WorkerList` (`ID_Worker`);

ALTER TABLE `ProductParameterList` ADD FOREIGN KEY (`ID_Worker`) REFERENCES `WorkerList` (`ID_Worker`);

ALTER TABLE `WorkerList` ADD FOREIGN KEY (`ID_Security_Level`) REFERENCES `Security_Level` (`ID_Security_Level`);

ALTER TABLE `TraceProductParameters` ADD FOREIGN KEY (`ID_Parameter_Type`) REFERENCES `ParameterTypeList` (`ID_Parameter_Type`);

ALTER TABLE `StoredMachineParamaters` ADD FOREIGN KEY (`ID_ParamaterTypeList`) REFERENCES `ParameterTypeList` (`ID_Parameter_Type`);
