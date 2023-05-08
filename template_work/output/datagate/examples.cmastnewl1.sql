--
--DROP TABLE IF EXISTS CMastNewL1

If EXISTS(SELECT * 
          FROM sys.tables
          WHERE SCHEMA_NAME(schema_id) LIKE 'dbo'
          AND name LIKE 'CMastNewL1') DROP TABLE CMastNewL1

CREATE TABLE CMastNewL1 (
    [CMCustNo] decimal(9,0) NOT NULL,
    [CMName] varchar(40) NOT NULL,
    [CMAddr1] varchar(35) NOT NULL,
    [CMCity] varchar(30) NOT NULL,
    [CMState] varchar(2) NOT NULL,
    [CMCntry] varchar(2) NOT NULL,
    [CMPostCode] varchar(10) NOT NULL,
    [CMActive] varchar(1) NOT NULL,
    [CMFax] decimal(10,0) NOT NULL,
    [CMPhone] varchar(20) NOT NULL,

    
    primary key (cmcustno)
);