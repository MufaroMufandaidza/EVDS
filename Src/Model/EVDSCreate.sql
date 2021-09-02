/*
This script contains all the information required to set up the database
to manage all the data required for the application
*/
--TABLES
Create Table dbo.Patients(
	id uniqueidentifier default newid(),
	name varchar(50) not null,
	surname varchar(100) not null,
	gender varchar(1) null,
	birthDate date not null,
	idNumber varchar(13) not null,
	cellphone varchar(10) null,
	email varchar(50) null,
	addressLn1 varchar(100) null,
	addressLn2 varchar(100) null,
	city varchar(100) null,
	postalCode varchar(6) null,
	constraint Pk_Patients Primary Key(id)
);

Create Table dbo.Appointments(
	id uniqueidentifier default newid(),
	patientId uniqueidentifier not null,
	facility varchar(100) not null,
	appointmentDate datetime not null,
	appointmentReason varchar(100) null,
	constraint Pk_Appointments Primary Key(id),
	constraint Fk_Appointments Foreign Key(patientId)
	References Patients(id)
);

Create Table dbo.Vouchers(
	id uniqueidentifier default newid(),
	patientId uniqueidentifier not null,
	voucher int identity,
	vaccineDetail varchar(250) not null,
	constraint Pk_Vouchers Primary Key(id),
	constraint Fk_Vouchers Foreign Key(patientId)
	References Patients(id)
);

Create Table dbo.Users(
	id uniqueidentifier default newid(),
	name varchar(50) not null,
	surname varchar(100) not null,
	Role varchar(100) not null,
	username varchar(50) not null,
	salt UNIQUEIDENTIFIER,
	password Binary(64) not null,
	constraint Pk_Users Primary Key(id)
);

Create Table dbo.Vaccinations(
	id uniqueidentifier default newid(),
	vaccinationId int identity ,
	userId uniqueidentifier not null Foreign Key	References Users(id),
	facility varchar(100) not null,
	voucherId uniqueidentifier not null Foreign Key	References Vouchers(id),
	patientId uniqueidentifier not null Foreign Key	References Patients(id),
	appointmentId uniqueidentifier not null Foreign Key	References Appointments(id),
	vaccinationDate datetime not null,
	constraint Pk_Vaccinations Primary Key(id),
);

Create Table dbo.VaccineLookUp(
	id uniqueidentifier default newid(),
	name varchar(100) not null,
	manufacturer varchar(100)  not null,
	doseQty smallint not null,
	constraint Pk_VaccineLkp Primary Key(id)
);

--STORED PROCEDURES
CREATE PROCEDURE dbo.usp_AddUser

    @pUserName NVARCHAR(50), 
    @pPassword NVARCHAR(50),
    @pFirstName NVARCHAR(40), 
    @pLastName NVARCHAR(40),
	@pRole NVARCHAR(40),
    @responseMessage NVARCHAR(250) OUTPUT
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @salt UNIQUEIDENTIFIER=NEWID()
    BEGIN TRY

        INSERT INTO dbo.[Users] (username, Password, salt, name, surname, role)
        VALUES(@pUserName, HASHBYTES('SHA2_512', @pPassword+CAST(@salt AS NVARCHAR(36))), @salt, @pFirstName, @pLastName, @pRole)

       SET @responseMessage='Success'

    END TRY
    BEGIN CATCH
        SET @responseMessage=ERROR_MESSAGE() 
    END CATCH

END

CREATE PROCEDURE dbo.usp_Login
    @pLoginName NVARCHAR(254),
    @pPassword NVARCHAR(50),
    @responseMessage NVARCHAR(250)='' OUTPUT
AS
BEGIN

    SET NOCOUNT ON

    DECLARE @userID varchar(250)

    IF EXISTS (SELECT TOP 1 username FROM [dbo].[Users] WHERE username=@pLoginName)
    BEGIN
        SET @userID=(SELECT username FROM [dbo].[Users] WHERE username=@pLoginName AND password=HASHBYTES('SHA2_512', @pPassword+CAST(salt AS NVARCHAR(36))))

       IF(@userID IS NULL)
           SET @responseMessage='Incorrect_Password'
       ELSE 
           SET @responseMessage='Success'
    END
    ELSE
       SET @responseMessage='Incorrect_Username'

END

CREATE PROCEDURE dbo.usp_AddPatient

    @name NVARCHAR(50), 
	@surname NVARCHAR(100), 
	@gender NVARCHAR(1), 
	@birthDate date, 
	@idNumber NVARCHAR(13), 
	@cellphone NVARCHAR(10), 
	@email NVARCHAR(50), 
	@addressLn1 NVARCHAR(100), 
	@addressLn2 NVARCHAR(100), 
	@city NVARCHAR(100), 
	@postalCode NVARCHAR(6),
    @responseMessage NVARCHAR(250) OUTPUT
AS
BEGIN
    SET NOCOUNT ON

    BEGIN TRY
		INSERT INTO
        [dbo].[Patients]
           ([name],[surname],[gender],[birthDate],[idNumber],[cellphone]
           ,[email],[addressLn1],[addressLn2],[city],[postalCode])
     VALUES
           ( @name, @surname, @gender,  CAST(@birthDate as DATE), @idNumber, @cellphone, 
           @email, @addressLn1, @addressLn2, @city, @postalCode)

       SET @responseMessage='Success'

    END TRY
    BEGIN CATCH
        SET @responseMessage=ERROR_MESSAGE() 
    END CATCH

END


CREATE PROCEDURE dbo.usp_AddAppointment

    @name NVARCHAR(50),  
	@idNumber NVARCHAR(13), 
	@facility NVARCHAR(100), 
	@appointmentDate datetime, 
	@appointmentReason NVARCHAR(100),
    @responseMessage NVARCHAR(250) OUTPUT
AS
BEGIN
    SET NOCOUNT ON

    BEGIN TRY
		INSERT INTO
        [dbo].[Appointments]
           ([patientId],[facility],[appointmentDate],[appointmentReason])
     VALUES
           ( (select id from Patients where  name = @name and idNumber = @idNumber), @facility, CAST(@appointmentDate AS datetime), @appointmentReason)

       SET @responseMessage='Success'

    END TRY
    BEGIN CATCH
        SET @responseMessage=ERROR_MESSAGE() 
    END CATCH

END


CREATE PROCEDURE dbo.usp_AddVoucher

    @name NVARCHAR(50),  
	@idNumber NVARCHAR(13),   
	@vaccineDetail NVARCHAR(250),
    @responseMessage NVARCHAR(250) OUTPUT
AS
BEGIN
    SET NOCOUNT ON

    BEGIN TRY
		INSERT INTO
        [dbo].[Vouchers]
           ([patientId],[vaccineDetail])
     VALUES
           ( (select id from Patients where  name = @name and idNumber = @idNumber), @vaccineDetail)

       SET @responseMessage='Success'

    END TRY
    BEGIN CATCH
        SET @responseMessage=ERROR_MESSAGE() 
    END CATCH

END
