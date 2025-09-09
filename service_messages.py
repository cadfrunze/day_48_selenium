import pywhatkit as pwtk

def send_messages(nr_telefon: str, descriere: str, pret: str, link: str) -> None:
    new_price: str = ''
    for num in pret:
        try:
            type(int(num))
        except ValueError:
            pass
        else:
            new_price += num
    pwtk.sendwhatmsg_instantly(phone_no=nr_telefon, message=f'{descriere}: Pret: {new_price} lei/n/nlink: {link}')
