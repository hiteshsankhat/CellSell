import smtplib
import ssl
from server import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "kvirat2944@gmail.com"
# password = "9004652865"

# # message to be sent
# message = "Message_you_need_to_send"
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, sender_email, message)


def preparedMailData(data, form, phone):
    msg = '''
        <table>
        <tr>
            <td>Name</td>
            <td>{name}</td>
        </tr>
        <tr>
            <td>Phone Number</td>
            <td>{phone}</td>
        </tr>
        <tr>
            <td colspan="2">Address</td>
        </tr>
        <tr>
            <td>Address line 1</td>
            <td>{add1}</td>
        </tr>
        <tr>
            <td>Address line 2</td>
            <td>{add2}</td>
        </tr>
        <tr>
            <td>City</td>
            <td>{city}</td>
        </tr>
        <tr>
            <td>State</td>
            <td>{state}</td>
        </tr>
        <tr>
            <td>Pin code</td>
            <td>{pinCode}</td>
        </tr>
        <tr>
            <td colspan="2">Phone Condition</td>
        </tr>
        <tr>
            <td>Issue</td>
            <td>{issue}</td>
        </tr>
        <tr>
            <td>Charger</td>
            <td>{charger}</td>
        </tr>
        <tr>
            <td>Ear Phone</td>
            <td>{earPhone}</td>
        </tr>
        <tr>
            <td>Box</td>
            <td>{box}</td>
        </tr>
        <tr>
            <td>Bill</td>
            <td>{bill}</td>
        </tr>
        <tr>
            <td>Condition</td>
            <td>{condition}</td>
        </tr>
        </table>
    '''.format(
        name=form.cleaned_data.get("name"),
        add1=form.cleaned_data.get("addressLine1"),
        add2=form.cleaned_data.get("addressLine2"),
        city=form.cleaned_data.get("city"),
        state=form.cleaned_data.get("state"),
        pinCode=form.cleaned_data.get("pinCode"),
        phone=form.cleaned_data.get("phone"),
        issue=data.get("issue_no_issue"),
        charger=("Yes" if data.get("charger") else "NO"),
        earPhone=("Yes" if data.get("ear_phone") else "NO"),
        box=("Yes" if data.get("box") else "NO"),
        bill=data.get("valid_bill_status"),
        condition=data.get("phone_overall_condition")
    )

    name = phone.modelNumberId.name + " " + phone.ram + " " + phone.storage
    return (name, msg)


def sendMail(data, form, selected_phone):
    port = settings.EMAIL_PORT
    smtp_server = settings.EMAIL_HOST
    sender_email = settings.EMAIL_HOST_USER
    revicer_email = settings.EMAIL_ADDRESS_RECEVIER
    password = settings.EMAIL_HOST_PASSWORD
    context = ssl.create_default_context()
    subject, text = preparedMailData(data, form, selected_phone)
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = sender_email
    text = MIMEText(text, "html")
    message.attach(text);
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, revicer_email, message.as_string())
