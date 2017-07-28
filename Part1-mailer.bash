#!/bin/bash
curl --url 'smtps://smtp.gmail.com:465' --ssl-reqd \
--mail-from 'emailacctused@gmail.com' --mail-rcpt 'myphonenumber@mymetropcs.com' \
--upload-file securityalert.txt --user 'emailacctused@gmail.com:password' --insecure
