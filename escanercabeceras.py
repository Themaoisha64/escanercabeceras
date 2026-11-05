import requests

HSTS = "Strict-Transport-Security"
CSP = "Content-Security-Policy"
XFO = "X-Frame-Options"
XCTO = "X-Content-Type-Options"

url = input("Introduce la url de interes: ")
response = requests.get(url)
estado = response.status_code
print("El estado de la url es: ", estado)

cabeceras = response.headers

if HSTS not in cabeceras:
	print("Warning: Strict-Transport-Security")
if CSP not in cabeceras:
	print("Warning: Content-Security-Policy")
if XFO not in cabeceras:
        print("Warning: X-Frame-Options")
if XCTO not in cabeceras:
        print("Warning: X-Content-Type-Options")

rutas_sensibles = ["/robots.txt", "/.git/", "/admin/", "/.env/", "/backup.zip"]

for ruta in rutas_sensibles:
	url_sensible = url + ruta
	res_sensible = requests.get(url_sensible)
	if (res_sensible).status_code == 200 and len(res_sensible.text) != len(response.text):
		print("Ruta ", ruta, " expuesta")
