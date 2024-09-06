#!/bin/bash

#on zip les fichiers
zip -r backup.zip /home/ec2-user/junior.txt /home/ec2-user/junior2.txt

#on l'envoie à amazon S3
aws s3 mv /home/ec2-user/backup.zip s3://mycohortebucket/backup.zip

echo "Backup done at $(date)"
