from scapy.all import sniff
from scapy.layers.inet import IP, TCP

puertos_escaneados = {}

def packet_callback(packet):
    # Comprobamos si el paquete tiene capa IP y TCP
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport
        
        if ip_src not in puertos_escaneados:
                puertos_escaneados[ip_src] = set()
        puertos_escaneados[ip_src].add(tcp_dport)

        print(f"[+] Paquete detectado: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

        if len(puertos_escaneados[ip_src]) > 15:
                print("ALERTA. Escaneo de puertos detectado")

print("[*] Iniciando captura de tráfico... (Pulsa Ctrl+C para detener)")
# Captura paquetes en la interfaz por defecto
sniff(prn=packet_callback, store=0)
