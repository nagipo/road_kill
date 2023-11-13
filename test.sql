CREATE   Table UPLOAD(
    upload_id INT NOT NULL PRIMARY KEY ,
    upload_img mediumblob ,
    account_id  INT  FOREIGN KEY REFERENCES account(account_id),
    identifi VARCHAR(100),
    challenge VARCHAR(100)

)
CREATE   Table upload(
    upload_id INT NOT NULL PRIMARY KEY ,
    upload_img mediumblob ,
    account_id  INT UNSIGNED,
    identifi VARCHAR(100),
    challenge VARCHAR(100),
    FOREIGN KEY (account_id) REFERENCES account(account_id)

)
INSERT INTO upload(upload_img,account_id,identifi) VALUES(%s,1,'Muntiacus reevesi')