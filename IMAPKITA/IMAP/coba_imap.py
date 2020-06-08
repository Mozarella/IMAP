import imaplib, email, os

#user='email client'
#password='password'

user =input('type your email : ')
password=input('type your password : ')

imap_url='imap.gmail.com'
attachment_directory ='D:/Materi kuliah/KULIAH SEMESTER 6/Sistem Paralel dan terdistribusi/tubes/IMAP/hasil_client'

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_directory, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))

#untuk mencari email yang masuk
#search('FROM','tubessister19@gmail.com',con)

def search(key, value, con):
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data

#untuk mengambil email yang masuk
# msgs= get_emails(search('FROM','tubessister19@gmail.com',con))

# for msg in msgs:
#	print(get_body(email.message_from_bytes(msg[0][1])))
def get_emails(result_bytes):
    msgs =[]
    for num in result_bytes[0].split():
        typ, data = con.fetch(num,'(RFC822)')
        msgs.append(data)
    return msgs
try: 
    con=imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)

    con.select('INBOX')
    # b'1906' sesuaikan dengan list data dalam bentuk byte
    result, data = con.fetch(b'1906', 'RFC822')
    raw= email.message_from_bytes(data[0][1])
    get_attachments(raw)
    print("BERHASIL DI-DOWNLOAD")
except:
    print("LOGIN GAGAL")
