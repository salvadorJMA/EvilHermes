
import sys
import argparse
#import dkim 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Definición de colores

class colors():

  magenta = '\033[95m'
  blue = '\033[94m'
  cyan = '\033[96m'
  green = '\033[92m'
  yellow = '\033[93m'
  red = '\033[91m'
  end = '\033[0m'
  bold = '\033[1m'
  underline = '\033[52m'
  blinking= '\033[5m'
  purple= '\033[35m'
  strongBlue= '\033[34m'
  strongYellow= '\033[33m'
  strongRed= '\033[31m'
  strongGreen= '\033[32m'
  gray= '\033[90m'
  doubleUnderline= '\033[21m'

# Creación del banner de la herramienta

def banner():
  print(("""%s %s
     )                              
                (   ( /(                              
   (    )   (   )\  )\())   (   (       )      (      
  ))\  /((  )\ ((_)((_)\   ))\  )(     (      ))\ (   
  /((_)(_))\(()_)_   _((_) /((_)(()\ (() )\ ()' /((_))\ %s """ % (colors.strongRed,colors.blinking, colors.end)),("""%s
   _____   _(_) | | | | ___ _ __ _ __ ___   ___  ___ 
  / _ \ \ / / | | |_| |/ _ \ '__| '_ ` _ \ / _ \/ __| %s """ % (colors.strongYellow, colors.end)), f" {colors.blue}Creado por Salvador{colors.end}", ("""%s
 |  __/\ V /| | |  _  |  __/ |  | | | | | |  __/\__ \\
  \___| \_/ |_|_|_| |_|\___|_|  |_| |_| |_|\___||___/ %s""" % (colors.strongYellow, colors.end)))       

  print(f"\n{colors.gray}#######################################################################################{colors.end}")



# Si hay algún error con los argumentos se muestra mensaje de error

def parser_error(errmsg):
    banner()
    print("\nUsage: python3 " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg + "\n")
    sys.exit()

# Parseamos los argumentos, si no se meten argumentos se muestra mesaje de ayuda

def parse_args():

    if len(sys.argv) < 2:
        banner()
        print("\nUse -h, --help flags for help usage\n")
    # parse the arguments
    else:
        parser = argparse.ArgumentParser(
            epilog='\tExample: \r\npython ' + sys.argv[0] + " -to recipient@gmail.com -subject 'greetings' -data 'hello my friend'")
        parser.error = parser_error
        parser._optionals.title = "OPTIONS"
        parser.add_argument(
    	    '-tls', '--starttls', action='store_true', help="Enable STARTTLS command.")

        parser.add_argument(
            '-helo', '--helo', default=None, help="Set HELO domain.")
        parser.add_argument(
            '-mfrom', '--mfrom', default=None, help="Set MAIL FROM address .")
        parser.add_argument(
            '-rcptto', '--rcptto', default=None, help="Set RCPT TO address.")
        parser.add_argument(
            '-data', '--data', default=None, help="Set raw email.")
        parser.add_argument(
            '-ip', '--ip', default=None, help="Set mail server ip.")
        parser.add_argument(
            '-port', '--port', default=None, help="Set mail server port.")
        parser.add_argument(
            '-subject', '--subject', default=None, help="Set mail subject.")
        parser.add_argument(
            '-to', '--to', default=None, help="Set mail to address.")

        args = parser.parse_args()
        return args


#Función pensada haciendo uso de contraseña de app debido a problemas con el servidor propio

def send_custom_email(args):
    smtp_server = 'smtp.gmail.com'
    smtp_port = int(args.port)
    smtp_username = 'example@gmail.com' #change
    smtp_password = 'passexample' #change

    # Iniciar la conexión con el servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.ehlo()

    server.login(smtp_username, smtp_password)

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = str(args.to)

    custom_headers = {
        'rcpto': str(args.rcptto),
        'helo': str(args.helo),
        'from': str(args.mfrom),
    }

    if custom_headers:
        for header, value in custom_headers.items():
            msg[header] = value

    msg['Subject'] = str(args.data)
    msg.attach(MIMEText(str(args.data), 'plain'))

    # Envío del correo
    server.sendmail(smtp_username, str(args.to), msg.as_string())

    # Cerrar la conexión
    server.quit()








def main():

    args= parse_args()

    if not len(sys.argv) < 2:
        banner()
        if not (args.helo and args.mfrom and args.rcptto and args.data and args.ip and args.port):
            print(('''%splease set -helo, -mfrom, -rcptto, -data, -ip, and -port %s''' % (colors.strongRed, colors.end) ))
            return -1
    
        print(('''%sSe está enviando el correo... %s''' % (colors.strongRed, colors.end) ))

        try:
            send_custom_email(args)

            print(('''%sEnviado %s''' % (colors.strongGreen, colors.end) ))

        except:
            print(('''%sHa habido un error enviando el correo. %s''' % (colors.strongRed, colors.end) ))
        
    
    
   
    

if __name__ == '__main__':

  main()
 
  
