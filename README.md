# Automated Email Schedulern
This Python script automates the process of sending emails using the built-in 'smtplib' library. The script can be scheduled to run at specific times using the cron job scheduler.


# Dependencies
1. Python 3.x
2. 'smtplib' (Standard Library)

# File Structure

├── send_email.py
├── config.json
├── README.md

# Usage

**Configuring Email Credentials**
1. Edit the config.json file with your email credentials, recipient(s), subject, and message content.

    {
    "email": "your.email@gmail.com",
    "password": "your_password",
    "recipients": ["recipient1@example.com", "recipient2@example.com"],
    "subject": "Test Email",
    "message": "This is a test email sent automatically using Python and cron."SELECT i.waybill_num,
       i.invoice_number_id,
       i.client_name,
       i.status,
       i.zone,
       i.delivery_mode,
       i.charged_weight,
       i.client_weight,
       i.origin_center,
       i.serial_number,
       i.destination_pin
FROM invoice_transaction i
JOIN client c ON i.client_id = c.id
AND VERSION = 0
AND i.charge_DL=0.0
AND i.charge_RTO=0.0
AND i.charge_DTO=0.0
AND i.client_name NOT LIKE '%B2B%'
AND LOWER(i.client_name) NOT LIKE 'skynet%'
AND i.client_name NOT IN ('AMAZONINDIA',
                          'AMAZON',
                          'TATABULK SURFACE',
                          'MYCLUBFACTORY EXPRESS' ,
                          'CLUBFACTORY SURFACE',
                          'CLOTHESBOX',
                          'IITTECHFESTBOMBAY SURFACE',
                          'Flipkart Heavy',
                          'EZ MALL',
                          'Mynta',
                          'MYNTRA SURFACE',
                          'Jabong INS',
                          'PAYTM HEAVY',
                          'Paytm Heavy Reverse',
                          'Delhivery',
                          'DLV Internal Test')
AND c.client_type IN ('prepaid', 'cod_netoff')
-- sum_dt is billing date 
AND sum_dt IN ('2023-11-01')
-- AND status_date>='2021-08-31 18:30:00'
-- AND status_date<'2021-09-15 18:30:00'
ORDER BY i.client_name;
   }

**Setting up Cron Job**

1. Open your terminal and type:
   crontab -e
2. 0 15 * * * /usr/bin/python3 /path/to/sending_email_through_google.py

# Script Explanation

**send_email_through_google.py**: This Python script reads the configuration from config.json and sends an email using the specified SMTP server.
**config.json** : This file contains the email configuration, including sender's email, password, recipient(s), subject, and message content.

# Acknowledgments
1. The Python community for providing the smtplib library.
2. The cron job scheduler for automating script execution.
