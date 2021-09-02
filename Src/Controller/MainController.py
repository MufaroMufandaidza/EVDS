from PyQt5 import QtWidgets
import numpy as np

"""
Import all the interfaces that form part of the workflow.
"""
from LandingPage import Ui_LandingPage

from HealthCareWorkerAuthPage import Ui_HealthCareWorkerAuthPage
from HealthCareWorkerLandingPage import Ui_HealthCareWorkerLandingPage
from HealthCareWorkerLoginPage import Ui_HealthCareWorkerLoginPage
from HealthCareWorkerRegistrationPage import Ui_HealthCareWorkerRegistrationPage 
from HealthCareWorkerReportPage import Ui_HealthCareWorkerReportPage
from HealthCareWorkerVaccinationPage import Ui_HealthCareWorkerVaccinationPage

from PatientRegistrationPage import Ui_PatientRegistrationPage
from PatientAppointmentUpdatePage import Ui_PatientAppointmentUpdatePage
from PatientVoucherPage import Ui_PatientVoucherPage
"""
Imports required for the database connection
"""
import pyodbc
import sys
sys.path.insert(1, 'C:/Users/Admin/Documents/SoftwareDevelopment/QT/EVDS/Model')
from Database import Database



"""
Configure start state of ui pages.
"""
class LandingPageView(QtWidgets.QMainWindow, Ui_LandingPage):
    def __init__(self, parent=None):
        super(LandingPageView, self).__init__(parent)
        self.setupUi(self)
        
#Healthcare Worker Pages.

class HealthCareWorkerAuthPageView(QtWidgets.QMainWindow, Ui_HealthCareWorkerAuthPage):
    def __init__(self, parent=None):
        super(HealthCareWorkerAuthPageView, self).__init__(parent)
        self.setupUi(self)

class HealthCareWorkerLandingPageView(QtWidgets.QMainWindow, Ui_HealthCareWorkerLandingPage):
    def __init__(self, parent=None):
        super(HealthCareWorkerLandingPageView, self).__init__(parent)
        self.setupUi(self)

class HealthCareWorkerLoginPageView(QtWidgets.QMainWindow, Ui_HealthCareWorkerLoginPage):
    def __init__(self, parent=None):
        super(HealthCareWorkerLoginPageView, self).__init__(parent)
        self.setupUi(self)

class HealthCareWorkerRegistrationPageView(QtWidgets.QMainWindow, Ui_HealthCareWorkerRegistrationPage):
    def __init__(self, parent=None):
        super(HealthCareWorkerRegistrationPageView, self).__init__(parent)
        self.setupUi(self)

class HealthCareWorkerReportPageView(QtWidgets.QMainWindow, Ui_HealthCareWorkerReportPage):
    def __init__(self, parent=None):
        super(HealthCareWorkerReportPageView, self).__init__(parent)
        self.setupUi(self)

class HealthCareWorkerVaccinationPageView(QtWidgets.QMainWindow, Ui_HealthCareWorkerVaccinationPage):
    def __init__(self, parent=None):
        super(HealthCareWorkerVaccinationPageView, self).__init__(parent)
        self.setupUi(self)

#Patient Management pages

class PatientRegistrationPageView(QtWidgets.QMainWindow, Ui_PatientRegistrationPage):
    def __init__(self, parent=None):
        super(PatientRegistrationPageView, self).__init__(parent)
        self.setupUi(self)

class PatientAppointmentUpdatePageView(QtWidgets.QMainWindow, Ui_PatientAppointmentUpdatePage):
    def __init__(self, parent=None):
        super(PatientAppointmentUpdatePageView, self).__init__(parent)
        self.setupUi(self)

class PatientVoucherPageView(QtWidgets.QMainWindow, Ui_PatientVoucherPage):
    def __init__(self, parent=None):
        super(PatientVoucherPageView, self).__init__(parent)
        self.setupUi(self)

"""
Class managing the entire work-flow.
"""
class Manager:
    def __init__(self):
        self.landingPageView = LandingPageView()
        
        self.healthCareWorkerAuthPageView = HealthCareWorkerAuthPageView()
        self.healthCareWorkerLandingPageView = HealthCareWorkerLandingPageView()
        self.healthCareWorkerLoginPageView = HealthCareWorkerLoginPageView()
        self.healthCareWorkerRegistrationPageView = HealthCareWorkerRegistrationPageView()
        self.healthCareWorkerReportPageView = HealthCareWorkerReportPageView()
        self.healthCareWorkerVaccinationPageView = HealthCareWorkerVaccinationPageView()

        self.patientRegistrationPageView = PatientRegistrationPageView()
        self.patientAppointmentUpdatePageView = PatientAppointmentUpdatePageView()
        self.patientVoucherPageView = PatientVoucherPageView()

        self.landingPageView.btn_hcw.clicked.connect(self.onClickHealthCareWorkerPage)
        self.landingPageView.btn_ptntReg.clicked.connect(self.onClickPatientRegPage)
        self.landingPageView.btn_ptntUpdt.clicked.connect(self.onClickPatientUpdatePage)

        self.healthCareWorkerAuthPageView.btn_rtnHme.clicked.connect(self.onClickReturnHomeHcw)
        self.healthCareWorkerAuthPageView.btn_profRegSubmit.clicked.connect(self.onClickSubmitHcw)

        self.healthCareWorkerLandingPageView.btn_hcwLogin.clicked.connect(self.onClickLoginHcw)
        self.healthCareWorkerLandingPageView.btn_hcwSignup.clicked.connect(self.onClickSigninHcw)

        self.healthCareWorkerRegistrationPageView.btn_hcwReg.clicked.connect(self.onClickHcwReg)

        self.healthCareWorkerLoginPageView.btn_hcwSbmitCred.clicked.connect(self.onClickHcwLog)

        self.healthCareWorkerVaccinationPageView.btn_hcwSbmitVax.clicked.connect(self.onClickHcwVax)

        self.patientRegistrationPageView.btn_ptntRegSubmit.clicked.connect(self.onClickPtntReg)


        self.landingPageView.show()

    """
    Logic managing page trnsitions.
    """
    #Start Health Care worker flow
    def onClickHealthCareWorkerPage(self):
            self.landingPageView.hide()
            self.healthCareWorkerAuthPageView.show()
            self.healthCareWorkerAuthPageView.lb_hcwNotice.hide()    

    #Return to main page        
    def onClickReturnHomeHcw(self):
        self.healthCareWorkerAuthPageView.hide()
        self.landingPageView.show()

    #Open Landing Page
    def onClickSubmitHcw(self):
        if(str(self.healthCareWorkerAuthPageView.et_hcwPRN.text()) == '1234'):
            self.healthCareWorkerAuthPageView.hide()
            self.healthCareWorkerLandingPageView.show()
        else:
            self.healthCareWorkerAuthPageView.lb_hcwNotice.show()

    #Open Login page.
    def onClickLoginHcw(self):
        self.healthCareWorkerLandingPageView.hide()
        self.healthCareWorkerLoginPageView.show()
        self.healthCareWorkerLoginPageView.lb_hcwlginpw.hide()
        self.healthCareWorkerLoginPageView.lb_hcwlginun.hide()
        self.healthCareWorkerLoginPageView.lb_hcwlgmissingnfo.hide()
        self.healthCareWorkerLoginPageView.lb_hcwlgnErr.hide()
        
    #Open Sign-in page.
    def onClickSigninHcw(self):
        self.healthCareWorkerLandingPageView.hide()
        self.healthCareWorkerRegistrationPageView.show()
        self.healthCareWorkerRegistrationPageView.lb_hcwmissingnfo.hide()
        self.healthCareWorkerRegistrationPageView.lb_hcwpassnotice.hide()
        self.healthCareWorkerRegistrationPageView.lb_hcwErr.hide()

    #Register as a healthcare worker
    def onClickHcwReg(self):
        hcwName = len(str(self.healthCareWorkerRegistrationPageView.et_hcwName.text()))
        hcwSurname = len(str(self.healthCareWorkerRegistrationPageView.et_hcwSurname.text()))
        hcwRole = len(str(self.healthCareWorkerRegistrationPageView.et_hcwRole.text()))
        hcwPassreg = len(str(self.healthCareWorkerRegistrationPageView.et_hcwPassreg.text()))
        hcwPassreg1 = len(str(self.healthCareWorkerRegistrationPageView.et_hcwPassreg1.text()))

        hcwName_ = str(self.healthCareWorkerRegistrationPageView.et_hcwName.text())
        hcwSurname_ = str(self.healthCareWorkerRegistrationPageView.et_hcwSurname.text())
        hcwRole_ = str(self.healthCareWorkerRegistrationPageView.et_hcwRole.text())
        hcwPassreg_ = str(self.healthCareWorkerRegistrationPageView.et_hcwPassreg.text())
        hcwPassreg1_ = str(self.healthCareWorkerRegistrationPageView.et_hcwPassreg1.text())

        if  (hcwName == 0 or hcwSurname == 0 or hcwRole == 0 or hcwPassreg == 0 or hcwPassreg1 == 0):
            self.healthCareWorkerRegistrationPageView.lb_hcwmissingnfo.show()
        if (hcwPassreg_ != hcwPassreg1_):
            self.healthCareWorkerRegistrationPageView.lb_hcwpassnotice.show()
        else:
            errFlag = False
            query = ('declare @rm varchar(50) '
                    'EXEC dbo.usp_AddUser '
		            +hcwName_+'_'+hcwSurname_+','+hcwPassreg_+','
		            +hcwName_+','+hcwSurname_+',' 
		            +hcwRole_+', @rm  OUTPUT;'
                    'select @rm'
                    )
            mydb.execute(query)
            for row in mydb:
                if (str(row[0]) == 'Success'):
                    mydb.commit()
                    errFlag = True
                    self.healthCareWorkerRegistrationPageView.close()
                    self.healthCareWorkerLoginPageView.show()
                    self.healthCareWorkerLoginPageView.lb_hcwlginpw.hide()
                    self.healthCareWorkerLoginPageView.lb_hcwlginun.hide()
                    self.healthCareWorkerLoginPageView.lb_hcwlgmissingnfo.hide()
                    self.healthCareWorkerLoginPageView.lb_hcwlgnErr.hide()
                    self.healthCareWorkerLoginPageView.et_hcwUsername.setText(hcwName_+"_"+hcwSurname_)
                    break
            if(errFlag == False):
                self.healthCareWorkerRegistrationPageView.lb_hcwErr.show()

    #Login as a healtcare worker.       
    def onClickHcwLog(self):
        hcwuser = len(str(self.healthCareWorkerLoginPageView.et_hcwUsername.text()))
        hcwpass = len(str(self.healthCareWorkerLoginPageView.et_hcwPass.text()))

        hcwuser_ = str(self.healthCareWorkerLoginPageView.et_hcwUsername.text())
        hcwpass_ = str(self.healthCareWorkerLoginPageView.et_hcwPass.text())

        if(hcwuser == 0 or hcwpass == 0):
            self.healthCareWorkerLoginPageView.lb_hcwlgmissingnfo.show()
        else:
            errFlag = False
            query = ('declare @rm varchar(50) '
                    'EXEC dbo.usp_Login '
                    +hcwuser_+','
                    +hcwpass_+','
                    '@rm  OUTPUT; '
                    'select @rm; '
                    )
            mydb.execute(query)
            for row in mydb:
                if (str(row[0]) == 'Success'):
                    mydb.commit()
                    errFlag = True
                    self.healthCareWorkerLoginPageView.hide()
                    self.healthCareWorkerVaccinationPageView.show()
                    break
                if(str(row[0]) == 'Incorrect_Password'):
                    mydb.commit()
                    errFlag = True
                    self.healthCareWorkerLoginPageView.lb_hcwlginpw.show()
                    break
                if(str(row[0]) == 'Incorrect_Username'):
                    mydb.commit()
                    errFlag = True
                    self.healthCareWorkerLoginPageView.lb_hcwlginun.show()
                    break
            if(errFlag == False):
                self.healthCareWorkerLoginPageView.lb_hcwlgnErr.show()
    
    #Open the register vaccination page
    def onClickHcwVax(self):
        self.healthCareWorkerLoginPageView.hide()
        self.healthCareWorkerVaccinationPageView.show()

    """
    Patient Flow.
    """
    #Open registration page.
    def onClickPatientRegPage(self):
            self.landingPageView.hide()
            self.patientRegistrationPageView.show()
            self.patientRegistrationPageView.lb_missingnfo.hide() 
            self.patientRegistrationPageView.lb_ptntRegErr.hide()

    #Open Details update page.
    def onClickPatientUpdatePage(self):
            self.landingPageView.hide()
            self.patientAppointmentUpdatePageView.show()
            self.patientAppointmentUpdatePageView.lb_voucherWarn.hide() 
            self.patientAppointmentUpdatePageView.gb_appUpdate.hide() 

    #Enroll for Vaccination.       
    def onClickPtntReg(self):
        ptntName = len(str(self.patientRegistrationPageView.et_ptntName.text()))
        ptntSurname = len(str(self.patientRegistrationPageView.et_ptntSurname.text()))
        ptntIdNum = len(str(self.patientRegistrationPageView.et_ptntId.text()))
        ptntCell = len(str(self.patientRegistrationPageView.et_ptntCell.text()))
        ptntEmail = len(str(self.patientRegistrationPageView.et_ptntEmail.text()))
        addLn1 = len(str(self.patientRegistrationPageView.et_addLn1.text()))
        addLn2 = len(str(self.patientRegistrationPageView.et_addLn2.text()))
        city = len(str(self.patientRegistrationPageView.et_city.text()))
        postalCode = len(str(self.patientRegistrationPageView.et_postal.text()))
        facility = len(str(self.patientRegistrationPageView.et_facility.text()))
        gender = len(str(self.patientRegistrationPageView.cmb_gender.currentText()))
        dob = len(str(self.patientRegistrationPageView.dt_DOB.date().toPyDate()))
        vaxDate = len(str(self.patientRegistrationPageView.dt_vaxdate.selectAll()))

        ptntName_ = str(self.patientRegistrationPageView.et_ptntName.text())
        ptntSurname_ = str(self.patientRegistrationPageView.et_ptntSurname.text())
        ptntIdNum_ = str(self.patientRegistrationPageView.et_ptntId.text())
        ptntCell_ = str(self.patientRegistrationPageView.et_ptntCell.text()).replace(" ","")
        ptntEmail_ = str(self.patientRegistrationPageView.et_ptntEmail.text())
        addLn1_ = str(self.patientRegistrationPageView.et_addLn1.text())
        addLn2_ = str(self.patientRegistrationPageView.et_addLn2.text())
        city_ = str(self.patientRegistrationPageView.et_city.text())
        postalCode_ = str(self.patientRegistrationPageView.et_postal.text())
        facility_ = str(self.patientRegistrationPageView.et_facility.text())
        gender_ = str(self.patientRegistrationPageView.cmb_gender.currentText())
        dob_ = str(self.patientRegistrationPageView.dt_DOB.date().toPyDate()).replace("-","")
        vaxDate_ = self.patientRegistrationPageView.dt_vaxdate.dateTime()
        vaxDate_ = vaxDate_.toString(self.patientRegistrationPageView.dt_vaxdate.displayFormat()).replace("/","")

        if(
            ptntName == 0 or ptntSurname == 0 or ptntIdNum == 0 or ptntCell == 0 
            or ptntEmail == 0 or addLn1 == 0 or addLn2 == 0 or city == 0 or postalCode == 0 
            or facility == 0 or gender == 0 or dob == 0 or vaxDate == 0
            ):
            self.patientRegistrationPageView.lb_missingnfo.show()
        
        else:
            errFlag = False
            query = ('declare @rm varchar(50) '
                    'EXEC dbo.usp_AddPatient '
                    +ptntName_+','
                    +ptntSurname_+','
                    +gender_+','
                    +'\''+dob_+'\','
                    +ptntIdNum_+','
                    +ptntCell_+','
                    +ptntEmail_+','
                    +addLn1_+','
                    +addLn2_+','
                    +city_+','
                    +postalCode_+','
                    '@rm  OUTPUT; '
                    'select @rm; '
                    )
            #print(query)
            mydb.execute(query)
            for row in mydb:
                if (str(row[0]) == 'Success'):
                    mydb.commit()
                    errFlag = True
                    break
            if(errFlag == True):
                errFlag = False
                query = ('declare @rm varchar(50) '
                    'EXEC dbo.usp_AddAppointment '
                    +ptntName_+','
                    +ptntIdNum_+','
                    +facility_+','
                    +'\''+vaxDate_+'\','
                    'Vaccination,'                    
                    '@rm  OUTPUT; '
                    'select @rm; '
                    )
            #print(query)
            mydb.execute(query)
            for row in mydb:
                if (str(row[0]) == 'Success'):
                    mydb.commit()
                    errFlag = True
                    break
            if(errFlag == True):
                errFlag = False
                vaccines = ['Johnson and Johnson', 'pfizer']
                query = ('declare @rm varchar(50) '
                    'EXEC dbo.usp_AddVoucher '
                    +ptntName_+','
                    +ptntIdNum_+','
                    +np.random.choice(vaccines)+','                    
                    '@rm  OUTPUT; '
                    'select @rm; '
                    )
            #print(query)
            mydb.execute(query)
            for row in mydb:
                if (str(row[0]) == 'Success'):
                    mydb.commit()
                    errFlag = True
                    break
            
            if(errFlag == False):
                self.patientRegistrationPageView.lb_ptntRegErr.show()
            else:
                self.patientRegistrationPageView.hide()
                self.patientVoucherPageView.show()
                self.patientVoucherPageView.lb_voucher.hide()
                query = ('Select voucher From vouchers '
                    'Where  patientId = ( '
                    'Select id from patients '
                    'where name = \''+ptntName_+'\''
                    ' and idNumber = \''+ptntIdNum_+'\')'
                    )
            print(query)
            mydb.execute(query) 
            for row in mydb:
                self.patientVoucherPageView.lb_voucher.show()
                self.patientVoucherPageView.lb_voucher.setText(str(row[0]))
                mydb.commit()
                errFlag = True
                break


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    database = Database('SERVER_NAME', 'DB_NAME')
    mydb =  database.cursor
    sys.exit(app.exec_())