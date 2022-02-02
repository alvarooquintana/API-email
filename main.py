from fastapi import FastAPI
from config import settings
import smtplib



app = FastAPI()

connect = smtplib.SMTP(host='smtp.gmail.com', port=587)
connect.ehlo()
connect.starttls()


@app.post("/email")
def post_info(name_company, position , contract, labels):
    if name_company:
        connect.login(user=settings.user, password=settings.password)
        msg = f" Nombre de la compañia: {name_company}, Puesto: {position}, Contrato:  {contract}, Etiqueta: {labels}"
        connect.sendmail(from_addr=settings.from_addr, to_addrs=settings.to_addrs, msg=msg.encode("utf-8"))
        connect.quit()
        return  name_company, position, contract, labels
    return {"msg": "Error"}

    