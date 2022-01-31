from fastapi import FastAPI
import smtplib



app = FastAPI()

connect = smtplib.SMTP(host='smtp.gmail.com', port=587)
connect.ehlo()
connect.starttls()


@app.post("/email")
def post_info(name_company, position , contract, labels):
    if name_company:
        connect.login(user='email that connect', password='password')
        msg = f" Nombre de la compañia: {name_company}, Puesto: {position}, Contrato:  {contract}, Etiqueta: {labels}"
        connect.sendmail(from_addr='email that send', to_addrs='email to get', msg=msg.encode("utf-8"))
        connect.quit()
        return  name_company, position, contract, labels
    return {"msg": "Error"}

    