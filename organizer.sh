#!/bin/bash
if [ ! -d archive ]; then
    mkdir archive
fi 
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
mv grades.csv archive/grades_${TIMESTAMP}.csv
touch grades.csv
echo "[$TIMESTAMP] Archived grades.csv as archive/grades_${TIMESTAMP}.csv" >> organizer.log
echo "Archived grades.csv to archive/grades_${TIMESTAMP}.csv"
echo "A fresh grades.csv is ready to go."
