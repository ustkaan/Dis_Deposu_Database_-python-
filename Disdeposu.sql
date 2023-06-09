CREATE DATABASE DisDeposu ;
USE DisDeposu;


CREATE TABLE Dishastaneleri (
    Hastane_No DECIMAL(7) NOT NULL CHECK(LENGTH(Hastane_No) = 7),
    Hastane_Ad VARCHAR(40) NOT NULL,
    Hastane_Konum VARCHAR(85) NOT NULL,
    Numara INT  UNIQUE,
    Email VARCHAR(50) UNIQUE NOT NULL CHECK(Email LIKE "%@%"),
    Hastane_Website VARCHAR(100),
    
    PRIMARY KEY (Hastane_No)
);

CREATE TABLE Urunler (
    UrunID INT AUTO_INCREMENT NOT NULL,
    UrunAdi VARCHAR(255) NOT NULL,
    UrunAdet INT NOT NULL,
    UrunFiyat INT NOT NULL,
    
    PRIMARY KEY (UrunID)
);

CREATE TABLE Siparis (
    SiparisID INT AUTO_INCREMENT NOT NULL,
    Hastane_No DECIMAL(7) NOT NULL,
    UrunID INT NOT NULL,
    Adet INT NOT NULL,
    SiparisTarih VARCHAR(100) NOT NULL,
    
    PRIMARY KEY (SiparisID),
    FOREIGN KEY (UrunID) REFERENCES Urunler(UrunID),
    FOREIGN KEY (Hastane_No) REFERENCES Dishastaneleri(Hastane_No)
);

/* Stokta kaç adet olduğunu görmek için
CALL getUrun();
*/
DELIMITER $$
CREATE PROCEDURE getUrun()
BEGIN
SELECT Adet FROM Urunler;
END $$
DELIMITER ;

/*Urunun stok durumunu ogrenmek icin
CALL getStok(Urun_ID);
*/
DELIMITER $$
CREATE PROCEDURE getStok(
	IN ud INT
)
BEGIN
SELECT UrunID AS `UrunID`,  UrunAdi AS `UrunAdi`,  UrunAdet `UrunAdet` FROM Urunler
WHERE UrunID = ud;
END $$
DELIMITER ;


/*Siparis bilgilerini almak icin
CALL getSip("E-mail adresiniz");
*/
DELIMITER $$
CREATE PROCEDURE getSip(
	IN mail VARCHAR(255)
)
BEGIN
SELECT Siparis.SiparisID AS `SiparisID`, Urunler.UrunID AS `UrunID`, Urunler.UrunAdi AS `UrunAdi`, Siparis.Adet, Siparis.SiparisTarih AS `Satin Alindigi Tarih`
FROM Siparis INNER JOIN Dishastaneleri INNER JOIN Urunler
WHERE Siparis.Hastane_No = Dishastaneleri.Hastane_No AND Dishastaneleri.Email = mail AND Siparis.UrunID = Urunler.UrunID
ORDER BY Siparis.SiparisTarih DESC;
END $$
DELIMITER ;

/*Call getSip ("dentalmerkez@dentalmerkez.com.tr");*/ /*Test etmek için*/

/*Urun bilgilerini tabloya eklemek icin
CALL setUrun("Urun_Adi", Adeti, Fiyat);
*/
DELIMITER $$
CREATE PROCEDURE Urunekle(
	IN urunad VARCHAR(255),urunAdet INT, urunfiyat INT
)
BEGIN
INSERT INTO Urunler (UrunAdi, UrunAdet, UrunFiyat)
VALUES (urunad, urunadet, urunfiyat);
END $$
DELIMITER ;

CALL Urunekle("Anguldurva", 500, 5000);
CALL Urunekle("Piyasemen", 1000, 4000);
CALL Urunekle("RVG", 200, 18000);

/*Not: Urunler hataya sebep vermemek icin onceden eklenmistir.*/

/*Hastane bilgilerini tabloya eklemek icin
*/
DELIMITER $$

CREATE PROCEDURE setDishastaneleri(
	IN Hastane_no DECIMAL(7), Hastane_Ad VARCHAR(40),Hastane_Konum VARCHAR(85),Numara INT, Email VARCHAR(50),Hastane_Website VARCHAR(100)
)
BEGIN
INSERT INTO Dishastaneleri
VALUES (Hastane_no,Hastane_ad,Hastane_konum,Numara,Email,Hastane_Website);
END $$
DELIMITER ;

Call setDishastaneleri (1234567, 'DentalMerkezADSM' , 'Kocaeli' , 4449531, 'dentalmerkez@dentalmerkez.com.tr', 'www.dentalmerkez.com.tr');


/*Siparis girmek icin
CALL setSip(TC_NO,Urun_ID,Urun_Adeti);
*/
DELIMITER $$
CREATE PROCEDURE setSiparis(
	IN Hastane DECIMAL(7),urunid INT,urunadet INT
)
BEGIN
INSERT INTO Siparis (Hastane_no, UrunID, Adet, SiparisTarih)
VALUES (Hastane, urunid, urunadet,NOW());
END $$
DELIMITER ;
/*Call setSiparis( 1234567 , 1 , 100 );*/ /*Test etmek için*/
/*Siparis iptal etmek icin
CALL Siptal(Siparis_ID);
*/
DELIMITER $$
CREATE PROCEDURE Siparisiptal(
	IN siparisid INT
)
BEGIN
DELETE FROM Siparis
WHERE SiparisID = siparisid;
END $$
DELIMITER ;

/*Stok guncelleme urunler satin alindiginda stok adetinden dusurmek icin kullaniyoruz.*/
DELIMITER $$
CREATE TRIGGER stokGun
AFTER INSERT ON Siparis FOR EACH ROW
BEGIN
UPDATE Urunler
SET UrunAdet = UrunAdet - NEW.Adet
WHERE UrunID = NEW.UrunID;
END $$
DELIMITER ;

/*Iptal edilen siparisin tekrar stok adet miktarini arttirmak degistirmek icin*/
DELIMITER $$
CREATE TRIGGER stokEs
AFTER DELETE ON Siparis FOR EACH ROW
BEGIN
UPDATE Urunler
SET UrunAdet = UrunAdet + OLD.Adet
WHERE UrunID = OLD.UrunID IN (SELECT * FROM Siparis 
						WHERE SiparisID = OLD.SiparisID
                    );
END $$
DELIMITER ;

/*Urun bilgileri view kullanarak gormek icin
SELECT * FROM urunView;
*/
CREATE VIEW urunView AS
SELECT UrunID AS `Urun ID`, UrunAdi AS `Urun Adi`, UrunAdet AS `Urun Adet`, UrunFiyat AS `Urun Fiyat`
FROM Urunler;

/*STOK ARTISI RAPORU ICIN EKLEMEK ISTENIR ISE*/

 CREATE TABLE StokArtis (
	StokID INT AUTO_INCREMENT NOT NULL,
    UrunID INT NOT NULL,
    Adet INT NOT NULL,
    SATarih DATETIME NOT NULL,
    
    PRIMARY KEY (STokID),
    FOREIGN KEY (UrunID) REFERENCES Urunler(UrunID)
);


/*Bakim ve onarim icin asagidaki kodlari calistirabilirsiniz.*/
ANALYZE TABLE Dishastaneleri;
ANALYZE TABLE Urunler;
ANALYZE TABLE Siparis;
REPAIR TABLE Dishastaneleri;
REPAIR TABLE Urunler;
REPAIR TABLE Siparis;



