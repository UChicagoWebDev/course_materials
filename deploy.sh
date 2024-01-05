rsync -v -r examples student@uchicagowebdev.com:/var/www/html
rsync -v -r images student@uchicagowebdev.com:/var/www/html/course_lectures
rsync -v *.md *.css *.html student@uchicagowebdev.com:/var/www/html/course_lectures
rsync -v uchicagowebdev.com/* trevor@uchicagowebdev.com:/var/www/html/