### System level tokens

_datetime....: 2023-May-03 13:55:26
_template....: datagate\datagate-from-1809\show-tokens.tpl.md
_schema......: dg_examples\examples.cmastnewl1.json

### File level tokens
 
dbname.................. *public/DG NET Local
library................. examples
file.................... CMastNewL1
format.................. RCMMastL1
description............. Cust Master by CustNo
type.................... simple logical
recordlength............ 151
keylength............... 5
duplicatekeys........... not allowed
basefile................ Examples/CMastNew
sqlserveruniqueindex.... unique
alias................... cmastnewl1
keyfieldslist........... cmcustno
allfieldslist........... cmcustno, cmname, cmaddr1, cmcity, cmstate, cmcntry, cmpostcode, cmactive, cmfax, cmphone

### Field level tokens

    name.................... CMCustNo
    description............. Cutomer Number
    alias................... cmcustno
    fulltype................ Type(*Packed) Len(9,0)
    type.................... *Packed
    length.................. 9
    decimals................ 0
    systemtype.............. System.Decimal
    iskey................... True
    keyposition............. 0
    allownull............... False
    sqlservertype........... decimal(9,0)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... PRIMARY KEY

    name.................... CMName
    description............. Customer Name
    alias................... cmname
    fulltype................ Type(*Char) Len(40)
    type.................... *Char
    length.................. 40
    decimals................ 
    systemtype.............. System.String
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... varchar(40)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

    name.................... CMAddr1
    description............. Address Line 1
    alias................... cmaddr1
    fulltype................ Type(*Char) Len(35)
    type.................... *Char
    length.................. 35
    decimals................ 
    systemtype.............. System.String
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... varchar(35)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

    name.................... CMCity
    description............. City
    alias................... cmcity
    fulltype................ Type(*Char) Len(30)
    type.................... *Char
    length.................. 30
    decimals................ 
    systemtype.............. System.String
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... varchar(30)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

    name.................... CMState
    description............. State
    alias................... cmstate
    fulltype................ Type(*Char) Len(2)
    type.................... *Char
    length.................. 2
    decimals................ 
    systemtype.............. System.String
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... varchar(2)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

    name.................... CMCntry
    description............. Country Code
    alias................... cmcntry
    fulltype................ Type(*Char) Len(2)
    type.................... *Char
    length.................. 2
    decimals................ 
    systemtype.............. System.String
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... varchar(2)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

    name.................... CMPostCode
    description............. Postal Code (zip)
    alias................... cmpostcode
    fulltype................ Type(*Char) Len(10)
    type.................... *Char
    length.................. 10
    decimals................ 
    systemtype.............. System.String
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... varchar(10)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

    name.................... CMActive
    description............. Active = 1, else 0
    alias................... cmactive
    fulltype................ Type(*Char) Len(1)
    type.................... *Char
    length.................. 1
    decimals................ 
    systemtype.............. System.String
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... varchar(1)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

    name.................... CMFax
    description............. Fax Number
    alias................... cmfax
    fulltype................ Type(*Packed) Len(10,0)
    type.................... *Packed
    length.................. 10
    decimals................ 0
    systemtype.............. System.Decimal
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... decimal(10,0)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

    name.................... CMPhone
    description............. Main Phone
    alias................... cmphone
    fulltype................ Type(*Char) Len(20)
    type.................... *Char
    length.................. 20
    decimals................ 
    systemtype.............. System.String
    iskey................... False
    keyposition............. -1
    allownull............... False
    sqlservertype........... varchar(20)
    sqlservernull........... NOT NULL
    sqlserverprimarykey..... 

