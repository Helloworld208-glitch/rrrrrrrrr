from fastapi import APIRouter,Depends,Body
from schema import Usercreate, userinlogin

from datetime import date
from database import get_db

from usermanagement import * 
authentification = APIRouter()



@authentification.post("/login")
def auth(userinlogin: userinlogin, session=Depends(get_db)):
        return usermanagement(session).log_in(userinlogin)



@authentification.post("/signup")
def signup(Usercreate: Usercreate, session = Depends(get_db) ):
        return usermanagement(session).sign_up_user(Usercreate)

@authentification.post("/getname")
def signup(authorization:Annotated[Union[str,None],Header()]=None, session = Depends(get_db) ):
        return usermanagement(session).get_user_name(authorization=authorization)

@authentification.post("/addappointement")
def signup(Date:date = Body(...,embed=True),authorization:Annotated[Union[str,None],Header()]=None, session = Depends(get_db)):
     print("working")
     return usermanagement(session).book_Appointement(appointment_date=Date,authorization=authorization)



@authentification.post("/getappointement")
def signup(authorization:Annotated[Union[str,None],Header()]=None, session = Depends(get_db)):
    
     return usermanagement(session).get_Appointement(authorization=authorization)
@authentification.post("/SecretAdminlogin")
def auth(user: userinlogin, session=Depends(get_db)):
        return usermanagement(session).admin_log_in(user)

@authentification.post("/getaADMINppointement")
def signup(authorization:Annotated[Union[str,None],Header()]=None, session = Depends(get_db)):
    
     return usermanagement(session).get_Appointement_admin(authorization=authorization)

@authentification.post("/SecretAdminsignup")
def auth(user: userinlogin, session=Depends(get_db)):
        print("tesssssst")
        return usermanagement(session).sign_up_admin(user)

@authentification.post("/Updatestatue")
def auth(  appointmentId: int = Body(...),
    statue: str = Body(...),
    authorization: Annotated[Union[str, None], Header()] = None,
    session=Depends(get_db)):
        
        return usermanagement(session).update_appointment(appointmentId=appointmentId,statue=statue,authorization=authorization)






